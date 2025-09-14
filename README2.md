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
| 93308155-ba18-3a5d-91ec-be0834cca003 | -11.2541 | -44.7723 | 2025-09-14 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d427dd05-9438-3845-8da1-3a360f93aa04 | -12.7863 | -48.0209 | 2025-09-14 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| a28d264c-2e12-393d-ada3-e3381ac9a634 | -11.3111 | -50.8548 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| df8d6aa4-5211-3a50-9b62-7171cf258e24 | -8.9551 | -46.175 | 2025-09-14 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d9315028-bd0c-30fa-993a-f626dd28e272 | -11.2349 | -44.7751 | 2025-09-14 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4bc7d01d-63f9-33a0-a5fd-5266e4a4f4f1 | -11.7011 | -59.3061 | 2025-09-14 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e2af760e-6fc4-33cd-836d-6d4e533a5c50 | -23.1538 | -47.5765 | 2025-09-14 00:20:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 1f9a1618-ead8-35a3-a1d6-6e9ba2f86355 | -17.8165 | -40.1636 | 2025-09-14 00:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| cd421650-7d26-3e4d-bdce-9ebb3809a0d4 | -3.5908 | -58.577 | 2025-09-14 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3f6c26b7-a1cc-32f7-883b-431a90322097 | -18.7282 | -51.7816 | 2025-09-14 00:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d5f0d3c6-a7bc-3119-b76c-455bccedafc3 | -3.5996 | -47.4923 | 2025-09-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 67566de7-6812-368c-a411-ec4ad39a9c85 | -10.9167 | -45.5546 | 2025-09-14 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 70c19ea8-3339-36dc-8626-37784bb055a4 | -12.7867 | -47.9986 | 2025-09-14 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 8c1920c0-2598-3d31-96a8-083a7ae89d30 | -8.9737 | -46.1955 | 2025-09-14 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1ed1d3ba-4bc1-3e46-be55-57cf4ddd659a | -17.7962 | -40.1692 | 2025-09-14 00:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| f547df82-8a6a-38ca-b9ba-f3acb4db15d3 | -10.8976 | -45.5572 | 2025-09-14 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6b198731-40ff-32f4-aa7a-ac53c7b947fb | -21.6462 | -50.1109 | 2025-09-14 00:20:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| e798e86b-a34e-3c51-8557-39a8d0ed83c5 | -11.3114 | -50.8335 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d7f6e726-871a-3f93-a40a-ce8f51a90e04 | -17.4106 | -40.3254 | 2025-09-14 00:20:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 100.5 |
| 696db59f-729b-378a-b46f-c6e94c7fd2b7 | -3.5995 | -47.5142 | 2025-09-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 284.5 |
| b9eb58c6-8a0c-3da4-9a31-4a24a1dc3305 | -21.6662 | -50.1293 | 2025-09-14 00:20:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| 9ea56cf7-e1a6-3db7-953b-f2a72ce75bb5 | -11.3491 | -50.8507 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 38b4f92f-edcc-3525-ac2f-365fd98a047c | -12.9294 | -54.7333 | 2025-09-14 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 6b1e6d52-24d2-32b1-8f0b-ed00b591cee4 | -11.3304 | -50.8314 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 8c12d51e-ec6a-3630-a3f7-2ec7aa26ad16 | -11.3494 | -50.8294 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ed48aca1-d42d-309b-8be9-25add82d4ee0 | -3.581 | -47.5149 | 2025-09-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 42755b57-8192-349b-b24f-4e96b2a25f8c | -11.3491 | -50.8507 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 769560fe-ca43-3635-a320-4bda9e71bb0f | -12.7863 | -48.0209 | 2025-09-14 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0827253e-d9cc-3056-9732-448a25e7d6be | -21.6668 | -50.1064 | 2025-09-14 00:30:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 59d2196a-0234-300b-b6cc-b0a6275c8b77 | -8.9548 | -46.1975 | 2025-09-14 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| aac579ee-fee9-3514-bbbf-03bdddb5cab3 | -21.6443 | -50.1797 | 2025-09-14 00:30:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.4 |
| 1639bc67-2697-34ca-9609-a4fa74e7d1f3 | -12.6639 | -54.6577 | 2025-09-14 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| ca3fffac-311e-3461-b8c1-f5f9ae0b7b99 | -11.7011 | -59.3061 | 2025-09-14 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 49556a58-7cc7-3374-bfbb-16f4a7c94bd0 | -21.6462 | -50.1109 | 2025-09-14 00:30:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| d8872a89-c90d-3774-adb0-c27dc8dee533 | -10.7579 | -44.7721 | 2025-09-14 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 4c34e9e0-6213-3992-abde-8889e769917b | -3.5908 | -58.5963 | 2025-09-14 00:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7d6493f6-9297-3738-b1ff-a9abf9f5216f | -12.7867 | -47.9986 | 2025-09-14 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 420d2408-07b0-37e0-826e-4db22af22255 | -11.445 | -50.7762 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4a87659a-2046-35fb-81c6-f090e678de26 | -11.2349 | -44.7751 | 2025-09-14 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d239a9ac-cb21-3a4a-b1dd-672c528185b0 | -12.9294 | -54.7333 | 2025-09-14 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 8175b486-f3ca-3413-9422-ab8a659231b5 | -3.6181 | -47.5134 | 2025-09-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 789b2471-6ac0-3f36-9fe2-f073997d0266 | -11.2541 | -44.7723 | 2025-09-14 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 3e644e66-36a0-32c1-bee1-7718b9ef8003 | -3.5994 | -47.5359 | 2025-09-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 110a1d75-f594-31d2-8baa-15cea6e746d1 | -3.5995 | -47.5142 | 2025-09-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 265.7 |
| 911408cc-c5fc-375f-9928-981217c06a1e | -3.5996 | -47.4923 | 2025-09-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e669073a-d99f-3ee0-9c35-51d6db1fe90b | -11.4637 | -50.7955 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 85ac4a48-98bb-325d-be52-63ec61755dbf | -11.3301 | -50.8528 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 6d488829-78b3-3dd0-a181-213f860eb1ae | -18.7277 | -51.8035 | 2025-09-14 00:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d0cbb036-1973-3211-bd49-620f400571f5 | -18.7282 | -51.7816 | 2025-09-14 00:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 433a86f0-bc46-31f1-86c3-b6b8239d0193 | -11.464 | -50.7741 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a374864b-0955-3673-a206-9e21c8061b3b | -12.6826 | -54.6763 | 2025-09-14 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| e688915b-e3d2-3a11-89a1-b3aaa0e2f4b6 | -18.7082 | -51.7851 | 2025-09-14 00:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b813998e-c503-3357-a737-b5b6b53fd46a | -8.9551 | -46.175 | 2025-09-14 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| aa200109-9fe2-3a87-b3e9-d2fea41a9146 | -10.9167 | -45.5546 | 2025-09-14 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f25e0584-4e20-35df-b722-10a25831f457 | -12.6636 | -54.6782 | 2025-09-14 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| d35bf7ea-fe80-39ab-8d90-aee41907eca9 | -11.3114 | -50.8335 | 2025-09-14 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 61b55ea3-d54e-3438-a300-78d8e4afe778 | -10.9163 | -45.5775 | 2025-09-14 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0b6df633-709a-3562-9856-0ae5322d0b1f | -10.769 | -46.4583 | 2025-09-14 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 52daff91-5c24-32b4-b43a-eea5c738e90f | -10.7579 | -44.7721 | 2025-09-14 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 790efeb5-1660-370a-a010-6cef2028a71b | -3.5994 | -47.5359 | 2025-09-14 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6055a3e8-42ce-31e5-9823-6452e8ff103b | -18.7282 | -51.7816 | 2025-09-14 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 22ba097b-3dba-33ec-abe0-9701cf641b57 | -10.9163 | -45.5775 | 2025-09-14 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c26832b3-9f7a-3a42-b72b-d59371861406 | -12.6826 | -54.6763 | 2025-09-14 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 189.3 |
| a2541e05-0541-3ae9-bdec-925ddb964d38 | -11.3304 | -50.8314 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 8b9e2a36-a65e-3bf5-bde2-3e0b2031e59e | -11.4827 | -50.7934 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6fd6d7c7-7b15-3523-8ec9-d691e88b4b2a | -12.6824 | -54.6968 | 2025-09-14 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| f7acd5bf-800c-3ce8-8be1-bccbca076a10 | -21.6436 | -50.2026 | 2025-09-14 00:40:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 0778d7e3-a07c-3b4a-9e81-65068f512c37 | -10.777 | -44.7695 | 2025-09-14 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1be0a818-994d-3a1f-96bb-5fb2583249d4 | -11.3494 | -50.8294 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 23998c46-067b-3747-9be1-c259962b13da | -13.9283 | -44.8341 | 2025-09-14 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 11539548-affd-3c2c-b525-17edfc105afc | -12.7863 | -48.0209 | 2025-09-14 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1364ce7f-b392-3b30-8c57-f3364c95a4f6 | -10.5937 | -44.331 | 2025-09-14 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 43a09496-7f84-3b60-9051-37d895153465 | -3.5908 | -58.5963 | 2025-09-14 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9664a161-f6a9-3e4e-b2f4-e47d2bc09ccc | -17.3119 | -46.0954 | 2025-09-14 00:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f120d921-24e7-35f1-bdc6-3250cb021350 | -12.6633 | -54.6988 | 2025-09-14 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 7a403798-a798-3e51-8d1b-3b849d63cd9d | -11.4447 | -50.7976 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1a8b1ca9-c762-3c05-b272-f84facc990f9 | -11.7011 | -59.3061 | 2025-09-14 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| fc869715-6936-37b4-9062-4b1160a8e6d4 | -11.4637 | -50.7955 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 077e3641-2aa9-3179-9044-c776ec8e2144 | -11.3491 | -50.8507 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 7b56a9e4-8172-3028-8f68-7a6c873cb892 | -21.6668 | -50.1064 | 2025-09-14 00:40:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| f4301f53-df1c-365a-822f-ce72f5ba9dd4 | -11.3301 | -50.8528 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 31f680e2-0690-342a-a694-0676f771c336 | -11.464 | -50.7741 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 7381d06d-4821-3add-bdfe-2f80025f3b07 | -18.7082 | -51.7851 | 2025-09-14 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e9d4fe39-8358-373a-9db1-9a1479e8bbfe | -12.4541 | -57.7872 | 2025-09-14 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| cfa10b81-1e5f-3c5b-b5d9-360dda5b91b0 | -18.7277 | -51.8035 | 2025-09-14 00:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a4485721-d7b5-3a34-a8e5-a5d4f4fafa12 | -12.9294 | -54.7333 | 2025-09-14 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 1938001f-12d3-347d-8c82-9f6ed13aaacf | -12.6636 | -54.6782 | 2025-09-14 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 290.4 |
| 8efcc226-3349-3ba7-976f-59b833fee45d | -10.769 | -46.4583 | 2025-09-14 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b910238c-2f38-39c7-8344-585bd0cb22e7 | -3.581 | -47.5149 | 2025-09-14 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 126b9b48-ab97-3f75-9ef0-9e4ec3991490 | -11.445 | -50.7762 | 2025-09-14 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 774a2acf-f81e-32a5-9fd6-4a0e79f0aa82 | -3.5995 | -47.5142 | 2025-09-14 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 241.2 |
| 7249e9c4-cd32-382f-9de2-ed849c3b18b6 | -3.6181 | -47.5134 | 2025-09-14 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 08af07d3-35e9-3ac0-a0e3-16e7a7b51fa0 | -12.7867 | -47.9986 | 2025-09-14 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| fbfc16b0-ac27-3e5b-9201-3e3840066cf5 | -11.3301 | -50.8528 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e88a4c32-7b62-37d4-8fea-aa4253a9b843 | -15.6364 | -44.3924 | 2025-09-14 00:50:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f74baae4-1d64-3c2f-8612-951a3539461d | -15.6369 | -44.3685 | 2025-09-14 00:50:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 4263b6a8-898d-3a09-a637-bf9d53b0709b | -3.5994 | -47.5359 | 2025-09-14 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9e211cdc-ad04-3390-82b7-cbee8010112d | -12.7863 | -48.0209 | 2025-09-14 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 115e1b18-abfc-3c1e-8699-83f6aef51ec3 | -17.3319 | -46.0912 | 2025-09-14 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9c2f0cf8-225a-30b1-8405-47ccc2166ae9 | -10.7579 | -44.7721 | 2025-09-14 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |


[Clique aqui para ver as próximas entradas](README3.md)
