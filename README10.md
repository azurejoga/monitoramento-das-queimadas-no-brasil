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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 984e38d9-6183-3bb8-9ab6-9936d1fc4998 | -8.2963 | -44.93914 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aca45b20-f2ee-34cf-9db1-79422b4a8885 | -9.24315 | -44.49636 | 2025-09-25 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca431aa8-d07c-3e98-b197-1d3c0d403e96 | -8.29748 | -44.93277 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd8c22a2-3968-3bb9-bdba-3b25c2170d90 | -8.64549 | -40.39687 | 2025-09-25 03:42:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9bfd4ab2-50cc-365e-bf24-1afc647e074c | -8.28795 | -44.95422 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abf03f3b-ca37-331e-a1e0-b7ec407279f8 | -9.65851 | -40.58869 | 2025-09-25 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8e80918e-40cb-327e-8313-a42d89902e51 | -7.17811 | -42.23736 | 2025-09-25 03:42:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e8df6e8a-593f-32dd-8dcc-3c62bd66c8ac | -6.42297 | -43.07724 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 3b303457-0a9f-3fcf-9e49-5341db491af0 | -6.89087 | -44.76209 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d75feaf8-984d-3520-a25d-3a4fddebc4dc | -8.68878 | -44.03677 | 2025-09-25 03:42:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9a14122-518c-3f1f-8940-98a19ff634bd | -11.40423 | -44.95789 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 479202f1-e75b-3fb1-995e-ad010f3cfc5a | -8.49279 | -45.01461 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9b862f4-5bed-31c6-b1e9-ea44d7eac28b | -11.65156 | -44.44544 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 141229d1-6da7-3b76-889a-278e52230da1 | -7.01424 | -40.31905 | 2025-09-25 03:42:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae71a647-bfe3-37e2-8b1f-f06e7e35bc63 | -7.37779 | -47.04398 | 2025-09-25 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 030ae60e-365b-3e61-bade-6b535fc935c4 | -7.17353 | -42.23663 | 2025-09-25 03:42:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 64bb352e-e969-3354-a94e-cc968dc4abec | -8.29571 | -44.94237 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7c92b54-ff53-3865-8fbe-3de140ae11cf | -8.50755 | -44.9951 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b75a6104-49c1-3c20-8cf6-1dddb653ad73 | -11.78102 | -44.90796 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 336d221c-d423-37d1-936a-a50ee5895779 | -6.5922 | -44.6232 | 2025-09-25 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fddf3b72-4d52-354e-9fbd-20a22478d6fc | -11.90969 | -44.7746 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7edadade-1656-3622-b3c7-fec886d8efa4 | -11.80165 | -45.56749 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b89da1ae-a196-30db-8419-281e149975ed | -6.55254 | -43.83432 | 2025-09-25 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84f87d20-cc0a-3cb1-ad13-c0d320e2dcce | -11.67359 | -44.40913 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 053524a3-c66b-37d2-a460-f8c1a905cce5 | -8.12853 | -44.14434 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76040e53-0aeb-3d3c-b020-7348777b3ade | -11.49393 | -43.54366 | 2025-09-25 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1915270d-4b43-342f-8f6f-800e1d06ef67 | -6.55201 | -43.83727 | 2025-09-25 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a80d444-3963-321d-ac76-0ba4f7427cd3 | -6.67671 | -43.13392 | 2025-09-25 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3eb09735-4978-3dd2-85f2-137e9c00d9c5 | -12.06634 | -44.84807 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99d220bd-c492-3c0b-8224-9cb4bbe7564d | -10.92259 | -43.75267 | 2025-09-25 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5526c29-b80d-3c5b-be6f-f35091d9bea8 | -6.68062 | -43.14038 | 2025-09-25 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98026e2d-fbd7-35bc-9f07-3a68c54986b0 | -11.42922 | -44.93779 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 735442f1-c294-36ab-a367-5eab457ba1e1 | -6.7999 | -41.75916 | 2025-09-25 03:42:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93340b1d-6368-3fd4-84fd-753a29fc1063 | -6.34866 | -43.35981 | 2025-09-25 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49a241c7-6c6a-3f64-a88b-156f72c53628 | -7.14631 | -43.53537 | 2025-09-25 03:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1725023c-6327-395b-9b31-4fc7509badd6 | -11.42861 | -44.94102 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f7e686-df94-3482-8fb4-d280cccc2e65 | -6.68253 | -43.12957 | 2025-09-25 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2267de1-b3c5-3df0-ab27-97b0e881b151 | -8.56639 | -40.98792 | 2025-09-25 03:42:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23d48271-176a-3a24-8d8a-bbc4face7ae0 | -11.04089 | -45.88853 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c962fe-0032-3a31-973e-1a58ed982e7e | -6.72762 | -43.97385 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07613f69-206c-3a78-ba63-fe8418474cc2 | -6.69502 | -44.61867 | 2025-09-25 03:42:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8a80f41-bf93-389c-bef5-0a64723015c8 | -11.01772 | -45.91801 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79bfd590-d2d3-38bb-9eab-77bcefe84e62 | -6.34918 | -43.3568 | 2025-09-25 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e398e1-17a2-3916-863b-298e1afb28f2 | -12.10096 | -45.78702 | 2025-09-25 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83c981a9-e159-3cfa-a67f-8580e4e4c419 | -11.04018 | -45.89223 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e56eeb8e-1e88-3869-ae4c-4cd1396dc6f7 | -11.69625 | -44.39626 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3483cc4-ace5-3968-954e-d19e6de87217 | -7.31616 | -45.76839 | 2025-09-25 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c471566-1247-3414-9885-dd7a0f880e38 | -10.93421 | -44.27788 | 2025-09-25 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a7d8a3d-d2ae-32d0-ab3e-854b14292778 | -6.72682 | -43.97331 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b2e1553-f390-3db5-88b4-55d03d69d420 | -6.74521 | -44.05539 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5002d948-12e7-3383-972e-92972bc9545a | -6.568 | -42.06171 | 2025-09-25 03:42:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| bb32e6cc-84b9-3db5-8df9-5bc9093f2ed0 | -11.40368 | -44.96077 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a58cde2a-c062-31a4-bf02-aa46bd978919 | -8.30104 | -44.94361 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c791886-618f-34c8-987e-813271ac0b48 | -11.76664 | -37.5772 | 2025-09-25 03:42:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0da6b009-96f1-363a-bf07-d97a30c57675 | -11.41458 | -44.973 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5512169-cdcd-31d5-8ef1-7fb6330f9b34 | -12.05505 | -44.82523 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8280745-b750-3c54-bb9e-cb4e088c6e7e | -6.89029 | -44.76541 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c57d6de2-ceac-339f-9cd6-9e19a598197e | -7.25729 | -43.02314 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 845504d2-92fc-3189-a9b4-d467d202c8d6 | -7.2792 | -42.98303 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| deb50b20-a604-3646-be43-0592c288b969 | -7.28011 | -41.86056 | 2025-09-25 03:42:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29bbf74f-fded-363c-821f-db61e59deda8 | -8.68823 | -44.03977 | 2025-09-25 03:42:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee85a34-e14c-3fb1-96ef-4787da8e7e36 | -11.62271 | -44.31744 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99217087-018b-3841-b874-c314adbb2862 | -11.62965 | -44.44586 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b186c38-c663-38df-a66c-bd07d622995f | -11.40136 | -44.95873 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c184a27-8242-3671-b949-24f573674bb8 | -10.84196 | -44.82952 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e223263-ed89-35a6-bbf7-3e53a168d4dd | -6.74578 | -44.0522 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf4ffecd-72b2-3f47-aedf-78999b907928 | -6.42203 | -43.08272 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d68a05fc-926e-39df-b6f2-4c7761935bae | -11.6687 | -44.40818 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92ee9b15-8fdd-3264-9ea6-a2b1f79ac850 | -10.82656 | -44.82701 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e93bd28b-94a1-3f0e-ad50-4eae01960035 | -7.29552 | -43.90961 | 2025-09-25 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51f992a1-0b56-3450-aa2c-7b4418008831 | -8.28855 | -44.95096 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 723a0acd-1ace-39cb-9b68-9622cd419b42 | -10.10523 | -45.3286 | 2025-09-25 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5011749-cd37-36d1-8ef6-2df049de7906 | -11.61276 | -44.34413 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 054b12e8-d292-317a-9b6e-79196d0d770a | -12.04949 | -44.82729 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96986a05-1692-3e0d-a4f2-9f7e3ff203dd | -7.28454 | -41.86142 | 2025-09-25 03:42:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 029294f5-dcd7-3cd1-b199-ebf654e46693 | -8.48115 | -45.00636 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcfc0a6d-ac41-3896-8a08-401520e3b5a2 | -12.48574 | -43.2155 | 2025-09-25 03:42:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2e01ba5-c3b9-3e9e-9d3c-c1bbbf2a12f7 | -11.40033 | -44.9643 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce5b68af-c8e4-31e2-be62-a7c06d8208f9 | -7.25744 | -44.90316 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f4ab14c-9d4b-3266-93e2-e59a5975b8cd | -6.72247 | -43.97279 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5478e595-7aea-3544-a33a-f316c6daeab2 | -6.42013 | -43.0938 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9e516e1a-184a-31fd-ba09-833e6338b383 | -11.79252 | -45.58675 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 502d1e38-76a9-36a8-846f-438f6494e3d6 | -7.15232 | -43.53056 | 2025-09-25 03:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57938609-956d-3762-834d-f35d1b994752 | -8.84062 | -42.99755 | 2025-09-25 03:42:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2777d10f-ae60-34f6-9177-85418a5d1c51 | -6.41126 | -43.08656 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77d8d16c-cd6b-396d-8424-f5cda17eaee2 | -8.48745 | -45.0134 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55741783-7f03-38ec-80bb-62515e93291d | -7.15181 | -43.53343 | 2025-09-25 03:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea6b308-3814-3af7-9cf9-15ace81f28b6 | -10.83625 | -44.83178 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cfd1378-3e13-37e3-a488-09a6a5c26312 | -6.48367 | -43.79363 | 2025-09-25 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bc2e9db-2d86-343d-9d5f-940e7f668592 | -10.83747 | -44.82526 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c517437f-fa23-3f66-a086-d152e1124fcb | -7.3169 | -45.7643 | 2025-09-25 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6ac628f-b7af-3aa3-86c6-a15e31fab7e1 | -6.42109 | -43.08817 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7615aa03-c3d2-3a29-8dcd-176df8e931e7 | -10.59024 | -44.0788 | 2025-09-25 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6f9ce1b-68fb-3bfd-9967-abb41b8a6fbd | -6.82762 | -43.17883 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 90e884ac-bc39-3c60-8b72-238647234471 | -6.59161 | -44.62656 | 2025-09-25 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a514a35f-673f-3061-a713-835499fe0308 | -11.11368 | -44.88686 | 2025-09-25 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ef925b7-47c5-3b68-a97a-f1c89d10dfdd | -6.56263 | -42.06565 | 2025-09-25 03:42:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7e80c307-b81c-304a-a55d-e4670d8847b6 | -6.8433 | -43.17585 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bcaa5aaa-50c9-3112-9b52-713120fadaf4 | -7.04954 | -43.95741 | 2025-09-25 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4994c043-2630-358d-9d9f-2db90247d4b1 | -11.79909 | -45.58095 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
