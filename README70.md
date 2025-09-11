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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37225c89-cd74-3859-9e96-1c41c3a62664 | -11.41838 | -43.53875 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6e97dc0-2219-34f5-b080-a7ab21cf9d25 | -11.02419 | -44.64691 | 2025-09-11 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0177369-6b08-30e8-881d-cc2e03d9f10f | -9.45241 | -46.42048 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0c07be59-9c6e-3730-9f08-501e6b2b93cd | -11.7433 | -46.53008 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2458ffc-a6ec-3373-879e-a9dd6e0c038a | -11.35572 | -46.50324 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cc5e1ce-3ba8-3274-a5e5-77cff803e9e7 | -11.37792 | -43.51771 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad01984d-fe5c-330f-9346-20d05cf3d344 | -10.08396 | -48.18234 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef1ba209-01d1-30e6-9f7f-9d1422a37493 | -9.99989 | -51.70702 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c22cf73-32e6-3fe0-a92c-0a25110918aa | -12.39176 | -54.16527 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4e62d06-a852-3c24-9930-f3ee86b04ff4 | -9.06838 | -47.06552 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07cb2700-08e0-3231-bfb4-d67f57117953 | -11.45604 | -43.59622 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92f9ada3-53b9-321a-bf20-90d2c1344821 | -13.16301 | -45.28922 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b98dd0c-8ff2-3f1b-9ef9-72170a088893 | -10.00786 | -51.71286 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b3726ad-b34d-38f1-b805-6581c9701c15 | -13.04533 | -48.00098 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 979626a0-23de-37ee-92ca-cd6a08e24811 | -9.51716 | -54.65022 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dee433f2-9ef9-3276-9ef4-8df297d8c3f5 | -12.09864 | -51.01534 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fee3f16-d239-39d5-be2f-012422526141 | -10.44357 | -47.77681 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe02150a-b791-3af8-96fb-4d6ff9378460 | -11.48783 | -43.6317 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 974c321e-c630-3ae3-8031-0124500f5764 | -11.15859 | -52.03041 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07d63403-9ad7-3482-8035-bf9a7b9a8e39 | -13.661 | -45.73223 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3abaacf-1154-351a-b9d1-dee0dfe9935d | -15.23048 | -44.02033 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f20e56bc-2c47-35b4-9e4d-8d83b27d54e0 | -12.84626 | -52.94579 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f72e04fe-47e0-3683-971e-6f638f2a710e | -12.06435 | -47.58789 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac0ede5d-2a6f-3a49-92b6-5f8072739996 | -12.94066 | -54.81607 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfdb7bf9-ca3f-3821-92d4-d230a41b88c1 | -12.41496 | -44.71856 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38b31ede-eace-351e-b2ca-deec3c6b86ac | -11.31969 | -47.37746 | 2025-09-11 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96961b39-0ba7-34f8-9a87-5dedba58eac1 | -13.85874 | -47.3615 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54d472e7-7b91-358c-b830-6e21d7025195 | -12.58845 | -44.78714 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 558f4204-4427-38fc-8a11-0f9717de8aac | -14.13813 | -45.3945 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 044e0adc-c431-3a55-ae33-5ceed384943c | -10.1769 | -46.19086 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 640f8289-1f59-3ee4-a22b-b885c5ece407 | -9.67847 | -47.5279 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a03071d-9824-35a1-b890-de2db80f3d78 | -9.08245 | -47.08722 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f06f31-c69f-33fa-9440-e947f4e3c0d7 | -11.38022 | -43.52601 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4136a8d-d7ef-3b0a-9263-56b9e17c3cff | -9.98876 | -48.38029 | 2025-09-11 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc7432ad-5002-32d8-bc6d-ba51f804d211 | -13.84035 | -47.34747 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec58b68b-6ea0-3445-850e-fac430d70dff | -9.7225 | -48.09654 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6c202c6-5a6b-384a-a635-c2b6251c4fb1 | -10.55438 | -47.23001 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6f3e6e5-a3eb-3423-b06a-eec4edad6500 | -9.90672 | -49.91526 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2686e7-2c80-3a11-8d30-737c049b0beb | -12.24994 | -47.33099 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 886ade42-74c0-3866-b0f1-f77797644809 | -12.96528 | -46.73447 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6fa30f7-3454-3f56-a210-8ab4de13ddff | -10.32279 | -48.81496 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 823d89a6-cdda-3cd3-91d1-ad3527ab0edf | -10.2668 | -43.8293 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ffec14-3a71-36ec-a96d-9c27d7ff840f | -15.2034 | -44.03848 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a83d3c5-b530-3369-898b-9bd585b87fb4 | -11.45893 | -43.60061 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ccdf014-6bb5-3c52-ae16-075c326c79fe | -11.02588 | -45.05675 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 43694c1d-7147-3609-976d-78aaff2d7914 | -9.12096 | -46.97914 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9adde8f9-ad67-3edf-bf19-9f29082e7cab | -12.96326 | -54.75435 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c037d9b-b114-3927-ad17-82a82fa506a4 | -12.01396 | -47.59868 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26b1c314-2625-310a-bdf0-b9e529a38937 | -12.93291 | -54.80169 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 311067c0-7a82-3c4e-890e-e49f9985e438 | -15.2464 | -44.0353 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 84465cfa-5b3a-3091-8e38-cae6a91f62ba | -10.27182 | -48.82861 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2560b6d-66a6-3b43-b3a3-b2447319c156 | -11.43056 | -43.57642 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbf56a44-339a-3923-a0ee-dfa03357f202 | -14.56822 | -48.76941 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3790568f-3b94-3b7e-81fd-4671054fd44a | -11.43172 | -43.56866 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1f69e5a-343e-358f-9a18-b62ecf1fec32 | -12.55679 | -44.65458 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2c16ab6-4429-33c0-90e2-dde1e684b3eb | -12.92417 | -54.78028 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15cd838c-37e7-37f0-b20f-fa8644f13f5a | -12.88072 | -47.95678 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d0125c-6ad3-335b-abbe-025e68d9788c | -10.26165 | -48.82226 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e251b884-53e4-3482-b847-a385be89369c | -10.31034 | -48.79982 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 81e20602-bccf-36ac-ab0c-867909ef4179 | -11.49135 | -43.65588 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37deb9df-d8be-35c2-9b78-79ea0e72962d | -11.39067 | -43.52763 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3715121-214b-38d9-891e-266e32c125c4 | -14.14149 | -45.39505 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69e12c6c-64f8-304f-8623-7484c75337f0 | -14.22773 | -43.08916 | 2025-09-11 04:23:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 95dbe59a-f884-3be1-bcba-d37a41743e6d | -11.67967 | -46.88298 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da1de73e-9322-3a9a-af17-15521d88febd | -13.29258 | -43.7556 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51d24ea1-45cc-34be-af53-c1b2ffc398a3 | -10.39726 | -48.5714 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82b8fa30-4cc8-3bd8-bb0d-fc72755047fd | -14.40078 | -47.31923 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de073c87-b88b-3772-98de-e2acc5a2e116 | -11.15709 | -52.03889 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21ece54a-9d53-3573-849e-938ac6144a0e | -9.08805 | -46.96586 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c909944-51a7-3d51-b3da-77e0479fc5f7 | -12.12518 | -44.85262 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0495592-5a7c-3c04-8c1a-2aedf9ebc4c2 | -9.70019 | -46.87582 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ed8307d-44ad-3557-8fbe-c05af7ff5375 | -9.00972 | -49.52821 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52ddeae4-5584-3dd6-932e-8eb0c50a137e | -12.84144 | -47.96609 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c262fea6-e397-364e-a302-a9523561ddb0 | -11.09277 | -48.43198 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 514a3e4d-3db0-3100-9b8f-8f14b0f0b2c1 | -10.54912 | -49.88553 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e9c4c840-4c3a-3670-9a1d-0095305bb420 | -10.88426 | -47.15521 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 95fd565c-d33a-3d70-be6c-3696a455a81d | -11.48494 | -43.64003 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e61bdcd-3a95-32a2-84dd-62c55282bc65 | -11.44794 | -43.57913 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c8df584-bf1f-3e2c-8f9b-973a684a93ed | -12.97334 | -54.75663 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d976a7f1-4017-3f57-97ca-c5d9c15691a5 | -12.1336 | -44.86506 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7699503e-8b08-35a8-866e-7e83dd651c43 | -9.44789 | -46.4271 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7d6782a4-156f-3f22-b671-b6a6d13a282a | -11.36168 | -46.56244 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f3148ac-4c1c-3c36-85d2-474b21b6a04d | -12.47156 | -47.49214 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e067cdd6-c0f8-3869-bd3f-2acadfa68e41 | -9.71534 | -48.33728 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b54dfd6-213b-3b6f-8298-841dff950d91 | -12.9317 | -54.80787 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 440ff744-48ff-3474-9645-1d4c6cf5e60d | -11.41084 | -43.54155 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cc89521-8840-384b-aa21-3d377d2b9f82 | -9.08465 | -46.9652 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efd03d7f-b10d-363c-a657-8d9f860bcf7c | -9.75159 | -47.85706 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b797a9f7-fa77-38d5-bccf-5105d71dbae8 | -12.0164 | -47.58377 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6693d1d3-378e-3e3a-ad33-95d012c2bc1a | -9.7551 | -47.85762 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c850672c-868a-3129-8ecf-3d2892ed8b4f | -11.64361 | -46.91394 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1b53c3b-1c35-3102-a388-9531dd60ffb7 | -13.98506 | -48.23547 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3087abf7-acff-3ab7-b2e4-48db43755f20 | -14.91556 | -47.313 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98d6b5b6-b6db-309f-916b-0748d7c3a340 | -10.65504 | -48.63471 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5475d3e5-bb17-3630-927a-1b688355aeba | -11.37095 | -43.51663 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38ae9002-db8a-330e-9834-8a54c037ec79 | -14.41079 | -47.32103 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ae5ad0f-5bed-38fe-8105-c573f05829d2 | -12.88574 | -47.96896 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 282dbc23-6141-3ec7-af92-66d7268913da | -13.51018 | -51.78523 | 2025-09-11 04:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcc8d422-0c65-3324-97b8-2becfc73eae0 | -11.79243 | -50.57936 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3d1774e-2c9d-3877-8cdc-2a54f64e98ff | -12.96195 | -46.73391 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README71.md)
