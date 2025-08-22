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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 052a5ee3-757f-3d82-8dcd-dea5536d055f | -18.88105 | -45.04212 | 2025-08-22 01:07:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1ea47f93-f142-3777-8d2a-2cfc08b975af | -18.8892 | -45.03369 | 2025-08-22 01:07:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 3b5cbd11-d419-3787-9318-72cce2c6d6dd | -14.7812 | -59.65657 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fb2856d3-d7db-3335-af51-fa79ac29b7c6 | -14.7567 | -56.03368 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e2692358-f16f-39d5-a53a-7bc11f5ca52b | -16.78561 | -47.66537 | 2025-08-22 01:07:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| e0dc0d0f-b47c-3f9e-91b1-e27e2683d454 | -14.77067 | -56.00367 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a35a6c66-1a1b-3ba9-bb30-7d94b69ad67d | -15.00419 | -54.84344 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a4c7ddc2-ce34-349b-b5d6-664f50e125a9 | -19.10384 | -52.86464 | 2025-08-22 01:07:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6f93b0e-9a3b-3165-ad2e-0948ac43c2fa | -13.43769 | -57.17002 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1f173cee-4cfa-3c87-8324-fecfb442366a | -14.64662 | -54.85675 | 2025-08-22 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7b55399d-0a7b-320b-b653-063849aed90a | -13.00281 | -45.21154 | 2025-08-22 01:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 86bcb0cb-3039-3061-8b57-15f6d954f176 | -14.32845 | -53.10465 | 2025-08-22 01:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 99fcb77c-9a84-3634-826f-2e6817d80668 | -13.34508 | -54.39564 | 2025-08-22 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f1df17a-ba61-32aa-b5d5-32b5687fe2c1 | -18.88236 | -44.9988 | 2025-08-22 01:07:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 674f5283-68ba-37fe-a1c5-89a61adbef56 | -14.88391 | -47.94009 | 2025-08-22 01:07:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d7e18935-b843-3de2-a536-b542b1e2602a | -15.66387 | -52.69743 | 2025-08-22 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8b909df6-4fe0-3996-84cb-ba52b380b578 | -15.55977 | -50.32391 | 2025-08-22 01:07:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 70753708-c7f9-3fc7-8c76-ff59bab21b18 | -13.428 | -57.16824 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 862b2d88-f72d-303d-8073-5cc7199deb4b | -9.19413 | -59.63999 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 20bd6ccd-6810-3c90-b9ff-cda1c4b91974 | -5.4419 | -60.16866 | 2025-08-22 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 33f6e52d-7e83-32b1-aa52-4bc756993f3b | -6.6288 | -58.54517 | 2025-08-22 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3040698f-c23c-325d-92b1-8976dad9ee84 | -6.57751 | -51.11813 | 2025-08-22 01:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 38ddc9f1-247b-3c65-9898-6d1dae78e108 | -9.17345 | -59.70937 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0c651e08-79ca-31e7-812c-7faa8f49dff6 | -6.45383 | -53.38943 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c50b680c-fa76-37d9-bf4d-cd27fdbd4dcb | -7.58321 | -63.44096 | 2025-08-22 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 002eea28-1585-3f62-b05f-fcd2b3a796bb | -6.87659 | -59.82177 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 195271dc-7f53-34aa-bec3-7dadb25a5779 | -5.44332 | -60.17907 | 2025-08-22 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 10c7b735-c13f-3e43-8a4e-316ef77531a2 | -9.88141 | -60.29174 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3b5ea957-7d3c-38f0-bdd9-df1b1a7615d4 | -9.51682 | -60.55279 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7a3de041-b972-3554-b2b6-449a842da1d7 | -7.30072 | -59.62886 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 5d498e65-2748-3aa0-8d52-ce396e1fc1ab | -7.45865 | -59.9468 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5753ec5f-9d48-3eb0-a305-f7f523e5d388 | -5.87842 | -53.63869 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d929b607-fe15-3900-9c25-f36cfd80594b | -9.10137 | -61.42788 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 0286bf7b-8c9d-3012-9a58-04768b8c331b | -3.55564 | -62.08075 | 2025-08-22 01:09:00 | TERRA_M-M | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 92c31e1a-ee77-3345-9c2c-3567b554a361 | -5.89365 | -57.75147 | 2025-08-22 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec2c2b77-48b9-3c9a-8040-397425c59ccc | -9.15555 | -59.59686 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e347a23b-7c77-3ac4-bd4b-e77442f7e7fd | -12.99295 | -56.87667 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 58f8a0a6-d6d3-3e08-9569-25514254f0df | -11.91668 | -50.53732 | 2025-08-22 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 9cd57278-a02f-3f5a-bf2c-5b37652ca77c | -8.87507 | -62.42051 | 2025-08-22 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 96f22349-7aee-3f64-ab6d-cce59060db66 | -5.13239 | -56.98167 | 2025-08-22 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de2e3f18-5dbc-3b04-966f-5d8fda8380f8 | -4.32463 | -55.12887 | 2025-08-22 01:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| bdb18ba3-7559-31f4-a55d-f032087e09e6 | -8.88695 | -62.41903 | 2025-08-22 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9a9d9c7b-591d-3cbc-9fcc-42eff93f8eae | -9.17204 | -59.69844 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 821e8c0f-4830-30c1-81d9-bf9565d16501 | -9.19273 | -59.62931 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 946ec5bc-4095-3f12-9e74-39b9b3361fcf | -9.1595 | -59.60101 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| bb3acc56-445d-31d2-9e4b-17b0cfeda197 | -5.88604 | -57.76155 | 2025-08-22 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fc086868-035c-3568-bd70-501b84a4bf86 | -4.1003 | -60.66927 | 2025-08-22 01:09:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d232d780-7d96-3e7b-98f2-838a20dc6ba9 | -5.79862 | -59.2149 | 2025-08-22 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9cb9a09d-4403-3e1b-aa67-1aed4a24f5b4 | -9.51359 | -60.52784 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 20a07a6c-eedb-33a3-8bed-f52fcc0a5213 | -6.44324 | -53.39107 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 721a8b57-daa7-3833-bfab-bb74f92445c7 | -9.51521 | -60.54031 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ac6041f7-3e86-3bf7-925b-2ff80944b5e8 | -9.20051 | -59.46486 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| bcb53819-b1ed-38cb-ab2c-1827f3aa6740 | -9.31075 | -57.01534 | 2025-08-22 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3cc441f-8d79-3652-81e1-f271892b15aa | -9.52556 | -60.53893 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5ce39296-2455-3efb-8acc-0f68e7ca752b | -9.18445 | -59.64147 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8aae4e3c-261a-3e3e-90d0-eca268f9ebd1 | -11.3161 | -55.22017 | 2025-08-22 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f2b0d549-244c-337c-85d7-79c39d425a5e | -10.4971 | -53.57708 | 2025-08-22 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0956b2d9-d8d7-3f54-990e-d992f76ca62d | -6.44745 | -53.38338 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d2aa65c4-d9ef-3b50-8a81-d71733d9d708 | -6.90093 | -59.89763 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2ad25b56-2230-3f21-bf0f-2a29e13fd9f8 | -6.44126 | -53.37795 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a9c970ae-524c-30b6-811e-a8e903317ae7 | -4.55506 | -55.96149 | 2025-08-22 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5281dec9-4c37-3365-9f75-523445307d3c | -4.09885 | -60.65858 | 2025-08-22 01:09:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf57684b-2373-322e-8f6f-9c59aef3afc2 | -7.05174 | -59.82821 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ff751eb-d32a-3db5-a7cd-2fa142fbc771 | -4.88982 | -55.98725 | 2025-08-22 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1d10c8d7-9c94-3469-9a0f-5d820011cb00 | -12.97635 | -56.8884 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0cadc087-c906-3d36-8b1a-e7fbc699b172 | -12.48645 | -53.80867 | 2025-08-22 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 66da2e95-e2eb-3305-bf12-8d5c36242a6d | -9.21011 | -59.46357 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 70f00bf2-5539-34bb-ac14-a3df99dc3569 | -12.50167 | -53.81105 | 2025-08-22 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 080564d3-5c76-33c4-9e8a-96910ef586b6 | -9.1032 | -61.44204 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a9090da4-238a-359a-acd0-ed37873360b4 | -8.89306 | -62.41249 | 2025-08-22 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 99229346-6754-34b3-9f3d-d970daa59149 | -6.44934 | -53.39654 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e5760a8c-dee6-3d79-bbac-dd433beef2cf | -5.87654 | -53.62588 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 682509cc-c8f7-38f6-a290-d705c90c6504 | -6.16347 | -53.76991 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1cd7a1a0-fc4c-3a71-bbef-d4a0c923b5b5 | -6.70365 | -51.41784 | 2025-08-22 01:09:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f3f47492-1ec0-3756-be06-b07e8b1ee889 | -5.80775 | -59.21359 | 2025-08-22 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d22166b6-07c7-3ae7-a44c-6e8d83b52f5d | -9.18305 | -59.63071 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f560acf0-ae09-392c-a51b-56301ed4b6d8 | -12.98652 | -56.89633 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 90c08d51-f2e5-31ce-b982-1d219d7bd4a4 | -5.87599 | -57.75398 | 2025-08-22 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e266c610-56e1-3b77-973f-cc021a70a37b | -12.98528 | -56.88713 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f1bca844-5633-3913-b5bc-bd62938a37b6 | -5.80904 | -59.22313 | 2025-08-22 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d3417183-95cb-3a43-8d67-5acf1ed70b8e | -11.32588 | -55.22185 | 2025-08-22 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e63043c4-7efc-3543-8ec5-f1eed704478d | -9.31198 | -57.02425 | 2025-08-22 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a4e9e095-5656-3043-879d-07f79410ef06 | -9.21877 | -60.79105 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 710dc14c-b41f-3cd5-8473-e4020d1fddba | -6.2783 | -53.70899 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cef3d9e3-a5c5-322c-8ff3-38ad2485a2e1 | -9.17056 | -59.61046 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 14d584bd-15be-3eab-8ad4-f5902cfc0475 | -4.55643 | -55.97115 | 2025-08-22 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4d1d964d-b77a-3da7-8324-a89be030c263 | -4.83337 | -55.77349 | 2025-08-22 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9223b48e-75a4-36a4-885e-585e0693aecd | -5.88706 | -53.62444 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4e1f93ee-face-35ae-aa4c-704313a7ce2e | -11.89973 | -55.88945 | 2025-08-22 01:09:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f34fe286-9874-36d8-8295-aac3212ae814 | -9.17883 | -59.59832 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 68317383-b8c7-300c-b3c4-071f3c6d62bd | -6.89082 | -52.86363 | 2025-08-22 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4e387754-743c-3c3a-85b4-5e829f6de87a | -11.7423 | -58.31337 | 2025-08-22 01:09:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 569dfcb7-20ef-3a1a-868d-7fc93f8495c3 | -5.88482 | -57.75272 | 2025-08-22 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 55a99f80-eec2-3789-b522-1b6c3cba880c | -9.5925 | -55.34938 | 2025-08-22 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fc1fb00c-c7fe-3196-8e38-722f1f1698e8 | -9.2087 | -59.45301 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1e8a4186-9050-317b-b036-b3594fea433e | -9.58473 | -55.35643 | 2025-08-22 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c436c1ef-c2e8-34a7-94d0-1da4a41a97d4 | -12.9942 | -56.88586 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 665ba8fc-d85a-3f4c-95db-cb9d20c41a5e | -8.89513 | -62.42931 | 2025-08-22 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8fefc734-365c-3aa9-8b13-fa898b212ff6 | -7.29934 | -59.61862 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6fe7d2ff-34e5-39f1-bb74-40331da35068 | -11.901 | -55.89847 | 2025-08-22 01:09:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |


[Clique aqui para ver as próximas entradas](README4.md)
