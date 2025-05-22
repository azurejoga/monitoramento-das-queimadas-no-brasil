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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3184c390-17db-3d13-bbcb-b1876a969589 | -12.27934 | -57.2701 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a002112b-b0cd-386a-b11a-0c106674058c | -12.66634 | -58.22044 | 2025-05-22 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d21407a6-e334-3167-9d15-03490ae2551d | -12.68508 | -58.12965 | 2025-05-22 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e8f4a9a-0d2f-3e3b-890a-8e5d8bbc8dde | -13.80804 | -52.89578 | 2025-05-22 04:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80172907-b876-3398-b3cd-c4e26b674932 | -13.66713 | -53.93261 | 2025-05-22 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d3e9321-0410-3c04-908e-b5aecca8c3b4 | -13.38699 | -48.45519 | 2025-05-22 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60535881-bcdf-3f2a-b505-dc21fef7da71 | -14.01555 | -55.13042 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cdd0f4e-1669-3a32-a9eb-11f0584ec01f | -13.69614 | -45.27462 | 2025-05-22 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 714b089d-8384-3837-a7f4-e7d319bbdd66 | -13.06745 | -52.02385 | 2025-05-22 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 848f64f2-b569-3680-8464-93c4849d9010 | -12.28824 | -52.50389 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e7ef345-efa8-3976-8e41-bf0dcd1d6079 | -14.15858 | -50.50367 | 2025-05-22 04:23:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab5efb01-306f-3d1d-9d4d-4cf36247ea01 | -12.48456 | -57.18642 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45a0bfeb-43ed-33a4-b5d0-5a9e2d32361e | -13.7838 | -54.30318 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b72a1580-d5e3-3771-8908-57d7784a797e | -14.03522 | -55.13751 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fee31cc-d128-3401-be5a-14a8e702875c | -13.77796 | -54.3076 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f66cbe35-ad87-35e0-a1a0-76f1034e2dee | -14.0206 | -55.13148 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2f7595e-6fa2-39e8-816c-4756858e3ae0 | -12.28902 | -52.49955 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af457faa-b664-3acd-84fe-d24c0537aa28 | -13.64936 | -45.55679 | 2025-05-22 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c0d4479-b73b-38a0-ba5c-116036671cc0 | -14.01943 | -55.13744 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6eae16a-13b4-370c-9518-493d5246aec6 | -12.50297 | -57.21823 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d8ced81-8c5f-3a8a-a4b2-2b349c3a6226 | -12.28385 | -52.50307 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4fc1ee6-e360-3772-960b-c09fd5ff0b0e | -12.29263 | -52.50473 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b8a48bfd-8bc9-31a0-b5bb-b09f6fdce34b | -12.72271 | -54.97249 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3422f57-d307-31d9-880c-e7fa05a92063 | -13.47865 | -52.28293 | 2025-05-22 04:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19edc34f-1bad-38c7-94fc-3c21d935c57c | -12.27759 | -57.27274 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f87795d2-4e54-3eca-b197-9d0f65d8e40b | -12.30141 | -52.5064 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98ff1386-e419-38b5-9982-42916817605c | -14.03382 | -53.3778 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ec559d1-6a5b-34da-8ff1-e8c4873bd605 | -12.13257 | -54.66259 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86922767-d7bb-364e-b961-e884d10ca9fa | -14.05374 | -45.5169 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51e793b6-d6ff-3564-b300-fcaf42804fba | -14.02898 | -55.14244 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33c052e0-1cb4-3b79-8bde-a95139c2aa9d | -14.228 | -45.83376 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 336751fa-f6c5-354f-80c7-427abdcb1c9b | -13.78176 | -54.31396 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be543c88-9a06-32aa-a91a-31d94ea95ab4 | -14.0347 | -53.37317 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e23df9c3-46b2-31ef-9e5b-ef391b6ca4f2 | -12.72174 | -54.97202 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c8d1999-cbd6-39cb-b914-7d2732bb1f1f | -13.67091 | -53.93859 | 2025-05-22 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65be92bb-4714-37e2-bbdc-d0519ddc1326 | -12.29702 | -52.50557 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 715ae69f-5c22-3a43-aabd-d4673c15ae92 | -13.70006 | -45.2715 | 2025-05-22 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df3353d4-a2ed-3a48-a2b0-61f0aa2f2cf9 | -17.09584 | -43.80277 | 2025-05-22 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0eefb8a-c3bc-35cb-8d5f-ebd43107ecb0 | -17.77784 | -42.80611 | 2025-05-22 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22cd6c23-2b18-3991-9412-b39e77340dd6 | -15.84993 | -46.48722 | 2025-05-22 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebf61adc-7da5-3f77-8889-f6d702689806 | -17.78148 | -42.81043 | 2025-05-22 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b2aad5c-2957-3ab1-a9ed-d1a5d832f686 | -17.7036 | -47.49664 | 2025-05-22 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b156cabf-11e1-36c8-a2c1-96e2b6542cc1 | -17.77719 | -42.81114 | 2025-05-22 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 942fe968-d684-36b4-a58e-76ec38c1800c | -17.7075 | -47.49359 | 2025-05-22 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6068b9d-cda0-3d5e-82cd-edb22756c6a5 | -19.15991 | -47.82003 | 2025-05-22 04:23:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5ffb1fd-40f2-3dd1-b133-f7b5454e82e2 | -15.85326 | -46.48777 | 2025-05-22 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cea21683-a8fe-3f1f-82eb-b7de7fd92754 | -17.91538 | -45.52679 | 2025-05-22 04:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d16b1aef-7acd-39a8-8b75-72471e036c7c | -16.84772 | -51.39992 | 2025-05-22 04:23:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7cf27b3-b70b-3453-8009-d410da0c3c1c | -19.51243 | -44.27705 | 2025-05-22 04:23:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 107aca06-f5d3-300d-a66d-f5b8186950cd | -16.38403 | -54.5796 | 2025-05-22 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ade2e15-2d06-3edb-bfb9-a007f81ab970 | -17.59638 | -43.19974 | 2025-05-22 04:23:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6b5af65-0aa3-3bd5-8f88-3cb8eefb771d | -18.92905 | -41.93428 | 2025-05-22 04:23:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f9a0083-ff99-3ebd-b483-74c91dfd20fd | -17.10233 | -47.93542 | 2025-05-22 04:23:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aada62b9-709b-33e6-8041-3606bae00e79 | -16.37939 | -54.57847 | 2025-05-22 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2de09a5d-d710-30d5-846f-e502e54cafb3 | -18.34967 | -46.4827 | 2025-05-22 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32d6e27e-7c1f-376f-a995-ce2925513c3a | -17.61873 | -54.17334 | 2025-05-22 04:23:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f308b57-0616-32a5-b61e-f1eb99921586 | -17.55667 | -50.52562 | 2025-05-22 04:23:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 751c1d46-7836-3f2d-bd5c-e1ebf637865c | -17.36096 | -48.79483 | 2025-05-22 04:23:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a4aca2f0-2101-3499-926b-bb55f0925593 | -17.15082 | -54.0113 | 2025-05-22 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d34b64c-dce3-3c5a-84b7-e9e8e68d60cd | -17.77759 | -42.80985 | 2025-05-22 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfc0e2b2-de6c-39e5-b66b-27275f62e123 | -14.04499 | -56.06715 | 2025-05-22 04:23:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15127af3-1840-3964-8580-989e29c2a272 | -17.27435 | -42.64939 | 2025-05-22 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b48e6651-1a94-3fff-995b-51eddea8a60f | -17.77828 | -42.80482 | 2025-05-22 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55a19598-96eb-3435-8f78-6f584d5762a6 | -18.81381 | -48.52254 | 2025-05-22 04:23:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14d7c017-2552-3d42-9eac-ef2c9904adce | -19.36748 | -47.61893 | 2025-05-22 04:23:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a87e6471-072c-38b1-83cc-a6f73f679636 | -16.28197 | -58.66535 | 2025-05-22 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| afb90e09-19e0-3d9a-b949-92d2b05f2a87 | -17.27825 | -42.65004 | 2025-05-22 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e593fa27-c828-34d6-b253-8844239033f7 | -17.55613 | -50.52767 | 2025-05-22 04:23:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 745a245c-b22c-3907-ba73-85e6811461f5 | -18.81046 | -48.52194 | 2025-05-22 04:23:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51efbca6-ca50-3636-844c-80413cbb10ce | -19.15658 | -47.81945 | 2025-05-22 04:23:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8dadeb5-ebfd-3ae5-b7b3-efdfe46ac7c5 | -17.61336 | -54.1772 | 2025-05-22 04:23:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7b7efb6-fa37-385f-a6f8-3af0450c69c2 | -16.81528 | -47.65875 | 2025-05-22 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f31b7dad-c15c-3249-8108-adf2ce5b0285 | -19.36412 | -45.35869 | 2025-05-22 04:23:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 282b66b8-5061-3a9f-8508-e68316537a23 | -17.28215 | -42.65071 | 2025-05-22 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9b65113-8e2c-3646-9de6-5b6443a2885c | -16.67999 | -43.88577 | 2025-05-22 04:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0015511-31a9-3e90-99e6-c83fdbc8f464 | -16.28095 | -58.67015 | 2025-05-22 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e7878d28-441c-3c4a-a9b7-dacb4068a1a0 | -19.36691 | -47.6226 | 2025-05-22 04:23:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2450ad35-cca6-30c8-9670-6c672aa58657 | -16.8524 | -51.39567 | 2025-05-22 04:23:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4a0b99c-638f-331b-aa97-cfcff696486b | -17.91481 | -45.53067 | 2025-05-22 04:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea919187-be04-39d4-837b-20b786b96ca0 | -17.8397 | -50.81073 | 2025-05-22 04:23:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d5b16c4-e241-31ca-82e3-a84b1a7af88f | -17.35757 | -48.79422 | 2025-05-22 04:23:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 135fa325-684b-37fa-bce7-a2053f9df51d | -17.26975 | -42.65401 | 2025-05-22 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0aed0e0-bfd5-3b18-87b4-317ce65baae3 | -14.05036 | -56.06831 | 2025-05-22 04:23:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bd283d0-2ac1-3867-9a1e-48df9a4c01be | -17.27755 | -42.65532 | 2025-05-22 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a488bf67-fe04-3bcd-9374-a7e29717058c | -17.83626 | -50.8122 | 2025-05-22 04:23:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fdea8ab-836e-3931-8dde-07d9f0208d00 | -17.27365 | -42.65467 | 2025-05-22 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d12d9b1-36ac-365b-900c-fc110fd9190c | -16.40798 | -42.26366 | 2025-05-22 04:23:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1e8902c-4ebb-3bfe-9869-2c8642fd1ae7 | -17.21422 | -44.79954 | 2025-05-22 04:23:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bf13736-4fe7-33cc-84f5-ef1e4ed8514c | -17.61786 | -54.17792 | 2025-05-22 04:23:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a88cfb9-ecd7-342d-902e-fde5e085e3f9 | -17.47036 | -45.47401 | 2025-05-22 04:23:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad7dbacb-c5d7-3273-9016-1d8a816dc1f2 | -17.70693 | -47.49722 | 2025-05-22 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee025364-af9c-32ac-87b7-3b5562bd2329 | -17.61424 | -54.17261 | 2025-05-22 04:23:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e60cc96e-055b-3838-9095-657438671e7f | -16.28185 | -58.6668 | 2025-05-22 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 769383f1-5633-3e18-a86a-6c5085ab703f | -14.16901 | -58.32331 | 2025-05-22 04:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83a55c2e-b728-3aae-8a6a-cd32a5e2839c | -17.34383 | -51.90242 | 2025-05-22 04:23:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd4a88c8-d4f3-3bc9-9a0b-847868f78dc2 | -14.17517 | -58.32465 | 2025-05-22 04:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58adaccc-4cd0-3cce-b8f3-64709a0ba1e8 | -16.38298 | -54.57719 | 2025-05-22 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76609647-837c-3f28-8766-0daee7a984d6 | -19.79685 | -41.94331 | 2025-05-22 04:23:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a486cd12-b801-3609-8db3-0509c8124b0e | -19.0655 | -53.45662 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fc1eef5-934f-387f-9e0e-b2feabe97d72 | -19.12115 | -52.69113 | 2025-05-22 04:25:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
