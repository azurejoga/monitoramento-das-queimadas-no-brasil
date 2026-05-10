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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cd6eb4d-1cf4-33e4-ba76-ce032a0e56eb | -9.41137 | -50.69414 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae7cd567-4e4c-3a62-a225-0092f2520439 | -10.55504 | -56.34186 | 2026-05-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29961e16-3ce4-32cf-a08e-53b6fa47cb41 | -9.41189 | -50.69819 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bb7d526-7124-3976-aa69-d69a42746ddc | -9.41657 | -50.69492 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1298b602-4b12-3bb2-a582-ffd1924251da | -7.26699 | -47.0943 | 2026-05-10 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b460c8fb-2f6f-32b1-b54c-95bf82c72784 | -9.75868 | -55.61903 | 2026-05-10 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 829ce138-32e0-38b2-b21e-1068e8b9c0f1 | -9.41308 | -50.68872 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e82471e-079c-385c-917e-fc0c50f1413b | -9.41269 | -50.69189 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73b0c746-6b42-39e4-a57f-f3d1cfd9fa58 | -9.41229 | -50.69505 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58b2642d-375a-32ce-a5e8-faef632f3db3 | -10.55441 | -56.3462 | 2026-05-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e8e1541-04db-380e-bb01-7511b4e8767b | -9.41829 | -50.68948 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff0c2839-5b05-33dc-bc71-04c25f6805d5 | -9.41095 | -50.69728 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cccc4c86-f2d4-33b7-b0cb-1238e05d5c7e | -9.41742 | -50.68858 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c5f658f-9c33-3378-a7bb-d3e80c18a94a | -9.41179 | -50.69099 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea79d563-cd06-3750-99e0-43cac236e04f | -10.93899 | -49.43972 | 2026-05-10 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72e43ff8-bb95-39b8-ba80-96967c115ae1 | -9.417 | -50.69175 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2d3043b-1cc9-3917-aa60-45224e9166f1 | -12.05801 | -49.7667 | 2026-05-10 05:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3be1802-72e4-39d9-ab9a-fa2246ef0397 | -12.05753 | -49.77073 | 2026-05-10 05:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9429868-b623-3938-be75-553b85f48436 | -15.31899 | -53.08766 | 2026-05-10 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f56a78f-1ef0-3d91-baa0-0e5527566c45 | -12.56961 | -46.67881 | 2026-05-10 05:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| febb6bf2-8b20-3c62-a22a-f00a697dacd4 | -11.47987 | -52.92037 | 2026-05-10 05:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e895214-0bca-30f0-a8b3-3b4173344e88 | -11.47526 | -52.91973 | 2026-05-10 05:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b6d1c0-9b3c-39d5-9fab-d4796879cbf2 | -12.55658 | -46.67889 | 2026-05-10 05:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c5c268d-3d50-3e9c-9ea4-683f9670007a | -12.56356 | -46.67973 | 2026-05-10 05:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 434f77c5-600b-318e-a60e-14e0d4d8d3dd | -11.47933 | -52.9217 | 2026-05-10 05:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 925b8398-f105-38ef-8fbc-06a6717958d3 | -12.55565 | -46.6772 | 2026-05-10 05:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 923d016e-ee11-3c54-95f3-880d0c30d772 | -12.05849 | -49.76266 | 2026-05-10 05:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3006802c-07ad-35a8-a3c1-3e7740e5e8b5 | -11.79916 | -56.99846 | 2026-05-10 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05ec908a-9277-3e9a-89cc-522d271a4f39 | -12.56262 | -46.67809 | 2026-05-10 05:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0427f82-799e-3ade-b10d-0ce617114bab | 3.67294 | -61.85758 | 2026-05-10 05:48:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5b04f5f-8b7c-3622-9ae7-1fc8dbc9e580 | 2.34236 | -60.69683 | 2026-05-10 05:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 154dab9a-230c-3b76-96b3-0b915b562c9c | 1.94003 | -60.84233 | 2026-05-10 05:48:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcb4e150-2774-3358-b612-852bbb241ffb | 4.14454 | -59.9939 | 2026-05-10 05:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da6fcf74-4272-3e35-9061-865470e549a5 | 1.65064 | -60.14761 | 2026-05-10 05:48:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd064343-dd41-346d-930c-a64276d95edc | 3.67352 | -61.86117 | 2026-05-10 05:48:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 827dea53-08de-364e-a069-18f795011a96 | 1.94007 | -60.84272 | 2026-05-10 06:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 525c5ee4-718e-3f9d-89eb-ab237f235546 | 2.34138 | -60.69814 | 2026-05-10 06:08:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3770167d-669d-3bf4-8752-040c896b71ca | 1.93949 | -60.84249 | 2026-05-10 06:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 725711c8-822b-3570-b07d-734928fc8cc6 | -14.1487 | -45.4242 | 2026-05-10 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1c14613f-12f3-3551-a5b5-f2a023a63d38 | -14.1487 | -45.4242 | 2026-05-10 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| e54aab3c-4d80-306a-8705-acda4876b5d7 | -14.1487 | -45.4242 | 2026-05-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 983d7e14-6f8c-34ce-affb-cbf26d202b9a | -14.1487 | -45.4242 | 2026-05-10 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c20051a5-44da-3cce-829b-899b9dd944f7 | -14.14611 | -52.89683 | 2026-05-10 12:19:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 141b5752-2bfe-3fff-b2b9-27893ff31296 | -11.47951 | -52.9216 | 2026-05-10 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9443e2c1-a521-3db2-b52c-952fef48bffe | -14.15504 | -52.89812 | 2026-05-10 12:19:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e8f42ea-3e04-38a1-92e1-bcefad4f0d90 | -14.14483 | -45.42237 | 2026-05-10 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 557a527d-3fc4-3b52-a350-d818ba05b6b7 | -15.31663 | -53.08817 | 2026-05-10 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4844095a-a615-3390-8091-fe3880322a31 | -14.1474 | -52.88756 | 2026-05-10 12:19:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 310b1203-ec10-3b9c-8540-f3655657eeda | -14.1487 | -45.4242 | 2026-05-10 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| c091b2f8-12b0-36c6-98fc-f9cd12a1c288 | -20.17943 | -46.4708 | 2026-05-10 12:21:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6a4a06b7-b859-3617-afab-81630373cb30 | -14.1487 | -45.4242 | 2026-05-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9f8272ca-5f79-37fc-b02f-0587a22632a8 | -14.1487 | -45.4242 | 2026-05-10 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 58b0e427-263f-39f6-805d-e9fb2d464039 | -14.1487 | -45.4242 | 2026-05-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| f6884be9-f441-33ba-9a73-0002b037c89b | -14.1487 | -45.4242 | 2026-05-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 532234c1-955c-3af2-a6eb-496bc5bd976c | -14.1487 | -45.4242 | 2026-05-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 515b1d70-b2a3-3388-a833-9ae06b3f95c6 | -14.1487 | -45.4242 | 2026-05-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 938a2d7e-5e12-3697-9a59-3d13ba12285b | -14.1487 | -45.4242 | 2026-05-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d7328259-1cec-3f68-ab32-44a89dc36d0a | -14.1487 | -45.4242 | 2026-05-10 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ef19c1e5-1660-3d27-8f99-1fb8d62aa53c | -14.1487 | -45.4242 | 2026-05-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4c256b8a-2482-3446-b506-4a123717c51d | -14.1487 | -45.4242 | 2026-05-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 19ed3a72-85ad-38cd-9b59-68d66560d8de | -14.1487 | -45.4242 | 2026-05-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b69e035e-233a-343f-af65-abceaa1c5779 | -11.7836 | -49.7286 | 2026-05-10 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 148e867f-5606-3e4d-aeff-707db115eba0 | -14.1487 | -45.4242 | 2026-05-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f7400f95-7f56-37ba-8b86-93b72653477a | -10.8737 | -49.6178 | 2026-05-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e7e52e41-912e-37c8-964d-c722a372ab84 | -10.8535 | -49.7062 | 2026-05-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b1c4cfb5-5145-3a97-8132-f9b97be7057f | -14.1487 | -45.4242 | 2026-05-10 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |


