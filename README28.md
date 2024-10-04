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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a6abcd1-16e5-3e43-83da-f77bd74b06c9 | -11.67181 | -47.69481 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ff5f9026-6805-365b-8e1b-9ece8ba0da67 | -11.66188 | -47.69576 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ec49979f-db2a-3a93-b9a8-9ccf872d5ac7 | -11.66105 | -47.70189 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 050a78a4-6b66-3a86-9d4e-7e0576f6b698 | -11.66012 | -47.68432 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 753f7910-f7b4-3b9d-8dd7-d28fb1e4ce81 | -11.6594 | -47.69066 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0d901696-2f50-3b0e-8cb3-0a3e9354043c | -11.39638 | -47.22984 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 27dbc155-6746-3480-a77f-ff07952e1350 | -11.39455 | -47.21765 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2307e0d6-bd15-34e7-bf73-3dbc26bf7fe0 | -11.38437 | -47.21932 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 36c3a747-4add-38d1-8da8-4496ea7cab3c | -11.38253 | -47.20714 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 199a8861-2eaf-3995-a709-00d29eab97b3 | -11.20867 | -46.94846 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d1b58b5f-4e0b-3c2e-a634-470bbe000e83 | -11.20672 | -46.93583 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 82758c1b-fa2e-34ed-860f-076ac756d08d | -11.19178 | -46.97707 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 2a7830c0-4646-3ab3-9e22-eaaf3f7bfa9e | -11.18982 | -46.96451 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dd7e7048-64bb-3840-b26d-7f0f51bd213e | -11.18585 | -46.98438 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| cc9a9a56-bcc5-33d2-a47a-eb6d21da91ff | -11.18396 | -46.97178 | 2024-10-04 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| bf70a823-cb81-31ba-8f83-406afc565a2f | -11.09106 | -46.50109 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 91b3f5be-aaef-39f8-9985-e9fcf906c551 | -11.08902 | -46.48775 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| ce1b5b9b-b220-3bde-9e6d-8ae43dfd52c9 | -11.06075 | -46.51952 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b0ba46be-2e21-3872-9560-ee4d14a282fc | -11.05199 | -46.5342 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| bc2df22d-f8df-3a6d-9967-7d401a297454 | -11.04988 | -46.52069 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a26a90ff-405c-3195-80f7-eddd58b1c56e | -11.03906 | -46.52219 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 67e8f939-80ff-3016-ab30-b6be81bf133c | -10.90593 | -46.63968 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1ca89a7e-7b46-32af-8dc3-bb91865e9c92 | -10.90383 | -46.62606 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 8a782175-4faf-3628-95c7-9a3ee50a3011 | -10.89966 | -46.59896 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f6fd5ef-71a6-3278-8e45-6cc8cded18e3 | -10.8931 | -46.62775 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4f0b741a-c318-3f52-90d2-09367c77ffd7 | -10.89103 | -46.61435 | 2024-10-04 01:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 302937c6-9c49-3d4a-9dea-78c72752d251 | -12.79221 | -47.45221 | 2024-10-04 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8a715df8-0516-3be7-99ba-9b925ea20559 | -12.37631 | -47.6871 | 2024-10-04 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a873ec16-2697-3c09-92b9-b8abbf39a8c5 | -15.20788 | -47.5061 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4bc1dfb9-222d-3ea9-bc56-540127b1d8a3 | -14.80794 | -48.04619 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b20eea6d-fd4c-3cd1-83c6-604e81700199 | -14.80644 | -48.0361 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2ff68a29-0f49-3f61-be9a-7f3086bd19a1 | -14.79864 | -48.04748 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| a01f3649-6f7d-3368-9a5c-bfcc59e91da7 | -14.79715 | -48.03744 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| e4d9b600-c8b4-3e00-882a-60601d1b626c | -14.78486 | -48.01873 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b83906e6-339d-3fba-8406-2855ac4c0d84 | -14.78156 | -48.06018 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c6393196-b348-3695-a596-7cf81e72b645 | -14.77705 | -48.03005 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b3bd0dee-96a0-3ee6-aa39-7e9bf676e00d | -14.77556 | -48.02005 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 839c9c40-410e-3f9c-b5cf-b326c6f9842a | -16.01152 | -47.82164 | 2024-10-04 01:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1212be3b-99de-3fe6-8470-90616637eb3c | -15.62273 | -47.19803 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 090232f7-fab1-336f-a66a-e5d92101c2d1 | -15.61479 | -47.2105 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 306d991d-8ce8-3fd0-80e4-e13204f7b7fd | -15.61314 | -47.1996 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5b37ab6a-e437-3455-bf3a-924c279fe02a | -15.41887 | -47.68401 | 2024-10-04 01:09:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 01143ad7-2348-35df-bbce-65622e8fdccb | -15.41732 | -47.67363 | 2024-10-04 01:09:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3fe214a0-ec51-3dcd-8cc3-b2eec00fa62c | -15.2495 | -47.49276 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e33ff972-0ff1-3caa-ba21-891941feca8b | -15.22685 | -47.50311 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9d950e37-3297-3f4e-a422-e27737f2ad38 | -15.21903 | -47.51585 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ca5584d0-c312-3d44-9b41-cea46bee090a | -15.21733 | -47.50436 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b0e53124-f18c-3013-89e9-84eb436915b0 | -15.17155 | -48.07446 | 2024-10-04 01:09:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 781847f2-08b0-312f-8fad-334eb7439bb3 | -16.70242 | -48.64133 | 2024-10-04 01:09:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb349eb0-f2de-3225-bbaa-d4ae747aa6e5 | -16.70106 | -48.63192 | 2024-10-04 01:09:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1c4d927c-a5fa-3e61-b0b5-8fd64c6aaf3e | -7.8083 | -47.47913 | 2024-10-04 01:09:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 97b87491-b16a-3823-8783-379a3a641a87 | -7.38785 | -47.2806 | 2024-10-04 01:09:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 410d18f2-2a38-3611-810d-c7683ecc3f06 | -7.11919 | -47.87164 | 2024-10-04 01:09:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3829efa5-b71b-340d-925a-441402de9fd4 | -7.10692 | -47.86084 | 2024-10-04 01:09:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a70a62c0-9365-3af5-b51b-c0b585f5a2ea | -6.72894 | -46.95941 | 2024-10-04 01:09:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ad819ce3-07e4-3302-8aae-50acb19367b1 | -8.53486 | -47.16217 | 2024-10-04 01:09:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 68a8e0fd-fcf8-3f1a-a408-b20b85328494 | -8.43231 | -47.12108 | 2024-10-04 01:09:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2ad41720-3309-3197-947c-5beba110e713 | -8.35989 | -47.5425 | 2024-10-04 01:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ad63bee9-803b-3ea7-9a92-11027767cf7f | -10.5632 | -49.02297 | 2024-10-04 01:09:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6c684d80-7165-3edb-ae36-b2b952eb65b1 | -10.73971 | -47.63295 | 2024-10-04 01:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 818f491a-3e04-38ce-936a-787dbc1ab2ef | -10.59741 | -48.12467 | 2024-10-04 01:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 66cba140-635b-3ad5-9d64-1f5f64fc9b7e | -10.52436 | -48.03642 | 2024-10-04 01:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 230673b7-61c6-3509-b64c-6ebda25c024f | -10.28856 | -47.69929 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 38bea253-a5d8-3852-a73e-6bae72a64668 | -10.27792 | -47.69468 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 030012bf-7475-3291-afd5-3ad3559eba90 | -10.27671 | -47.68907 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 10536212-40a9-3ad5-b7ab-26bc0e1d2c2f | -10.23306 | -47.73798 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bb42b1ee-4403-3e1a-b414-abedb476b32c | -11.32379 | -49.00151 | 2024-10-04 01:09:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 64715e78-71bd-3ee7-acaa-ff27d41d161e | -13.51788 | -48.61493 | 2024-10-04 01:09:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4734e0a-7999-3f55-9117-3147dbeb98a7 | -13.51644 | -48.60508 | 2024-10-04 01:09:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37fd5862-ad9c-3eac-9ac6-8d6c1978d8b9 | -13.50726 | -48.60638 | 2024-10-04 01:09:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3fbf6d24-0a7c-3e48-80e0-7c69648d37d5 | -13.50237 | -48.63701 | 2024-10-04 01:09:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| aaddef55-2b71-3d21-bf02-9cca0cfed52c | -13.22732 | -48.64848 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 107ad0ab-a873-3a45-87a8-8e0778b820c4 | -13.22589 | -48.63876 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d3fa3ea-e013-36d7-b3ff-05b742bc0ba4 | -13.19351 | -48.67373 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3568e444-4e81-33d1-a90b-c9f3c6ca1310 | -13.18682 | -48.68074 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ac04ef70-d1da-36f5-849b-8b8888dc8fc4 | -13.17978 | -48.63216 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0d5690fc-f5a8-390e-84ba-1cb86b7b20ed | -13.17627 | -48.67266 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b559f058-5b20-397a-8aa0-6b00f396d6cc | -13.172 | -48.6432 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 268d355d-4514-3fd8-9d2f-8e5d41b2bf9d | -13.17058 | -48.63347 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7e2a1e84-0109-3f6d-86d6-b0577b7c0b34 | -1.58599 | -48.03611 | 2024-10-04 01:11:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f00f14a4-e735-374b-a6b4-c478222fa022 | -1.58485 | -48.02972 | 2024-10-04 01:11:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f03b1a99-ef7c-34de-ad59-27dc45f556c6 | -3.40732 | -47.5955 | 2024-10-04 01:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7c4ade2a-52c5-3e89-bb07-117ac9f7f1be | -2.33607 | -47.97709 | 2024-10-04 01:11:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e26f5dc-e2ac-3591-aa3e-8616b99fa88b | -4.02829 | -48.92138 | 2024-10-04 01:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0ade3b83-b466-3183-bb3f-0547743f406e | -4.57265 | -48.01606 | 2024-10-04 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ea8008b4-82f1-31d3-9f5b-1f33df8e1970 | -4.08992 | -48.49523 | 2024-10-04 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5469f8a2-ffe8-3569-b328-eb424582cd46 | -4.08811 | -48.48271 | 2024-10-04 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 298964da-0349-3b5a-8f9e-c3ec6e43eec1 | -4.08628 | -48.47011 | 2024-10-04 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 092c2aa2-d599-3d64-8e97-617dc797f410 | -4.07946 | -48.4967 | 2024-10-04 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5cd52ab4-e26d-3622-8c09-01e1cbd48ad7 | -4.07763 | -48.48414 | 2024-10-04 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 16fbbc75-809d-38f5-bf0f-896b5e913105 | -5.79574 | -49.32716 | 2024-10-04 01:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 226cb001-1f83-38bf-990b-e8c42db7bb7b | -5.50802 | -48.81896 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f8c5a7cc-2fee-323c-b05a-62c84e3e11d5 | -5.50634 | -48.80745 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 1aed3bd8-3c87-39cf-acf5-3277adc162d5 | -5.48828 | -48.96099 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6384f4cc-2415-3a73-97fe-05c75fb4bf12 | -5.48808 | -48.967 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5d4f29bf-a29c-34f0-b2b8-e1a424eed8f4 | -5.43869 | -48.9052 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2abe4e48-6cb7-3d00-bdde-4c5ce80d4c76 | -5.43705 | -48.89384 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8b7e41e0-d467-3ea8-a76e-a5355a3e0294 | -5.30162 | -48.11192 | 2024-10-04 01:11:00 | TERRA_M-M | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1828fc15-25eb-3205-bc7f-77249bc43654 | -3.3093 | -50.45499 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3cb68cf6-e4bb-368f-a548-d94e041975ec | -3.30372 | -50.46162 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |


[Clique aqui para ver as próximas entradas](README29.md)
