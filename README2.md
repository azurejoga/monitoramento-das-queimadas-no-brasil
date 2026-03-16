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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70fb5985-b41d-362d-ac78-f95b2e47f9e9 | -24.12573 | -46.70886 | 2026-03-16 04:14:00 | NOAA-21 | MONGAGUÁ | SÃO PAULO | Brasil | 3531100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87e3bb07-5475-396e-a047-6e239e3d02eb | -23.40632 | -46.42049 | 2026-03-16 04:14:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a5972985-dd4e-3534-b80a-329c81470e31 | -28.86963 | -50.66175 | 2026-03-16 04:14:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4e6db8e8-b313-3c19-b53c-61ae999d303a | -28.8741 | -50.65785 | 2026-03-16 04:14:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| be5fba14-a427-328b-99b5-4305253a8f2d | -28.87324 | -50.66254 | 2026-03-16 04:14:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 14718029-7605-300c-bf7a-e87ebfa1aade | -30.05117 | -50.84967 | 2026-03-16 04:17:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 86a50b79-e05e-31a7-802f-74024caeefe1 | -31.51864 | -53.72524 | 2026-03-16 04:17:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| cf88289a-64c3-3597-8dbb-687f17eeee1e | -31.52262 | -53.72637 | 2026-03-16 04:17:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 9665f9f2-43d9-3718-8784-f66842773136 | -30.47392 | -56.38845 | 2026-03-16 04:17:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 533b094a-4a65-369c-a160-27137d74f84a | -31.51948 | -53.72119 | 2026-03-16 04:17:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4ab1fd2d-fa1b-3aba-8883-27d11188723d | 1.20956 | -60.16881 | 2026-03-16 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e82d74d-8d03-3e2b-9fd1-1b8ab5fbf273 | -6.98815 | -47.07745 | 2026-03-16 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f7d01ce-16ed-3213-9bc1-52096baa192f | -6.98481 | -47.07692 | 2026-03-16 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6c288de-fea9-3e83-9c2d-6ddeaea58172 | -5.48837 | -44.98381 | 2026-03-16 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff70f0b5-6143-32d6-9926-ce391f81849a | 1.21048 | -60.16903 | 2026-03-16 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60fa7009-91a6-3786-a394-d6e4339d58e0 | 1.2094 | -60.16198 | 2026-03-16 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec9194b0-4d2c-3ca8-9b68-c0b6f78bf8b0 | 1.20843 | -60.16174 | 2026-03-16 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3933919c-0e97-350b-9896-76d8f958f99a | -10.00075 | -36.28893 | 2026-03-16 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bf180938-10b5-3011-af47-5d78544fa61a | -11.95566 | -58.74996 | 2026-03-16 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f0716e6-366b-3589-9f3a-ef52ea64f803 | -11.77679 | -47.0895 | 2026-03-16 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2fca5c5-a830-336b-9bc7-eb44fcd7fd1a | -11.77965 | -47.09381 | 2026-03-16 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ec33a11-5578-3527-b404-c4b71f369819 | -9.9942 | -36.28805 | 2026-03-16 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 293f76a1-a67d-3111-8f61-1d24f69aa6e1 | -11.95592 | -58.75027 | 2026-03-16 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f78aa7b9-6cc9-3f1e-a5ae-82bee52c89f2 | -11.78023 | -47.09003 | 2026-03-16 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9b819de-8265-3160-af54-f984334e1a26 | -20.23044 | -46.6675 | 2026-03-16 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3700680-d0c0-3488-9ef0-084852bcb42a | -25.3957 | -52.14154 | 2026-03-16 04:44:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c39a2b4d-5190-38ba-be86-81bddbb274fe | -30.47562 | -56.39014 | 2026-03-16 04:46:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| fe748dff-2b6d-3505-801d-ed137a32bfc7 | -30.61515 | -52.00616 | 2026-03-16 04:46:00 | NPP-375D | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 87e6a821-8cdd-3381-a5c9-4c043db61f82 | -31.52425 | -53.72851 | 2026-03-16 04:46:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 749d2688-f69d-3f83-870b-53fd2c1af5a2 | -31.51759 | -53.72709 | 2026-03-16 04:46:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 59356c2d-a4cb-37f7-9ce2-c4ecaf49d1eb | -28.87039 | -50.66422 | 2026-03-16 04:46:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fef3851f-d613-3b35-ac0a-8be3a50752fd | -31.51822 | -53.72303 | 2026-03-16 04:46:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d21de63d-702a-3ee5-bf5e-f431962744f5 | -28.87099 | -50.65979 | 2026-03-16 04:46:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76895de3-2f9e-3661-89b7-60f2599c37b2 | -31.52092 | -53.7278 | 2026-03-16 04:46:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 86185ef0-f914-3745-8c47-fbd4bdc488b8 | -31.51885 | -53.71897 | 2026-03-16 04:46:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 661e73e5-5812-353e-81de-29122350a3a3 | -30.05037 | -50.85026 | 2026-03-16 04:46:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 599e8eaa-0f36-338b-815b-590b9c1b8bc1 | 2.24399 | -60.29924 | 2026-03-16 04:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ea8adbd-6106-34d5-9230-8c1d86f6f008 | 2.25298 | -60.29214 | 2026-03-16 04:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac30db73-4944-3581-8550-77924ded5e09 | 2.2534 | -60.19631 | 2026-03-16 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c370473e-b61c-34d2-80ca-75efa1053ffe | 1.12286 | -59.58408 | 2026-03-16 04:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fceb1b5-529e-3bb7-9c41-80c4ebfeba5f | 1.93826 | -59.99409 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fc68ee3-45a8-3300-b0e4-b7117c087e26 | 2.24806 | -60.29289 | 2026-03-16 04:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 754f7236-15ef-3386-bd21-5b72e61db9a1 | 1.21003 | -60.16372 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e68b496f-77a2-340f-9c76-df0f9d90f2c4 | 1.01011 | -60.23202 | 2026-03-16 04:57:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1989fa-aeea-35d0-a171-a6b628734d45 | 0.95648 | -60.23483 | 2026-03-16 04:57:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10a2f728-d3c1-3e85-8909-5bfa0a8a79c6 | 0.90789 | -60.29789 | 2026-03-16 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81b403d6-bcac-3e68-a946-ec68756ba182 | 1.20945 | -60.15958 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 25a4f5a6-6d4b-3d52-aba0-8e88fa77fc99 | 1.55084 | -60.28337 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 341138bf-4f04-3b4b-b885-6ffe5439e202 | 0.9077 | -60.30182 | 2026-03-16 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7be1b9a2-4ebb-39b2-a8ad-d2390a862b00 | 0.9069 | -60.29655 | 2026-03-16 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b33a96a-51e4-39a4-be4e-6eee9f2b11ea | 2.33628 | -60.39874 | 2026-03-16 04:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cf87b04a-c2ee-3947-bb7e-c5118f1ef90d | 2.25424 | -60.20174 | 2026-03-16 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20101b8c-2ca1-3b5a-b65b-e6ae255c8054 | 0.95566 | -60.22952 | 2026-03-16 04:57:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ba0e0b5-8bba-32d3-bc6e-dbf7428e9725 | 2.33519 | -60.39944 | 2026-03-16 04:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e8fda68d-daaa-3f87-8ab1-b5e6ec48e6f7 | 1.5528 | -60.28436 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 866c7fdd-0007-3f5d-bef6-5f541a1e0c26 | 3.63602 | -60.95185 | 2026-03-16 04:57:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d09fc9-7842-3688-ba3b-a70263d17eb1 | 1.20925 | -60.15855 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 76e8d21e-7a16-3cfe-9d9e-17eb4f334c03 | 1.5557 | -60.28258 | 2026-03-16 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97058757-564d-374e-9693-55c3fa468c72 | 0.90873 | -60.30315 | 2026-03-16 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fa08426-f03f-3701-8915-507fa7ef6223 | 0.9127 | -60.2971 | 2026-03-16 04:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed19b429-73ae-3531-a365-d41250b47646 | -16.31175 | -58.48989 | 2026-03-16 05:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 892e2f86-055d-3618-af31-2424ce22a443 | -11.95856 | -58.74547 | 2026-03-16 05:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43b7fff0-a576-3698-999f-f967548a1402 | -11.95784 | -58.74966 | 2026-03-16 05:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af38e53e-8e53-3bfc-b726-af38b7c32407 | -15.66954 | -59.2923 | 2026-03-16 05:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af43ab8c-4d34-3578-9431-d82bb27f13ef | -11.95426 | -58.749 | 2026-03-16 05:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c60066a5-7530-32bd-8821-607ba8d0ea9e | -11.78087 | -47.0947 | 2026-03-16 05:01:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a8fdf47-2ebf-36d4-872f-9b72d5e4619b | -11.78164 | -47.08876 | 2026-03-16 05:01:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a92eed84-3efa-3601-80b6-8554196e3398 | -11.78126 | -47.09174 | 2026-03-16 05:01:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 999465b2-f29a-399b-b87e-9a996f81ff89 | -9.99574 | -36.29649 | 2026-03-16 05:04:00 | AQUA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 166.7 |
| 6ac56ef1-75b0-37a8-8920-f1fc1bc84c9f | -10.00529 | -36.27789 | 2026-03-16 05:04:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| 10786a0b-4055-3fb5-8c6a-4cb7aa6d26f1 | -10.00005 | -36.27158 | 2026-03-16 05:04:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 365.5 |
| 53c4b5ec-b92e-360c-963c-feb69cb3033a | -28.87093 | -50.66044 | 2026-03-16 05:06:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 081d4b99-bbc9-3e01-8a99-30efd29bf6e5 | -30.47612 | -56.39089 | 2026-03-16 05:06:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 99fe61f8-c600-3775-908a-ff99b2b13236 | -25.39302 | -52.14005 | 2026-03-16 05:06:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc9f1aac-f94c-36ac-be4d-dd2d1b32a0d6 | -31.5167 | -53.72409 | 2026-03-16 05:08:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 4f0cf6a6-9dce-353a-bf28-4b27a0b81210 | -31.52098 | -53.72469 | 2026-03-16 05:08:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 0f21cd20-311d-33a8-99fa-a3d4f3c756c7 | -31.51718 | -53.71939 | 2026-03-16 05:08:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 69e45aff-cd9a-39aa-b156-3fc82b8aec27 | -31.52049 | -53.72942 | 2026-03-16 05:08:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| eee2f038-5716-3ecd-bd48-64d84e370a62 | 3.13309 | -60.7774 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d80815e-d91a-3332-ac2d-607fc91d4ab0 | 3.1255 | -60.82545 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0bf786e-2566-3a6d-ac12-bd839fbdd7e6 | 3.12933 | -60.778 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d79b219-0485-3de4-aadd-a9d587655870 | 3.36414 | -60.37579 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72cb99b7-094b-3ea5-b136-5bb4024d0af7 | 3.12571 | -60.83288 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7fb3924-3a0e-34fb-8d71-18d586a8458a | 3.13007 | -60.78258 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37af02c4-94f3-3f5c-928b-4ae09fd0155c | 3.12625 | -60.83 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f95766d-fc29-3c1d-b316-e383881c6454 | 3.12803 | -60.82316 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb508de8-05eb-385d-a869-4eb5479dad33 | 3.33949 | -60.46787 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 714f2c9a-3e25-3b26-aca3-853f68d92a4b | 3.12499 | -60.82833 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4433b56-5d8f-3d84-9063-ded95a03d536 | 3.13384 | -60.78197 | 2026-03-16 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c6796fa-952a-34ce-b3f0-c37d8d788ce5 | 1.20886 | -60.15772 | 2026-03-16 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 144bd94c-b2fc-3fb9-9edb-1c2312c1ee5a | 2.20514 | -59.80782 | 2026-03-16 05:48:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a71cc270-412a-3eec-aede-ff69fa364a01 | 0.95659 | -60.23015 | 2026-03-16 05:48:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6df1a640-55af-36d8-ab2f-a496be8fa00c | 0.75792 | -59.89332 | 2026-03-16 05:48:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6832fb2-2e1d-34f2-be3a-9c727107097b | 0.66065 | -60.50021 | 2026-03-16 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b5e94df-11b3-3596-b415-f6dec15ce37b | 0.9531 | -60.23423 | 2026-03-16 05:48:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fce952d0-dffc-3fed-81a6-db2558ae4e03 | 0.95255 | -60.23074 | 2026-03-16 05:48:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55bc0552-ee62-3796-a959-525c80f99ef1 | 1.20942 | -60.16125 | 2026-03-16 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ee5df45-3ed3-3f58-8200-c8d34e1da38b | 1.04144 | -60.41914 | 2026-03-16 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcf8581a-b78a-3584-a2ad-443c1581c5e4 | 0.88055 | -59.46021 | 2026-03-16 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a302633-30dc-3ad1-ad56-bece627d2681 | 1.71281 | -61.12712 | 2026-03-16 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
