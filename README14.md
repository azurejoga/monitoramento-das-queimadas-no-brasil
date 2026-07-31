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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a690ecc2-da92-3504-ba8e-6d3abfe6e3fb | -6.18366 | -55.52524 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0189cd4-be4f-3c19-b5bc-870c804b1ba5 | -10.07842 | -60.50454 | 2026-07-31 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4241bfd-9fcd-3b33-ba39-d2ba227fe185 | -9.49515 | -63.30424 | 2026-07-31 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03303307-2830-340d-bc29-8f6be05ca54c | -10.06084 | -60.50181 | 2026-07-31 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03cad1e4-0441-3d85-8d76-d1f8d3b90565 | -9.9665 | -64.9662 | 2026-07-31 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23f90081-d91b-34f7-9c28-3d380e42c742 | -7.84772 | -72.90157 | 2026-07-31 05:36:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5324aa9-9f52-3d0c-bd1e-4ef96efca986 | -9.49184 | -63.30371 | 2026-07-31 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 423e8b4b-d3e8-3b33-aab7-a1678ed70a13 | -10.07491 | -60.50399 | 2026-07-31 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18e84e29-1ada-320c-b549-25aa274b64a8 | -7.84699 | -72.90549 | 2026-07-31 05:36:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a88f51c2-f1e5-35d0-a8b3-215b0c76c29a | -9.89942 | -63.06921 | 2026-07-31 05:36:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 194f9095-1265-3302-bec4-d1fd91eea74f | -9.47196 | -63.27906 | 2026-07-31 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cb2f78a-24c2-3c87-8a19-23a44306708f | -9.46865 | -63.27853 | 2026-07-31 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55d74297-4b4b-3d3e-85a8-566a6bcf9cf7 | -10.47237 | -62.44983 | 2026-07-31 05:36:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab5feb7c-221b-39dc-8c3f-2c9d245931a4 | -22.15981 | -56.02209 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f09927d-e321-36dd-9600-44a0975408a5 | -19.02005 | -56.42266 | 2026-07-31 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bea2e273-ecb9-3e7c-8b90-ad0bf3a895c2 | -20.61261 | -57.30111 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75c8c755-60e9-3396-b779-7897eb43e4fd | -22.16018 | -56.01834 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ddde3c8d-769b-3d7a-85bb-14a9dc4dd05f | -22.24458 | -56.70866 | 2026-07-31 05:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c51c587-f393-3c27-8b1e-a6908eee8d72 | -22.16133 | -56.02219 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5c9a6236-f9e2-39a6-9ca2-8f86f91fa3a9 | -22.24492 | -56.7053 | 2026-07-31 05:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2425c7a5-3445-3fd8-9c08-36f09261faef | -21.38197 | -56.83433 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1779cc15-630a-30b4-b17c-3f4fa82df5a8 | -18.81079 | -53.14769 | 2026-07-31 05:38:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2a9a681-f3ef-39a0-88ae-afc502094cfd | -22.16204 | -56.01455 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3f8ebba3-c8d2-3ac4-be38-a44d99e5bf08 | -21.38167 | -56.8373 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 528f3726-4245-3643-bf82-f3401770797b | -22.1653 | -56.02215 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f123698a-87a5-3c40-ab1f-acfec94bb43b | -20.32483 | -58.0852 | 2026-07-31 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fd5de554-63a8-332c-ada0-7f8bc35d9143 | -22.19377 | -56.02825 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8e3b7ca-6148-32a9-86c2-6a88070c5a89 | -21.37687 | -56.83355 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc155375-99dd-32a6-bcac-8d7337abb501 | -21.38678 | -56.83791 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15e87a55-f73f-3730-8c30-41d4880ae68b | -18.81129 | -53.1423 | 2026-07-31 05:38:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 647aed9b-6015-32fc-be46-23b7ca984fce | -21.37657 | -56.83649 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cee9dd47-e27f-3484-a8b3-ce9c26521339 | -22.16683 | -56.02218 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c58d7148-d9b5-370c-a2fb-6adcd495f7f9 | -16.40301 | -53.3359 | 2026-07-31 05:38:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fc0bf57-1a73-3b42-af24-f23fc8922df6 | -16.40251 | -53.34056 | 2026-07-31 05:38:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85430c5b-9885-37a3-a117-52de53005f30 | -22.16568 | -56.01838 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4a8ce889-a87e-39b8-bf41-73846a83a06b | -22.16056 | -56.01449 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| dbbb7486-ce80-3a93-a4ca-536e8ef7190d | -20.57208 | -57.26082 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af6ae26-f598-38b6-b9b6-050a920b4c32 | -22.16168 | -56.0184 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 02279af8-22cc-38b4-8aa8-2e00e0fd6458 | -21.38709 | -56.83498 | 2026-07-31 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d407d3d6-7a55-3a24-83ec-a690c7b09e91 | -22.19412 | -56.02459 | 2026-07-31 05:38:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb5e8cbd-85f9-3d7a-b32f-d9b404204bde | -22.1578 | -56.0217 | 2026-07-31 05:50:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 58.3 |
| bd53550b-bcd9-3ba5-b289-79e5343b1ca2 | -22.1578 | -56.0217 | 2026-07-31 06:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 919e19ec-5fc9-3470-8934-360fb04cc1e6 | 1.09822 | -60.52017 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d2087306-36dd-30a7-8b8b-12346580e3a4 | 1.09529 | -60.5025 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 407d24c1-70b3-324e-be74-cf02f8bcc27a | 1.10055 | -60.51791 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67a46c87-4244-308e-907e-efb32bae6794 | 1.0943 | -60.49654 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 530a7884-9d64-371d-a52d-467dd80f34c2 | 1.09962 | -60.51204 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 99937af8-b8db-3971-b0ea-47ce58ff4d42 | 1.09627 | -60.5084 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 799b4a93-cfb7-33c9-b434-a281f4eb09c2 | 1.09774 | -60.50018 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c23237be-72e9-3df7-8666-e4d9573719f0 | 1.10391 | -60.51324 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8a81f40-8683-3e50-8fbb-6770537abc7b | 1.10148 | -60.52379 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c6579df-6564-348a-935c-1ce46d70d5e5 | 1.09868 | -60.50613 | 2026-07-31 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 961a1e7f-f276-359b-8d4c-079d646e42b0 | -7.84685 | -72.90134 | 2026-07-31 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fa32b11-3bc5-3f30-9f33-9273973a53f7 | -9.96827 | -64.96735 | 2026-07-31 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a549a56-c08a-3623-92cd-d10b0fd5014d | -9.96951 | -64.96666 | 2026-07-31 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d263dc6e-6496-3ac2-8faf-c0d7844d4c79 | -7.85031 | -72.90186 | 2026-07-31 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b92ac5e5-1f85-3776-9c66-f58f903fe5f2 | -2.89308 | -48.00943 | 2026-07-31 06:48:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9b07994-6b58-3c4d-9cac-9e401719110d | -3.0525 | -48.73577 | 2026-07-31 06:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e86c04f-9c32-3f6a-8f94-ab0759271d9f | -3.11089 | -47.91311 | 2026-07-31 06:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2c577e81-a963-3d23-9aae-2989d1bd4bce | -3.1123 | -47.90386 | 2026-07-31 06:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 4c26d7d3-d69d-328f-b7f1-0d2b3923cb50 | -3.96638 | -48.12801 | 2026-07-31 06:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 19b54917-6794-323a-891c-b23c9d734dfc | -3.96776 | -48.11878 | 2026-07-31 06:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54162b71-e05f-3466-9ff7-c79c74c7be3e | -3.05117 | -48.74456 | 2026-07-31 06:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db50b179-b7c8-3dce-90d1-3f79b915c133 | -4.27024 | -48.19991 | 2026-07-31 06:50:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 510b707b-55ac-393c-9ac2-ae3611886029 | -4.27163 | -48.19069 | 2026-07-31 06:50:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 07f75b07-bdd4-3353-a646-881ff879f445 | -4.37075 | -47.77032 | 2026-07-31 06:50:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 87f5cced-6270-3e56-9c8a-c77872ca2a1d | -14.38703 | -48.06659 | 2026-07-31 06:52:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f9bdcded-7577-35f9-8e64-91178cca4e7f | -14.37665 | -48.06596 | 2026-07-31 06:52:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9cb7ac33-2dcb-3246-b19d-013164e08fac | -14.37835 | -48.05325 | 2026-07-31 06:52:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1c8a02c7-f92f-3caf-bd95-e5f9316524d5 | -14.38541 | -48.07864 | 2026-07-31 06:52:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2ecf1960-ef4d-37d0-a5d7-f72fa4632b6e | -20.11547 | -50.75157 | 2026-07-31 06:54:00 | AQUA_M-M | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 0d9f4b16-6c92-3712-a4b6-e60836478be0 | -18.87203 | -47.51561 | 2026-07-31 06:54:00 | AQUA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f00a95ab-6f50-3c15-b7d1-56f1e28f5108 | -20.11694 | -50.74085 | 2026-07-31 06:54:00 | AQUA_M-M | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| b4f96802-f8d0-3252-a255-728425dea77d | -22.16447 | -56.01658 | 2026-07-31 06:54:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 23085d1d-6ac0-3edc-b1ed-7440c0b37605 | -7.84758 | -72.90154 | 2026-07-31 06:59:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97cd47ee-df71-3114-9e3a-ed4a9787e11b | -7.84713 | -72.90472 | 2026-07-31 06:59:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07ad3ec2-2210-37f0-8ce0-295746abeecd | -14.3855 | -48.071 | 2026-07-31 07:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 84669c7d-68c0-3503-9514-16d91bf98bff | -14.3855 | -48.071 | 2026-07-31 08:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ee52d360-9331-36c1-9dcc-51e71fb735b3 | -14.3855 | -48.071 | 2026-07-31 08:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2b4f93ba-6f3e-3d78-b81c-5a1766be2226 | -14.3855 | -48.071 | 2026-07-31 08:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 50739e6b-746f-3df4-8737-3fc10a7d8f01 | -12.6186 | -44.6116 | 2026-07-31 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c539aebf-ef74-3d83-a905-610616c0ae69 | -12.6186 | -44.6116 | 2026-07-31 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 570e84ef-fa74-3015-a276-a5870374c229 | -12.6186 | -44.6116 | 2026-07-31 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| db686460-ac5f-3c11-88b6-3ea213a2c86d | -12.6186 | -44.6116 | 2026-07-31 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| bdd969a0-d2ac-3abd-834c-727b34a537b9 | -6.89023 | -47.97358 | 2026-07-31 11:38:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| e3e684be-7215-3ef0-8b2e-b4ca1fd768ae | -6.88026 | -47.97224 | 2026-07-31 11:38:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e0ffa539-3299-3e61-acf7-dcfdeb362d5e | -6.88245 | -42.85743 | 2026-07-31 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 85b375a3-ed42-3ab7-85b7-55af89ba19be | -4.38951 | -43.27976 | 2026-07-31 11:38:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40e98823-b8ce-3ddc-9583-512be003193a | -6.88379 | -42.84769 | 2026-07-31 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 99b8a3c8-9cfe-3e16-b05e-dff3d1bf5361 | -6.55088 | -41.84208 | 2026-07-31 11:38:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 402191f4-af99-30e2-b4f5-d43485b03946 | -6.89981 | -43.52958 | 2026-07-31 11:38:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2bb6ebc-8841-315c-8320-d0ba5a91bf16 | -4.00302 | -43.27506 | 2026-07-31 11:38:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| f3e363bc-255e-3008-b48e-89ec04980a71 | -6.89211 | -43.51914 | 2026-07-31 11:38:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a4fed10-c2ae-3e64-aa61-78693db11a1a | -4.38823 | -43.28875 | 2026-07-31 11:38:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0513ca50-182d-31dd-8d5a-1051a54fdbff | -3.24114 | -41.80764 | 2026-07-31 11:38:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 506904f4-5333-33bb-8083-080ccb362af8 | -6.97905 | -38.13245 | 2026-07-31 11:38:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 07e343ae-2177-3da4-8ca4-f072f2e19c9f | -6.28314 | -41.85373 | 2026-07-31 11:38:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b2d5c071-9cb5-3249-9f43-0b52d04912f2 | -7.38165 | -46.2194 | 2026-07-31 11:38:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2ee5de20-356a-3a99-a5b7-eea299c50bd4 | -5.04621 | -43.2662 | 2026-07-31 11:38:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd39c755-f427-3f07-8c1f-59c54d2ed663 | -6.54943 | -41.85283 | 2026-07-31 11:38:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |


[Clique aqui para ver as próximas entradas](README15.md)
