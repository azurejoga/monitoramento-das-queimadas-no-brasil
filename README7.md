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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cee890b5-8d6f-326d-a1a6-33e994528000 | -13.1613 | -56.81866 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9394b93c-be44-389e-9055-3f9bbb48ae6a | -9.28876 | -57.55194 | 2025-05-18 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d42257f7-3cd8-37c1-98c2-68edc95dea1f | -12.37176 | -56.40248 | 2025-05-18 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bea7f3c-e5c0-3617-8f0d-874fca1ef890 | -12.03895 | -54.96389 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8097093f-cf28-3056-be91-2523987b745b | -13.14526 | -56.80828 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a9549e7-b852-3bff-a965-78cc5d6048db | -14.01782 | -55.14047 | 2025-05-18 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4d048c8-ac86-339e-a085-f72a4be9e82a | -10.68141 | -57.60745 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8763447-0a6f-3d0e-b25c-c51aeba12178 | -11.79139 | -49.32027 | 2025-05-18 05:12:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 121b2de6-53ff-3eb7-83c3-81e2a4af674e | -13.04564 | -53.71907 | 2025-05-18 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69ef86ac-7fc6-36e0-9764-623758ed803d | -12.45398 | -57.19138 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0db3d64-7635-3883-b204-59a3c4c72dc8 | -11.29725 | -53.9773 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02e31bc4-d1a5-3d18-981c-4f018c1c7ae3 | -12.12838 | -54.66062 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5d89f52-2ba6-3139-bac6-953fc52e422c | -9.5803 | -63.24466 | 2025-05-18 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 292ecb7c-04fa-3f2e-b698-41b289af76ba | -11.56274 | -47.87349 | 2025-05-18 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7608d38-6041-3daa-babd-b377196d451a | -12.30246 | -52.47374 | 2025-05-18 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5594cdf8-83b2-35c6-aa4a-df319de0a5cb | -11.6483 | -54.39314 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4ff9598b-d27d-39ab-abb6-ef8c302b8614 | -11.58173 | -47.61259 | 2025-05-18 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 578cf9ed-e592-36e0-8988-6ed87fe9e013 | -12.03768 | -54.97276 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55f13c7b-8c30-35e9-a2e9-dc1a9344f492 | -10.04124 | -64.97566 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6cb88f2-6d59-3d94-89e6-dde533a44353 | -11.79181 | -49.31691 | 2025-05-18 05:12:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38f361b6-fc12-31c6-b62b-af59a24a8c2e | -10.75983 | -57.23073 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8bb75b6e-f320-33ba-9e7f-6eef6276da6b | -10.48047 | -46.51989 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7bef7cb6-2b97-35f1-9575-3af245d8dbec | -11.62442 | -54.93703 | 2025-05-18 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15fd0571-bb07-335e-82b5-27eccf536080 | -10.48732 | -46.51588 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9da1ed26-4db7-374c-aad8-b481cb75f950 | -12.68495 | -58.13142 | 2025-05-18 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00b0bc3f-1a07-35a3-bc53-820ab93f91a3 | -13.14183 | -56.80776 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a5f065-7b19-30f6-9419-71ac1089465e | -13.94949 | -54.48925 | 2025-05-18 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c0db576-addc-30b0-acc7-355cf33ff145 | -10.49359 | -46.51698 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8ca35633-9d24-3291-a3ca-f4827106b292 | -12.3683 | -56.40196 | 2025-05-18 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7be81560-cdc1-36cb-a906-ef16ae6592d0 | -13.8513 | -59.72278 | 2025-05-18 05:12:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae016ea0-6767-3058-b24f-957f1150c601 | -15.29419 | -53.20831 | 2025-05-18 05:12:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed38694c-6113-324b-a46f-945def9dd338 | -13.85405 | -59.72689 | 2025-05-18 05:12:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e6d5ea5-6d00-3447-b8ed-8142f89d3d8a | -11.79673 | -49.3211 | 2025-05-18 05:12:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e5f854-17d0-3d59-bc91-dd20e54a1433 | -11.13367 | -58.6158 | 2025-05-18 05:12:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4873016-cc0d-3dae-9dfa-bd5eeb71b969 | -12.12483 | -54.66215 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e992658f-70f0-3f1b-ab2f-a4637d0b9e94 | -11.7488 | -54.71989 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca07faba-f722-38bb-af2d-892f7ed52c30 | -10.49423 | -46.51141 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6ba74e37-552d-3462-ade1-9555546f22e8 | -11.58225 | -47.6082 | 2025-05-18 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5b1fa6aa-dc03-3809-aeb0-ac23f88913b6 | -11.79631 | -49.32448 | 2025-05-18 05:12:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19ba4bd9-59c0-3d7e-bc36-f81832a6b482 | -13.39217 | -56.91605 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 845add91-e3f1-3b3f-832e-11255cd101d1 | -10.3709 | -57.50431 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64cc9f98-a345-3ea6-b581-a39fc2aea23c | -11.64763 | -54.39791 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caae953d-5378-3117-994b-3fea68b9b950 | -9.28931 | -57.54845 | 2025-05-18 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 295a1d81-1971-3235-a0fd-822628b43485 | -10.67809 | -57.60693 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aba46c94-1b87-3835-a4ff-f19836142526 | -10.07887 | -55.48839 | 2025-05-18 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecf6e531-caba-3648-b0ce-935ac4ba9acb | -12.45005 | -57.19455 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72b1e0b5-a351-375b-be09-4742ef692e8d | -10.68195 | -57.60392 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e88c589-d78e-3964-8d4a-bca5bb2a7306 | -11.4044 | -52.95828 | 2025-05-18 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac1d4cd-a1da-3408-b92b-c39122b43845 | -13.04159 | -53.71851 | 2025-05-18 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 474f2d75-9353-3735-b8cf-d26897a51ec7 | -9.24145 | -63.28973 | 2025-05-18 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ddc82b5-81aa-3622-b605-c8ec01ed560d | -14.01975 | -55.1264 | 2025-05-18 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 052c0c80-2782-3adb-ae0e-077177bc409c | -12.03831 | -54.96833 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25e87d3e-86fd-37b2-8d0e-35a05f9f8f6e | -15.29095 | -53.19932 | 2025-05-18 05:12:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e607480-0985-3a89-ba68-0ed28480add6 | -9.24023 | -63.29704 | 2025-05-18 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54c8700d-9c97-3a8a-8ebc-cf73147c7028 | -13.1487 | -56.80881 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f3e9cea-0fd5-393b-9032-c50369fec7e9 | -12.12795 | -54.66741 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d4a3d88-390b-32a7-8485-ef4f252c569a | -11.40025 | -52.9577 | 2025-05-18 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ce034d2-4ee9-3ffa-9b43-573423c394a4 | -11.42634 | -54.29346 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b31384f5-0744-38f6-8249-50b48a03e6a2 | -10.75649 | -57.2302 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3dd159e0-ccdb-344c-a233-f38907b2edf2 | -13.14583 | -56.80444 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d00fdb-c608-3bb9-bb49-b8a02d2cbf31 | -10.47538 | -46.50846 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 486ca9b3-c4d0-38dc-9018-b4830472515e | -10.75928 | -57.2343 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 637099c5-7e7f-309c-9bcf-1a3a1672cd59 | -12.60638 | -54.06776 | 2025-05-18 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c095db46-bbcd-302c-b0ed-80b1e1ee5705 | -12.29811 | -52.47312 | 2025-05-18 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a8a0a2c-f3f6-3acd-93af-e4ffae1e85bd | -11.91638 | -54.41312 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 623cc526-b32b-398f-b71a-8cf15ee7076f | -12.12771 | -54.66529 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d477de9-1273-3dca-9c3c-b9295f87e02a | -20.35338 | -50.19458 | 2025-05-18 05:14:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 31fed1e8-1253-34f4-b9b5-215529a4fe69 | -20.99624 | -51.79295 | 2025-05-18 05:14:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e1433d9-87fe-3bbb-ba84-57bbb141dfbe | -20.95386 | -56.61154 | 2025-05-18 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6af03b3f-2d86-3252-8945-bd8513a47986 | -17.74924 | -56.30533 | 2025-05-18 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c798faed-189a-3317-a600-9ff6cfacf174 | -20.95449 | -56.6066 | 2025-05-18 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7fbfd0b7-b42a-3cc3-9bbf-8bc49030ce14 | -19.06886 | -53.4565 | 2025-05-18 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53732c71-1841-36ad-b7d4-c01d784ed8c8 | -22.77617 | -47.62864 | 2025-05-18 05:14:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0bdcddf5-dbd2-3d41-9ebd-558677b4297b | -22.21184 | -56.19995 | 2025-05-18 05:14:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1c58d14-677e-3506-bc22-e17d4d147ae4 | -20.95826 | -56.60719 | 2025-05-18 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a2663113-0bf4-3130-9a9c-486781c6fe2a | -19.06569 | -53.4584 | 2025-05-18 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8cf4ad16-f5fd-3285-9f28-1a7695432bad | -17.76399 | -56.30757 | 2025-05-18 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6a9d3c02-a1af-37a4-841e-e5d9383aadd0 | -17.76768 | -56.30813 | 2025-05-18 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4d4e858a-b5c3-3779-b252-d78b3669ad6b | -20.47216 | -54.57581 | 2025-05-18 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9352ee1e-ba0d-3faa-a8b6-aad0fc435a4b | -19.06387 | -53.46047 | 2025-05-18 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f517857c-e863-3018-9722-7d68c9dc2574 | -19.06834 | -53.46109 | 2025-05-18 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca8d4b0c-99e1-3fbd-b03d-f32924fcbe36 | -20.1702 | -54.17949 | 2025-05-18 05:14:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f58a062-ca9c-32a9-a629-0c223ccdfac8 | -17.75601 | -56.311 | 2025-05-18 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f34ee786-ef03-34e7-8b95-03f477e6abb2 | -17.75232 | -56.31044 | 2025-05-18 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e58e810-95e0-39d2-9667-ca9e1a0fd346 | -18.95345 | -54.75092 | 2025-05-18 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb53b31b-6a43-3115-8a47-86219ca979a4 | -20.95513 | -56.60168 | 2025-05-18 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b15a925-e603-3ca8-b633-6bb579ed87bf | -21.18499 | -53.18346 | 2025-05-18 05:14:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1811dc3-ebdc-3c0c-ae2d-87d644001603 | -19.06438 | -53.45593 | 2025-05-18 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5d6405e-2366-3cae-8cbc-c6d20052c08c | -20.95073 | -56.606 | 2025-05-18 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7a104814-4f1e-3746-9815-bf6d34d5b30e | -17.7093 | -54.08887 | 2025-05-18 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b61ec1ab-a892-308a-a307-0a6b1f796bfa | -13.14754 | -56.81334 | 2025-05-18 05:38:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dd290507-afb3-3cca-a8c9-413f85eea875 | -12.36466 | -56.39922 | 2025-05-18 05:38:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 431217e9-95d7-384b-ab00-3fa793add01c | -10.04945 | -64.99684 | 2025-05-18 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1cc9d6b-3614-3e44-b078-dde5e1b57f0e | -11.4264 | -54.30068 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2947746-080f-3233-8e75-f9a06f6fde4c | -12.4506 | -57.19332 | 2025-05-18 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a194880b-250f-3498-bc5e-2572a0ccc632 | -12.36985 | -56.39983 | 2025-05-18 05:38:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2f3c190-e061-39d6-91de-5d179e1cbd16 | -10.37285 | -57.49726 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecb4a462-2357-3ad1-9067-ac46c2e21672 | -11.29075 | -53.97626 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c993d7-5c92-3f1b-ab7a-c247ff4a5858 | -9.24181 | -63.2909 | 2025-05-18 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f31df30-0f1e-3856-9800-4c8fadeb5873 | -10.30541 | -58.44897 | 2025-05-18 05:38:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
