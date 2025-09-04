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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 962277ca-60e0-38ef-895f-ce3e19c82a04 | -7.64173 | -46.55531 | 2025-09-04 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba3c8b18-c93b-33cf-942c-af30b07dc2c8 | -8.64783 | -45.76123 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e5b5843-34a4-33df-99d8-b5329aab9c01 | -6.8571 | -44.26992 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1bf6637-7378-375d-9966-3e72391ce97f | -9.04301 | -47.01628 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03444caa-01ce-3719-8f56-dc863e61680d | -5.62647 | -51.13895 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcdb5df6-02f4-3fd2-9484-f6bc070d80dc | -8.83107 | -52.00888 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f70138-0d42-3483-93d4-67f1c11e224a | -9.26181 | -56.89492 | 2025-09-04 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ed04450-a053-3938-8eba-a332b28dcc88 | -7.69172 | -50.26244 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2ee15d3-27e8-37e5-be0c-ed90912b8956 | -6.76899 | -63.13041 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a591d35f-da1e-317c-b609-f8a819e5bdb6 | -6.27749 | -43.848 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d740aadf-1bf2-3ca8-95f9-21c23a535b15 | -9.97507 | -51.62859 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d365ecd-970c-3f8c-8a41-0ffe0bee2501 | -7.74053 | -48.77063 | 2025-09-04 04:53:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77dc80cd-2269-34bc-b02a-8e1f853868d4 | -6.46633 | -55.887 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 345855d7-e9d7-3a63-bcc7-5a960b062cb2 | -7.70567 | -50.28902 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 884eda53-70a9-350f-adf9-ca92e5c98c11 | -6.24918 | -42.64707 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd44bfd2-0913-3798-8f94-021d4e6b6bd0 | -5.60368 | -45.02816 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f097b1a3-5ca0-3770-8d89-e8b397bc1c05 | -8.44091 | -47.33931 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73bc5ba9-44a3-36e2-8342-fca8b3fe7735 | -6.22414 | -43.54353 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55febb06-f670-3777-9c28-6dbacac8d7a3 | -10.4294 | -50.38298 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51d8832-85af-3ade-8207-f94afeb0ff7e | -7.04611 | -43.26717 | 2025-09-04 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4de91805-887e-326d-845f-4e0cc4c5bf96 | -8.03494 | -45.37958 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4344c97a-eae8-3c29-8bcb-9c47ec6c86f7 | -10.75478 | -45.26834 | 2025-09-04 04:53:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6980015c-5be4-30bd-bd06-480533003cc3 | -9.70774 | -51.0235 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aab6348a-afba-39e4-9fc8-8f1446724074 | -6.49544 | -44.08535 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb21072e-af09-3ce3-a7dd-3de686791d76 | -7.70531 | -50.31604 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 576e862e-cc5c-3fb8-b8c7-51da05b5ab89 | -6.62855 | -43.9691 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83c09997-1432-338d-b97b-7dddfbf91add | -6.0407 | -46.00337 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18f2d8a7-5a78-382c-b5ac-5429d24d0b23 | -11.0364 | -45.12809 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a19ac7d-aabb-3729-b587-aceca8a4fecb | -6.85669 | -44.27278 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a0b48f3-dbfc-3efe-93eb-0489ae0b98b9 | -6.1231 | -44.14274 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| babb5021-0db0-3a8d-a817-4ef8803f626e | -7.38593 | -56.68805 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7621b672-f8a3-302f-a92c-565d3b64ae3a | -7.05172 | -50.86395 | 2025-09-04 04:53:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc346a73-deff-3843-a4a9-20f4d52a0849 | -9.97907 | -51.62537 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc361916-06fe-3eda-9d18-f3c0a940f4a2 | -8.89394 | -45.81268 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e56a4a28-b93f-3711-8844-9c0c1c83558d | -8.86601 | -47.93785 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e99a5150-bfe5-3c58-bf4c-4f953566ee8a | -6.36243 | -45.64642 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34c59f1a-5dd1-3332-a85d-0a99daa1278c | -6.73287 | -42.27681 | 2025-09-04 04:53:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a17e7106-9e08-3748-861e-c16fe1c7cb29 | -5.6962 | -45.39565 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6355fc1c-a27a-3785-992c-9d3dd3fe480d | -10.43125 | -50.37042 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c3446a11-4c12-3c89-aa6d-17207d8447e0 | -5.68483 | -45.60028 | 2025-09-04 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 194aa758-90ef-3672-90c7-033e967e41dd | -6.73388 | -45.92154 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1117fde8-52a5-39ed-b897-aef625f365dd | -7.92919 | -44.92717 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97bf9201-886d-370e-8bd5-6dfb894f6e5c | -6.23053 | -43.3777 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e6cdaaa9-fbc8-32ba-9134-dc1c5516a6b2 | -6.48817 | -44.09992 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61b1c956-7cd2-38c0-832f-78c83bc1f23a | -7.71472 | -50.32535 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7f58db7a-0612-3a53-8f4f-e28ddbfbb97e | -8.08123 | -45.36411 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3bcbb78-5c30-37cb-91bc-9bfb314fb2de | -10.97864 | -46.84399 | 2025-09-04 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6728c088-1ef5-335a-ac23-629f94a47b82 | -6.68058 | -48.40062 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0fa1bf6c-7dbd-39d9-9573-fe5678fd8cba | -9.3004 | -47.09105 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a152646-9f1b-3a4a-9e60-c707e3514c30 | -6.69619 | -48.41404 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f4e9771-e358-391c-a8aa-e985172795a6 | -6.32554 | -45.68079 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9de8849-320f-3bcb-81c8-36d3270b287f | -6.47263 | -53.40228 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c15bbea4-393c-31d3-9692-037d6f1dbd72 | -7.18926 | -44.16499 | 2025-09-04 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48d18c3e-8b5e-3a31-93a8-ad46c6c25de2 | -7.67374 | -46.7059 | 2025-09-04 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0db6284b-99c5-3539-a960-3d3cf60570ef | -5.90329 | -45.95732 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4199c5ab-a2ff-3683-bdf7-c5270d9e3937 | -6.78636 | -44.09408 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 05d1ad65-2986-3838-853c-648066679a28 | -8.01521 | -44.78325 | 2025-09-04 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54764885-19b2-3613-8e9e-fc8852d532d7 | -9.47632 | -47.60983 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3e72854-1dfc-3fd2-aeee-8b079889fe24 | -8.0342 | -45.38493 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e87bb03-90b2-3f8c-bc2f-880868c1ddc3 | -8.53439 | -51.30983 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52812f66-1fb1-37f8-a54f-2d26d1fcd47e | -5.92876 | -45.55245 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e8302ed-bcd7-3685-a44f-ca7995eb5e03 | -6.74345 | -58.73281 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 0c7d612a-6c1e-3b65-9ae7-7b81083da782 | -6.6869 | -48.4108 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d70ea89-7d88-3e2b-a69d-fb80cdc0a9b7 | -5.65563 | -51.27085 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96fd734f-e8c4-35ee-b6e5-b4759c4a8b80 | -6.5094 | -43.56895 | 2025-09-04 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d108eb6-d774-3cd6-80e3-e75db51cd6c5 | -7.36941 | -49.39804 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d674d11-c025-3403-b535-bab1bf10f832 | -6.22532 | -43.54995 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c3626f4-a73e-3b7e-a19d-618bae78ddf0 | -8.5745 | -50.23585 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3622384f-1bb3-3d24-8788-842f556c8ad5 | -8.00828 | -50.09844 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30ee027f-49e9-3888-acfb-2d857f94e499 | -7.69941 | -50.25938 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef78c678-ed3e-3d0e-a94d-467cda24204a | -7.71117 | -50.301 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c831233-b201-38fa-ae7d-2c864d300acc | -6.25257 | -43.2966 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ead78990-0b39-384d-b15d-280dd281e253 | -6.74709 | -58.73775 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a6378fa0-2d2f-3680-a6ae-a24b9fa3f03c | -7.47425 | -45.66264 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43736a6c-46e1-3734-8b85-0615cfaf52a9 | -6.76998 | -63.13259 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a132f963-8057-39ce-85b9-3fae01291c6a | -9.6023 | -47.03864 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f3e82ff8-ca91-33cc-ad7c-41e9a745283b | -8.01786 | -44.14428 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d72be025-ace9-34e4-ba11-0adc0dc03913 | -6.68528 | -48.408 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 901e49ca-99af-384f-b888-2ff0dd6f3ad3 | -6.28386 | -43.8475 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad425525-bceb-3575-8def-23d4d52d1dcb | -7.70884 | -50.29248 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d812a70-ff36-3c59-9eeb-ebc9de30f7c0 | -10.48655 | -46.7699 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06cd3a78-5c74-3f72-85b8-9509270abe6d | -7.55421 | -45.72195 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1943ed4e-e61d-3806-88b4-e28641b0ff9b | -8.06884 | -45.3476 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0a22c04-e692-31b5-91c4-3ab435fdbac6 | -7.68755 | -50.26606 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bca69f5-ddd1-3e24-80f4-8d6c46aee473 | -7.77626 | -50.95722 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d11f8272-47db-32f3-a7ca-32ee17e13bde | -5.78414 | -46.16636 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6015fbf2-8d4d-31a1-89e4-2f7c419946a8 | -6.2388 | -42.43598 | 2025-09-04 04:53:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4aafee9f-b39c-34fb-8b9b-44118949fabf | -8.44938 | -45.09719 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0e55aec-18c2-37b9-97ba-904e15680764 | -5.74452 | -45.53978 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 169803f5-a32a-347d-9b0a-902e5161c277 | -6.92689 | -46.90012 | 2025-09-04 04:53:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e774b7a-29cf-393d-b41c-523c6e3252de | -6.75655 | -45.92492 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c0e6a2b-f54b-3d9e-8edb-cf08377f9d25 | -8.36098 | -48.34139 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9762179-9f0a-3623-b769-b6196e516bda | -6.76318 | -63.12926 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6758978a-82c1-34ae-b145-01c120ba2f9b | -11.03168 | -45.12439 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ce6aa1-7653-3920-b2c6-5910b3865735 | -6.24029 | -42.61038 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46ffcf82-5b82-3e2e-bd73-c69f5b5de0fb | -6.67988 | -48.40524 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ec722e4d-316c-3d52-9015-ee1ced01c340 | -7.71237 | -50.31703 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b9f9bb1-4872-3e7b-b991-88db9ad92949 | -6.84152 | -59.15714 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cd3d314-d5a9-3c9c-97aa-b47156b8e192 | -8.46969 | -45.0603 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04afd5f7-9cbd-3de2-89af-58a18e619762 | -6.67675 | -48.39993 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README58.md)
