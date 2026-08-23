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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5ac112e-3840-3680-8291-476ceab4553a | -12.2999 | -43.1781 | 2026-08-23 14:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 235.5 |
| 4c391b52-4483-3350-b360-d53124335c41 | -11.8497 | -51.6859 | 2026-08-23 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 44adf9a7-3d45-386b-9cf4-8ce7b221f82f | -13.6614 | -51.8535 | 2026-08-23 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 8b2319be-d4d2-3e09-a924-c5fa46d99d9b | -10.6928 | -47.7171 | 2026-08-23 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 5ff3b1ab-f5ae-3405-be79-b349bce9f745 | -8.5028 | -54.8827 | 2026-08-23 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 847ebab2-3c90-374d-8aa8-91bb781a0f44 | -13.6999 | -51.8487 | 2026-08-23 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e4e078de-681f-31c2-a884-1e1f373ec0c9 | -5.9628 | -51.9579 | 2026-08-23 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 8358c347-eae0-3766-add3-791bf3ca983d | -13.6617 | -51.8323 | 2026-08-23 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6780ed12-2558-327f-9823-c6adda9c87b8 | -9.0526 | -45.9393 | 2026-08-23 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3131d125-2153-3f2c-98d6-f98f52bc6faa | -9.5181 | -60.5075 | 2026-08-23 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| ec524f0d-9591-3d24-bbdd-15e15af59c98 | -9.1331 | -65.9746 | 2026-08-23 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| ded72353-b0da-305b-8efc-fa51488a810f | -14.3365 | -51.7662 | 2026-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 58bed13c-7ed3-3a1c-bc24-6b2d7dd0aac7 | -10.6738 | -47.7194 | 2026-08-23 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ce70016e-4703-36da-b636-bfa3da3031b9 | -14.9586 | -52.6614 | 2026-08-23 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e34a5535-e19a-3836-8198-93fb1f17a414 | -13.4904 | -51.7475 | 2026-08-23 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0f244282-3d12-380f-beaf-6c4249ff9b03 | -14.3168 | -51.7901 | 2026-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fd757157-896d-30f7-a7a7-ea5624288103 | -13.1694 | -51.4471 | 2026-08-23 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f77301b9-5af2-33c3-8202-9593e183ae29 | -11.9872 | -45.5187 | 2026-08-23 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| dd15baea-7f68-39f6-be92-106f758a624b | -11.638 | -50.5625 | 2026-08-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cf34ec37-4ca6-398a-80b6-870ad49e3aa2 | -16.0706 | -50.4332 | 2026-08-23 14:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6b449ebe-2064-3b8e-bbb2-ff9f7512046f | -12.8554 | -48.4541 | 2026-08-23 14:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| de4f2775-4c14-3bb2-860f-89410b7c251c | -9.4996 | -60.4892 | 2026-08-23 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ffef2c92-464a-3768-aea7-0b0c0ab2d1b9 | -13.2078 | -51.4423 | 2026-08-23 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9f011cc0-0d7b-3d1d-b6d0-2967ea3bc313 | -10.7512 | -50.254 | 2026-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 01b320b1-3f6e-3f4c-97b2-347158b33d52 | -10.4905 | -49.9604 | 2026-08-23 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| b3e972f9-f959-3971-99db-55fa82ca7fb2 | -14.3275 | -53.4577 | 2026-08-23 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 0a5bbd85-e8cf-3836-94aa-d630872bc87f | -11.1542 | -46.1824 | 2026-08-23 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| bec7a3f5-fe6c-32e0-97f8-f34b7493f6aa | -9.0529 | -45.9167 | 2026-08-23 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 1d0d47ac-0b61-3762-8c52-d81c38504915 | -12.0559 | -50.5996 | 2026-08-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1ab3eee6-c747-34ef-9317-6b6edd30f1b4 | -13.896 | -54.0092 | 2026-08-23 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 38241f44-1d47-39a9-aaea-0152e6b03d6f | -5.9442 | -51.9589 | 2026-08-23 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 74dcbbeb-a0f8-3029-b140-ecf99d859c75 | -10.3292 | -45.4028 | 2026-08-23 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 0aec41e5-5ac0-39fc-97d4-8c11d5ee9911 | -10.4905 | -49.9604 | 2026-08-23 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| f69d2ab6-a208-3ccc-b14d-817fcf74c513 | -10.6738 | -47.7194 | 2026-08-23 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| b7aad068-bb23-3c92-8733-e5abd76d9d0d | -7.6665 | -63.3261 | 2026-08-23 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ff52bb8b-591e-3786-9017-e275b9d7d126 | -12.2999 | -43.1781 | 2026-08-23 14:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 039d8873-296a-3c56-8da0-7004eeba3bfe | -7.0193 | -48.0106 | 2026-08-23 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d7c6827a-3a75-3d3f-8a27-dd708203733d | -14.2572 | -53.0468 | 2026-08-23 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 7cbfbe85-09be-3ef9-8930-ff537646ab3c | -16.0509 | -50.4363 | 2026-08-23 14:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| ed494f4d-1873-3da2-b274-218f7cd0764b | -13.1694 | -51.4471 | 2026-08-23 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 50154398-28a3-3c7b-b3e2-7f6a2aa74182 | -9.1722 | -59.4629 | 2026-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| cbf5d40e-b53d-3667-9dc8-bf483520c0c4 | -16.0514 | -50.4144 | 2026-08-23 14:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9f2128c3-ac16-30b2-ae0a-275a8395cfa3 | -14.3554 | -51.785 | 2026-08-23 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| fb47f202-38cc-3b48-ad59-e601789d6d90 | -6.5232 | -51.4488 | 2026-08-23 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2ec60756-a918-338a-bec7-f23fe15be98a | -14.4126 | -52.9643 | 2026-08-23 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bb5be32d-478d-3bcf-bd0e-8807da4b216c | -9.5183 | -60.4882 | 2026-08-23 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 782a8d92-8524-33dd-a55a-cee4fb759e9a | -7.1498 | -42.7926 | 2026-08-23 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| a9ec65d8-18bb-3e47-b8a2-a0723fe7b1fc | -9.4996 | -60.4892 | 2026-08-23 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 78df8da9-c3f2-36e1-8aee-27b278fb8d05 | -13.896 | -54.0092 | 2026-08-23 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3a4ed0c4-38c8-316b-8148-895619a1b4eb | -8.579 | -54.696 | 2026-08-23 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8e871e9c-ab76-322c-8d08-15ab115e9dfd | -9.1721 | -59.4823 | 2026-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 793703e3-8145-3100-955c-d698f736cfeb | -10.7512 | -50.254 | 2026-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b9fba414-dca1-36a3-a466-6ffe7b32df0f | -9.4995 | -60.5085 | 2026-08-23 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 263.1 |
| 424326ad-c29d-3c18-8221-f0e11ed23052 | -14.9586 | -52.6614 | 2026-08-23 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| e03165a5-7144-34a8-abc9-0e4cd5ea55d5 | -9.5181 | -60.5075 | 2026-08-23 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 35ddfdbb-0c16-3287-b0b3-0698f1ae3fee | -10.6928 | -47.7171 | 2026-08-23 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| d3654768-0694-3006-84da-c4d0e70bebf1 | -10.6925 | -47.7393 | 2026-08-23 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f6b59166-1d66-32c2-ad0e-18afe05103c6 | -11.8497 | -51.6859 | 2026-08-23 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 8ba4f97e-86f8-39e8-881b-32b3b9dd884f | -6.7162 | -52.8824 | 2026-08-23 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d257af40-8693-3470-8fc0-74cfcf870998 | -13.6614 | -51.8535 | 2026-08-23 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 2f009f51-840c-3720-a893-26c38fd15b17 | -15.6955 | -53.7878 | 2026-08-23 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 2b3e7366-016a-3888-b6ed-90c893e11004 | -10.8364 | -50.9479 | 2026-08-23 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1761ba05-4857-3c76-9a3d-4f1407e3a585 | -10.3902 | -50.3984 | 2026-08-23 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 1e40d90b-f635-3f72-8730-7e3cd4905334 | -12.075 | -50.5974 | 2026-08-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e25eef32-e233-3ad4-be0e-399ee7fb1ea0 | -10.3292 | -45.4028 | 2026-08-23 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| bcd7d12e-dc94-397a-bb3f-9889804348ac | -5.9442 | -51.9589 | 2026-08-23 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0020fe1c-90e1-3fb5-8d61-a8c3c461a130 | -9.1331 | -65.9746 | 2026-08-23 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| da5651c4-7546-3ca4-aaca-816782205dbf | -13.6617 | -51.8323 | 2026-08-23 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c3b93bfd-a4b2-330c-abee-ae182ec13332 | -13.6806 | -51.8511 | 2026-08-23 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 213.6 |
| ee5f59eb-96a0-3d36-ba18-b23584d000dd | -11.85 | -51.6648 | 2026-08-23 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 8e84d9ec-13d7-3b9c-8115-f0b2f30d62ab | -16.0706 | -50.4332 | 2026-08-23 14:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e7df1731-4725-3607-9dc3-22666daf6e0f | -14.3558 | -51.7636 | 2026-08-23 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 904462cf-c1d8-3e45-8202-af1d5e9ff8fb | -14.6155 | -53.5271 | 2026-08-23 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| d2faf052-9b03-3e24-a01f-a9c51111c097 | -9.1332 | -65.9559 | 2026-08-23 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 96bb51d6-6386-3bdf-b154-9a3d19b3ee27 | -10.7702 | -50.2519 | 2026-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 8e0f2509-4df6-38e7-9ac9-a333d1ca73e7 | -5.9628 | -51.9579 | 2026-08-23 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 07668eed-2952-3ab8-8f42-00ab48d205b9 | -14.3275 | -53.4577 | 2026-08-23 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 297.3 |
| 81dfae67-15a6-36f4-a811-034c34cb4ddb | -13.6999 | -51.8487 | 2026-08-23 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d18ba643-66ae-3b94-8eea-2ea29ef87f2f | -9.1517 | -65.9554 | 2026-08-23 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4852503e-1df9-3f58-82eb-0787c67873df | -12.5576 | -47.9419 | 2026-08-23 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7b446a06-de5b-39d3-ad40-ab1186d71c08 | -8.3481 | -46.5058 | 2026-08-23 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |


