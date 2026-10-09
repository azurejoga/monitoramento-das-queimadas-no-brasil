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

## Dados Diários - Página 210

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54de128c-34a8-3e39-a0a0-e4ad340b9471 | -3.10335 | -53.96223 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8cf8b9d9-5c13-3e55-8770-fd21bc9d7756 | -1.09957 | -54.17237 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b0b74e-2792-3c73-97cf-7d1cd9a259fb | -11.39123 | -46.67907 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a6cdfb7e-cc9e-3719-8c91-e4aa5db6ae57 | -2.88218 | -54.19163 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58ff5e03-a758-3047-a009-d2949c445a89 | -4.09103 | -48.9618 | 2026-10-09 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 862a21eb-f8f9-3244-96a9-e7b4a4582a96 | -2.98722 | -54.11413 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac015921-16a5-3f31-b97a-0a748c3e8d6b | -3.57527 | -58.63608 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89d7c774-4d79-38a4-8522-5fb9230191c1 | -8.98537 | -45.91023 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ed397e1-b869-3e4b-925b-881b7a6c7fd3 | -3.56826 | -54.48413 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4240dd48-c3df-3034-a634-98ad8de514b4 | -1.11007 | -54.1785 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70504343-8269-3f36-9199-819e887e4c4d | -2.99427 | -54.14425 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37693c3d-1b70-36f3-813d-bfbbe020dda7 | -3.9801 | -54.44808 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9292289-4345-3a18-8165-9c283c6f08ab | 0.52725 | -50.9038 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a31ca908-7eb4-3f27-9c6e-2a36c937df84 | -3.31538 | -54.04333 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1235cd7-a54d-31be-b794-c660f262e642 | -11.87588 | -47.38718 | 2026-10-09 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92f7ecd7-0e54-3890-ad5e-5f6c08bcba8a | -2.94115 | -55.79013 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d50b1bd3-2735-35af-8d5e-cf429769c4fe | -3.77969 | -59.25279 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 662bda6e-8cdd-3efe-8529-bbe70d0f1e35 | -1.39966 | -57.93371 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e304068b-9ab2-3058-b0bc-6c75b972f811 | -3.57462 | -54.68959 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2718930b-de7f-32ce-90b3-2efbc9965232 | -2.99539 | -54.06188 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8fac01-e779-307c-be07-114798289027 | -3.30991 | -61.1688 | 2026-10-09 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c9b00d5-a143-383f-80c7-78683aac2bed | -3.79059 | -52.39587 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9da700df-cae6-37c6-99b1-25625121274c | -2.51385 | -56.16446 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0b6a171-fa91-32ff-9439-ce0d882f0d32 | -3.8945 | -58.95904 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 078dad16-3764-30e7-bb17-038e658c2d8c | -2.4913 | -58.07768 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7ac522d-33b2-30eb-81c3-1b6b087f90fe | -3.58876 | -54.57811 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8a833ed-7ee5-30eb-a48d-1027affaf4be | -2.84495 | -57.47451 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 567806f1-b561-3bdb-860d-184970092084 | -3.48045 | -54.73022 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5b463dc-2f0e-3884-87c8-2918d9b2b044 | -10.02209 | -48.04033 | 2026-10-09 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed69d5c0-a75f-32ba-8878-6151984d583b | -3.20618 | -53.86945 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81027695-eaa7-3e2d-a703-b8482eb00ba2 | -3.10712 | -53.93796 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3e96485d-1640-328d-98af-6dd3cacaa6ae | -9.07413 | -61.14503 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 062e35c6-a0e0-36ef-b49b-37fdcd4d70ab | -3.50555 | -59.26624 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaf116c4-ba7d-3459-9e77-1de072b6ed02 | -2.88144 | -54.19631 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f515c1e-a8af-3872-9d90-0293ac22451c | -4.27058 | -54.87326 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0053ab8d-59c0-39ef-a9d5-36eb36678a44 | -2.62083 | -56.48779 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77f95c62-baa8-3a14-a6a6-a1381547327c | -3.65511 | -59.71104 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71d2165b-6f8e-353e-984d-7747447e55ab | -2.32429 | -48.49427 | 2026-10-09 05:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a58bdac-1076-3459-ba30-e1d8636c5756 | -3.14874 | -58.56171 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| beef13bd-776d-3679-852c-24c37e9c639e | -3.06026 | -54.21449 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9049acf1-b22e-3136-937b-e9cfa7cb66b5 | -8.33341 | -49.12518 | 2026-10-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8d018ae-0c80-3c25-9d80-5edd2ee4b284 | -3.63269 | -59.00188 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73167aa0-b705-3ced-8eb0-c040a5d0a3b9 | -2.56262 | -57.41261 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1402aca-6839-3eb9-b569-dd6aaea9abad | -4.02546 | -57.87297 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f043e945-de50-360e-aa39-5dac74d2f45b | -2.88131 | -59.19599 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23fe7b56-95f0-371c-be9d-6788cf79f71b | -3.55593 | -54.68674 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 251a07e5-db0f-35b7-9da8-bf1e1c0be747 | -2.54893 | -58.0372 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0db63ce0-313b-31e1-a8b7-9cc3743f13d9 | -3.1165 | -54.17192 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8d5f4b0d-3e76-3f6b-926c-2c9f154846be | -9.69344 | -58.09195 | 2026-10-09 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00dc510b-8ae8-3651-80c2-b9f951180cbb | -3.38898 | -56.93167 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf0054e4-456c-3d9e-92ab-1b022e5a9bd0 | -2.98857 | -54.08032 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17c8412d-6c35-3b7e-8a72-ffe351b78c2a | -3.18763 | -58.63837 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca9a1fc8-10da-386e-8967-244d4de08fff | -3.20217 | -50.83134 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1fa83d0-b89d-3ecc-99e2-b6da337f38e6 | -3.20601 | -50.55176 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c5bd577-77e9-3b23-8282-71a33dabb0d8 | -2.77549 | -54.08161 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152114a6-59ec-3e47-88b1-ddd0b8e76182 | -3.26619 | -50.39899 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 677e3ad8-0f1c-3dd6-a7dd-0e77b8742927 | -10.42286 | -47.28709 | 2026-10-09 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ceace1ea-fe0a-3811-bee1-ea24fb5e7961 | -3.10288 | -54.18432 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba5ab179-fdb3-313e-b9e9-bd3c38da7dca | -2.46983 | -58.08488 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8256f6a7-e311-3a4f-9c2c-99ee6891c306 | -3.09174 | -59.26166 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 931c00ca-080e-3d46-9360-6603d3ae517c | -2.58734 | -56.16411 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9935480-f526-39a3-a0af-d817498194b0 | -5.09079 | -46.22148 | 2026-10-09 05:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1a51da-dc31-3906-b874-e5e1f0818e35 | -3.34621 | -50.41241 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86b9aabd-f177-385e-9c23-d387257cda64 | -3.01802 | -54.10651 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 219fc8b6-33f6-3f35-be3f-516a85266032 | -3.00443 | -54.7922 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b051fdd-2bbc-3090-a4b5-df518e907767 | -3.50218 | -59.30855 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5e4bebf-fd1d-30bd-9f52-615fa6830628 | -3.70759 | -58.2939 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0afe51aa-243c-3ff5-bd14-03403c660ace | -8.99241 | -45.91177 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d0d9c2b-c778-3621-9e95-cad7e289eef3 | -9.26264 | -47.45198 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c600fcc3-5114-3908-8c60-495bab1816e9 | -3.44435 | -59.54733 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24da6cd6-5d0b-36d6-8a85-3c5bf9cd3d33 | -3.7267 | -55.97708 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02ac8cb4-f639-372e-b9b1-683b24c9bdb4 | -6.92276 | -59.27407 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e045a14-ce43-3975-8f69-924c10e35035 | -9.88699 | -50.48578 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d5b264c-aab1-39eb-bfe8-606c7006f7b9 | -3.73359 | -59.45641 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38e34bd1-e1e2-3092-8f24-47e44e52135e | -3.63138 | -59.56627 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e60d40af-b51d-396d-b84d-52e8fc944e11 | -2.77577 | -56.50709 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9aeb0aee-2c40-3755-88cd-d07d4524e3b5 | -6.92826 | -59.26076 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a059cf93-aed4-3eaf-b274-b96fdaed483c | -1.3885 | -55.35028 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 265482f9-35df-3b2e-97ac-93970dddcb48 | -4.15435 | -55.13808 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24c7888c-30d2-3d35-b84f-32482dce75c6 | -2.93659 | -53.92204 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf9e448d-cfcc-35ac-92bc-eeddcb4d93e6 | -3.17549 | -58.62941 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd9bb19d-2614-369a-aa63-64e61f10e8f7 | -3.83805 | -55.98141 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be3b9118-8843-32e5-a522-b13183259d2e | -3.929 | -56.02616 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4eef89c3-f982-390f-a2a6-d8f3fadb5183 | -4.3707 | -54.75322 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b310e269-ff73-3db1-8044-db7097094a42 | -3.91605 | -52.1348 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c31fad0d-8709-31fc-bbd5-23dc2f994eaa | -3.68658 | -60.53796 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be3f560-f567-3a81-98a5-2cbd87edca3b | 0.44515 | -60.5333 | 2026-10-09 05:23:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f12622c-c35b-39f1-b2e8-5d548b761337 | -3.53322 | -59.34921 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b92c15c-65ef-3661-b411-26886782a017 | -3.01257 | -54.2454 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b915fc30-d0f5-39c4-9cd6-7be2dbaaf4a0 | -3.18323 | -58.64473 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2310a510-6d5c-31dc-8f68-f7f13c2e03ea | -9.39573 | -49.00056 | 2026-10-09 05:23:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e227c6d3-450c-3273-8c4f-2492636f08e9 | -3.76917 | -59.25469 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc00f4c9-23ca-3c8a-b6c3-0e21684feb6c | -3.35116 | -50.41318 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5715b3fc-4fa6-3e8e-be6a-5ab01548908b | -3.31388 | -54.05301 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e14e8de-0c13-3f16-a807-1c5ccb910cb4 | -3.73191 | -59.46691 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 889b62e8-90e3-305d-90a1-6715b2756e29 | -2.48302 | -56.09037 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8242b4e4-4b7f-3c3e-b778-8ffec785217b | -2.49945 | -56.18899 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb3785fa-cf25-3c5f-b6d4-02e99d4a35cb | 2.76571 | -60.00632 | 2026-10-09 05:23:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2d4c0dc-2ce9-3294-81b7-9d3900d35021 | -3.36521 | -50.48943 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78a17a94-5c53-3468-85b0-5c9842c42292 | -2.745 | -54.10108 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README211.md)
