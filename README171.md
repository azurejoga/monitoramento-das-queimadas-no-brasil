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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2adc27c0-5318-31b9-b6ed-850463feac1e | -5.9424 | -52.51644 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87fe7836-5f4c-35d6-b270-e3cf69f2056c | -2.47357 | -49.35107 | 2026-08-31 16:52:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbc74605-2df1-36bb-8232-f6ecaa4a8f36 | -2.79195 | -49.52407 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4fb37b2-2a57-3a98-aaf4-69338a6dab12 | -5.85351 | -52.08783 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9cfb70f7-c06c-3d8b-9076-1a122c6a4697 | -5.82311 | -52.39192 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 461a017a-8b96-32eb-bfec-11a97078a5ad | -3.63783 | -59.55278 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01e45ee9-d685-370f-a7a6-7d52d8b56c9c | -5.77822 | -57.55779 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f18f47f8-3ac7-3caf-9958-42f101aebbae | -3.58682 | -55.60373 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81c1ab3f-9452-381a-a0ad-99a5f51c150e | -1.58307 | -52.67686 | 2026-08-31 16:52:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f80ea89-da8e-3beb-b7b6-5f7dfde90799 | 0.84277 | -51.1534 | 2026-08-31 16:52:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 75955d67-e31e-33e0-9d09-587cb7203078 | -5.96197 | -57.6732 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 92c04bf6-1ba7-3234-9e8c-b94937373d24 | -3.87654 | -59.56554 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 70319e44-b32c-34f4-a9ca-3f6003c3ce04 | -2.52094 | -44.15162 | 2026-08-31 16:52:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efd8f6dc-f61c-3e49-9856-22e59fd3dc8e | -6.20535 | -52.98691 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4a6d4055-5502-3f6a-b387-e4b5c2aa5a93 | -5.94052 | -57.6911 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| efbc360d-4a5b-31f2-89bf-67f8c9065fea | -3.66577 | -58.90384 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6998b694-7321-3b8d-8c50-23e4c8e80c8c | -7.34228 | -60.58241 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d2f3c46a-20a9-3edf-8531-dae57d3d4a06 | -6.10878 | -57.86321 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4fb5dce4-adc7-3652-b914-7c5f9b3702d0 | -1.32876 | -46.74247 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| adf25229-3c52-31ee-9acc-91dae497bd9e | -6.1511 | -52.64043 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3b80ff15-edf5-3c9e-aa57-0089b6fcb810 | -4.6484 | -55.84984 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9cc35d41-a61d-3373-a41b-da1681a2b1b4 | -7.30823 | -60.58555 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e812ae5f-040e-302b-b555-cc4d540ea1cb | -2.36901 | -44.44334 | 2026-08-31 16:52:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| b48057ba-ecc3-3b65-a167-c580c5154d91 | -3.83573 | -55.56666 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 982e1f8d-d11f-33fb-adbd-fd9dacb56226 | -1.82226 | -47.81657 | 2026-08-31 16:52:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5b75c3f-257f-359f-855b-2e7e884cc9e3 | -3.7065 | -58.11568 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 96baa89d-950f-34cc-b4c7-87835a487fb4 | -4.07167 | -55.78201 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 256407e2-d0c6-399b-b389-09d66399adcb | -3.71717 | -51.10605 | 2026-08-31 16:52:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4bc6edce-b6d4-39dc-bb95-5f52ea641668 | -3.33277 | -59.39591 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bbb2e990-dd2f-33f4-8ac2-5d06ece906b5 | -5.98987 | -57.68736 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d9181a4-18ea-3365-9b4f-db290435c580 | -5.58127 | -60.24006 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a72be6e1-caf5-3922-a369-f523da431c1e | -3.51185 | -56.31618 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 40b31b9d-ec5f-3db5-adb3-19b1cfac5979 | -3.32727 | -59.39669 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c42ee34c-d9b9-35dd-b2b0-670168dc331c | -1.12431 | -46.32803 | 2026-08-31 16:52:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 361b7568-7b31-3617-9758-19e0e8a940fe | -5.96479 | -57.69403 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6ec2ee69-695d-3a34-aaa9-9d6d0cfe7d67 | -3.38937 | -59.39553 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 111a2111-7605-3183-8acb-d9ce5f71d287 | -5.89405 | -52.23921 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 05099472-bb5d-30d4-8e9c-aad9d90dfbc6 | -4.27105 | -56.12977 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1b267ef-94d4-30ff-8357-4dad0af15b62 | -1.92828 | -44.80923 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 996d7cbe-e19b-338c-b464-35602215c823 | -1.59464 | -54.40492 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da8ab722-609b-3fa5-9d7a-5735abbfe8db | -3.87599 | -59.56181 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2447add7-da65-3302-a3b9-053f72ab9bc4 | -4.43616 | -55.44733 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c856441f-753c-3594-a5b8-be75c0183b78 | -6.84606 | -59.72696 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c5195056-10f4-334d-aaef-02544060f458 | -5.72802 | -53.73177 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 47d6acec-7605-31a7-a072-da237be427f9 | -2.64077 | -43.45022 | 2026-08-31 16:52:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f1a61090-e226-3746-8987-4688ebb494c2 | -3.58623 | -55.59978 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 57369d00-94a9-3c51-acf0-a5357cb6fd94 | -1.28527 | -46.01404 | 2026-08-31 16:52:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 50059c69-463c-358f-9f79-ca50f44de906 | -6.24268 | -55.41101 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5e1291a9-23a2-3a9e-892b-776d74121263 | -1.4613 | -54.2185 | 2026-08-31 16:52:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| c164bed4-e399-348d-8c44-52f1d8a56fe8 | -6.14637 | -53.51516 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 69731e41-a939-3a62-8b01-b9d4cce56811 | -3.70608 | -58.11274 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b29f1a57-e871-360b-9c8a-6975e234c737 | -6.11201 | -53.86353 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4b5b40d8-95e5-3934-a3de-c93bb19475c8 | -6.35277 | -55.86166 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba86438c-7e60-372c-9e15-54c9ff1b7d39 | -6.27583 | -53.3382 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7a8db739-df64-37d8-ab6c-cfc18f6c1046 | -2.43678 | -48.43343 | 2026-08-31 16:52:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dba3eaa5-951e-348b-b9ff-95d7abbf3ed4 | -6.67896 | -58.74355 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ab16bd8b-5f64-3d2b-900e-a0c791ed48bd | -2.00881 | -44.63244 | 2026-08-31 16:52:00 | NOAA-20 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96a631c5-515f-3f52-a949-e457226da5b1 | -4.91007 | -43.46275 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 12b4eaf7-b592-3053-aae4-033ec1f8b034 | -2.86397 | -45.14402 | 2026-08-31 16:52:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e7d6bda7-acdf-386b-a8b4-92adac782d87 | -2.47209 | -49.31936 | 2026-08-31 16:52:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eee7c19c-a5b6-3ab3-a231-576a00001d28 | -5.91497 | -57.69421 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77995755-80b4-3d34-a679-52ebb4af5170 | -4.30098 | -49.09348 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 53a6ee0d-3132-33ed-90f1-8c33521a49a4 | -4.85163 | -55.82684 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ee4da494-e466-3383-bebb-38e87150a15d | -1.83745 | -54.4861 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 47747003-59f5-306c-9db9-f49ec9e1438a | -1.76054 | -44.85146 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f514dc08-68ac-3834-95eb-af7fb76a4eab | -3.32875 | -44.16325 | 2026-08-31 16:52:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1210205-70d7-39d9-bcfe-d1413fd79bde | -6.88149 | -56.5076 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 115307da-fa02-31af-b0f0-782f5dfd5ba5 | -7.44655 | -60.75945 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3372a7ee-7fdb-33fa-934b-0fc6d4da6aaf | -6.87544 | -56.57106 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e52de4e9-ff23-3d88-b24f-11f52d21eb21 | -1.00442 | -48.19009 | 2026-08-31 16:52:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e979a85b-e384-3517-9f63-7d64eae4d2f6 | -6.88081 | -56.50612 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 318e1445-f1b4-3486-bc53-50e28aa1cfd3 | -4.22917 | -59.86325 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ddf5faab-077d-34cf-8f6c-ccb7e812e38e | -5.95582 | -57.68909 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0e86ca40-02e3-32ef-b0da-f7ab4a87bcc1 | -6.14568 | -53.51037 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2048ae1d-8f5e-380d-93ec-d32481919080 | -5.58728 | -60.23926 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f6dcb9c-ff5e-32f1-8fdb-8931a69c9077 | -7.44208 | -61.42373 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 06e64f93-d22e-38c4-9d41-823d79ce7ba9 | -6.20665 | -57.66765 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2a7f6553-f66f-362e-a602-84a83d7e6eab | -1.77961 | -45.29458 | 2026-08-31 16:52:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4158bca-44bf-39c0-846b-27d61978c35c | -7.34098 | -60.59174 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| feb8efdb-6266-3e10-a77b-ec8df18da8fb | -0.84635 | -48.68464 | 2026-08-31 16:52:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b21326a1-3575-3ebe-9489-8801c5ec5e7a | -0.8089 | -49.20461 | 2026-08-31 16:52:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5e8423d7-01bf-3070-9b86-1fe0e2bd3836 | -5.98156 | -51.92722 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fcd236e1-b803-35f6-9c73-379afd0ad1e3 | 1.09793 | -50.97172 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 673524a1-8e19-38be-b954-20e5d467b761 | -1.93652 | -44.80798 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 852928bc-7766-3d03-a47d-a7024a723147 | -6.8794 | -56.42882 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f97e1d7-4dd0-3d21-9aef-f6b698a9d82f | -5.28309 | -47.88359 | 2026-08-31 16:52:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 8eae357f-5e39-3437-bbe0-f490209b6973 | -5.487 | -57.15328 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d57d47a1-7dcf-3020-8b3d-e6c93fc10aa1 | -6.07654 | -57.65057 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eea16bbe-6135-36ce-9f05-1a55a8d360a0 | -7.33741 | -60.59375 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 76686ab1-89b3-3012-961c-dcb8ea2f1737 | -5.73245 | -49.13205 | 2026-08-31 16:52:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| d06b239c-f2d7-3ba6-8e8e-50ef37e1c438 | -7.44585 | -60.75419 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78c0d3bb-1315-3114-a8ce-bb85a585238d | -6.86996 | -59.46697 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b5e40eea-fba9-37b2-83f4-b70c3cae7e79 | -5.88301 | -52.06662 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 4b28c9fc-3be5-3c71-803d-bae4b68b58d9 | -7.52754 | -61.31998 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4e4e2c0f-5205-34da-83d4-d928a4553561 | -3.72148 | -61.62923 | 2026-08-31 16:52:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b68e8949-87f4-3080-9cee-f400ff9956da | -6.81555 | -59.67863 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5d03e457-885d-3e2e-a953-8288c32c5f2f | -3.69339 | -45.838 | 2026-08-31 16:52:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 573d3cf8-59af-3340-a432-5844a599f629 | -4.30721 | -47.13036 | 2026-08-31 16:52:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c58b1fc-93fd-3bfa-ba78-b79c015553f4 | -3.39688 | -60.1365 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd0e0c3f-345c-3040-aca5-d409b639835b | -3.09297 | -58.11512 | 2026-08-31 16:52:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README172.md)
