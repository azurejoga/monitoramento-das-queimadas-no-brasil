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
| c1c9fbd5-7671-3a0a-af52-eb2d290f52d7 | 1.14109 | -60.44269 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd6cba9b-b2a9-3171-8b4c-04199ffcc00b | 1.94281 | -60.37681 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20cb196f-8f54-3c57-a419-423c8af6fb7c | 2.35092 | -61.00491 | 2025-03-06 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adb8279d-3ad8-3494-bdf3-3fe7c2310491 | 1.85634 | -60.58334 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb8e4227-52c8-3f3e-aaf7-9072f9cf7e99 | 1.14163 | -60.44611 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7beb4e70-d8c3-3186-a6ca-2190e4bbc85f | 2.63023 | -60.42347 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ac94631f-cddf-3d39-b677-1600ae913580 | 2.85416 | -60.87659 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c46193aa-49ff-3700-b99e-cbcb7a67d779 | 2.85361 | -60.87312 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f19c614-6c43-3cc9-8e58-a8cf56152608 | 2.30717 | -60.20679 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6163f0f-8feb-38ff-82b2-35d5979365cb | 1.8492 | -60.58092 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6efc4474-671f-3889-a39f-ccceb7bfc951 | 2.37309 | -60.23558 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d9457f4-c6bf-36c1-b736-39bf59b600d5 | 1.94167 | -60.39102 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42342658-fc00-36eb-b3bc-f5b2731732eb | 2.26748 | -60.25505 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6307fe26-e8aa-30ff-92f8-ac2b957be827 | 0.83238 | -59.94999 | 2025-03-06 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efc851c4-124e-38b6-92a4-9b5aef95a6c2 | 1.12602 | -60.51873 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99fb716c-b4c3-301b-8529-a6647891a11d | 2.30441 | -60.21073 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 782b75cd-10a1-373f-8c5f-eea6b70d52f4 | 2.85252 | -60.86616 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 70bc3cbe-4bea-3538-bd88-d164100cc11f | 3.82502 | -60.98118 | 2025-03-06 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 209c694a-6047-3d58-8c42-90542b7a4c11 | 0.82571 | -59.28411 | 2025-03-06 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e51050f7-f5b4-3d20-8905-c57ad1eabf78 | 2.85366 | -60.85174 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6cacfb5-98b1-3b77-8525-a80fed1fe078 | 2.36783 | -60.70043 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450e593f-3e03-3976-8e2a-fb3f0843193c | 2.85421 | -60.85522 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c118a0ce-4eed-34dd-b9e6-7fdb5d15a6ca | 1.13208 | -60.51427 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cab9bf8-5838-3074-bbef-54690b44f5d8 | 2.3209 | -60.20816 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fde5c6f-e5b2-30b8-95d8-d585866263af | 2.23726 | -60.2181 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c10705a1-5781-3791-87ae-024941658552 | 3.32798 | -61.23511 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb01931b-f88d-3824-a04f-e70c54fa378d | 2.26802 | -60.25848 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b3c474-cf2f-3852-b2e9-9a955106691d | 2.84811 | -60.85972 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 056b7277-110f-34b2-91dc-dee93e567ce1 | 1.12494 | -60.51187 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5da60e7c-4b6e-3552-a007-0cd4eeeb0b35 | 2.15444 | -61.82975 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ae7605-07f7-35b5-b7ae-0e641e328af2 | 3.34697 | -61.24676 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f831db7-a22a-332f-a781-c240b38ebffc | 2.35479 | -61.00784 | 2025-03-06 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae37e78-48a7-39b9-95e7-c5bdeabd3797 | 2.85307 | -60.86964 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 097cb4b6-5abf-39f4-9a48-aa705f2201d7 | 2.11441 | -61.81746 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7406f993-2f9b-3d57-a31b-9e926e218144 | 1.85526 | -60.57646 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 21462949-e027-3fca-bc2a-06277f2a37f6 | 1.12878 | -60.51479 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc53f1f9-8a37-3906-b5a3-4e2ae0e6ceeb | 1.13154 | -60.51085 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb7da82-beb3-3d05-8f2a-f6f1b26fe2cc | 1.12272 | -60.51924 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a6ff25f-adc8-3f3d-b310-3ac92cb88793 | -13.61324 | -59.76995 | 2025-03-06 05:31:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa8db387-d74c-3aa8-b8b5-9ae3294b7acf | -13.95658 | -48.16309 | 2025-03-06 05:44:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f61c66f-1ae6-33d4-88ea-41b5123f57c8 | -20.72831 | -49.43265 | 2025-03-06 05:46:00 | AQUA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d4aa09ab-5a8a-3e36-a1ba-d9ae36a773bf | -20.719 | -49.43121 | 2025-03-06 05:46:00 | AQUA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 73e12d23-099c-3463-a97b-e64120b66499 | 3.32675 | -61.23355 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e79ae841-137c-3822-8fc4-138efc4a2cd1 | 2.77013 | -60.32301 | 2025-03-06 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5cd08c67-63ab-3fa0-8e3d-7f7c9925c99a | 2.37645 | -60.2361 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8b4b096-472b-3c85-9b0e-1a11afc694c1 | 3.32222 | -61.24146 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb2a64aa-9cb9-330e-ad27-6185de354e13 | 1.32706 | -60.67105 | 2025-03-06 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2046a850-fc3f-3507-859d-42f4126a9b6b | 2.62719 | -60.42261 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ccd1da0a-6f39-3d13-9356-c72d400fdb81 | 3.32148 | -61.23697 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 827ebdbe-02d0-3d9d-bcd4-88c54af622a1 | 1.3205 | -60.67219 | 2025-03-06 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe3cd9a9-4c1d-3caf-97e3-8d89dac8da63 | 1.32143 | -60.67786 | 2025-03-06 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bda3370b-c876-3c81-815a-00695377451a | 3.32754 | -61.2382 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d5cbc4e-ce73-341f-b7b9-73a9e3b5d18d | 2.77764 | -60.32747 | 2025-03-06 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 20d6a098-7eeb-316b-92e4-2a0f37a6fe90 | 2.37448 | -60.24069 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe4e8f1b-8fd8-3402-990f-7754e2f29af6 | 2.37343 | -60.23456 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d97030f-d94f-3711-9f9e-3e16a9b7ae64 | 2.62619 | -60.42309 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8d788bb5-a22b-318c-974e-9d2b5821178a | 3.3276 | -61.23561 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ef3eb03-f41c-34d5-91d7-fec2fe1d7575 | 2.36992 | -60.23795 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 852e41aa-4f14-31b7-ad76-7c3fe0faf6ed | 3.32063 | -61.23487 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ba85602-90db-3950-b879-6dd42e3752a2 | 3.32141 | -61.23944 | 2025-03-06 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 73fda931-17d2-3854-835a-7f0fc0bcf7f6 | 3.53744 | -60.08056 | 2025-03-06 06:18:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83eea6c3-88cd-3e50-aa22-9be596795020 | 1.85268 | -60.58297 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb44fe50-ccb9-303e-89da-c2a27d2eca05 | 2.62525 | -60.41759 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| eed76d5c-ef8f-3473-8141-de07139f0ad8 | 1.85174 | -60.5773 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8e7b854-c4ff-3f51-bb23-d405e0a898e5 | 2.62628 | -60.41708 | 2025-03-06 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 94a35666-302a-3cf9-8990-54f6d8d8a974 | -20.1175 | -47.039 | 2025-03-06 11:30:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 117.3 |
| d94ff855-7f08-3522-aa00-1c25d4f4854d | -20.1175 | -47.039 | 2025-03-06 11:40:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 151.5 |
| bd6bf7d5-76b6-3cd7-9e9f-b5497c62ad84 | -20.1175 | -47.039 | 2025-03-06 11:50:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 6517eda2-0427-314f-bcbd-060f3d38da30 | -5.17155 | -37.86733 | 2025-03-06 11:59:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ee826c15-7589-3d8c-a8ac-d91341a471f6 | -20.1175 | -47.039 | 2025-03-06 12:00:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 268.3 |
| 692cee3d-a95b-3502-9c29-87240fe6a486 | -5.77267 | -36.03222 | 2025-03-06 12:01:00 | TERRA_M-T | CAIÇARA DO RIO DO VENTO | RIO GRANDE DO NORTE | Brasil | 2401909 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7d2d029a-0dcb-37a6-9f3a-ad94d1ae1a8f | -11.60933 | -39.41941 | 2025-03-06 12:01:00 | TERRA_M-T | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c3e41c16-d9ae-3134-8182-d1f40fb37032 | -5.60282 | -37.94958 | 2025-03-06 12:01:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| dc063bf1-00e7-3e78-a972-ad0f7348b3f5 | -10.04142 | -36.43755 | 2025-03-06 12:01:00 | TERRA_M-T | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 250b71f2-4b0b-3879-90ee-8ae681b494a2 | -11.84458 | -37.67037 | 2025-03-06 12:01:00 | TERRA_M-T | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6a0d521f-ad4d-3d05-a047-6415d0e9c7d1 | -9.80342 | -37.04995 | 2025-03-06 12:01:00 | TERRA_M-T | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 7973a7b3-633e-3847-96e1-05f843cb90f4 | -11.34796 | -37.65564 | 2025-03-06 12:01:00 | TERRA_M-T | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 542a632b-182d-33e9-8ad0-34682702ff4d | -16.0166 | -43.59639 | 2025-03-06 12:04:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| af18c10b-a798-36ca-8df7-233b16c4cef5 | -20.05141 | -41.4272 | 2025-03-06 12:04:00 | TERRA_M-T | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 672f7825-618f-39a0-b777-874dea5b3771 | -16.007 | -43.59484 | 2025-03-06 12:04:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9dcae4b5-6726-31b3-9ec0-0f1af2d312ee | -22.98719 | -43.30859 | 2025-03-06 12:04:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a029713d-0d71-3eec-9c15-6eeee9df7a70 | -20.1175 | -47.039 | 2025-03-06 12:10:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 319.8 |
| 4123b20e-6179-3804-9f02-19a316ef4134 | -20.1175 | -47.039 | 2025-03-06 12:20:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 316.2 |
| d4beeceb-e102-34ec-b74a-abd71ee140ac | -20.1175 | -47.039 | 2025-03-06 12:30:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 284.0 |
| ecd10ace-3eb5-39e2-b5f9-145cc007caef | -20.1175 | -47.039 | 2025-03-06 12:40:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 65b645b4-e745-3931-8d3a-981e186f78cc | -20.1175 | -47.039 | 2025-03-06 12:50:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 146.2 |
| e5c27112-605e-3c76-bfa9-6f2a3a9d430b | -20.1175 | -47.039 | 2025-03-06 13:00:00 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 575e0cb4-3279-3faf-8de5-213a83e4540e | 3.9323 | -60.5976 | 2025-03-06 14:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 75f9f452-3cf6-3c30-81a6-435079feb951 | 3.9506 | -60.5972 | 2025-03-06 14:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 438fa25f-bb44-397b-8286-a363b53ae5b9 | -28.6221 | -50.2026 | 2025-03-06 14:20:00 | GOES-16 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 268.1 |
| a54fde1a-f6da-373b-9641-d14e027411c8 | -28.623 | -50.1781 | 2025-03-06 14:20:00 | GOES-16 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 8c27bd1f-b123-3111-b2b6-a40813337edf | -28.623 | -50.1781 | 2025-03-06 14:30:00 | GOES-16 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 116.3 |
| 0e2beb90-b270-381f-a607-36cafe0bd1a0 | -28.6221 | -50.2026 | 2025-03-06 14:30:00 | GOES-16 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 202.2 |


