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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 630ed96a-acea-35a1-8947-0900d051fbfd | -10.29906 | -57.1338 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 226167cd-d268-3a54-ac5d-29001aa6f51b | -11.9547 | -58.76047 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0e871cc8-6813-3e98-8910-40031c300daf | -11.9095 | -44.17627 | 2025-06-19 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fdb84ea-19dc-3e8f-8463-97b213f801db | -13.64661 | -53.93849 | 2025-06-19 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0bffbb-6bdf-3071-b29b-d4eae2280b75 | -9.12316 | -47.58543 | 2025-06-19 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45517dda-b496-3f98-85ff-b6d780ec44ca | -10.15592 | -48.98449 | 2025-06-19 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c979130-4bed-3a4d-b4e7-6cff6f45d2c6 | -11.33072 | -45.20966 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44ebc8c2-eb58-3845-a298-74b384f13f63 | -9.79179 | -47.1865 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7b24942f-8e84-303b-9165-928bfedc7b6e | -2.91718 | -48.23891 | 2025-06-19 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d0fc0e-5a0c-37fa-8f5e-02a52b65bd6f | -9.88321 | -47.81078 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c62bdfa-a6d7-3a88-97d3-e2951226e0b2 | -9.01299 | -49.58739 | 2025-06-19 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d65a3ef7-4ecb-36df-aa25-e3520199fc3d | -9.87975 | -47.81014 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cad3c9e3-af7a-31ab-9462-55ae95fce1b5 | -14.21646 | -45.51156 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a57fcf4d-7836-32ed-a34c-eb797430ab6b | -10.50022 | -53.5829 | 2025-06-19 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 935ac59a-b9fc-3763-a560-9b92fd7c02fa | -12.28719 | -48.80207 | 2025-06-19 04:19:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37a3a39a-b5b2-30c1-bbce-9eee96144faa | -7.56804 | -49.29842 | 2025-06-19 04:19:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9fd25d2-05c8-347c-9d30-5767878b8d36 | -11.78508 | -44.28254 | 2025-06-19 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4d3eea9-84eb-3ba3-be1f-5ebbe2dfd34a | -13.28668 | -57.07222 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13ef77e9-cf16-3577-be43-2f64b878b671 | -11.28881 | -48.69839 | 2025-06-19 04:19:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8777dc3c-9f75-3312-a627-27a9800ff5f0 | -9.43093 | -40.38853 | 2025-06-19 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8b99ff2-f918-3c6c-a646-2e3db460317c | -10.23133 | -52.23021 | 2025-06-19 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e27686b-2e19-3647-bf94-339edb05322c | -13.44144 | -44.48118 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79f9ca1c-5011-398d-92b9-6781ee6418b8 | -9.49648 | -56.09307 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc00e4ee-b6e3-31be-951c-b85a1c6923bb | -10.64558 | -49.46097 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bff20ee5-93fe-3fe0-b342-7e557fc2b1e7 | -8.12487 | -46.08299 | 2025-06-19 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c560886-cf29-383b-b5e5-6146d11a8d2f | -11.64388 | -54.14445 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cabb804a-4151-3170-a870-8ee654f0c374 | -12.48468 | -58.47035 | 2025-06-19 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f40bf0-9546-39c5-8b64-9cc2653f41cd | -9.03276 | -48.15937 | 2025-06-19 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7cbc5fe-45c8-398b-a5fd-f6106ad819b7 | -11.41675 | -41.39587 | 2025-06-19 04:19:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7fbd8bc0-9b8d-3133-ac22-f0657364912e | -9.43143 | -40.38503 | 2025-06-19 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0ac0502-1220-39a6-a045-824cdede81cb | -2.94066 | -40.78422 | 2025-06-19 04:19:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91a6e311-9f85-36e5-a509-1c05725e0ee5 | -11.94394 | -58.74622 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| a13e6f8e-b4c2-3e3a-937a-c5966375aa56 | -10.50771 | -53.58297 | 2025-06-19 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bc5446ff-9f32-32e8-a9e5-4e772a315cd0 | -11.52435 | -56.99907 | 2025-06-19 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e3b5bfe-17be-3387-a2eb-2735367064bd | -11.07719 | -55.05286 | 2025-06-19 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 026a1af6-af92-39bc-be61-830f53ac08a8 | -11.16376 | -50.08641 | 2025-06-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99f427c7-30e1-36e1-9185-5a8760097c84 | -14.43604 | -48.90385 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d095f5e8-80df-3439-ab5d-1a56802749d1 | -12.7955 | -48.73632 | 2025-06-19 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc42e7f5-4123-3834-9746-f6eec2217392 | -9.49068 | -56.08691 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 34e9dea8-f70e-391f-9134-dceeb25a672f | -9.7964 | -47.17964 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0ab0d5c0-bcd2-3bf5-8c67-18859d576823 | -3.32326 | -48.71318 | 2025-06-19 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e398599-3685-397e-9ffa-7e5d6ee3cfcf | -10.52308 | -47.58484 | 2025-06-19 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4095c78f-8f3c-3e21-a774-09ecd7222ab2 | -9.41578 | -48.42988 | 2025-06-19 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03cda091-0a60-3650-b78d-d4dccee5a567 | -12.7563 | -44.40813 | 2025-06-19 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 874b3c51-3439-3abf-a159-16d102e41f86 | -14.44231 | -48.90908 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7144f1d6-e333-3950-a981-1075108c81d6 | -11.95052 | -58.74751 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| f1674d30-790f-3157-8284-114a3ef471ba | -9.24802 | -50.03053 | 2025-06-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e3d72c5-6ec3-352f-999a-fa98a9e41805 | -10.72494 | -49.56659 | 2025-06-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 111cd0ba-3c86-3b03-92c6-38e69c9324a7 | -10.0923 | -52.73925 | 2025-06-19 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b570ed22-93ae-3d6f-baa0-96f64aa9d6ec | -12.52005 | -57.20254 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddf2561e-10a4-34ff-809e-18d24d1c8f6a | -13.28751 | -57.06805 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ae2b640-2c9d-36ef-981b-ca5460032d24 | -10.19258 | -48.46846 | 2025-06-19 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501d4d6e-4cb5-3546-b2d7-3c8c3cf09469 | -9.25195 | -50.03122 | 2025-06-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df5a306a-8344-3178-8773-5cd78060a53a | -12.01956 | -57.09758 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3def447f-6312-3511-93bd-1b56be6fc211 | -9.01379 | -49.58257 | 2025-06-19 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f78f6a-934c-38ae-9721-20b7b9ac86cc | -13.2399 | -48.41501 | 2025-06-19 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1116cd19-10d0-3479-9e0f-b33d708e9d80 | -11.08185 | -55.05735 | 2025-06-19 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06952e82-46f8-3b24-87ad-1ae931dc7e9e | -8.96096 | -47.97791 | 2025-06-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39f3f686-c093-3aaa-8fc0-425091f32be1 | -14.60374 | -42.88346 | 2025-06-19 04:19:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7e067172-f84a-358f-a4c3-7eb63e2a0b33 | -12.52228 | -57.20644 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63fb4f5d-a9eb-3e19-a3f7-ef58e3f7a38c | -10.64185 | -49.46032 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 51c95535-d607-3947-a401-5b9c9f934683 | -4.00798 | -43.23967 | 2025-06-19 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f0dc1e4-7213-3d6d-8697-1394de7f2f50 | -11.33127 | -45.20612 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a190ea1-c21d-3ecc-a2b0-d46b3877229b | -11.77208 | -54.36681 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da06c59-e0f3-30f0-95b6-6c5b2a81539f | -11.91234 | -44.18053 | 2025-06-19 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92da9760-2348-3470-b018-5fafdb4842e0 | -12.46551 | -58.46621 | 2025-06-19 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf0d6156-6320-37dc-82ee-f771b51c9b06 | -13.44643 | -47.84093 | 2025-06-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1a61fce-3bce-39bd-a5e5-913af5f4298b | -14.44016 | -48.90058 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a4d8641-a894-362d-a1b7-d61dd58f3bd9 | -8.18969 | -47.15473 | 2025-06-19 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e25e946-8f8c-33ca-8af2-f37d3d7144e1 | -9.32523 | -47.83353 | 2025-06-19 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43369ce0-5e68-3b43-8067-b0872560822c | -12.26384 | -44.6117 | 2025-06-19 04:19:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01f04602-46d0-3d74-bb0a-e6daca7a5caa | -11.57171 | -47.436 | 2025-06-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 030b780f-e5b9-3395-bbdc-a67e019bd17a | -11.95707 | -58.74892 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a1cf4723-c179-3afa-8daf-c41a8fd896a6 | -11.64495 | -54.13879 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 137b4bef-cb95-374b-98c7-36d13dba8925 | -9.89322 | -48.02047 | 2025-06-19 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98b2d0d2-fef7-3f98-b019-3da97dca4ff7 | -12.12908 | -54.66735 | 2025-06-19 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 083c5173-e19d-39ac-a5b4-e0984f760ea8 | -10.72572 | -49.56202 | 2025-06-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 407a0f75-3755-3c0f-9cdc-f3eda11a8248 | -12.79617 | -48.73235 | 2025-06-19 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a26d4eba-0edf-32ad-ac60-caf989a3d98b | -9.49651 | -56.08802 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 953239e1-8728-3a04-ac7b-ab947004e9dc | -12.23555 | -44.19582 | 2025-06-19 04:19:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d05a4aef-1482-30ad-938b-536b3844726e | -9.7924 | -47.18279 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3cc23772-0e45-39a2-9bfb-e51866962b0b | -14.06496 | -53.39753 | 2025-06-19 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5a63b4e-8a65-341b-81d3-a64254297cb3 | -8.722 | -47.99815 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a30a6aa0-f140-3d9b-a0af-a7a3ca94ac15 | -12.02736 | -57.08958 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836e465d-fc8c-3c6a-9713-d59e0c273e51 | -12.47827 | -58.46908 | 2025-06-19 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b4ec1bb-394c-30ad-b4e9-df581c505356 | -10.65533 | -49.44864 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0048c60-745b-3bc0-8604-6cd02ec4daeb | -12.26887 | -44.6013 | 2025-06-19 04:19:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2d6bbf36-62bb-35b1-bef1-069f0463a206 | -11.33403 | -45.21018 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5747d2f5-fc54-32a0-9b08-51d2d281679f | -12.39941 | -46.36251 | 2025-06-19 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a144c75-2174-3ca2-bdfb-ddad9ea45955 | -14.21979 | -45.5121 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1318cbcb-c204-3b28-bacb-0b9c7504f2f9 | -9.49144 | -56.08766 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 61b0aae0-58ec-329f-b5b2-3c89ca5e9cbd | -9.21157 | -45.34063 | 2025-06-19 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3193cbb6-6b16-33e8-a81f-d91f75d88061 | -8.71421 | -50.26762 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ceacd639-9892-395a-a518-84f5304802f0 | -9.50362 | -45.44764 | 2025-06-19 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dcc7667-e6dd-365f-b812-3d38f759b119 | -14.21312 | -45.51102 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e19f5761-e2cb-3fa1-9bb1-925348fd7e7f | -12.2644 | -44.60806 | 2025-06-19 04:19:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04e614d2-bd68-3b66-965e-b384c28b462a | -11.15992 | -50.08574 | 2025-06-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20bb86d5-7015-3ff1-b74c-1add17c40407 | -9.8004 | -47.17652 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5bafbad6-e68a-31e2-a05e-c875d9158056 | -12.20358 | -49.65025 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76736499-7cca-30dc-842d-63f781ab6cb2 | -9.37676 | -47.63781 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README16.md)
