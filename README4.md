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
| 2cea6fd4-f252-33ad-b228-165823da4e01 | -16.25247 | -60.03158 | 2026-04-15 04:51:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59adc424-c209-39f7-ab12-f001135fe14e | -18.50214 | -51.5967 | 2026-04-15 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f29ab0ca-a5a5-3a71-bce8-ca9156093861 | -21.04142 | -48.55164 | 2026-04-15 04:51:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 55783ced-b1b2-3bd5-ba01-ec23b8b4370a | -18.31097 | -54.64048 | 2026-04-15 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd9a5260-a268-3010-a18a-654d83c4ed80 | -20.18084 | -46.60086 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7da0bf0-eb71-3be1-a710-5db7b589c54d | -20.15996 | -46.74379 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33938acc-11af-3c83-b6ca-b7a23014a1b2 | -20.53882 | -49.50273 | 2026-04-15 04:51:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6851f49f-c7bc-3136-ac28-93ea309de988 | -16.22093 | -52.47448 | 2026-04-15 04:51:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8085a546-5b01-3820-83ea-bee84e7907c0 | -20.24433 | -46.54327 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d8e1ba7-8b1e-3886-9bc5-842dd6137b27 | -23.51528 | -46.21638 | 2026-04-15 04:51:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18eea5d6-c520-3429-ae9b-4764ef65ac9f | -18.51096 | -55.51821 | 2026-04-15 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ab4260f8-befe-30fc-b4b5-e4f72d09a72e | -20.8952 | -54.11236 | 2026-04-15 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05c0ca9d-1694-3231-8836-9e91af152d47 | -20.53891 | -49.49623 | 2026-04-15 04:51:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a340f15c-8cce-3555-9055-a2996981738a | -21.8885 | -56.26767 | 2026-04-15 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6efc1fc8-3da4-3854-ab1c-8b14cf87404e | -20.53625 | -49.49157 | 2026-04-15 04:51:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46ecad6a-5432-309b-8452-8de0f4bebec2 | -20.22929 | -46.46722 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e50c4b9e-492e-375e-9430-33e4ffc9173f | -20.18139 | -46.596 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86351635-0b43-3a35-8f79-5418eb8dfc34 | -20.18602 | -46.59689 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41eab73b-4e11-397b-b484-390eef4b02a6 | -18.73614 | -49.79179 | 2026-04-15 04:51:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a57dfcf7-d8bd-369d-b484-c9855b66b3ed | -20.22397 | -46.47205 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1ecc673-5d5d-3828-b650-e271fe0c4c87 | -20.18828 | -46.57697 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f67ff00-583f-31c9-810f-2286c23b9ea4 | -20.32814 | -55.00578 | 2026-04-15 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e59cac45-4cca-35c2-bd0e-d6a5d984eceb | -21.69916 | -56.30856 | 2026-04-15 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fc1daf6-6857-316b-9a73-a47354c58b6f | -21.72141 | -48.43897 | 2026-04-15 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c8af44a-e4e3-32a4-b24b-b56c37fe1097 | -20.53821 | -49.5015 | 2026-04-15 04:51:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d8f8ea09-5a97-3723-972e-44804e8b64de | -18.73177 | -49.79585 | 2026-04-15 04:51:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b60d194-2fed-3ecb-9ea1-d65d0ec76d25 | -21.19426 | -48.61179 | 2026-04-15 04:51:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4984db5e-1d4f-3bf7-9048-3249c72068fd | -22.96637 | -52.70087 | 2026-04-15 04:51:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1fd27fc1-5ea2-36b7-ab8e-49359320ce66 | -20.32208 | -55.00085 | 2026-04-15 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3c01baf-ec69-3e8f-8fee-a74658319948 | -22.87844 | -48.64407 | 2026-04-15 04:51:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b76b0fe-54c6-3c0c-8eff-fc46c2cee91d | -20.32541 | -55.00146 | 2026-04-15 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86b77be1-347d-3f1b-9c2a-bb554a96527c | -20.16361 | -56.35591 | 2026-04-15 04:51:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ede3020a-f1c7-319e-95b5-dab4499b3309 | -20.32874 | -55.00208 | 2026-04-15 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ea6975a-c84f-36c2-bf46-f2930c0a3d57 | -21.41715 | -48.61494 | 2026-04-15 04:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3757e70c-4770-3e13-b4e0-d6d8e6f47b81 | -20.15531 | -46.74348 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63cc395a-0a91-3abe-86af-de66b7036900 | -30.27105 | -50.97431 | 2026-04-15 04:53:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| c128caec-6831-38aa-800f-c9f447819c3d | -25.65309 | -50.11904 | 2026-04-15 04:53:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a3a93226-73d2-3917-98aa-96cb0d2859af | -24.23556 | -49.19848 | 2026-04-15 04:53:00 | NOAA-21 | ITARARÉ | SÃO PAULO | Brasil | 3523206 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55beaeb7-6aed-36a0-a9cf-2e8f1943010f | -30.13951 | -52.55883 | 2026-04-15 04:53:00 | NOAA-21 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 55322f8a-34f8-38c4-92cd-2ef996188df6 | 3.23711 | -61.21746 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3581a95d-b1bb-33fb-9be1-46122b72947e | 2.01538 | -61.08598 | 2026-04-15 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd807fe4-f8f3-36c4-a90a-8e5adfae2db6 | 1.10442 | -60.52117 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5336cc66-f292-3a07-b626-b2355a0edd3d | 2.94016 | -60.17629 | 2026-04-15 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cd7a1bf-9e89-342b-935c-68c00041738b | 1.90124 | -61.09592 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91b5cbb2-136d-3918-b3dd-7e696d430817 | 1.14591 | -60.55152 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 031aa50c-5dff-391b-95b1-4a39fa1aa34c | 2.56518 | -60.54907 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5192b42b-875b-366c-a647-3c3a494def97 | 1.91458 | -60.45169 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6db87cc-9001-30db-bb62-9b154d8b3916 | 2.56925 | -60.54847 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 69ca7352-9466-33f4-beb6-952d044abf7e | 1.91782 | -60.57619 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cd6ed0d-a2f8-3799-9cc0-0c39d6862405 | 2.01191 | -61.0863 | 2026-04-15 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e3a760c-a334-3123-84e2-bcdbfb7516c8 | 2.57678 | -60.3269 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667601be-047f-3502-af38-bf0e04277b23 | 2.38606 | -60.89151 | 2026-04-15 05:16:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb1d9575-5c63-30ec-8660-94a005a63f50 | 1.10362 | -60.51608 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f142274f-6b8e-3ca6-a7f7-d2cab57a4095 | 1.90471 | -61.09435 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4babecc1-d50a-3512-8f58-050fad79139e | 1.84971 | -60.64478 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61f49aad-65a2-34d7-9632-73be9484839f | 3.89952 | -61.86977 | 2026-04-15 05:16:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce4d739f-299e-35a4-94ef-efe926f9d83e | 1.10362 | -60.54225 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b38b3c43-df81-3e1a-bb57-7b2b0d72b9a9 | 2.56575 | -60.55269 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a63450ee-b7a8-36e6-a1ce-45cfbe709cab | 2.1565 | -60.53492 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72d2365-e8dc-3962-aedf-256dc3b7f667 | 1.81527 | -60.44596 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1c8cf33-f7f2-3641-b08f-ce68f524fdcc | 1.10203 | -60.53202 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71486aa9-02fd-3b77-b48e-6e77078d37ca | 1.906 | -61.0991 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14dd2d80-0081-34d7-a467-d099be30f015 | 1.10999 | -60.53076 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bc9e40a-ea10-367f-a3b4-ae6fcb0a52a0 | 2.01119 | -61.08661 | 2026-04-15 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd68bf50-e6b1-3d0b-8bba-c7c511491bbb | 2.57625 | -60.32343 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61edaecd-b591-384d-8aed-d2d3d1324c1a | 2.94415 | -60.17567 | 2026-04-15 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e9d0ac4-95e7-3389-812e-59330cf990fe | 1.90532 | -61.09816 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 397f303e-9384-3980-9e2a-d04c081c410b | 3.23771 | -61.2215 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d32c113b-f853-3c91-8260-73695e756807 | 1.10919 | -60.52566 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76307d1b-2544-347b-beef-96b27cd4979d | 1.90542 | -61.09527 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 602a19d9-f9ed-3d9b-a092-c7415c4183a5 | 3.90406 | -61.86904 | 2026-04-15 05:16:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e3c466-fc18-35f5-9725-aeed2d3d32b9 | 2.93875 | -60.17818 | 2026-04-15 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38d048ce-5d4d-312e-ac16-a83f758d74ec | 1.91175 | -60.45124 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36ee44a7-3f10-39ce-838c-0ceafa36fd4d | 1.09646 | -60.52245 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bc2958e-a04f-3d8c-a021-bcdbadce6ac5 | 1.10123 | -60.52691 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b11ecae-c268-3f48-8d88-ee2be984b4dc | 1.14673 | -60.55667 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ed1760d-3329-39e2-847d-2d329dee2802 | 2.94194 | -60.17244 | 2026-04-15 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e659e22d-0c2c-369d-a5c8-33434ff2cb51 | 3.23281 | -61.21814 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0f77de8-f88b-396c-8ad0-8341f70bc4c9 | 1.10601 | -60.53139 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a24d705-13cb-3d25-98a6-9d16ff7ed002 | 2.38665 | -60.89527 | 2026-04-15 05:16:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62bf446d-ec27-3b84-83e7-aa021cf6a963 | 2.57277 | -60.32756 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de897b9-7662-3c52-bef6-99dcfdbddb99 | 1.85376 | -60.64414 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1bfb9098-fb06-3b19-96bb-8809ae179a88 | 2.57224 | -60.32408 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8262677e-aa23-355c-8653-c545c165c7f2 | 3.2279 | -61.21477 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75beb03d-f588-3447-b007-1acee0439ebb | 1.10521 | -60.52628 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3edb39e-1c43-32c4-b83b-393ed332b10e | 2.94674 | -60.17698 | 2026-04-15 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4892c36-fc96-357d-80cf-87b33d3d423c | 1.1076 | -60.54164 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0043dfa-e6b7-39c2-847a-0d8c2ea77de1 | 2.0161 | -61.08566 | 2026-04-15 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4b7caaa-9706-3c2e-86dc-e8dcf8402277 | 2.56982 | -60.55208 | 2026-04-15 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 33ea254b-c215-31f7-a57d-67bab12cfd79 | 3.2365 | -61.21342 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37033902-6d84-3763-8c28-f47d9e48d09e | 2.94274 | -60.17758 | 2026-04-15 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0433aa60-1d24-3c16-9461-ae869625d27e | 3.2322 | -61.2141 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f22ba49-eb67-3239-89da-ea536f06f102 | 3.22851 | -61.21881 | 2026-04-15 05:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36c37cf7-06fb-3169-bd44-d9abc9145341 | 1.10282 | -60.53714 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e5bbfab-3429-3b0c-82b6-dbab47e2db7c | 1.48175 | -60.92178 | 2026-04-15 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bac5bfa-5f55-3e0a-9cad-c2123db493cc | -2.75304 | -54.59288 | 2026-04-15 05:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b889b860-af7a-350f-8eab-e08cbd31ed8f | -11.20259 | -56.8756 | 2026-04-15 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf80770-7a87-32a1-b372-a9a166b0f956 | -11.92882 | -58.07416 | 2026-04-15 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0333c33-7388-3462-874e-aad056a1dfbf | -14.82774 | -59.83377 | 2026-04-15 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87c95aac-9ec1-3101-a659-3d6fd996278e | -11.20567 | -56.87926 | 2026-04-15 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README5.md)
