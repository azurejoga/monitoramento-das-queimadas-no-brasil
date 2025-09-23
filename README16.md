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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1004460a-0ebd-3652-9a0b-4ecf133e61da | -8.95905 | -44.4872 | 2025-09-23 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0af7c108-f19d-3e26-a9a8-8b6c1ce50030 | -7.36238 | -44.45029 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c209e7eb-e2e9-3086-a8ca-fd4bbf43abae | -11.45483 | -43.52444 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22f49065-0a0f-3a27-962e-d6265deb746b | -8.00489 | -45.7135 | 2025-09-23 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f568d51a-420f-387e-8ab4-b675f8cdc105 | -9.14976 | -46.66407 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 695f7946-d24e-3475-a054-a5fd3f2c7680 | -6.71547 | -47.20235 | 2025-09-23 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bc388f6-7fa6-3b54-9f77-17e4920e07c1 | -8.54188 | -44.91868 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36936c86-a9ec-30b4-a60d-e34dc83a748a | -10.57689 | -43.82313 | 2025-09-23 04:19:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f7f585a-27d6-30a5-9216-6bca895d3831 | -8.00265 | -45.72751 | 2025-09-23 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c20e1474-fc07-3c62-96d1-4571a2886468 | -11.42227 | -42.92434 | 2025-09-23 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7186c07b-aea3-3db5-8f9b-a33f4de4ae4f | -10.82463 | -44.80199 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24e44f37-741d-38b4-a21f-baad2c5557f6 | -11.44731 | -43.52727 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5e511f-926d-39c4-a693-311d4795566b | -6.35098 | -56.19349 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 298d3298-90f1-3431-981f-40ce0df8f57f | -11.4163 | -44.94621 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc740f7-9125-360b-91fb-2b2f95fbeeac | -9.18908 | -44.62376 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d948fe7-f328-3338-b171-56c6603da83e | -10.8202 | -44.80851 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e88d9fb-70b3-39db-adac-f448cb25c866 | -11.52867 | -43.61348 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42e4815b-f4e6-3800-b0cb-b047cfb3fe32 | -11.40521 | -44.95172 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0cf825c-5978-38b6-9b5b-78841803c6a4 | -11.41963 | -44.94671 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9aca802-cef1-3297-bc3c-92dbd97f1494 | -1.6749 | -46.70162 | 2025-09-23 04:19:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f510871c-0079-35d7-bae9-fe8e9550c426 | -6.59476 | -44.32204 | 2025-09-23 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0de05631-b517-3478-84d7-f805198fce55 | -7.88072 | -44.02273 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f51520b0-3d1b-32b4-8a43-54cd6e9b0ddb | -10.82075 | -44.80499 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a02227d3-4635-34c2-8efc-3f660b89c4db | -10.76941 | -49.14649 | 2025-09-23 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c41a247-796d-3dcb-87b5-f371bcd2db3a | -11.02313 | -45.89603 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf05f3c0-e52d-39bc-8c0b-ba0e99d55ac1 | -5.65286 | -51.47208 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0fc8aff-ecd1-39a8-848b-e26e554bdefd | -11.41187 | -44.95276 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b040f8a5-7799-3ba3-ad02-422a6d9c09d8 | -7.88516 | -44.01617 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6d14cd1-7526-3085-afa2-a884c3826fd8 | -11.53041 | -43.60193 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba69d8fa-ad93-3553-b42f-62311e56e8b6 | -8.00101 | -45.71648 | 2025-09-23 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edc0da08-e157-3097-a34e-4361cc755428 | -6.89537 | -44.76343 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87846fe1-b6c4-36e9-94eb-d809bb192ea1 | -11.86653 | -56.88023 | 2025-09-23 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7df228a2-e40c-3baf-9647-4afb4b69dada | -6.25423 | -45.33727 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 282787ae-b1c6-3493-84f1-ca0bd3ae9599 | -8.01088 | -45.46383 | 2025-09-23 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fd36d6d-90a4-3fe9-9155-974876999608 | -11.52291 | -43.24527 | 2025-09-23 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1e51495-00f1-3b2f-9901-f459615a1070 | -8.52648 | -44.95185 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fd0c49f-258b-3f73-a76c-31199a3d6248 | -7.79048 | -46.18733 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ae78595-4dd0-3e96-803d-d107a6085ee3 | -7.22724 | -45.17832 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00b5d277-e47b-395e-90f4-e5ba325f283f | -11.86358 | -56.87709 | 2025-09-23 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc510729-aa64-3c3f-b4c3-b6a4535e0278 | -11.4152 | -44.95327 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f26c34da-6966-326c-aedb-38f45fd01c39 | -6.90702 | -45.57018 | 2025-09-23 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac797aea-7d4f-395f-87b0-7522ecfbbf68 | -7.362 | -44.53918 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecfce53c-b246-3ecb-8308-a5fea9b8c6a3 | -8.8077 | -43.0766 | 2025-09-23 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db45911f-efee-3efa-a0b4-d3cb6a33405d | -7.90129 | -44.02229 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6b841b1-5e47-388f-969e-8d1f66d962e6 | -10.8526 | -45.42701 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb46101b-a130-327c-a46e-aba1e2181d9f | -11.535 | -43.61841 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e8e17a9-d11a-3da0-8ea1-0443dffd1739 | -10.02311 | -46.28855 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87fea3eb-3972-3e4b-9250-29c81075490a | -8.94521 | -44.4886 | 2025-09-23 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d88c5ae1-cb16-38d1-9cde-b8e9417b0762 | -11.89121 | -41.27464 | 2025-09-23 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fa0c8cf-e7d9-375f-92b4-6b8dd1a9695f | -13.56091 | -42.55931 | 2025-09-23 04:19:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c18ed0c1-eceb-32c5-8bfd-af1c90d78a69 | -6.9579 | -45.20621 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73ad16d9-bd93-3e16-ada9-b78c53d20df0 | -5.69234 | -51.05305 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ffe00a8-631f-3d62-8e6a-902ef9a4717c | -6.81541 | -47.0157 | 2025-09-23 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c18870bd-d511-30d4-b0f9-0acfbe2fdf0a | -13.49963 | -47.23845 | 2025-09-23 04:19:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33b4e4e8-d2cf-3011-97c7-7d6593fd623c | -6.58583 | -43.59354 | 2025-09-23 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7852921-2bac-3b81-ac33-0c25e7c71a66 | -7.28673 | -44.15287 | 2025-09-23 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 525c0ff9-c2bb-317a-a793-0a960c3adf4a | -9.01812 | -48.03623 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5bb2b7f-e0e0-30de-a2cb-d399259812a5 | -6.89483 | -44.76689 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79c996e8-376a-35e3-a93f-835c1c59f252 | -7.46573 | -42.62883 | 2025-09-23 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe78ed44-7452-3fc5-984e-332b63528946 | -9.00593 | -48.02163 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6b58b5b-e8e4-3ea4-ab2b-d3cbfd7f6cbb | -5.64826 | -51.4713 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e48008d-9af4-3e00-855d-c992cf34c519 | -11.43808 | -43.51797 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf6a33a5-452f-357e-90f3-753bf85b0cab | -11.89583 | -41.27027 | 2025-09-23 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23f345ed-79b0-3677-b25a-c785b624873f | -9.59182 | -46.43732 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64bd738d-49e5-3c3c-8c03-da847f75fea9 | -6.89814 | -44.76741 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94a8dc73-db91-3ad6-bb37-e3f664bfc9b5 | -13.51649 | -42.34885 | 2025-09-23 04:19:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7618e01-3c1f-38e8-bb21-985ec06bc459 | -11.02368 | -45.89252 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a795e23e-646d-3a28-844e-88d5187cff8b | -8.13712 | -44.46872 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 058ef060-addd-37a0-a446-a55bcbcc8fc7 | -7.89517 | -44.01773 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4b5e808-8e63-334e-9071-4703ede842b2 | -6.89759 | -44.77087 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c317ddd-cc16-3db3-9315-1bf96f088226 | -10.81687 | -44.808 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f14f19f0-48e1-394e-9df0-13970b7b2230 | -10.96144 | -45.70667 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 177f586d-0cea-3c55-a10c-6afbed7ab2a3 | -11.9173 | -43.42837 | 2025-09-23 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d67c2b44-345c-32d0-80d4-9c2ac34f8481 | -11.88801 | -41.26912 | 2025-09-23 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f6faef26-2f26-3dda-864f-3831b5a5abe3 | -8.54133 | -44.92215 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd062db9-a0f3-34a6-b9b1-9364c12cd381 | -7.8637 | -42.95478 | 2025-09-23 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2281bc13-5524-3f51-9852-8c463587aecb | -6.26088 | -45.3383 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9336c75-cdf7-36b2-8707-4868fcfdc297 | -11.41854 | -44.95379 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a9d1d8c-954e-39b6-b555-f76b9586e3b0 | -10.34166 | -46.05848 | 2025-09-23 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43f605f1-1caa-3d08-be17-caaf047e6697 | -7.87962 | -44.02979 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fb571ef-173a-3ba3-8a0e-450a1353785e | -13.56224 | -42.56127 | 2025-09-23 04:19:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9b3bc34-5789-3325-8d16-0f8dd84693cc | -9.15975 | -44.61546 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d702211-feeb-3902-b1de-30bfdb45fc16 | -8.91678 | -47.23247 | 2025-09-23 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dca03f99-0670-3c30-8ab0-a31bd4d5f467 | -6.96453 | -45.20727 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0365022d-9c8f-322d-8fb7-99a51eeb4003 | -6.96122 | -45.20674 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e91dcffc-04ee-3c1b-a215-d047e7a0c89f | -8.81995 | -44.33548 | 2025-09-23 04:19:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| debed6af-ba5f-3543-b671-fc1ce4d448a9 | -13.65531 | -42.50885 | 2025-09-23 04:19:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d1b73c5-a025-3b57-8909-4fa4a2badcc8 | -10.8537 | -45.42001 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f2b393dc-25d8-3599-a227-054dda6de71c | -11.39468 | -55.11862 | 2025-09-23 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5a97f27-6ece-359b-9288-9a1661643d4d | -6.96177 | -45.20326 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 020e94d9-94ed-3533-ba61-69f50fb3717f | -7.51854 | -43.69049 | 2025-09-23 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4a62f157-e863-39f3-8e52-84f2ee101f94 | -7.88795 | -44.02023 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b0e1802-5de3-3e34-9796-254ae0b7cafd | -7.69897 | -44.90163 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6539cca1-e5b8-3ac5-b424-1d00a260ad86 | -9.19905 | -44.62532 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9216544a-1bc5-3066-b841-4caf6555225c | -8.52372 | -44.94786 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e08f520f-fe99-3aff-96d7-3b656981914a | -7.3372 | -39.70742 | 2025-09-23 04:19:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b36cd307-0438-3918-98ba-caa43c323adb | -11.40909 | -44.94872 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2e13f96-516e-36b6-b0a4-f13f0fc5860f | -9.44844 | -40.39235 | 2025-09-23 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf7df5d8-1b67-3483-b210-5221c5aa4f37 | -7.59677 | -45.73824 | 2025-09-23 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1badaaef-a775-3ddc-81ac-513026080bc3 | -7.79758 | -46.19908 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
