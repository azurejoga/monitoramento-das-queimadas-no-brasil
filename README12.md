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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef826699-cfb0-3e01-b348-b2fb858ea083 | -11.27352 | -44.65104 | 2025-07-29 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1bdc9d0-48bf-3036-92c7-40ba094b48f7 | -9.5838 | -44.46283 | 2025-07-29 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e7c8f34-312f-3619-b53b-37aeb352b062 | -12.00153 | -46.96751 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cce6f5ca-8f7c-3a16-9ae3-cc4951c49c24 | -11.42566 | -45.12646 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a73c6395-8ae0-365a-ad93-b8f061a2de50 | -13.0888 | -47.31898 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b65c9d3-1846-3bd4-9a0d-03649d1c34df | -13.49006 | -45.60297 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49852a12-a862-3ca4-8f03-25818a7cc516 | -11.74684 | -48.18674 | 2025-07-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92d05e7c-9f52-3779-8afd-389463b1e541 | -11.42899 | -45.127 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 75f52b5c-16dd-31f1-bef4-cea114b278da | -11.98254 | -46.96088 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20823797-bed9-32f1-9f1f-f3236920637e | -12.94895 | -44.73642 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39189eb8-bc16-33e7-a10a-688546c4ce07 | -9.62816 | -48.55275 | 2025-07-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6f3e07d-aab2-3c8f-a7a1-229032ab1a71 | -14.37782 | -50.32982 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 922790e9-47e2-3ff5-8ccc-25b8facf50f6 | -13.07138 | -47.34227 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b7dbeb4-1e29-32af-9430-84d95c29433e | -11.34582 | -51.24986 | 2025-07-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4031f0d-8f5b-31b8-aba6-15e11b9971a6 | -9.57674 | -43.88403 | 2025-07-29 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d5648bc-9ff0-387c-97d9-a5b73382c380 | -12.94273 | -44.73165 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ef7c69-d7a3-3727-abc8-8038171013f1 | -15.81807 | -41.89081 | 2025-07-29 04:21:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff412b72-88a2-3967-ac5c-f971ee19eb81 | -10.62845 | -45.22884 | 2025-07-29 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42b41dc6-f774-38ae-ab1f-9d329bb2fea1 | -8.88738 | -47.34253 | 2025-07-29 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85d83527-9909-303b-87cf-c74189ca73b1 | -9.27184 | -50.25621 | 2025-07-29 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9e6da0-d16f-3b0f-964a-c52a19d4d0c6 | -14.507 | -46.54406 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9695916b-c974-3620-ae9e-836a0b5bf798 | -14.74498 | -46.30239 | 2025-07-29 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3c24708-6696-31f0-b5f6-05e6ea66abbe | -13.10627 | -47.3809 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41c4fee6-95a9-3d4b-aa58-36c374dcfe65 | -11.96384 | -46.69241 | 2025-07-29 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f6d0f81-4d0f-3a35-aea0-b031ba949693 | -11.97921 | -46.96033 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45fc9cb2-1396-3c1f-be2a-1ec58d865ba7 | -13.76595 | -56.12251 | 2025-07-29 04:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2dc6b6a-45d3-3ac9-908d-adb484628dd4 | -11.74747 | -48.18295 | 2025-07-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fb57d9d7-15b0-32b4-b717-afae8964141b | -11.98649 | -46.69975 | 2025-07-29 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23943bfc-8949-372a-bb88-8c11bbc1938c | -14.00272 | -44.62234 | 2025-07-29 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc12a659-69b4-3e51-9f2c-d22ec9d7a90e | -13.00251 | -44.89525 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19220aca-9c8a-3ca1-9240-17a55449878d | -8.95044 | -46.7517 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b9a06ab3-e60c-3f88-af17-b471ae779b0f | -10.81561 | -46.68192 | 2025-07-29 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83367e60-3714-3ae9-b85a-fe1a2ef8fc50 | -10.71595 | -49.4826 | 2025-07-29 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f887523b-2d0b-3c61-aef5-0b15a97bb955 | -11.43232 | -45.12753 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 346dd9a1-bc07-3949-806d-f52bd61c0ee5 | -8.49618 | -47.61374 | 2025-07-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccda905c-6c7f-37da-b38a-ff5924cc22cc | -9.36547 | -45.7422 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 503041eb-b4f7-3de1-b12d-9674da2ee598 | -11.43511 | -45.13161 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9229d8de-337c-3402-82c5-21e7a01927c5 | -14.5048 | -46.53642 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba5a5b8c-1571-3365-9c02-4364984c385c | -15.12309 | -45.33219 | 2025-07-29 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a350afd-779b-3620-91db-4ee1235f034d | -14.31708 | -48.64899 | 2025-07-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 984cb47d-c48c-329f-96a8-aa2213f4c94f | -11.96328 | -46.69594 | 2025-07-29 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4cb9ed2-e243-32b9-9178-b5662d4e7ab5 | -14.12593 | -45.27994 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78b9d627-1650-3acd-81d8-bdba32c1d949 | -9.99963 | -48.12687 | 2025-07-29 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 44f078e2-2e91-3513-bef9-10a4a19e30ed | -10.42716 | -47.22178 | 2025-07-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d5f2ab8-d7fa-3f4c-b837-919833a2c23f | -15.12647 | -45.33273 | 2025-07-29 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ac1a2df-ffcf-350b-a13f-f35976a2253a | -9.08433 | -50.84777 | 2025-07-29 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6019f6e-4cdc-3fb9-aa2a-04cd17fc7801 | -11.43124 | -45.13462 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 27eac524-317d-300b-8b26-9c53eff7678d | -12.00267 | -46.9604 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c98adac-8c31-3774-833d-edc21203bcca | -14.1321 | -45.28467 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 943c82a8-03dd-31bb-8621-2d021c76f652 | -8.94429 | -46.74702 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e2b97d86-be67-3d6c-a297-2a346c2beba2 | -13.49953 | -45.63018 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0163612-7c8e-3a62-9120-54cc125710f7 | -11.34113 | -51.25277 | 2025-07-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a08856cd-a5e8-3dcb-a0a6-7869b338f149 | -14.50424 | -46.53997 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4468ae3-a336-3947-bc8c-6970040bb519 | -13.49785 | -45.6189 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a463215d-a7ae-3334-924e-06779dc14af3 | -10.05175 | -46.56494 | 2025-07-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98cf60f3-72d9-385a-ae65-7410d63a362a | -9.36599 | -45.71732 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 705f68bf-30bb-3179-a891-e04006904d2e | -13.49727 | -45.60043 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdff1256-4952-399d-a86a-2c8f7560e52f | -13.11626 | -47.38267 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47007e8d-9218-3da7-a16e-dbe787997a25 | -12.40907 | -47.78424 | 2025-07-29 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d72c3b74-6595-3dce-b1f0-635310247454 | -9.58769 | -44.4598 | 2025-07-29 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b99eb1d3-e7af-3682-b5f9-d637ade59d3f | -14.02238 | -40.98285 | 2025-07-29 04:21:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b512008-3f75-3273-8f83-b6395a416b88 | -10.00311 | -48.12748 | 2025-07-29 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4323c1b3-f0ac-3940-a2ea-25f48f7146f3 | -13.10569 | -47.38452 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ff91e4d-c690-3a60-b1c8-57defb03b83d | -11.42512 | -45.13001 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bc8259ca-6476-3b2a-ba8f-bbf88ef16960 | -13.00754 | -44.88472 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 234ce567-73e7-3274-b361-3de7a4af1699 | -8.74999 | -48.04201 | 2025-07-29 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08944bec-226f-3409-a4a6-6e52ff232f40 | -14.12929 | -45.28047 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd53f516-433a-371c-a030-af180267902a | -13.13808 | -47.3498 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38fde0e3-7ab5-30c8-bf4c-667197717f6e | -16.55377 | -40.50885 | 2025-07-29 04:21:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6318b39c-b1a4-3d01-8689-b9f1932021e7 | -11.69296 | -47.43299 | 2025-07-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9b82266-5cfd-32d0-bc2a-033d36622c04 | -13.50008 | -45.62659 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26c31522-2fc4-3b59-be13-150cca04529b | -10.00658 | -48.1281 | 2025-07-29 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 118c0b78-74ad-3f89-acef-2c06845c85e5 | -9.21833 | -48.5985 | 2025-07-29 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb090d15-cc2e-324b-ae2c-85ffdca0024d | -15.34384 | -49.42806 | 2025-07-29 04:21:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd2383c9-b0a1-33cb-bf63-0dd84f0c51dd | -11.99866 | -46.94528 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4058cea1-86c7-3828-8fbb-30926b8b288f | -9.19296 | -43.15299 | 2025-07-29 04:21:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| edebfb93-2a1a-32a5-818e-5a99398a3f2b | -9.62885 | -48.26231 | 2025-07-29 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16b6a498-e648-32ea-a316-8424ef7e66a2 | -15.8221 | -41.89139 | 2025-07-29 04:21:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 611d1f34-7b49-3b1e-87a6-581fd4ca34d3 | -9.62459 | -48.55217 | 2025-07-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eddf3ca-ae7e-363e-b78e-4a8e29cd5f28 | -8.13626 | -49.51023 | 2025-07-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cdac137-6454-368e-abd4-146ee4c6c004 | -14.00615 | -44.62286 | 2025-07-29 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e9058b8-71d0-399d-aee7-9612aa1cceb1 | -13.13256 | -47.34478 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b995ba22-9203-37e2-8f22-0b8f08571ecb | -10.92175 | -45.79243 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dcde34a-64bc-3395-8e0b-08ba2bb49d46 | -16.32295 | -43.61876 | 2025-07-29 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1d69837-c8f2-38a9-9320-69407aa2f319 | -10.5168 | -50.2589 | 2025-07-29 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73595e82-6e9a-3f00-9856-b190f7616ccd | -11.97865 | -46.96389 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea10216f-b754-3e23-8d6d-6a213f4fa53e | -9.59982 | -43.84627 | 2025-07-29 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 67904197-5825-379f-9d6f-45983b3024e6 | -13.00196 | -44.89893 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4643b732-f6ae-34f8-8c85-e0e9892e362d | -12.12522 | -56.91489 | 2025-07-29 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a7dbc5d-1d3a-30cc-ac8b-87d8f7d91297 | -8.94708 | -46.75114 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6d5fd92b-51d2-31c5-83f3-dee7a83bd82f | -11.74059 | -48.1818 | 2025-07-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 59835415-4639-3253-a20b-f71fa73f03a7 | -13.49449 | -45.59631 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb65f48-8286-3c75-9c51-0868b337dd2b | -9.36544 | -45.72079 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df0a769f-27d0-35c0-86fc-7366ef226e1c | -15.93348 | -48.39572 | 2025-07-29 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12113d8f-36b6-3ad9-b479-6ae06d0966f1 | -14.35162 | -47.10112 | 2025-07-29 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 325e27ae-7942-37d2-a810-32bdf0fa8839 | -8.37009 | -51.0751 | 2025-07-29 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0840ce6d-5f2d-34ea-b934-f38a8e3df950 | -15.13096 | -45.32582 | 2025-07-29 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 452847d2-6e78-34f3-a4d1-229bd7b107a6 | -9.87475 | -44.69381 | 2025-07-29 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43d91246-e79c-3c6a-b3ea-ba9a6d6949cf | -15.93012 | -48.39516 | 2025-07-29 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69408321-d824-343b-8102-578290c53e7f | -13.06681 | -47.37079 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README13.md)
