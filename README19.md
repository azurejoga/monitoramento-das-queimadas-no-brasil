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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e51f88a9-f396-3aad-b8e8-048ad0e5d12f | -10.05 | -36.21116 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3075f318-6ecb-313b-b9a5-6aee870c9994 | -11.31072 | -45.21188 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf59ddd9-5da6-3229-ac4a-004fee2cb92a | -11.31314 | -45.20489 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a4fd834-adb1-3d27-aa09-a7dca485f039 | -11.30876 | -45.18709 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 694843c7-4008-3174-9b80-78f5746822bc | -11.94718 | -45.06389 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcc8cbd1-b710-3903-9b38-16ba82b6aeee | -10.81957 | -42.36819 | 2026-09-01 03:36:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0250d658-d720-3b8d-8678-fe8c2c298122 | -11.30856 | -45.19213 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03c53656-d23b-3844-9283-d56ac0e5ad34 | -10.03596 | -44.69473 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d12a57ac-d16c-3642-82e5-b2ef89306e1e | -11.48482 | -45.09536 | 2026-09-01 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 462eeab9-fdce-3487-870e-08d6251e2a2c | -11.32164 | -45.16328 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b7baddf-f78e-3f7e-91de-e95a9dc12c3b | -8.42169 | -44.99648 | 2026-09-01 03:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69351b07-4ef6-32ab-b2de-18dcd538fcac | -8.41439 | -44.99585 | 2026-09-01 03:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 373644cb-a87d-3f21-8cf7-9d0efc00abb6 | -11.91004 | -45.07243 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce78a05c-e67b-3e44-9c74-1a5c6c569b7c | -11.48061 | -45.08133 | 2026-09-01 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0891082-1971-3a7a-9b04-3bac1504ba27 | -11.31209 | -45.20543 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea13192f-2cd5-3cb8-b010-61da33ee1fbc | -11.31333 | -45.19952 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59b1a1db-a024-388a-b31f-5a953ac86c93 | -11.31005 | -45.18102 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7c50f89-db43-3c41-bdbe-eb11885cb7db | -11.30935 | -45.21841 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5423626-7b1b-36c6-920f-0d2eba980385 | -10.05308 | -36.2171 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 65038ff6-7673-367d-9637-e86eafe6dcee | -8.84259 | -36.53091 | 2026-09-01 03:36:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 956b7b58-e580-383e-995b-c84537f7c84e | -10.05797 | -36.21261 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6bf14e58-196e-3671-8053-65e4a4bf5e7a | -10.8663 | -45.36371 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fabd0113-0756-356a-97ff-2e7f35d1c009 | -11.31947 | -45.17042 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4d29c19-9e93-3313-bced-b250e02c8506 | -10.0278 | -44.69976 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 628cdd9d-7abe-395c-ac98-f55560eca626 | -12.20967 | -38.98452 | 2026-09-01 03:36:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad2a1853-fbe5-3f7c-9a51-c299f13f98d3 | -11.32082 | -45.16405 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07d4480c-069e-34b1-9c80-af52a518564c | -10.03032 | -44.68748 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92d0f506-f62b-3b73-9cf2-96c63b883f89 | -10.02263 | -44.69316 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 66131081-b5d6-3c5a-9d4e-cffe5945a947 | -8.48697 | -44.73949 | 2026-09-01 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f9ae377-c290-3ddb-ae3f-5f383261050f | -11.31784 | -45.18191 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11f51eca-5149-329b-8e94-e1b57c519ded | -10.86893 | -45.36392 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 769b2001-033d-3792-a6aa-4d2c9f9efc4d | -11.94034 | -45.069 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 233d0dfc-fffe-3e5d-b97f-e042971aadbd | -11.30971 | -45.18652 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bd02fa5-546b-3738-b358-56eebfd1ce11 | -11.48344 | -45.10197 | 2026-09-01 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f51b2a4-590d-3c69-aa78-3f807a6dfb87 | -11.31435 | -45.19899 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82dd16ac-823c-3435-ac9a-c914211b1908 | -11.37025 | -45.23043 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c574079-f040-31f3-a8b9-3440a613b573 | -10.0364 | -44.69556 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe35cde4-591c-3095-83f2-a95f3aa91e37 | -8.48948 | -44.74549 | 2026-09-01 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5730024b-34bb-3012-8982-39dd1c059db1 | -10.04691 | -36.20526 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3125879f-9c02-355e-9d1f-77d0302ff79f | -11.30758 | -45.19268 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7713a93e-56ea-3f3b-8995-f7eee76e988d | -10.0509 | -36.20596 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 8e3042c7-7b71-3aa4-a530-0f0ef7841b63 | -10.03073 | -44.68824 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c075f63-c00a-3ead-8e9c-6730561a526f | -10.86326 | -45.37828 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 987551e1-a323-3d5c-81b1-37dc4a4135a8 | -11.3293 | -45.15786 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab9c2e14-7cc8-30af-bdcd-d6319c577f83 | -11.49165 | -45.09681 | 2026-09-01 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6a47ab7-fd9b-3fff-9d1e-3b8e541bdc7f | -10.05398 | -36.21189 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d444398a-bff4-3ee6-af30-064b7a4b6625 | -10.81872 | -42.37249 | 2026-09-01 03:36:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| fe6b6ae6-9f2a-3894-818b-3501567dc945 | -11.25978 | -45.11547 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ac6f866-75ee-3db3-b7fd-176f5f0be8b5 | -10.86754 | -45.37078 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9aa9aa87-fede-37c6-9f76-896f454d9889 | -10.87324 | -45.36551 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 562de160-09b4-3d43-8b05-1d4daf676a2e | -10.15834 | -45.76102 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c553d2ed-4ae7-3d4b-a3c0-d94594741e17 | -8.48562 | -44.74639 | 2026-09-01 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc5b8dec-15fd-3b4b-8ccf-b2a98586371d | -8.84675 | -36.53156 | 2026-09-01 03:36:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f5aaafd-e8ba-3c85-a9f9-6c5e596371e3 | -10.02907 | -44.69357 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68cf708a-2e2f-3db1-b04d-149a1b950428 | -12.21054 | -38.97969 | 2026-09-01 03:36:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 815c3a10-445b-3e44-9c56-67e2b48171bc | -11.31819 | -45.17652 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 411d0991-c119-3ffa-aad9-22506dbe8a13 | -10.03468 | -44.701 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89e90d66-8474-35ed-934f-b929a26d097a | -10.05488 | -36.20667 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 78dc5935-25a9-34fc-8f37-5feeff4305ec | -10.15671 | -45.76888 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6f3d1a1-897c-3beb-99df-4f4d87abaf80 | -10.0491 | -36.21637 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7081c967-73a2-3c63-bd53-73e8c2a9bc91 | -8.94552 | -38.00513 | 2026-09-01 03:36:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 037dae0f-286b-35a3-97b2-bd66fbfe3a1e | -11.3301 | -45.15698 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df7d60da-abad-3e22-94c8-a51fa92fb55b | -11.94843 | -45.06429 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 365d3161-ed58-333a-bcad-5f3bbaf97c27 | -10.03516 | -44.70187 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aeeab14-86c8-37f2-a814-0f0fa46da07c | -11.93913 | -45.06862 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceea027b-59f5-37e0-b3d3-e6e79a741ef0 | -8.49512 | -44.75383 | 2026-09-01 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c657f75f-1afc-3ed8-9451-f3d574052461 | -10.04601 | -36.21044 | 2026-09-01 03:36:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 27c1c421-f6a8-3a41-8557-f42a1ea2ed69 | -12.09884 | -44.98574 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 55c5d0c9-9b3a-3485-86ed-e99e86e2120d | -10.16404 | -45.76995 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a040683-ef41-3f3a-91cb-79b05a8c5d3a | -11.31692 | -45.18251 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84e5f6e6-f589-3090-91d4-9986b6726dc7 | -8.08564 | -34.96305 | 2026-09-01 03:36:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8b9d74cb-554a-3497-8e92-bfc72cb40d0b | -11.48745 | -45.08271 | 2026-09-01 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab80dfdd-0e3d-3e5d-9d9d-1989b25ca9b6 | -17.38512 | -42.36645 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aafe471-849c-35e2-a3c0-53aabb496126 | -17.3781 | -42.37919 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afb98abf-8314-316c-b7c8-a54ef931b477 | -17.38746 | -42.35533 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 62e6b062-7f85-3189-91a9-85a5bdfe2824 | -17.39343 | -42.35737 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e4c1dc7d-9a88-3e69-80c2-667a578823d0 | -17.39262 | -42.35671 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d11ceef-f31c-368e-8985-da01db7d9cdf | -15.2117 | -46.22624 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7deb153-9a5f-35dc-af41-18dec66a4f6d | -12.95394 | -45.97174 | 2026-09-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58025e6b-fa20-3ef4-86f2-04b5f68a7aff | -12.0721 | -44.98574 | 2026-09-01 03:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 676bf65d-b5ad-329c-bd10-50f192224b78 | -13.3507 | -43.67448 | 2026-09-01 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f08d8270-5f57-3501-95a4-1700e8245a7b | -13.34429 | -43.67599 | 2026-09-01 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df95c8fe-b4d4-302b-ad1b-ceece5a65e13 | -17.53996 | -44.61256 | 2026-09-01 03:38:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b829ce4-d5e3-360e-b7d2-5e6caa78db72 | -12.95536 | -45.96512 | 2026-09-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40243d5c-bd50-3516-bfd3-b941b05f4a9f | -17.37929 | -42.36819 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 194ce382-6408-35ae-9f1d-75306afb9895 | -12.09358 | -44.98388 | 2026-09-01 03:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 849ec702-d385-3fa2-be59-b5e599d35997 | -17.3802 | -42.36889 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea13a65-8f1a-3136-a6b1-61c1a078410e | -17.37297 | -42.37757 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75220b38-b675-36fb-b653-5504d030950a | -13.35038 | -43.67733 | 2026-09-01 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb3c168e-1d89-37c8-9023-2e34d4a33222 | -17.38588 | -42.36285 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d7559a7e-31b3-3484-bde2-3e47240c2f94 | -17.39342 | -42.35292 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4f5628f7-9eca-3151-9e20-30171abd6d7b | -19.39035 | -40.87418 | 2026-09-01 03:38:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 206c2895-05f6-3103-b487-14aba4d14315 | -18.30697 | -45.08476 | 2026-09-01 03:38:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a463fd5-d944-3222-86cb-da429f044c6c | -17.32314 | -42.70296 | 2026-09-01 03:38:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3404667-6697-3c33-9453-ce76e1705dfe | -15.67377 | -45.91225 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83ed4a49-f20b-37ce-ac18-c34bb92b15d6 | -19.39147 | -40.8685 | 2026-09-01 03:38:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7aad967c-e68e-3248-9406-2de475c8ec01 | -12.10022 | -44.98571 | 2026-09-01 03:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9400f94d-d9a6-35f8-8022-5692153b664a | -16.36651 | -46.88107 | 2026-09-01 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d93e2e5-8111-3f47-a772-2e4738472784 | -17.31911 | -42.7049 | 2026-09-01 03:38:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f4ec6ec-a318-3356-9365-c00e0c472a60 | -17.79463 | -39.70682 | 2026-09-01 03:38:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README20.md)
