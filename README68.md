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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe35658c-d284-36b7-a51c-c0dd7acd3aac | -2.87273 | -54.15305 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 22403d61-36bb-356b-8d22-336a2e2fc78d | -3.08121 | -54.17428 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bc883c3-1f0f-3fcb-97de-d9d456243961 | -3.63208 | -55.27917 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 115e0a90-ff49-3d34-bdc1-163b1fa47075 | -3.68649 | -55.94604 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e94f5f01-84ef-336e-bafe-8fa718f23e06 | -3.07968 | -54.18493 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f5c5464-973f-3c38-ae65-053d47f66fc4 | -3.08047 | -54.17045 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2edc3b1f-563f-33ce-b7aa-0f700d7122de | -3.0835 | -54.24907 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1172bc49-3d52-3e3f-8ff6-869ec216b839 | -2.99422 | -54.13001 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4fae69f3-40ed-349d-9ec7-2a23fbc82590 | -3.68528 | -55.95405 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1761102a-9504-322b-8073-f96b270f8b0c | -2.77292 | -54.10582 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d932c8ba-6285-33c1-a117-0948e90e1622 | -2.78676 | -57.66954 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40cbf3ba-b0ff-3d3f-ba10-63f439550c90 | -3.04702 | -54.21878 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c70fad4d-a98d-3b10-b1c0-e6fcabb4d1f9 | -3.23675 | -53.87018 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec2e3f12-1332-3ee0-9a62-ad36fc0cab1b | -3.13328 | -59.01628 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96fcfc9c-6796-3403-b5e9-91e2b3ba5832 | -3.06434 | -54.14673 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77bcc78d-6cfa-34ac-8c21-d023aa0b77ce | -2.78477 | -57.67015 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb0e4acb-a269-3d9d-a097-174bb9387600 | -2.15693 | -59.22506 | 2026-10-06 05:59:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90438483-7868-3f50-9f27-537b60f27584 | -7.0559 | -59.23449 | 2026-10-06 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b2ffb3-ab9d-310e-ab21-0a23637bf23b | -2.98166 | -54.12838 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3fd39f4-05a3-3166-b9a9-2a25bc368796 | -6.69405 | -55.20435 | 2026-10-06 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ca95656-cbe5-30e6-9e41-7e13a51af456 | -2.95024 | -54.16051 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d9a4d61-2a69-37d7-b9a3-a9d20ebcccb2 | -3.49805 | -54.62079 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 046ef1ae-d45c-3621-a2a5-c39fb28bcff1 | -2.87342 | -54.14831 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 130c02f7-da47-39a9-984d-a35aea006750 | -3.16835 | -58.63585 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d55ed8eb-deb6-3dc2-a8bd-905b57d4ea64 | -2.7863 | -57.67249 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7c1e597-8002-3152-bb70-a55bef0fa2fc | -5.68363 | -53.4903 | 2026-10-06 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc63f90f-bd30-3ea2-a378-be462b593fc4 | -3.0952 | -53.71438 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 164c52b5-1bef-3c8f-8997-09f3404edcfb | -2.98938 | -54.11856 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c7c8a52-f1b5-3336-bbc4-23ba08faa720 | -3.67373 | -55.95226 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab19e463-292a-3b51-9a72-7ebe3c090b7f | -1.28286 | -56.98272 | 2026-10-06 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f464ea96-a40c-335c-b737-f64ee6d502c6 | -2.95905 | -54.14547 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c79ef5ba-45c1-31fe-85c4-148610c54db6 | -4.46276 | -54.96328 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afcd85f5-0912-3e8b-9680-3164a7cbf82b | -2.79376 | -54.14101 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d84c2b76-0e04-3071-bc62-4c501d9eb2ac | -3.23694 | -53.88142 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b428c10b-0fc2-3596-b831-d023f7841cb7 | -3.16819 | -58.63174 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f85fab7-a588-3195-92fd-545455a7a3d9 | -3.70894 | -58.9294 | 2026-10-06 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd7b9af0-db57-341f-a814-d2b3b74bb61f | -2.89601 | -54.16236 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a4ae4e9-bca0-32c7-8c9f-640fe934db45 | -3.50289 | -54.63152 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fae55e9f-4576-3a7a-896b-c4debe1648b9 | -2.87432 | -54.13267 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cff2300-e2b3-3a50-b02e-579f9dfc1ff0 | -3.69049 | -55.95866 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee823845-df94-3bf0-9b30-78fcee8ba9cf | -3.09967 | -54.17364 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f43d6581-fdf0-3f2d-822b-8cb0de206787 | -3.09558 | -54.16558 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5ec151d-ae6f-3d68-b079-9986a2bb2612 | -3.87134 | -55.81478 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e16dce5-cae7-3fd6-a669-096bbe82674c | -2.87679 | -54.17021 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc64af6-ca45-3001-892e-8e2e155ac8e8 | -3.67494 | -55.94427 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2380d09b-6004-35e9-912d-251349c42360 | -3.27655 | -54.18718 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52b2b857-76d7-36d3-a9c1-843dcba1cbc9 | -3.08687 | -54.17154 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37b2efd8-a01c-3c3a-848c-b9c3877d14c3 | -5.67496 | -53.50209 | 2026-10-06 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69a4e4e4-6afc-3a6a-b52e-b88d75728c99 | -3.62604 | -55.27831 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e62f8d0b-6e4c-3a07-9371-3c404ff1922f | -2.07176 | -56.85865 | 2026-10-06 05:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f1ada3f5-9410-395f-a634-a96d955299be | -2.32537 | -57.9847 | 2026-10-06 05:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6883749d-8038-3e3d-a32f-db0b1fdbc2d0 | -3.0813 | -54.16496 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d18890-ddde-3fb5-9f55-75557a1b6856 | -3.06058 | -54.21553 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88883cb0-1394-30c0-a34d-bc0105c1b5d4 | -2.87771 | -54.1535 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11102248-d0d3-3be8-aa95-08274d805b23 | -3.07664 | -54.23914 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 829d7895-920a-326c-bb9c-80f177f62ebf | -2.06642 | -56.85803 | 2026-10-06 05:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b42fb8-1a73-3874-9d3d-f805d960bac0 | -3.09273 | -53.73119 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b9c655c-850d-3353-be02-45b6f7aeeeeb | -3.07884 | -54.18123 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd62460c-fd30-370d-8608-254bf648a4a3 | -3.68482 | -55.96056 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c0ff77db-a8c8-3ab1-8235-26294ffbf692 | -3.09401 | -54.17645 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6c846d4-e794-3b88-b396-d0eddf091853 | -2.5271 | -58.08938 | 2026-10-06 05:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1145474a-97eb-30a1-a93d-778b0b3dfd59 | -2.78169 | -54.09129 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 402fb34c-1363-34eb-9a1f-387421e1279f | -2.90799 | -54.08426 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 961b8189-31e0-350e-b152-57c8d167756e | -3.09326 | -54.17265 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e973b39a-bd84-3a25-9cba-ba88f5cc59ca | -3.6796 | -55.95584 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6e10b06b-e48b-35e7-9a39-453cbd57c11b | -3.10049 | -54.16824 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a826c9c-aea2-3f3f-b6b4-49afe1014e2d | -3.68651 | -55.94886 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83b9f046-342f-3661-8ab7-e77751160972 | -3.09606 | -53.70853 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017b7013-27cd-3100-8d73-7c2eafcdaeaa | -3.51003 | -59.50863 | 2026-10-06 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c978d4-097e-3050-871c-79ac016c3a11 | -2.32322 | -57.98935 | 2026-10-06 05:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f92e5ac2-7bd1-3648-8c9d-59f2057c76b0 | -3.87781 | -55.8115 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ede6ccc-0beb-35ef-b72c-7b8090edb1e6 | -3.09038 | -53.71901 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3761a29a-ecf7-3ab5-9f69-4d1dcb42ae6c | -2.87842 | -54.14882 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04d66a92-6492-3e7f-801a-61e1728d7a4c | -2.87354 | -54.13784 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bec1537b-cd18-3a32-833e-dfc79052a785 | -2.78434 | -57.6731 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8fc6b47-f628-382c-9e9a-ad96ac62c452 | -4.4577 | -54.96654 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec1c3bcf-bf65-3cb1-aa8f-eac5ad267c38 | -3.08043 | -54.17968 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83907eb8-ff0e-3814-b10e-0167b9923357 | -2.13384 | -56.70176 | 2026-10-06 05:59:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1ef11cd0-25f4-3220-af9a-6886486ce63d | -2.95182 | -54.14998 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f231d8dc-26dd-39d7-a42d-ec5e1b585a87 | -3.06604 | -54.1792 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3edca710-aa81-306e-bb5a-099f993b2e3e | -3.88495 | -55.80363 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4057e0f7-48f5-3d9e-bc38-766fc7d25355 | -2.95103 | -54.15524 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95df221a-efeb-37e1-9e3b-247b67a52b92 | -2.89107 | -54.16204 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f131d8be-35cb-3279-8971-5328580e9fa1 | -2.77605 | -54.08521 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d89d503-d8a6-311b-bf8d-ed506fc521dc | -3.17313 | -58.63657 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7e8c507-d52d-386d-b106-27921b3586ff | -3.09124 | -53.71338 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 249d0f6f-aa24-3e5d-93a7-5a781bd9bfcd | -3.02247 | -53.90028 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d5cbfb48-6028-3128-af5d-2f2afb98241d | -2.7839 | -57.67606 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88217aea-c710-3ce2-8e36-53f7ee5769c8 | -2.80229 | -54.1322 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8d7aa52-97ae-3579-844d-2e9af6104b96 | -2.87635 | -54.12807 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 847a43dc-354c-39f3-a7cb-faa6ac6604a6 | -3.0751 | -54.24929 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 510762b0-c38e-3bb0-a5de-79f2af077cfd | -3.10755 | -53.76755 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6f24912-b659-3f2e-b0c4-8a308daff5c1 | -3.0612 | -54.16774 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b614a666-cad2-376d-a99e-dd36427f5caf | -3.00087 | -54.13179 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93c6ab20-83ff-39d3-9182-5405f8ca6fa1 | -2.98221 | -54.12248 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de9adb4e-73c8-3542-9d6e-56db117d30f2 | -3.08276 | -54.25418 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d57a2b2c-186e-32ad-a45e-fad0311a30fd | -2.86637 | -54.14191 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b1d872-6cb6-330b-af00-75324eb5cb89 | -2.98955 | -54.11922 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08ec8939-118d-3975-a74d-79d5e9130bea | -3.06356 | -54.15198 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e57cfcb-ff72-3699-8224-bd91cf34c4fb | -3.46577 | -54.59679 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README69.md)
