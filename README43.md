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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f7efd6f-b52b-3679-8aeb-1b99ccea5bc4 | -9.41011 | -50.03297 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a0eccc8-62b0-37a6-8213-77e8d3807bf3 | -9.39613 | -50.01187 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11219a3c-2ade-3c9c-a98f-10b3423b0b4c | -9.39275 | -50.01131 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8927636e-bb82-31b4-8be5-4375b5c7e1cc | -9.37303 | -50.00432 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d36f8f-2b69-3d92-8318-e3fee6765123 | -9.3589 | -50.00576 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a1c7e1-ece4-3752-b1ff-c4b82a36a123 | -9.35552 | -50.0052 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 286d8a75-b35f-36c1-a3c9-3516908485ef | -10.1817 | -50.53368 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef274ff9-7505-303c-b5c9-c090f1d26e71 | -10.17889 | -50.52936 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d62ca42d-efff-3d93-898a-ca454bf32644 | -10.11371 | -50.00411 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9263cf7e-1107-3b92-819a-0383a5a945db | -10.11034 | -50.00356 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d6daa55-70e7-3d69-a265-b22ffa4e6c06 | -10.10697 | -50.00301 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52da6be8-fc6d-3eb5-b9d2-d46805f48076 | -10.10301 | -50.00608 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94a6e5d4-2d2f-3c83-9d9c-32fc3bc1ef1f | -10.05065 | -50.30585 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19c3d726-8a53-36f6-93a6-554dfe2ed186 | -12.24384 | -50.4535 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 037b530d-364a-3adf-86ef-37c714774b6d | -12.22637 | -50.64653 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bcdff3a-4e35-325d-a80b-1a6539896b7b | -12.22577 | -50.65022 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dcbb4cb-3759-3367-bb5c-5887aab86aab | -12.22277 | -50.66867 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fc4e196-5ed5-365b-a293-0918d687b8c4 | -12.22239 | -50.64965 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4ae964d-25ab-3e61-b8eb-29f363291213 | -12.22217 | -50.67237 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bed71070-eef8-3f96-a479-e7b90e51a38d | -12.22179 | -50.65334 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3bf6ddd-20f3-3665-aa81-1209db0b7b40 | -12.22157 | -50.67606 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eebf60b-f3b8-3200-95d6-3ea962d78ed2 | -12.22097 | -50.67976 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 439326a4-5d17-3d98-ae14-8973390dfa72 | -12.21841 | -50.65276 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 033e16ca-1d01-32e8-91e9-531dbfb4daa7 | -12.21434 | -50.48608 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1842eba-81a8-3b8e-9787-37d15029025a | -12.09052 | -50.0133 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d5f7e08-ec3e-3bac-8060-7c01f6a232ea | -12.08995 | -50.01688 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a919139-20ba-3f25-be24-c3ed30f25675 | -12.08661 | -50.01632 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ed400a5-b7d0-3903-870e-a7d5a6568325 | -12.085 | -50.00504 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d04cdcb-18ae-365f-937e-dd89a486d1d3 | -12.08472 | -49.60349 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c8f996f-de05-3093-897f-85b84ce6b9fb | -12.08443 | -50.00861 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b005bed9-ba73-358f-bc2c-fbdbce47b8f4 | -12.08416 | -49.60703 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fee993b7-7b79-3eac-9a11-122476df8d27 | -12.08385 | -50.01219 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae26d0f-5bbc-3942-a5f4-3cddb3aa53f5 | -12.08327 | -50.01577 | 2024-09-30 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa900773-eb90-3a33-963c-989a7266a347 | -12.0814 | -49.60295 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10c535f3-2b36-3bbb-89e7-f7a47b773a31 | -12.08084 | -49.60648 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9626b55-db44-39b4-b6a9-167bd57077e7 | -12.07752 | -49.60593 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc1ebad0-1d5c-3949-8c2b-5d0574053bd4 | -12.04946 | -49.99179 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbffeec2-5bda-339c-84ee-f718952a7e4e | -12.02886 | -50.03978 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77690b5e-1386-3eb6-a26b-37360f92d284 | -12.02495 | -50.0428 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d47fb55f-1864-3ba3-a965-a51efc99a836 | -12.0238 | -50.04997 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bde04eb-874f-3652-8767-b5bc48e84e88 | -11.7075 | -50.03167 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8819c5e9-ce07-3aaa-981c-48b43c869414 | -11.70359 | -50.03471 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3050f49e-3620-348d-a45e-e06c0d1afbd0 | -11.70294 | -49.93158 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 480bad82-b159-3610-a76e-fadd6bbec6b3 | -11.69846 | -49.93818 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6742b71f-da70-3a63-962b-a72a17c35877 | -11.69789 | -49.94176 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94b8bf3a-73c1-3474-87d4-84dda0de9c94 | -11.6936 | -49.90435 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04160d7a-172d-3e6e-8706-132a31889912 | -11.69303 | -49.90792 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 098c778c-c2df-3643-8b12-09db177ef6e8 | -11.69246 | -49.9115 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a0beeec-3373-3a40-b258-bf4c30a23286 | -11.69189 | -49.91507 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58941fcd-2cbc-31dc-93d0-e151a499e2a6 | -11.19857 | -49.93647 | 2024-09-30 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b994198c-edd1-349d-877d-bdf177568467 | -11.16079 | -49.72903 | 2024-09-30 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7330d2bc-9fba-3fac-a788-15cb450df0a1 | -11.15746 | -49.72848 | 2024-09-30 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 691e1550-e7a6-3a95-a549-d35b07ae3daa | -11.10915 | -49.586 | 2024-09-30 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d361d348-3245-35f4-a930-8b149ccc6746 | -11.10526 | -49.589 | 2024-09-30 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9abfd0c-ff9c-3575-b2b6-48a43c9775d4 | -11.1025 | -49.58491 | 2024-09-30 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27e10152-0e72-3d5e-b7d7-5557bfe7b9fe | -11.10193 | -49.58845 | 2024-09-30 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c75e63e3-3cb9-312f-8eab-5ac66db04f0b | -11.09917 | -49.58437 | 2024-09-30 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be108f85-bf57-37e1-be42-649e06f4e43d | -11.09861 | -49.58791 | 2024-09-30 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0022c528-00e7-32f6-a8b1-926c5ce210f2 | -10.99869 | -50.18974 | 2024-09-30 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b19fc30b-2c57-398b-a130-5aec089a2f54 | -10.98421 | -50.17239 | 2024-09-30 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 299193a8-07e2-3092-a2e8-aa6f75dbfa4b | -13.67607 | -50.92566 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e1052f5-5806-3def-8413-b95b719309e7 | -13.67546 | -50.92936 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831782b7-c8bc-3ce5-b29d-586c158292ed | -13.67451 | -50.914 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e80639-e8c4-31be-8dd7-cb4456a8e2bd | -13.67173 | -50.90973 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98868bb1-d75f-34a2-a932-e93d40543101 | -13.67052 | -50.91712 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eff3cf1e-16ed-37eb-b86d-89a136e1ad06 | -13.58066 | -51.07746 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acce47b5-d792-303c-a6b4-d832d713ea77 | -13.57979 | -51.10421 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f17dd29-151e-3f31-990b-0e525e69b0b1 | -13.57822 | -51.0924 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 351d9363-0d7d-372d-81bc-6d9906757e09 | -13.57788 | -51.07314 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31e921ee-9de8-3ef9-a7b1-fa42109b5bce | -13.57761 | -51.09614 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66d79ab0-a123-354c-bcdb-68c2bdb33a03 | -13.57727 | -51.07687 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bd1b2d1-67f7-3a57-8b4e-d8462ff8b8ed | -13.57639 | -51.10363 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c40f075-3830-3b20-b1d9-dad268e50059 | -13.57327 | -51.08003 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5acfd4ae-c7f8-327d-bee5-a4f2b4a13729 | -13.57292 | -51.06079 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f97e9f19-7009-30f4-ad76-474fd6c8b85c | -13.57232 | -51.06451 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e70e238d-2584-3c8c-8860-2a7b6c4fd3cb | -13.56954 | -51.06021 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c56ab81c-fa59-30f7-8025-edcd405c5f2f | -13.56554 | -51.06335 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bcc23089-d9f2-3077-bed7-9dcc4601eba7 | -13.55258 | -51.05729 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4fade36-cd77-3cc9-91e8-a276a3b5eb5e | -13.55046 | -51.09148 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb53a869-52c4-3c6c-998c-ea71cbb9de1f | -13.5498 | -51.05299 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 070fbf61-d8c3-34a0-a899-c6d30fbf581f | -13.54858 | -51.06044 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4f9047c-74d8-3353-b1a7-1d2885f83a6a | -13.54768 | -51.08716 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f94d0d8-5a96-3769-be3a-3b106560d378 | -13.54519 | -51.05986 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7b4781e-7a37-38cb-b4ef-83ace2ee51b4 | -13.07642 | -50.85606 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4ba4ce0-0129-38be-8237-3c4665699b08 | -12.43145 | -50.95977 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9259e35-f002-3bd8-b61b-da9e24e91799 | -12.42621 | -50.97047 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14c94584-a748-3620-b77c-316325ccb25b | -12.4256 | -50.97423 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ce6a24a-f532-3629-9c4b-0ef836fc9386 | -12.4228 | -50.96989 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c30786f5-423f-3c00-9d72-21aed396d2b4 | -12.42219 | -50.97366 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75659568-71a5-3ec0-a875-2b9d0eb74de7 | -12.42122 | -50.95802 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1103ec03-a187-34f7-b690-1ac8f5231796 | -12.4172 | -50.9612 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5988c265-15e0-3fbb-889e-d9049e2340c8 | -12.28732 | -50.64122 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d1a662a-e558-3dd1-9c81-bfc9417b3fdd | -12.28699 | -50.4645 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf5b6b32-64f1-35e5-a7ee-dbd8bf06c66c | -12.28672 | -50.64491 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e690dc67-2e82-3580-b7d7-6662f5c8aa03 | -12.28394 | -50.64065 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf973f6e-86eb-38b8-b6ca-ddef0efa6b30 | -12.28334 | -50.64433 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d3f1dbf-3d3a-306b-b153-eb645b61bed4 | -12.27935 | -50.64745 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ab12878-4c37-3ec3-9c55-321217cd1d0f | -12.27672 | -50.4853 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 042d9496-604c-3033-8147-0fdfd7168721 | -12.2668 | -50.46112 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f106c95c-e5ec-39cc-ba85-b0a89d45659b | -12.26627 | -50.52863 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README44.md)
