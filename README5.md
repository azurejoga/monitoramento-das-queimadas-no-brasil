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
| c80f150a-e61c-3929-83de-8b73e8dd3fac | -3.43122 | -39.04554 | 2025-07-26 03:36:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc1e1a53-37a7-3b41-b83a-5576dd7b3765 | -3.05779 | -40.02576 | 2025-07-26 03:36:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 4411c7e2-3d96-3c7a-95ed-84fd3d2f1420 | -4.25388 | -38.04865 | 2025-07-26 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| baa8fd12-d8e4-3a63-8cd2-f027f9af8b37 | -3.63006 | -43.07169 | 2025-07-26 03:36:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b389522-4290-3f87-8543-953b4aa594b0 | -3.59111 | -41.65152 | 2025-07-26 03:36:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 682f7543-f750-3890-a551-db28ae5a9d6c | -3.82589 | -41.57101 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 39b05c97-1950-3d2c-a02d-dfc17fce7632 | -3.82789 | -41.55914 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33c40a84-2853-31fc-a02c-b87689558a1b | -4.0708 | -42.5437 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d8700eb3-4776-3ba5-9759-9b2fa0fe6a7d | -3.82838 | -41.5562 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07c39b64-0b86-3b5a-aad3-e958b1a86b63 | -4.04014 | -42.5134 | 2025-07-26 03:36:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 7fd84931-4455-3d67-a736-e814587f4681 | -4.75728 | -38.48043 | 2025-07-26 03:36:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e7a4a13d-ccea-34b4-9ebf-7113f8d8ed19 | -3.82539 | -41.574 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68a4e65c-63e8-3de8-834f-66f8f9a3d3a8 | -3.81344 | -42.54809 | 2025-07-26 03:36:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7beddd1b-8b21-3349-bb4c-08dddda4b323 | -3.49416 | -43.31431 | 2025-07-26 03:36:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcab78c2-c41c-3a69-97f4-796976a94d28 | -4.03957 | -42.51683 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 3b2844f6-bf86-38e1-a1fa-ac21b20e8e75 | -3.82739 | -41.56208 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 58b2dfce-9ec0-3cc1-971b-1e57ddc26e46 | -4.04438 | -42.52113 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| cd23ed61-6d16-3703-967c-5dfbd17ec4c5 | -4.066 | -42.53941 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ecf8f227-7443-3b25-8b38-55c18a751327 | -3.05759 | -40.02421 | 2025-07-26 03:36:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| b7758358-7952-31df-b11a-59e30cbc21d0 | -3.05318 | -40.02502 | 2025-07-26 03:36:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3bad321e-3ff4-368b-9d33-603572b930da | -4.7567 | -38.48398 | 2025-07-26 03:36:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6fa8ac4d-17e1-3a32-9172-13ed3df0fa98 | -3.43568 | -43.14041 | 2025-07-26 03:36:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af738576-7bf2-343e-b993-d25bc9be5e22 | -4.039 | -42.52028 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e7a4877e-831e-3289-b162-871a41bb7175 | -4.06478 | -42.53151 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 38e74a64-00f9-3fe3-a211-d8e8a745d0b1 | -3.82332 | -41.55541 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3999831-d97f-387b-8ba9-c262a959ce0a | -4.25253 | -38.05054 | 2025-07-26 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 66897971-9486-34d5-a275-845eae93310e | -3.82689 | -41.56506 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cf516c05-8269-39cd-a1bf-a94f1690ae71 | -3.58549 | -41.65369 | 2025-07-26 03:36:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00408eb7-b9cb-38b3-a030-d6b6dd30760a | -4.07139 | -42.54028 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 0a8e04d5-57a8-3877-bb35-90550ca8af4c | -4.06542 | -42.54282 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| afec8941-c374-3854-bd6c-a16ed9c7f2ea | -4.0631 | -42.54171 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 258a7c35-c7a4-3c2b-b2fe-26417b5d3124 | -3.82639 | -41.56803 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4984e3be-4211-31e3-8751-50db88b6cda7 | -3.62819 | -43.07105 | 2025-07-26 03:36:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11ea92fa-c1a6-310b-b16e-2f6ed3a4d3dc | -4.0594 | -42.53064 | 2025-07-26 03:36:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee3a5601-9eb1-364f-a82b-6306282fa965 | -4.0342 | -42.51592 | 2025-07-26 03:36:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e6f8d94b-bcfa-3e1c-ac92-360282d636c1 | -13.10461 | -47.36487 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e372995-c84d-34b5-9ef3-fe6a5c4ae605 | -14.9405 | -46.95724 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c3a9289a-9aa5-3920-996a-19c667e5381c | -15.78738 | -41.32197 | 2025-07-26 03:38:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9fa06ca-8ff2-3deb-aaab-eb35ec2eb56d | -11.11 | -45.12384 | 2025-07-26 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74d14062-6d51-3547-8e7b-ff75cc7a7f34 | -13.11941 | -47.32513 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ea23475-0b4b-358c-82f6-165db1eb15ab | -11.74026 | -48.1857 | 2025-07-26 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 81b17099-7d53-3da3-9eb3-6fd9f1c094a9 | -16.09835 | -42.27822 | 2025-07-26 03:38:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| ac370ad9-89e8-3f32-9538-82d6ba55a05f | -14.30833 | -43.79249 | 2025-07-26 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c5cfbea-c91b-37d2-8849-85e54af4c718 | -13.6389 | -45.70353 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbc744f4-7f7d-308f-86ae-efdd90b7e03f | -13.11167 | -47.33103 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da532407-3599-37f5-bae1-01fa0ff463ab | -13.1247 | -47.33098 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6f712375-72be-3b3d-92f5-60ea587de43d | -12.71619 | -46.27754 | 2025-07-26 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dc267ac-bb90-3f74-a4c3-0518ddeb191d | -9.91994 | -47.76558 | 2025-07-26 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9ff1a63-d1c2-31c1-8f3e-4d3c37156568 | -12.04766 | -45.44286 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b748cc-9e90-3139-8738-f34ff1fe3709 | -13.11693 | -47.33703 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 770cc9d0-b274-3855-99e1-d882ece22d1b | -13.18343 | -42.32403 | 2025-07-26 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a442e22a-60de-3f11-b6df-1855423c0b3c | -13.64076 | -45.7063 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cb3edd8-6778-3409-bea1-8609105207a3 | -12.04646 | -45.43705 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b57e6c85-63d5-37b3-87e3-9946fe68155f | -13.69883 | -45.69515 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d01c1c87-1b9d-32c0-a101-6164555fc07f | -10.59545 | -44.74418 | 2025-07-26 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57dc441e-6fbb-3b49-ab29-e411b6edc696 | -13.69478 | -45.6863 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6a92d2d-eae0-3dd4-aaa4-a06d8454e4d0 | -13.70113 | -45.68357 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 434b9b89-61f1-35f1-bda7-59a3b53a6e19 | -13.11238 | -47.3589 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a28abb41-537b-3e4e-84ce-7a0067f7a287 | -10.36153 | -46.65902 | 2025-07-26 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 279dfa7e-6c0c-31b4-9c4a-78a8e41ed633 | -14.96179 | -46.97348 | 2025-07-26 03:38:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d139d17d-3fa3-3bf7-b028-9f1dd9286a18 | -14.96747 | -46.97585 | 2025-07-26 03:38:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26fb8c74-34ef-3aa4-8c83-c67dabd26bfe | -9.36341 | -40.31046 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| fd125917-0594-3b43-b2d8-8067422bee6e | -14.93948 | -46.9621 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 793dd166-dc7c-37e8-8e29-68779bcb315d | -13.0991 | -47.3423 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65b445fe-f330-3095-8088-89fa32620eb3 | -16.55297 | -40.50658 | 2025-07-26 03:38:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ba049a0-7cc3-3e8c-b1ad-ef28e6d6f4b6 | -13.72562 | -45.69645 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ff9ca74-9527-3db2-9089-35b3a51584e5 | -8.07134 | -48.01754 | 2025-07-26 03:38:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c589d992-495f-34b9-a7c6-be045f12dda5 | -14.93715 | -46.94381 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8a2c34bf-93c7-3dae-9021-5c87a83c8c82 | -15.7867 | -41.32565 | 2025-07-26 03:38:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 59969904-b63d-3bce-98ba-166817235826 | -13.18224 | -42.32602 | 2025-07-26 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 26be4deb-faa3-3299-9df0-8d55a6b1462f | -8.87127 | -45.58114 | 2025-07-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ed2c8c9-f118-303f-844c-dddd499a1362 | -15.3744 | -44.28179 | 2025-07-26 03:38:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e948c428-43ce-30c7-9375-3012523cc506 | -15.87517 | -43.26109 | 2025-07-26 03:38:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5636cb87-b439-317b-8bed-99f479dcd54b | -9.58356 | -43.85985 | 2025-07-26 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 976c9b9f-1b1b-3264-bd69-6e87e7c93a12 | -14.94795 | -46.95113 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0759102b-b11f-34a3-8052-4aaf800f2ad3 | -13.69959 | -45.6913 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7bfa084-5e16-3ab7-89cd-87d78a65148e | -13.69555 | -45.68245 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 302b8770-12b5-3613-800a-3f796cd45703 | -12.04281 | -45.43768 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e129b409-f879-3026-a8fc-f5b499e265e0 | -10.36276 | -46.65282 | 2025-07-26 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a365f80d-d14d-347d-a0f0-710527d3aca6 | -14.95739 | -46.965 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d72cc22-4bbe-3f6c-8ad7-32ee4b88ac01 | -14.13558 | -45.28492 | 2025-07-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9cc47ef-e382-3ab7-92e0-50e6513d916d | -9.47907 | -40.37078 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 9e78a770-e1aa-39ce-820e-10fd6f1bb1d8 | -13.23816 | -40.60362 | 2025-07-26 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 56322aed-5538-35d1-a4e2-7a580d667ec6 | -13.72639 | -45.69271 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10162e08-047b-398e-9058-21ae5eeb1150 | -10.33075 | -39.20869 | 2025-07-26 03:38:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b5af77f8-6426-3015-8a53-0c434d7275d0 | -10.35771 | -46.64532 | 2025-07-26 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61c6ec18-ab4e-38de-8ca2-3285542d5321 | -13.6915 | -45.67361 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 981dfad2-7917-3429-9763-95205659c9a3 | -9.46989 | -40.37331 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f30039e1-bae6-36ac-9924-ba97e44277a3 | -11.73773 | -48.18494 | 2025-07-26 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 48371375-1ca9-3c53-80ab-2a9c08ccb42a | -8.07268 | -48.01065 | 2025-07-26 03:38:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5f9da62-2ee8-36c4-8c45-a1b392e2d353 | -9.35918 | -40.30972 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 0d1c6463-02d2-326d-a91c-15849071df41 | -15.14989 | -46.18936 | 2025-07-26 03:38:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cb0fc59-3d22-3f88-a994-e9b468a09b6f | -14.93617 | -46.94846 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c89811ea-36ca-38cd-b1da-0f9cc0fd81da | -10.62116 | -44.76056 | 2025-07-26 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8174f59e-f6ce-317e-b938-fbc18366d891 | -9.50454 | -40.37525 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c01aa9e5-9e00-38ea-8a06-f482759e62e6 | -13.09256 | -47.34245 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caf1fa13-5d49-3620-95ee-f64d45a68d45 | -13.69227 | -45.66977 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0b8dd2b-329b-3522-a274-024de268513d | -13.0969 | -47.33943 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 244473cc-9737-3855-ae59-49e4c5289cac | -14.94152 | -46.95236 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 7bd40a21-7c28-33bc-bec1-12d68d0ff925 | -9.47838 | -40.37479 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |


[Clique aqui para ver as próximas entradas](README6.md)
