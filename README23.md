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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36bf0101-700b-3f32-86cf-a74d2501bcc4 | -8.9065 | -44.940399 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d1a6f0b-7166-3dda-9d45-a28a64903a46 | -6.4513 | -46.016998 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4da97d73-6f6f-34e9-8530-9bbe17da02c0 | -2.7502 | -54.120998 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f086cd3b-7ccb-3fcf-8926-7901999720b9 | -18.785101 | -46.4664 | 2026-10-09 00:28:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab170874-5208-37f7-8491-f4e4234b917b | -10.4089 | -48.875401 | 2026-10-09 00:28:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa54771-04cb-3e43-804f-c72f4c0f41ed | -8.975 | -45.9202 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1806f009-f7ef-34de-bc1c-a941cf539da9 | -9.8306 | -44.787201 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 560a2576-6e89-32af-828c-098e3923c21e | -7.6572 | -45.383999 | 2026-10-09 00:28:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 92be35cc-2205-31b1-b67c-1bae6b35e671 | -8.8952 | -44.935699 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98a48855-74b3-3714-acbd-1524e45e2211 | -3.3 | -53.702301 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7194e1d8-c901-3d1c-a943-9abdb715fff1 | -3.002 | -53.922798 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f75bdc7-7157-37a7-ad4c-9103129aa3ca | -11.7728 | -43.541302 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf4e2e0-30d3-3bad-950d-a2c94ea2cabf | -3.0933 | -54.193401 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f63762f-6df5-3a0a-b0fc-6974f4818c09 | -6.5014 | -43.954201 | 2026-10-09 00:28:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b632f8b-9179-3aed-a7f7-da2f14dc24a5 | -11.7889 | -46.772701 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46966f98-cc6a-3f15-b280-d4d6648b04c9 | -3.0756 | -54.297001 | 2026-10-09 00:28:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75551955-0262-3854-aa8d-2237e447048e | -11.861 | -43.565601 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c263c872-5444-3090-8673-ad604678438b | -2.9937 | -54.0681 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62b569f4-0a3a-3576-8e3f-343977bf0055 | -7.0609 | -40.950401 | 2026-10-09 00:28:00 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de57a6aa-6813-35fb-9f0d-da54b9f31e48 | -10.7382 | -48.548698 | 2026-10-09 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b44145f7-dca3-3e27-958b-720f4a4427d5 | -6.8781 | -45.8993 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c93ef60-dc45-3f8c-90c0-c0bc8fce7bc4 | -2.8218 | -54.121601 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53198123-9625-32c4-8d02-894b2f8dc842 | -4.6587 | -49.240398 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da3c586-f28b-3893-8ef5-8e37a64567d2 | -1.1405 | -54.237598 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47e31693-a511-3c41-9119-7e1b7c1ed193 | -3.918 | -56.0261 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59536a11-aa36-377e-893d-d60f1d5005ad | -10.3626 | -45.131401 | 2026-10-09 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90626d5a-1a37-3596-8784-d3c7496fbfb1 | -11.6244 | -43.702999 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90a98efa-f27e-3d72-a2f2-9ed2199ea28d | -4.5403 | -47.037998 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10bb5fac-3206-3c77-8364-e74621d95e67 | -2.9714 | -54.105301 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8c73c3d-74aa-385a-af5e-0b3bd072a03e | -8.9684 | -45.165699 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1127318-0183-30a7-8a50-a50928f7878f | -13.9958 | -48.765202 | 2026-10-09 00:28:00 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 966cf14e-0038-3d86-a58e-cac94f29c072 | -6.7282 | -55.145699 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9660dc37-7b95-3874-9015-32b31b83996a | -11.8993 | -46.573101 | 2026-10-09 00:28:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d99a1ec8-f3e0-3639-a297-ef099b86b5ac | -2.5711 | -56.180901 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b6e7cb-724d-3060-8e0a-cddf9bef7adb | -8.7238 | -45.177898 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb99598-fafc-33c5-93b3-d33a6094a231 | -1.8159 | -56.169899 | 2026-10-09 00:28:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be28e56b-027a-3993-88c4-9f986fd494e2 | -7.089 | -47.741199 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9838c017-8049-34b3-95c5-bb33afcd2ab0 | -13.8809 | -43.827099 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c37b0dc-fc49-343f-9df2-1e974cef4436 | -17.8239 | -52.341 | 2026-10-09 00:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e164fe64-6aa4-3591-ad35-8755c0ad045c | -12.029 | -43.4436 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd3a5cb3-83a0-3de4-90d8-3dffc310829a | -1.7323 | -52.248501 | 2026-10-09 00:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7036bf1-b09c-3961-86cd-a5cf0f9904c6 | -9.2991 | -47.459499 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f2dacbd-e879-31f2-8a6c-de4e75207606 | -5.5063 | -43.053001 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1884480-54c6-39d8-8218-c7f54ef68419 | -14.4394 | -43.9259 | 2026-10-09 00:28:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ec097b53-6ed1-3336-8b50-17ed88ab0766 | -9.8441 | -47.460499 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1434d8f5-d448-36fa-9e29-5c0c74c6d16b | -13.6328 | -44.417 | 2026-10-09 00:28:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aada01f8-308c-33d2-9051-8a8b782d22f1 | -9.9153 | -44.796902 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18776776-10b3-3c69-a8f1-a24cdac2e60c | -10.7753 | -46.604301 | 2026-10-09 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b882673-5ae5-3a87-bf8e-4a8c227bfe5c | -3.3434 | -50.428699 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07e14413-4ec5-3310-9c29-9e3907603c59 | -16.5219 | -42.5145 | 2026-10-09 00:28:00 | METOP-C | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| edfe5f6f-5f02-320e-ab8f-65da2533280c | -4.9816 | -46.038399 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74a4780e-f2e9-300d-9e98-e8960645d249 | -8.9833 | -45.911098 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c31aa58-67f7-34f2-9bce-631b28dcba56 | -11.613 | -43.608799 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0906276-df94-37bf-8189-9b709e31f5db | -4.5485 | -47.028801 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8da764-912c-3fc5-bb9e-ec407bb4de62 | -4.0853 | -44.124599 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48d89075-f40a-31f9-b752-247ed4315825 | -15.4281 | -43.2384 | 2026-10-09 00:28:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 0ded0f76-eed2-3811-90b6-c98dcf674ed9 | -6.8573 | -48.775398 | 2026-10-09 00:28:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e91b60db-0777-3740-9734-3a21647da120 | -7.4828 | -42.8549 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2642321-66c0-3cdd-9a7e-538db59e52bc | -5.3821 | -45.941101 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c1b501f-2975-3472-9f33-a7320ab1ec74 | -12.0225 | -43.460201 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14c402d0-fe0f-3d12-8357-7c2f0e2979a7 | -13.3456 | -43.967201 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11076864-01e1-3297-8120-5fbc967b12b3 | -13.1628 | -54.350498 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34376db6-9b49-363b-8a52-6366957ae340 | -3.0935 | -53.966301 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68732194-f5e1-3fa9-bad2-0f1897b160a6 | -4.5374 | -54.962502 | 2026-10-09 00:28:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 859bfa62-d384-3e20-88f5-4165c3aa135e | -11.6538 | -43.696201 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1cb7d25-4a9e-344d-a234-ef0181e58516 | -8.9034 | -44.926498 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd4f51ad-d058-33af-9881-9bde4b8251b8 | -7.3398 | -45.304199 | 2026-10-09 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc72fed9-213c-36b5-ba54-e8ba14360c6d | -10.4252 | -47.299999 | 2026-10-09 00:28:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56ceab9d-1ac9-3158-8a6c-9cb83e972a7b | -2.4554 | -56.073502 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd24756-e0e0-38d3-a33a-6d2f3a4ec3bc | -12.0192 | -43.4459 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c52692c4-8d2e-3f2f-8cbe-74c2e288c021 | -5.3404 | -45.176899 | 2026-10-09 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0c01bf5-7275-366c-8d29-a81697db2d7f | -6.7137 | -44.112301 | 2026-10-09 00:28:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9f0fb44-2f14-33e2-9d37-0b673d002c4d | -12.0094 | -43.493301 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 397e56c7-1830-34b2-8e17-23a40a0d8efd | -7.0634 | -47.3983 | 2026-10-09 00:28:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d3c5ced-2e7b-3720-8865-bde976b8b6ec | -2.9979 | -54.132099 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddd7d77b-3f31-3e3b-a21f-f4b153178655 | -2.7514 | -49.542099 | 2026-10-09 00:28:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e689f54a-e350-3592-bb0a-cdd7c48cc225 | -4.2765 | -49.0965 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7df1d65-001e-3ac0-aad6-4dcee2b5bd51 | -5.2857 | -47.915001 | 2026-10-09 00:28:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 906a405d-0760-3b81-bfc0-a5fda30d4422 | 2.424 | -50.8251 | 2026-10-09 00:28:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b3ac72f4-61eb-34c0-96ef-570d971717bc | -1.0979 | -54.1852 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a236db7-92dd-307b-8cd9-f62cce12d353 | -3.1977 | -50.830299 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8ac4b62-a613-3a1f-88d6-30aa26115fa8 | -5.9251 | -51.8452 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13325e1a-c81b-319e-96f0-33d87b93e65b | -3.0201 | -54.0947 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4a39fef-c460-356a-8bf0-9ce1ad8afba9 | -6.8883 | -43.7099 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17f1f637-8645-3e49-a05b-8594055ef591 | -5.9586 | -46.387501 | 2026-10-09 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1205ad2c-4495-304f-992f-5e4d605621fb | -11.6146 | -43.615898 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7b4a2b-9aba-3942-9276-84f109fca942 | -4.5088 | -45.821301 | 2026-10-09 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d55ecc6f-07c1-31f3-8b8d-03dfb730e809 | -5.1086 | -46.232498 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5cfcc87-3fb7-3835-aa2a-f06118fbc7c6 | -4.0951 | -44.122299 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4272fe0a-92ec-360d-b92f-4d1fd16cf291 | -4.6658 | -48.952499 | 2026-10-09 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce32dca9-2a6b-3aa6-9c38-989d9bf61547 | -12.011 | -43.455399 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30112645-f86f-3f63-9c30-6e9599e3996e | -12.0241 | -43.4673 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44caeb4e-02b6-3c8e-bb88-77760be38741 | -5.675 | -46.364399 | 2026-10-09 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00f8145c-f709-3b89-a288-8118e7bae764 | -9.0829 | -45.125099 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84cd014f-9c43-3154-99de-0c0e8347f556 | -14.4312 | -43.9352 | 2026-10-09 00:28:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f802992a-ab5a-3891-b725-dbd5db059ccf | -5.517 | -42.835098 | 2026-10-09 00:28:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 603f228d-fa19-37c5-b22f-d665d15f4ac2 | -9.1051 | -48.818802 | 2026-10-09 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4fb36e8-959d-378f-8d4d-556130a0b340 | -6.7379 | -55.1437 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caec8dd8-50db-3acb-983b-ec4eef439f49 | -6.7502 | -45.7911 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86bbe6e5-5e4a-3ee5-abb1-62e372f1cc25 | -3.072 | -54.280998 | 2026-10-09 00:28:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
