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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 715ad0de-20a3-3090-8404-e74bb47a5d27 | -4.49824 | -46.37217 | 2025-08-27 04:02:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d443429f-a323-3061-b075-42e6649984e2 | -3.42242 | -49.03928 | 2025-08-27 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 52dced79-3cac-3d4f-aa45-3b73e19bdf34 | -4.49669 | -46.38169 | 2025-08-27 04:02:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7e6c8dfa-821f-3027-81bb-2740d663b829 | -5.50888 | -36.67779 | 2025-08-27 04:02:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c52315e-588d-3098-b162-c5e66c76154f | -2.93403 | -41.15826 | 2025-08-27 04:02:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3afa426d-6df5-3373-86d6-75e57e92e612 | -5.79292 | -46.1353 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fce4c3b1-5b94-3cdd-abf3-a480d74f3416 | -5.63296 | -45.72145 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cafcbd6a-d26e-382f-8f35-8e5ce98ca70c | -5.62223 | -45.73225 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23a21de0-54aa-3e86-97ff-b47064836032 | -6.69641 | -42.97026 | 2025-08-27 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05aa2653-be47-3cdf-8b72-e61073120eeb | -4.48444 | -47.66758 | 2025-08-27 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 739a2e34-7064-3d65-8f96-1195f2a2bf2d | -4.85132 | -42.8904 | 2025-08-27 04:02:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff62c990-540f-3d90-94c1-818a86e558d8 | -4.31212 | -48.1021 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0e50ba2d-1af7-3aa9-a7da-ae75ff5e7613 | -5.12145 | -43.20732 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5dde4ddf-791a-35e7-b2f3-2e16f9373a5c | -5.11327 | -43.21061 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 163e4576-9b81-3a77-828a-125ec0898a84 | -6.32268 | -42.87983 | 2025-08-27 04:02:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e36cd0b-be85-3d2c-ba21-c756758c4200 | -4.4809 | -47.66578 | 2025-08-27 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b418b1f-0219-3054-a169-5c1d5509a2c8 | -4.84987 | -42.89288 | 2025-08-27 04:02:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39c7dc6a-9777-34e0-9894-0d7a87dbf68b | -5.78698 | -46.1434 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4a5fd71-0077-3044-8846-af25d8116851 | -5.48334 | -41.41878 | 2025-08-27 04:02:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2f53cca-b2f3-370a-a165-f7b66022d030 | -4.31264 | -48.09894 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 74c9b3c2-59e5-3a00-83c1-f015c2ae7a8b | -4.79316 | -47.27396 | 2025-08-27 04:02:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 518d989f-31a0-3ae8-9162-308c98b253ef | -5.68961 | -40.98032 | 2025-08-27 04:02:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3cd6b6a9-e145-3a7c-8e76-b7673e950e78 | -6.12991 | -45.07897 | 2025-08-27 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0b17e89-6bac-3d42-ad4e-6392a8c8e407 | -5.50809 | -36.67432 | 2025-08-27 04:02:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5174b05-a19c-3e36-9e58-7f132ca9ac4c | -3.32636 | -43.03609 | 2025-08-27 04:02:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1d10f75-1550-37de-9016-d283dc24f325 | -6.12483 | -42.9491 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a5b62f0-02cd-3ac2-aae5-81fed3145338 | -3.98001 | -43.24577 | 2025-08-27 04:02:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b9bcd24-1f38-3fd6-8ce1-b0603a62536c | -5.11515 | -43.20408 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 35effbe7-e376-316f-ab35-b77ee7026280 | -5.11441 | -43.20852 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8ac67390-05fd-3ef0-9d73-a869e58ccf2f | -6.05063 | -44.88551 | 2025-08-27 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9ecd029-9dd5-3a1b-ae29-ee6473adb035 | -4.31159 | -48.10527 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e6f4e2f0-299a-317f-8fd2-4f67ae2e2bbf | -5.11888 | -43.20466 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 23d1f576-c23c-3700-b009-509c39c336cc | -6.83727 | -39.40923 | 2025-08-27 04:02:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3428b2a6-2a2c-33e4-93af-36b98bd132c9 | -6.20082 | -44.16184 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad63457e-a381-3010-b984-d6df18ce7b77 | -5.7472 | -40.44511 | 2025-08-27 04:02:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f84de7a1-6410-327d-a77c-cf4e5513a27a | -6.20002 | -44.16666 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb19da3f-5e07-39aa-a2ab-bf6f262fed50 | -5.06936 | -37.71638 | 2025-08-27 04:02:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 586fbecd-64e8-3f8c-bfdd-14a0dd8142b5 | -5.13086 | -43.22478 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5f13898c-0931-3c0f-9c99-8ff8ef1f3dc1 | -6.32562 | -42.88452 | 2025-08-27 04:02:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ea330e8-f05c-3df5-ab27-eabff6d34232 | -6.75477 | -35.1391 | 2025-08-27 04:02:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4d9798ba-8ffc-3955-afa4-f49b4d430061 | -5.4767 | -42.59912 | 2025-08-27 04:02:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| a45fa9ec-4ac9-38c4-9465-d61f3b1fa400 | -4.31139 | -48.105 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| df3b11e4-e1c9-3f32-be88-2ffe730bfb07 | -6.20473 | -44.16232 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e27a01-15cc-34ba-999d-918d9894ecc4 | -5.66281 | -47.48841 | 2025-08-27 04:02:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46619e0b-1a8b-315d-94ad-a414b5b3b654 | -5.53438 | -36.84704 | 2025-08-27 04:02:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6edeb1b9-2177-3c02-9d3a-faa5f63d9dbc | -5.40115 | -45.11918 | 2025-08-27 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e580c639-eb65-3f41-933c-ae1101b6d55d | -4.31769 | -48.09962 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f52cd7bc-2a8e-35c3-a20c-728ae25e1e90 | -4.91662 | -42.09366 | 2025-08-27 04:02:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88a8700b-3eaf-3f70-b2e6-e818c643a93b | -6.59321 | -43.14413 | 2025-08-27 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56fe2bea-68f7-30b0-b6d1-dbfd7306a086 | -4.87873 | -37.48214 | 2025-08-27 04:02:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 88a503fd-08ef-315f-b368-fb4b7777d884 | -6.50318 | -42.94132 | 2025-08-27 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 277b857d-1cf5-3118-94ce-bac40e67acc8 | -4.88217 | -37.48267 | 2025-08-27 04:02:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6730381c-345b-3b2f-b745-da40508235f1 | -5.48052 | -41.41446 | 2025-08-27 04:02:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f41571ee-5928-3dee-960d-2c3278606ab2 | -4.31193 | -48.10184 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7a631d9d-50d5-357d-8423-de2d048c543c | -6.13141 | -42.95453 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 20e1ef20-1148-3317-9515-b3f6ac9c9d2c | -5.69018 | -40.97673 | 2025-08-27 04:02:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f53a9b1e-032f-37a2-8492-84306f0dfcb5 | -5.85917 | -42.90774 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e95c6f46-bb5a-3eb3-a568-43ce51a0cefb | -4.48042 | -47.66867 | 2025-08-27 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940d986f-2de5-3f23-9107-a0c68785afa3 | -5.11367 | -43.21295 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 223dee72-4034-3a70-8406-950cdd3927b1 | -6.20163 | -44.15699 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9196d5d8-6137-3002-bd56-a09228bad1d2 | -3.42115 | -49.04668 | 2025-08-27 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b0b03132-0ffb-30b7-bdf9-18e550dfeb2b | -4.48394 | -47.67047 | 2025-08-27 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 637a45c4-700a-337e-807d-ee3a600e88b7 | -5.8718 | -42.41528 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7153636a-777e-3180-abc3-d96618b1a236 | -4.79225 | -47.27925 | 2025-08-27 04:02:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615ff1e8-6902-33a2-9eaf-17563c7318ff | -5.76069 | -43.38943 | 2025-08-27 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8c224a6-3038-30fa-8c57-4fc053851d97 | -6.28798 | -43.77769 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 101944b6-7261-325f-9caf-6598a2237169 | -5.75995 | -43.3939 | 2025-08-27 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8613c450-012d-3876-998d-7382299a9972 | -6.51874 | -42.98232 | 2025-08-27 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d7f2fe3-1fa3-3bb5-b798-a779af59688e | -3.36225 | -43.37203 | 2025-08-27 04:02:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1228cf4a-4225-3f2d-a5e6-60cf809bad87 | -4.49565 | -46.38015 | 2025-08-27 04:02:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b59ab3dc-64d0-3c12-9ae9-4f0d9e1f39b2 | -4.8216 | -46.00453 | 2025-08-27 04:02:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 643ef5f1-8a8d-354e-bcc5-26047385d09c | 0.77866 | -51.33136 | 2025-08-27 04:02:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 776aa12e-b540-3e03-9681-f1d9e8eb6927 | -6.75875 | -35.13968 | 2025-08-27 04:02:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5cfc0212-bd16-363c-ae31-afff6f59d7c8 | -6.23792 | -44.7348 | 2025-08-27 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7c00ca-c0dc-383c-8736-62e79b87b424 | -4.87815 | -37.48587 | 2025-08-27 04:02:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c7a96f72-02fe-346d-bbc4-6db52a3f8201 | -6.8406 | -39.40975 | 2025-08-27 04:02:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 983339f5-dd05-3e20-ac3a-975765f05d33 | -9.09438 | -49.5699 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 99e39d4d-dc30-3f67-9844-939cf73911cf | -7.74572 | -47.45258 | 2025-08-27 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a188480-1607-302c-8c18-78e817c2e6fb | -11.15631 | -44.80729 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98bcf995-11ad-3cf1-adb5-900cd1c27798 | -11.24543 | -44.98774 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba9e0632-4f3b-3a23-a817-fad1ccd8e4e1 | -11.25082 | -44.97912 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fd5132-d968-3ac8-b239-2bb745472719 | -13.18494 | -44.04226 | 2025-08-27 04:04:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82408798-34fd-30c2-b55d-5c15a4bd2a13 | -8.2612 | -45.11661 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8acb7ed3-0dab-3cd3-aa23-8a54497a135a | -13.50246 | -46.86288 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0965f883-7f69-377c-8bd7-3543f82ed8ef | -12.8971 | -44.64008 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 89923696-7d8b-3e3d-bfc8-a9c8888dfcd9 | -12.74743 | -48.19552 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 218ddd66-5790-3ab3-8fa4-029d0a7e83cf | -7.38162 | -47.04665 | 2025-08-27 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d73ff72a-9a95-32f4-857f-ed05ea300a67 | -13.05688 | -46.30356 | 2025-08-27 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5ae9bb3-d09b-3b78-901e-7083dc5ddff6 | -11.61455 | -46.407 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 681ec184-03f5-3b5a-80b5-cc325d5f4edc | -6.8843 | -44.4334 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31d2d6ed-c8fa-3f35-b454-15f64886be7b | -7.40264 | -44.06732 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2befddda-8200-3807-b10b-1abd7facbf56 | -11.2484 | -44.99315 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 867b92dc-5b5b-37e0-912f-b1ad98d03d8d | -13.17024 | -45.29443 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 423592d1-7258-39dc-995d-0ad0f176b6f5 | -12.78316 | -48.15417 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 177b9eeb-6898-3742-97d7-031ec2582b93 | -9.08572 | -49.60647 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1ad48ae-1d1f-302e-9ab1-422bc79ffa63 | -7.64953 | -42.66549 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dfcc1efa-6b2b-3ac9-b420-8b326c5d210f | -11.91522 | -46.7452 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8abc00b-21c3-3cfd-81a8-94dccbf386c8 | -8.07236 | -44.98649 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31255c20-8424-34e6-b22a-faca70c5773b | -7.73741 | -51.14289 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db73c9b2-6cd4-3319-8897-41ccd72c01eb | -13.22267 | -44.54969 | 2025-08-27 04:04:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README25.md)
