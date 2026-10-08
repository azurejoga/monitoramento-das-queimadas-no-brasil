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

## Dados Diários - Página 370

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 400860b0-90a9-32b6-8b4f-9e034176e75a | -5.38961 | -44.18704 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 043b63be-a644-39d7-b20b-80a07ee5edb6 | -5.99964 | -53.49702 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 99d2a619-141c-31ef-ad73-ff58b0cb7909 | -6.86656 | -51.8619 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f1f5408-fb11-3b4d-ba14-5eb9589efbd5 | -6.85019 | -59.29383 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 29eb8f1a-9d88-36c4-93db-778bbb8de433 | -1.52824 | -54.81807 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f99e364e-8cd9-38e5-9e07-f74f8b0bfe42 | -3.02084 | -54.73327 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0c793711-4bde-32d4-8308-843b90854cb9 | -0.98865 | -48.64302 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58f27ff7-34d8-3002-8043-9ab9003c6837 | -6.32282 | -55.32116 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35258108-88f4-3d36-855a-5502853c9414 | -6.7887 | -56.23796 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| f45beec6-7523-355d-9854-ea3b5f5a67bd | -3.29676 | -54.01211 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 04628575-0733-3bb7-aa55-5fb9956ea6c4 | -5.16999 | -45.33292 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f923d6e8-f221-388e-b66b-884e168a6c8b | -2.84647 | -57.46709 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 85d581c3-46f1-3ff2-98b3-621688e42baa | -1.32392 | -55.43884 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d15c2155-1fd9-31b6-a717-e56f8adad129 | -6.71613 | -56.14005 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fa86d522-43e6-38ff-b5f7-3083a5959399 | -3.1631 | -57.69561 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b46a29a2-ec21-3d2a-b128-06ceb637bf06 | -0.21343 | -49.78503 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dedbbfd6-073b-3220-a04c-5ba2f388450d | -5.27809 | -45.72897 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8d62d99-ada0-32da-9411-ce972b114f93 | -5.62557 | -43.0617 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7c69199a-54e7-3057-8fc5-efddba0628fd | -6.64346 | -52.95924 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 18c93da5-e364-3ee9-a0d6-eda31285973e | -3.25961 | -54.02259 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a00b0a42-d7af-3d8e-ac1d-6762890be04f | -5.39124 | -45.64747 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 120d01bb-0408-375a-9fee-43e5cf598ed0 | -3.3275 | -58.2271 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ca1076b7-4872-3406-b93b-21ecb57d8240 | -2.98402 | -54.08031 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| adc3bf68-1d6a-3461-aca0-577666737663 | -5.09118 | -46.21435 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 9d71adce-e112-38e4-8358-499d78ec3bc9 | -4.83953 | -40.40025 | 2026-10-08 16:39:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3154ebb3-8773-35e2-916b-a49a2cb29b6a | -1.28557 | -55.41656 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a4c2fdd8-ad95-368b-ace8-6df41f727e1b | -1.20655 | -55.68574 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f1a5e870-ae3f-3f44-80f4-36c85f6e369f | -3.26432 | -41.62929 | 2026-10-08 16:39:00 | NOAA-20 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 04127375-c0b7-39a8-8557-75529a1f7485 | -5.3761 | -44.64396 | 2026-10-08 16:39:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3712e2b3-b5b2-390b-8887-dea2610e4ef0 | -2.01589 | -57.0753 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb004265-1ee7-3eeb-960c-9e9fe3da39c8 | -0.59757 | -49.43093 | 2026-10-08 16:39:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| fdc68584-7ea9-3458-9df8-04abc2e79a6c | -7.226 | -55.09399 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 16a52674-0cb6-3367-95fb-31a7a452e43f | -5.51135 | -42.83947 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 53a80bfe-73f0-34b2-93f9-1da6915abec0 | -3.79325 | -59.31637 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 83e9aa27-4d39-36ca-bdbe-3164f89b66ae | -3.46706 | -59.25312 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ed32b493-46b8-33d6-bbd9-2a951fdb453d | -6.39617 | -52.72639 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 334b1a2d-735c-3628-9ed3-4f6e50659037 | -3.03723 | -54.27524 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e4800c3e-4d94-3608-aa12-dd1c90799a97 | -5.45697 | -45.58986 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d545554-8776-3ca3-be5a-8f3d3737ed4a | -6.16673 | -52.65705 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2db55b45-6d0e-39b5-86c2-ea90ffafd871 | -3.30259 | -54.67104 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b01ad946-8ce9-3843-a1a0-4268bfa1dd43 | -4.32253 | -41.23484 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 443b04c1-db60-3370-93a9-e056b7afaae9 | -1.19634 | -48.9222 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 37b122cb-d850-3a08-a839-fd0e81db57d1 | -2.052 | -54.29765 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8c5ccf69-8903-32ab-b15c-877058f2b435 | -1.33388 | -56.39803 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 849eef7e-5c29-36bc-8323-3cb2a87b1648 | -5.97912 | -53.59401 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6aabc883-1d2e-3e11-8b10-12a7fa170847 | -2.3014 | -45.70986 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea240248-b2e9-3c2d-954f-7449ae4c597b | -1.53962 | -54.82755 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| e6d40201-688b-3622-8522-1fcaaf7fe3ff | 0.39087 | -51.15231 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b893b757-6f21-3d44-9d4a-b6624fc74763 | -3.30516 | -43.09155 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2afada38-bfd3-3a1b-9eff-af4e109f3b4d | -5.69552 | -53.48921 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2856fa77-6cb3-3d1d-8ba2-2b0c625988fe | -2.55064 | -58.04966 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 09ca2cd9-076a-3809-8fa4-0f27163293b4 | -3.73327 | -59.44368 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 354c2700-cc4f-3441-935d-3a70b17f9d0c | -3.48725 | -59.50772 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 01b9204a-bc6f-3d4b-bda1-76272116d19b | -3.01938 | -57.77988 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6063971-5e88-384c-9e3e-b2c10676346e | -2.87614 | -45.75986 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 21b36d9c-87d5-3982-bbbe-fc13bd2e1c8f | -1.19826 | -54.20821 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3f083c51-8afb-37ac-b52b-d9625c808b53 | -3.20622 | -50.54885 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fb6d937b-52a7-31b3-ba65-67bcb6d18872 | -4.72528 | -40.9433 | 2026-10-08 16:39:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1c4ccc08-09a5-31f2-8ace-f58e63dc4362 | -3.49424 | -43.3386 | 2026-10-08 16:39:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1851a2d7-199b-35de-8ea0-0a0b76e37d0b | -6.27326 | -55.25821 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a8f9f1b-ab15-383d-b81b-fa5152f19639 | -2.80876 | -57.05341 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d08e670-a230-37a2-ae48-08d68a78369e | -5.73202 | -45.14961 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 19081e9f-ee35-3611-b919-c271ab4acf52 | -5.09501 | -46.2173 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.0 |
| a3e38aae-376c-30e4-b187-05ebb9e12527 | -3.07788 | -53.95656 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| da1c6792-5672-3f81-9a09-bdf660886348 | -5.4636 | -45.58886 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4da9cde2-f68e-3a9a-a65e-a02743c6544c | -2.10886 | -47.96051 | 2026-10-08 16:39:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c223c955-705d-3008-a9d7-1bd64112fdbc | -6.7332 | -55.11339 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e72c4cb3-65cd-38b6-8fc4-4ba913ab93a4 | -6.1351 | -53.06796 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 7dd4f08e-66db-3810-b4a7-a48a8fa46098 | -2.87686 | -54.18216 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ba45bdb-ad25-3059-8ed9-dbf43ab404be | -5.39407 | -45.90902 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 62889484-1785-32be-89a9-6b009e1fc041 | -6.1271 | -52.71574 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2d9e43c3-695c-39ff-8a3b-d69b022cb5b3 | -4.09822 | -44.12489 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7b97ec56-4c2a-397f-8353-a9f6f89b4c6c | -3.90805 | -44.39116 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a84d7b16-5118-3f1d-b663-457d5bf352ba | -1.41306 | -57.87314 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b3326406-45ec-31be-a15f-9e9e6b0f2d20 | -3.80291 | -40.46887 | 2026-10-08 16:39:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 52632987-7f23-3c9e-804d-fea36218f8f1 | -3.79151 | -41.66778 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 038df1af-3ee3-38be-b499-21c1682b1e7d | -6.4802 | -53.68258 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bad84ede-5164-3bac-b0da-9dabec55f4ea | -5.9247 | -51.82416 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 72305799-60f3-330f-b6cb-790c170c5cf0 | -3.47554 | -44.31067 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 563bebae-4dc4-38f2-aa82-3e1bed298d06 | -6.83187 | -55.26976 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f2ce834f-d8b4-363b-838f-60aa9259ec2f | -3.16353 | -54.73263 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b335fb19-ab38-396b-900c-56610ab1210b | -1.28512 | -55.41367 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a3019352-3b56-3b14-adfa-a24a4ef0f526 | -2.73428 | -44.32965 | 2026-10-08 16:39:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 80c73ea2-8aef-3f70-80e2-b676af675ff0 | -3.0637 | -54.3815 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d9902fea-b3f6-337c-b479-10aa020cf728 | -6.95143 | -59.52232 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 85f762ff-c059-3151-a84f-6d54f2481556 | -5.48757 | -45.04018 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 555298a3-2dff-3594-9128-9c44ff1dc078 | -3.49894 | -60.20604 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b64a3af2-6cf5-3f33-8950-8976bc2e910d | -2.22782 | -58.11141 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2c9bffd9-063c-3b17-81ad-32e56be86752 | -3.01934 | -54.12169 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e253fdb-c3a1-3e5f-927a-574453e15827 | -3.05934 | -53.92884 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| ddf00550-5cc5-3039-9280-45b0c163303b | -2.49567 | -44.17413 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c71fd362-9119-30b9-8e24-04bc55be6ba2 | -3.21225 | -53.86227 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 728f80f7-76a1-3bac-956e-69fcb0f218bc | -2.49424 | -56.16324 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f5dc2ad0-5255-3db9-8032-b377bc7a820f | -2.62022 | -56.48471 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 33385b28-83af-39f8-955f-a2f1e57077f1 | -5.6341 | -45.79283 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| d346aa76-c5b6-3986-8c64-9814e634dfca | -7.5038 | -54.99728 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa216c10-32c4-36ec-94f2-f003844bbbaa | -4.49649 | -42.54738 | 2026-10-08 16:39:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| ab10d06f-a1ec-3b2d-8774-b3e631e31145 | -0.83524 | -49.26484 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0fc91266-bcc1-3a1a-b3e7-c94b8a973aa0 | -5.37364 | -44.19719 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6acea4b0-675b-39ca-89dd-06284972e836 | -3.65088 | -54.05666 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README371.md)
