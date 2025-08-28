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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 733582ba-2825-3070-aa52-ea7de369ca26 | -6.3682 | -44.05499 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753b3397-f55d-3d8f-abb5-9a3d8389fba3 | -6.28169 | -44.47404 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b497d45d-7d9a-3b82-abe9-c59a10e64b53 | -6.1701 | -44.06816 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abe6927a-9a8d-3ffc-86ba-48e420a32379 | -3.78639 | -45.04229 | 2025-08-28 04:06:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f4cff0f4-779a-3374-b382-6f21d68ec918 | -6.8106 | -44.36158 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 633ce0ab-9340-386f-b835-114d8dbe048c | -6.80832 | -44.35334 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3009ea-6155-3df0-853d-29e73db67b6c | -6.68645 | -44.02966 | 2025-08-28 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90c0a912-8a25-384f-93b1-975edb303a32 | -6.16348 | -44.398 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9736e65c-fd71-3eab-9555-ea36e12d5e99 | -5.19033 | -46.07182 | 2025-08-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7831f241-115e-300c-8d80-68ff08cd56d0 | -6.87252 | -43.61189 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e49e04-8209-390c-a83d-ef23c29ca15e | -6.18952 | -44.01529 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 148c0060-e41b-37ab-b06c-7595812ba084 | -6.18572 | -44.0386 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b9407f9-70e7-3691-8eea-523d959a69d2 | -5.03526 | -43.58313 | 2025-08-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 793d34a8-8047-3ad0-86fb-d998ed509dbe | -6.69202 | -37.52237 | 2025-08-28 04:06:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ab5f030-1e4f-3b38-9858-4b474dbd40f2 | -6.80639 | -44.32082 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0a672b-210d-3eb1-89c7-ec5e86825c8f | -6.2924 | -44.47574 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc99c57-8c09-379f-842f-33a6884476e9 | -7.64044 | -42.67011 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2377caa7-06de-3628-8e42-d2eb74aa8027 | -6.18153 | -44.17495 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02fab7ee-5cc2-38d2-82bb-6b7cd8b2a27e | -5.81208 | -44.76414 | 2025-08-28 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48f82ecb-1df3-3d8d-840c-e64c24775573 | -2.44039 | -47.32708 | 2025-08-28 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dadfc9a-0d00-3b49-9d20-fc7b2c12e957 | -7.39387 | -44.07294 | 2025-08-28 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a78d02aa-44e2-3748-a727-6c2931b98e9e | -6.16198 | -44.18394 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8730fc1-4f6a-3ebf-af80-ee8dd385f129 | -6.015 | -44.28389 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 574e815c-01d3-39a2-98fd-eff6942c7d65 | -7.63372 | -42.71226 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 55e421fb-40e0-30a0-bbd6-1e2a31f1ca91 | -7.17775 | -43.84743 | 2025-08-28 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 130ce669-fba2-3778-8071-69d2f2525b3a | -7.62762 | -42.70768 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbd82289-9de6-31ed-a935-49f6aa1a5755 | -6.16284 | -44.40194 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3dcc43c-9ca7-3cc7-aa5e-81a23e1b46c1 | -3.27693 | -52.51637 | 2025-08-28 04:06:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bd818cb-7f60-3b09-acc1-43f58b79d683 | -6.01159 | -44.48285 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edc927a9-d767-3259-bbd0-fd313538ff0d | -6.68994 | -44.0302 | 2025-08-28 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a659280-ef67-352f-8392-8478e1183f45 | -6.76501 | -44.8224 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b8a3a40-76d0-3ec2-aa08-8734edaf463b | -6.87549 | -43.59327 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 355cd729-d745-372e-9cc7-03df1f91fc37 | -7.18027 | -44.87309 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5bcd8f99-10a3-3feb-b687-003ef4d9ebde | -6.12393 | -44.41643 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381141db-e645-3d95-8373-57bdadd2b590 | -7.24378 | -39.18006 | 2025-08-28 04:06:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d8890093-0c09-34f7-a82b-306e8838be77 | -6.18665 | -44.0109 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17b419d7-0196-39d5-a97a-f142d93bb032 | -6.7607 | -44.82615 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9407e252-2dd0-32d5-91fa-79740dc02ab0 | -6.8759 | -43.6123 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6bf798a3-ddff-3dd9-a168-4568f3c3a729 | -6.15897 | -44.02644 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d174528-cc40-39f8-a9e4-b7887de58ba4 | -6.13594 | -45.07222 | 2025-08-28 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 708c6c60-a762-3d77-af65-9fdb4d28dac7 | -6.81081 | -45.00179 | 2025-08-28 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37883d3b-5519-3e1f-920c-c1e699e0e2fc | -7.39102 | -39.69092 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 0c5ebb54-04f1-314e-9aab-ee0d11700051 | -6.88275 | -43.61339 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 51e425dd-4be3-3f4f-b0b6-465f6753cd8b | -6.30156 | -42.49918 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c371ca07-015b-3f80-8c13-0efcaeaa9084 | -6.36702 | -44.05523 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a18ce6b1-5832-3f29-8ece-66af68abc4f4 | -4.84952 | -42.8897 | 2025-08-28 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea501b60-fb14-32ab-b5da-6e368bcca4ed | -6.07934 | -44.00168 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc4ba806-806d-3e3b-b33c-f6ddbf20f097 | -6.43537 | -44.57257 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 60f3fd60-c56a-37e9-b897-fa13cef4db10 | -2.44275 | -47.11395 | 2025-08-28 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c1437f6-28fc-3726-9608-b15312a2348b | -6.68415 | -44.40318 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 244f0e0a-cd34-34ad-82f4-922166f600ab | -4.88453 | -43.15101 | 2025-08-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84b6d91a-0625-361b-920d-9218bb2b599d | -6.15766 | -44.38885 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9877f63f-2e9a-357d-8e1a-4501f2ac2575 | -6.1578 | -44.1874 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9f89e6a-441c-3779-83a8-3a6f4901eb6c | -5.45933 | -47.90618 | 2025-08-28 04:06:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa33ae47-308b-3208-91ec-99aa8c5b7480 | -6.18343 | -44.16326 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c974de83-9697-3a24-9260-6eaf0a47ee94 | -5.54282 | -45.37591 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa45703-7f1f-33c4-90e8-608079456af2 | -5.51983 | -46.47013 | 2025-08-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8f61e2-74b7-3568-b0e3-bbd5648fb5b2 | -6.36826 | -44.04753 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83d7dc4b-f771-3e22-9cd5-c1ec07b2f640 | -6.44056 | -42.41726 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fff2c004-5409-344c-9095-8b83a1bd9154 | -6.46155 | -43.72358 | 2025-08-28 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8b40f30-7b9c-3c89-8887-80277295ba82 | -6.25068 | -43.85865 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50666c6d-b7b0-308b-a0f3-43ab0d8f6eaf | -7.39446 | -39.69145 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 7aef1b88-5053-32c5-b0df-8cda53fcf1bb | -4.2464 | -41.90063 | 2025-08-28 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb5eed36-f3ae-3d3e-88c8-ed415f7cfa38 | -7.39733 | -39.69575 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5de1dd45-64a7-3336-b86f-023067ced5f2 | -3.23141 | -43.44286 | 2025-08-28 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 510836cd-1de9-3e9e-9d5b-0cc5254b235f | -6.87126 | -43.61922 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f1737ba-d05b-37af-bcc9-4af74054bded | -7.39332 | -39.69899 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f3581abe-6f50-30b4-82af-98d98f8001fa | -5.23057 | -39.37612 | 2025-08-28 04:06:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b9d00d66-714f-3fa0-8f17-6887c8abb62a | -6.13106 | -44.41753 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35a0b8d0-7e43-34ba-8673-bb66f3456598 | -5.53425 | -36.84982 | 2025-08-28 04:06:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9bcb08e2-a41f-3ed1-964a-dcb3cb7b5181 | -6.16316 | -47.27764 | 2025-08-28 04:06:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7f3ee7c6-d0d6-3405-a4e9-2c6068231538 | -7.39216 | -39.68337 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 474e7217-479b-3900-b086-c2f3e20e43ab | -2.38296 | -47.62592 | 2025-08-28 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a423ee7f-b190-3797-8fed-963056b4b67e | -7.62933 | -42.67551 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c81f44d6-b3a5-3cdb-ad82-ddf469ab5d92 | -6.99812 | -44.41158 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd2d1e27-d17c-3415-9996-73cc5e65f4d3 | -6.87065 | -43.62296 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5e4b96c-cb12-39d6-83e9-8eacfebf0d2b | -7.38356 | -39.69363 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 356f0a22-44c3-3826-a590-1851ff4fa829 | -7.42181 | -40.08374 | 2025-08-28 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cfb4f2ed-df5c-3548-9939-280726e6174b | -6.15845 | -44.18344 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2485990-6d66-356f-9af6-72138031d336 | -6.08057 | -43.99415 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edaedc4e-13ec-3585-b461-dea625eaa242 | -6.16213 | -44.05096 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aebfe707-1073-36f5-8685-225e5d7d1d7b | -5.59274 | -45.14235 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0adff964-93cc-3772-af7d-eb810933bca3 | -3.23492 | -43.44343 | 2025-08-28 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cd319b2c-84d1-32ac-81c1-30a748a3b8e7 | -2.7402 | -48.56598 | 2025-08-28 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31c37762-7c94-365d-8eb6-6e97f93b7e54 | -6.80928 | -44.32532 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f27aee54-b415-3e5c-a9a3-3df7f4b19c84 | -6.85986 | -43.62519 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0394a11-8985-38b2-80ff-09a83f04d798 | -4.66721 | -41.02168 | 2025-08-28 04:06:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 18ccf198-08e9-3546-a1f0-e2e2d876de6f | -5.72491 | -45.35172 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52c7e3eb-793c-383e-8435-44568842b3eb | -7.43794 | -42.04131 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f6c58df-7e53-3b6f-aa8a-0501666bb92d | -7.38701 | -39.69416 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5fb94166-3dec-3e40-bdbd-5a595761844a | -6.19176 | -44.15641 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a13591f-84c1-39d3-9dfd-94b3cc44db9d | -6.86448 | -43.61827 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c380a175-1682-3e7c-9535-36ab7e9e8bbd | -7.62874 | -42.70065 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 228ed509-a4d2-374a-bb2e-6912f0bd78f7 | -7.41898 | -40.07956 | 2025-08-28 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a24f4e80-26f9-34e8-9d72-eaa9dad85bcb | -7.43077 | -42.04372 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 547cc96e-2267-357c-8429-1345f13127bf | -7.54632 | -36.75597 | 2025-08-28 04:06:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85f660cd-f79c-307b-9346-8930bfff1ec4 | -6.87309 | -43.60801 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7477b5c6-9480-34eb-afc0-cdaf934d698b | -4.56334 | -44.01009 | 2025-08-28 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a490735-8246-3e84-87e6-4983711b2498 | -6.16436 | -44.05926 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2578abf2-0daa-36b1-bc6f-73e684ad9d41 | -6.88397 | -43.60592 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |


[Clique aqui para ver as próximas entradas](README32.md)
