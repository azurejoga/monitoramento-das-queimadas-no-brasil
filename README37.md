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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8865ab2d-1125-3de2-a545-6593b796086d | -9.89595 | -44.89565 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49eeb1fc-158f-35e5-a1d4-728bc3cf6bb8 | -7.79855 | -46.46051 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 03a3ae64-9ff7-36c6-8213-ab93b17891d6 | -6.13957 | -41.84712 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b74fadf4-a68d-3862-9cf7-5d39a11f2fa6 | -7.8898 | -45.69116 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5c9ba10-b449-3ff2-8e73-2a76e7cd184b | -5.66539 | -42.87834 | 2025-10-29 04:23:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 49472051-d110-3ebe-a379-548e4ceae01f | -6.13418 | -41.85863 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a8d9dfb6-142e-3699-b03e-3403cb155a47 | -6.93687 | -47.01104 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8291be7e-b21e-3200-bb18-9f78f904772a | -10.39171 | -40.64989 | 2025-10-29 04:23:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 161f892a-d106-3780-ab8a-fa12d915b8c4 | -6.45984 | -43.55822 | 2025-10-29 04:23:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1965357e-d9ea-37aa-88f2-e946cfa161d4 | -6.10242 | -42.4432 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| db868c6c-2c89-3454-81fe-a3524c406aa8 | -9.23851 | -45.56975 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9d6fd51-5f16-3ada-95ad-0911e2f739be | -7.40826 | -46.9926 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2be89ef5-56af-3f06-bd4b-83f6b77e0f0f | -6.48783 | -42.21153 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea45ca4b-ab53-3124-a3d9-7ba37e5f0c6a | -5.34357 | -46.86068 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ecc2dc89-e46e-3ced-b2a8-423636367d4c | -9.88092 | -44.88241 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dbf3fc8-f7cd-3774-abba-a040f99fca82 | -8.77656 | -46.49082 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19c7e62b-b20f-3ac5-b7e2-fde76eb69015 | -10.54971 | -44.84253 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82dff045-fa53-304f-8fc9-b0f3f3125b78 | -8.19142 | -46.94805 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8df0028c-ca0a-3942-ae95-620c9a9610a1 | -10.2105 | -45.94951 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bb6fa4b-dc55-3deb-9aea-bd1c5ef5aea8 | -4.96593 | -47.59294 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6631b47f-b342-3d6d-8cbd-2e6a8b723173 | -6.10462 | -42.4749 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 24191d96-2f81-32d1-b39c-13a934fa9365 | -5.348 | -48.17031 | 2025-10-29 04:23:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0cd8c22-dde4-338a-85c5-cedb16c9a0d6 | -6.10976 | -41.72 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f1b77ef3-e097-3af0-be53-4bf622ccd60a | -9.48865 | -47.0089 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4bb05ef8-8705-3b0a-aa91-d023177b3699 | -10.51314 | -47.7303 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9595d25d-5f9c-3e7e-9740-0233646a6c56 | -7.07544 | -44.95698 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 68e228f8-9829-3a3d-a193-7d84c581be37 | -8.69576 | -47.13886 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320eb5ba-8a8c-3def-bc05-78e055905d82 | -7.7408 | -44.72424 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9c2595b-2104-3aef-95fa-4d293a960fbc | -10.65091 | -48.00425 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 90893676-eed5-3cc6-820f-671d00c93c5b | -7.63619 | -46.92494 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 359d6db1-5fce-38c5-9301-7584c12b08ee | -6.14123 | -41.68989 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a8eb8aed-6a90-37cd-8e37-444b78cad0d1 | -7.36172 | -47.6326 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb6ca5d7-2961-3a87-95dd-06c34dae0dc5 | -7.20363 | -44.16304 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5814b835-4b68-3b26-aa04-97279343e53b | -6.10851 | -41.72807 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6aa926d-0b5b-3cdc-ad0c-3b875e205c6f | -10.95299 | -47.62745 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6903635-61fb-33ac-a854-1378b9b7efb1 | -5.60903 | -47.11405 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4573d621-f887-3740-85b6-1e156f924118 | -5.96612 | -46.32203 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c514d53c-72c0-3c0e-837b-17c16a9aa626 | -7.05467 | -44.81128 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17862c33-db8a-378c-a500-d08a3057e453 | -5.68875 | -44.48507 | 2025-10-29 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a31b7657-dc9a-374c-b264-d85a69546dc0 | -9.33194 | -49.82079 | 2025-10-29 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfc6a1d3-feed-38f1-852c-f8c04d4aec16 | -6.85801 | -43.44645 | 2025-10-29 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2334f964-f5e9-3b17-b5cb-e4d9e5699dbf | -10.54112 | -45.05187 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd9e0258-4686-3da0-9312-2f385d8bb1aa | -7.27115 | -46.89707 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 260e783f-03ab-36ca-b8fd-13b616ca84e0 | -5.24024 | -45.20044 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 987eb59b-3909-3b7f-bb5f-fbb316fb60fd | -5.65148 | -46.45131 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aefbf5d-7f77-3930-8d0b-f82eda8ebe9c | -8.03202 | -47.4166 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a319d82a-26c5-3619-b1c3-87428a973793 | -5.64423 | -43.28284 | 2025-10-29 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f61e576-17af-37b0-ad3a-9d531cd2e4b0 | -6.12827 | -41.84942 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 34fe474b-bcdc-34fa-ada1-48672c1445e4 | -9.47736 | -46.92812 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f857937-3660-3c3a-a479-3906777b1e08 | -8.29197 | -49.3167 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5753cfb2-8bb3-3f50-9ce2-f5cf16d310fd | -10.74302 | -44.75686 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b29fc0d3-0f96-39c5-b0f9-6a829fe6a98d | -10.5687 | -49.8421 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eeb83508-6955-33ef-b1ed-623c668bfd54 | -7.78825 | -46.48117 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 544f91ef-2d78-33d9-b292-814cbd5ab778 | -4.83276 | -48.54842 | 2025-10-29 04:23:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5b1076a-8ba2-3dc1-a175-2e87d7768be7 | -7.08728 | -47.25529 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebed1d9f-bffc-30be-ab9a-b3ea16a73f27 | -10.55306 | -44.84307 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e428e559-e106-3c39-a5d2-0ebb8c4702f7 | -7.60569 | -43.57206 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35b391a2-9224-3353-89ec-2eae51d3624f | -7.79104 | -46.48536 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ac7c947-b06c-3440-ad1e-5ed44c00d285 | -8.33096 | -46.23276 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9ca1227-fd76-3160-9be0-89e67a1cdd84 | -9.88788 | -47.45079 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7147d38f-b95d-34eb-a031-11cb5300524f | -8.76177 | -40.60979 | 2025-10-29 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 83c71aff-2797-3f3e-a0c9-c606490d4ad4 | -8.25213 | -46.9191 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fca14f81-22c7-3723-b2b7-a8692ef883de | -6.14699 | -41.57397 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 379bc2e4-8293-3b07-8429-93be19082f4a | -8.25274 | -46.91536 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17630bdf-5e88-37cd-99f7-7af42e89ae28 | -11.26794 | -45.52958 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c66312c6-5c46-3062-a76a-7dfeed04d434 | -10.87937 | -45.07299 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dda926c5-3b74-30e6-b78a-987fcc647b40 | -10.8432 | -47.74131 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 373f7d5d-d40b-3da2-9714-72b7a01d76d1 | -7.3055 | -45.68025 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abd44f5d-83db-34ee-b52c-d4e025c41647 | -10.43921 | -44.70115 | 2025-10-29 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b216eb7b-09d8-37ff-8df9-2730e431ec85 | -7.78222 | -46.45419 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdae42df-01e2-3cfd-bd71-d9fa9f1dc2ad | -6.11946 | -41.70469 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 750029e3-d2f4-316f-b97d-56999aaedf85 | -6.96632 | -45.51448 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00522bf-5137-39a7-89f9-880f29a8de37 | -7.74745 | -44.7253 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec539118-bdfb-3517-bc3a-73a6a8245df9 | -10.91294 | -48.38816 | 2025-10-29 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b10bb8f-79f5-3ca0-81ce-fdffc74f11e4 | -6.54011 | -46.76633 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0617981-e58e-3be3-9e6a-d62c967ec6d6 | -9.05686 | -45.05357 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c8cd942-f291-3753-a5e5-1491d2c46766 | -7.32018 | -47.19711 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c7365d9-1b3c-3c3b-886c-81e64ed0e392 | -7.68967 | -46.28477 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bccf069-59c8-3d7d-828d-80ea8843442b | -10.77285 | -45.10717 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc28728e-08f0-3e9e-b3be-9c9d54e23b1c | -8.64483 | -44.80951 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da31da33-7642-39f7-915e-7381c5894958 | -7.3442 | -43.90965 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e67c92c5-4072-3b58-96b5-e683c75fc811 | -8.24371 | -46.9063 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b84f2dcb-c2c0-331f-a2f5-9d82dd0b981b | -10.65566 | -47.99707 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5b0f02f8-0b7c-3b9a-937b-049b7b1a02ae | -10.75085 | -44.75072 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8ef2c76-4ac7-3896-8c89-aaaf96f10c6a | -5.47923 | -46.43927 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 868dc54c-940d-39ed-9639-bb1eee66f63a | -5.19259 | -45.6302 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b3a1ad8-aabe-307b-9003-50d3dd718361 | -8.61543 | -44.80131 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7eed847-9d0d-3524-964e-4935bcf38080 | -10.91813 | -48.00871 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72bf76b9-7180-3d0a-9cec-1b06973a2d49 | -10.56593 | -49.84426 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68f39d54-aab7-3086-a576-e0c313f6429c | -10.6585 | -48.00156 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 86b052d7-8a6f-3056-95e1-3475e02dd0ef | -10.52285 | -47.73586 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae5fc26-f8fd-3aab-a676-fdbf99993954 | -8.88681 | -47.53569 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55dd47b6-0c25-3d52-ba57-880cae05418b | -7.57054 | -43.99973 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a44b209-3150-327d-aa93-a3e26a0dafa0 | -10.51849 | -47.7194 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf5caeda-4372-34da-98b7-31161175952f | -7.442 | -46.61279 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0879b0e1-e1f7-394f-8e42-4dbe555ef10c | -5.49102 | -45.23696 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b177c28-71ea-385f-99cc-303bf8465daa | -8.49809 | -45.58731 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cabc17e-7537-38e5-8c65-ecfe3b0eda82 | -8.55575 | -44.33459 | 2025-10-29 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5f83d4d-042a-390e-b825-ed1ee626a4e7 | -10.3914 | -40.65033 | 2025-10-29 04:23:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30fccee1-82a6-3524-b251-4a94d9f12901 | -11.27735 | -45.51304 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README38.md)
