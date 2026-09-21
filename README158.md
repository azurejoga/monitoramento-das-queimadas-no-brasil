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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fc759c0-7618-3c46-90b0-a2c6e3859dab | -9.45023 | -45.38394 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e641d209-33b7-302c-9706-f59372a314ed | -11.96423 | -46.51925 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2af2bba-2e62-3ccf-ba99-22cee1a98107 | -9.16937 | -50.01776 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 09c80a46-c903-3d0c-88ef-6bf5180519a6 | -12.44284 | -47.07089 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 618e5bc4-9ec4-3faa-bf9c-938fc3998ba7 | -10.75206 | -46.33688 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6589158c-50c7-3629-bf67-aa200f5b0287 | -11.65581 | -43.42314 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0b7146e6-33c4-3a80-8509-cfd2384ff47b | -9.61602 | -43.93741 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| a88f6392-4d7d-30c0-b212-8c93547b1630 | -8.7627 | -45.86751 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9e42c583-784e-3103-b731-54d172363568 | -10.02793 | -43.76255 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 73baff1e-a04e-3fb4-a022-056d23e2a790 | -9.54048 | -46.51245 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c79a5283-b8fe-3571-91bf-fc2af87701b6 | -9.44826 | -45.40773 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0e903677-977e-3824-9d56-9ec9de94f0be | -11.86875 | -46.85546 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 62e1d199-c3f3-366d-a09f-3d10f59e9cc7 | -9.82506 | -48.45913 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f1fddbd8-141b-3065-bdfc-3a043d9e0664 | -11.90821 | -50.0855 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8bed1d13-87f0-3e2a-bba4-966e8ae80cd3 | -10.76367 | -46.34275 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c5263099-20d6-3b95-b43d-a2df995a850e | -11.67649 | -43.44314 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4e68ee96-03e8-3104-8e14-6cd80ff55924 | -11.84629 | -46.84083 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 70791446-b287-3cf0-a51f-992c69e86c6e | -11.67477 | -43.42972 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| cad903ca-29cb-317a-89ec-9ec6343ff5ad | -11.79252 | -49.80945 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fc31d0a4-630d-3423-b926-fdc320c9d52b | -11.0776 | -49.74416 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8429658f-cec9-31a1-9559-dec6769c8276 | -11.10351 | -48.30173 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cb235caa-8fca-33be-b258-7eb861dcbb60 | -11.49996 | -47.74288 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 455c1df2-4415-3f05-bb13-07628d69fce4 | -11.85072 | -47.60989 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41515fd8-2329-3c20-9f76-11a84182b6d9 | -11.10452 | -48.30997 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9bb15273-a0a7-3322-8848-33f764ee13f1 | -12.13985 | -38.94013 | 2026-09-21 16:01:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8770ed99-c015-3201-b8ab-e3f85f994a77 | -8.46004 | -45.08873 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d44f3816-5399-372f-a456-b1fb3690dc7b | -12.43718 | -47.03594 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 13f132f7-27fc-3a74-a3a5-ff8d91662f6c | -11.82624 | -50.03563 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| f7021af9-c748-3dc7-a890-6be1939178d0 | -10.06665 | -50.24161 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9bdc9e9d-400d-3d0c-ba55-6a603137cdd2 | -8.61208 | -37.20393 | 2026-09-21 16:01:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e8d8d07-afe5-3407-aeef-f23180dc57e2 | -10.07553 | -50.276 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 251e471e-a008-3f0b-b9c9-3b50fe7b6d72 | -8.77527 | -45.85203 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5f6a42ae-4103-3da4-83b8-333e5f705e85 | -9.95936 | -45.73182 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5a1c6ab2-778c-368a-8865-5098981fc929 | -12.40702 | -47.02718 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b2d954d3-e4fd-3d83-988f-6fb6947b39b6 | -11.85126 | -47.61428 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3204f5fd-80c8-3e70-87ee-b58fe92321f3 | -11.84439 | -46.82524 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7ebec473-d668-394a-901c-6c08cb3312e1 | -10.0944 | -45.82869 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7eae15fc-a2cc-3883-b439-207566c15b75 | -10.25259 | -49.99754 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e1b8b8a0-ba56-3940-be99-b230363ac05d | -10.99751 | -48.24404 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 36e57e97-06b5-3e74-a7f8-6e9197f13c20 | -13.29496 | -42.67118 | 2026-09-21 16:01:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 0c54f48d-8bf6-3530-af41-106cd6bd8ae4 | -11.10053 | -48.32808 | 2026-09-21 16:01:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8088aa7-9b81-3f32-b3bb-db65b6911ee0 | -9.61482 | -43.92846 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 36258f08-b33f-3db3-a6c6-49a701b90a55 | -12.30269 | -50.70897 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6b819cb3-ea83-3ddb-9901-3289e76bbd1c | -8.32727 | -44.75697 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f270cd8c-f755-328d-bcb7-5f826b2a887e | -14.36615 | -43.76966 | 2026-09-21 16:01:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7600f1f2-db7e-3d77-b413-fe47ef8c125c | -10.14577 | -45.55474 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 02c14089-633c-329a-9af1-a96234f16ae6 | -9.8792 | -48.44741 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| edfbf666-6533-350b-9ba8-a4c70317353d | -9.54146 | -45.39018 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d29b7ac1-306d-35e9-9585-9cb772d0eead | -9.55604 | -48.41271 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c20fbec8-63f5-36e5-92e5-545cd4a0f976 | -9.88679 | -48.40888 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 67b70134-02b1-3b7a-825b-cb2efce61c2e | -10.10513 | -45.83089 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 933125a0-d616-395c-979b-2cff7795d1c9 | -11.66286 | -47.78522 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 26696722-bbac-3fd4-acbf-d941c2168838 | -11.38977 | -44.04897 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 84d9fed5-dd9f-3116-be16-76f3e212f5e6 | -8.64897 | -47.36019 | 2026-09-21 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f4c76c0-e7c6-309e-bb14-ba055e57b575 | -13.89533 | -45.47832 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97e1452a-8f0d-3abd-ab59-9da738a13664 | -11.86829 | -46.85151 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f8ceb41d-46f5-3424-a59f-778a1b2722e2 | -9.82128 | -48.44051 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5644f57b-c58b-336d-be20-122092732250 | -11.10347 | -48.29519 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cfc763ca-722c-39ab-989c-d0fa9cd85584 | -10.37947 | -48.91756 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 75e75720-61f3-3620-8877-987e36a170ce | -8.32839 | -35.28415 | 2026-09-21 16:01:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 75b663fe-23fd-36d1-bc53-0522e8107c12 | -11.09097 | -49.74266 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 742f4103-80fa-32df-bc64-9e8307ab0483 | -9.24363 | -46.24932 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5ccd6e39-1ad1-3e98-bdca-90096cd1208f | -11.95051 | -46.50232 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 206124ad-884f-3da4-aa20-853622249a27 | -11.85 | -47.61768 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d1de8c2-b078-33ae-a401-406d577cf489 | -10.71568 | -50.76023 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 9b72a009-1b11-3f37-ac7e-2f1f8b05f783 | -12.30963 | -50.66975 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d53be311-b9ca-3b89-821d-323cd41efc85 | -11.86217 | -48.98223 | 2026-09-21 16:01:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3cc59471-b962-3439-ab2f-96ab7c578269 | -12.1817 | -42.35515 | 2026-09-21 16:01:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0bf99fd2-0203-3b72-b6f2-be7997d81725 | -9.16868 | -50.01196 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 037a119c-799e-3551-87ce-89649600bd5a | -11.47627 | -47.64417 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 48ef576a-0cf8-3a13-ab0b-89bbd34feed6 | -11.98552 | -44.88937 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 24565eb3-2ff5-31d5-a48c-4397b7a238cc | -11.95652 | -46.50562 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 61c3995c-17f5-3340-a6e7-5af88e817816 | -11.33954 | -40.5531 | 2026-09-21 16:01:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 64f30be3-8ee5-35f0-bc50-6cbf7a9f6275 | -9.23512 | -46.17591 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 65cdfb5a-d87b-361b-bbf1-9b35e268063a | -10.11536 | -45.55531 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e51003d-5b0f-3e34-915d-64e6e8672f07 | -12.44739 | -47.07188 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ab5f8adf-3a34-3fe4-8aa5-7fbb26eec4bb | -9.16272 | -50.01851 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 0a87c388-c173-3bf8-99d7-62059ac1d5f8 | -10.71964 | -50.79461 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 78258b98-41fc-31ae-9e90-2c7025516e6e | -12.43865 | -47.03423 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 780e6ba4-acef-389e-a85c-ef70634a6349 | -14.12239 | -45.54888 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c9fdd294-5dc7-3410-8f16-55324315e2d6 | -11.68211 | -43.45153 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a24b7b23-0d61-3980-ad74-0fb2e6e25ec8 | -12.42336 | -47.06627 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6f647c1-8a5e-3c5e-bbe6-4307f714c2ac | -10.47387 | -45.10012 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 56e3a46f-283d-31a8-8587-21d6fe2df94b | -10.74656 | -46.3195 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b67dc43d-8524-359b-b47c-c7999bb099fd | -11.03014 | -46.54939 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 90c9c64c-9cec-3f95-8179-54dcb8fe251a | -12.44813 | -47.06612 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| edf7b9f7-98d1-3ed0-bc92-7fc24beb5d75 | -9.01512 | -45.00258 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 33f543c5-0e5f-3873-a4c5-3ab7675b99be | -10.53705 | -42.2174 | 2026-09-21 16:01:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c86ce592-7c78-32eb-9853-064e69635f1c | -8.73335 | -45.45564 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6fdb8008-4ea0-3916-a733-34ab7abf434a | -14.868 | -49.2143 | 2026-09-21 16:01:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 1ac7ab3c-c485-3433-8db0-6971aae03330 | -11.44805 | -43.30568 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 286.1 |
| 1d450d8f-9874-3951-a07b-08d777b98c8d | -8.41655 | -43.96303 | 2026-09-21 16:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| afc25de6-c83a-3ddf-b3fa-5c88e370e073 | -9.27814 | -48.22813 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f95d671-ff29-30e9-90fd-f371f9d54ba5 | -8.78155 | -44.27449 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 1ce8fb09-98cd-3427-9de9-641728ad363c | -9.54302 | -46.53217 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25d6c6c4-eda4-367b-87f5-ad4badc47cf5 | -9.28298 | -46.21889 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a587f95e-ab3a-3c8c-8167-f1c625ea8dc2 | -11.80607 | -49.80814 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b06174c0-afed-3333-96dd-ed351374351a | -11.04499 | -46.57978 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 31554027-5f45-325c-b7d0-aa8938192a1a | -11.39724 | -47.72348 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c8dfe1b-3a45-34a7-a4df-58b62c33b597 | -9.24983 | -46.24974 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README159.md)
