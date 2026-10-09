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
| 9b4e5dda-e06e-3e82-9ca2-114712024f6b | -11.06802 | -44.08384 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3077a44-f033-3fb0-8701-07184ea8b419 | -13.63455 | -44.42528 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb8b8859-a0b8-3875-96cf-761674d014e0 | -9.07862 | -45.11393 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cdca01b-521d-3c2f-a11d-bc84dcb9cca8 | -8.74298 | -45.14825 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c15d188a-5b91-3341-925a-3bb9169607d7 | -8.91203 | -45.23125 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cfc2368d-4279-3db7-b29e-4e9a42b26bae | -9.90049 | -44.7928 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a37c20da-487f-3e00-9431-e92e3f49d5b3 | -11.61213 | -43.61292 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f86d53b-a40a-3adf-98be-1a508f540fb5 | -13.25103 | -42.2579 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 9418fe89-a8dc-3f47-a3bc-6bb4d8a575bd | -9.29766 | -47.46778 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93c06574-fa99-33e3-af90-8d001a32da19 | -6.87526 | -45.90452 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b5b30934-6386-3eaf-a8c8-56c5237cb730 | -8.9838 | -45.91238 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27dcbf7a-45c2-39c4-b16a-c5ea4501a6df | -13.36664 | -43.88978 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f200263a-9997-32b9-a1d3-aaf7b68cf0a7 | -9.02878 | -44.38725 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b2e03dc-b6c3-36c4-8258-72fb96f9037a | -11.24985 | -46.30336 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a0059ad-959c-39c5-a97e-4554a1920771 | -8.97065 | -45.91437 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8740223b-6b5b-38e6-bb6d-fa5d288d7d5e | -11.65222 | -43.67979 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 911f5796-1bab-33c2-aa07-feb5ae36ad80 | -13.25198 | -42.25267 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 72f2c956-fe65-3976-ba3d-34be454f061b | -7.25162 | -48.0664 | 2026-10-09 03:45:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c228e954-83f8-3567-a248-10b686c2eb68 | -11.18104 | -45.3079 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98cd51eb-61e3-34d8-956d-db1c031962fc | -11.18019 | -45.31227 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc89ca33-86eb-3f5d-9f3b-45045e931c1a | -8.96883 | -45.15748 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2c5208f4-fe0c-3db4-9910-4861a17a5fea | -8.4119 | -46.94671 | 2026-10-09 03:45:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1f6fa33-ca53-310f-9bc0-512365de3498 | -11.25527 | -46.27587 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3e2e65f-7942-3998-a777-b9a24398ae1f | -11.07212 | -44.08397 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c0bdf3-59b4-35c4-89c5-1d3acf5f4648 | -10.59333 | -46.41531 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb605ad4-0ffc-3a81-800a-dad0ad63ae22 | -11.0881 | -44.00109 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bffd35e4-773f-36e2-b1cb-50430d943ad5 | -11.22012 | -45.32038 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fc4b7bf-c9d8-3fe0-a04d-3d9bbb94e6cc | -11.86405 | -43.56615 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 630d5200-5439-3aae-8c32-b37ed975408c | -7.47414 | -42.84288 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| be58c8dd-1273-363e-8ab3-980ebb61c82e | -11.60698 | -43.69524 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bb75908-d0b6-3e76-8848-e4909e909295 | -13.49693 | -44.37612 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 06684780-93e0-3277-9236-53a6081ed839 | -12.0361 | -43.44781 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 722dfcec-34c4-37e7-af8c-7e03db6343b5 | -11.77329 | -45.56192 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b02c17c2-0369-39ff-8f2e-b1b894f0e4e7 | -9.01837 | -44.38097 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba37ddb1-ddad-3eb9-ad56-bfddca35ef99 | -8.90401 | -45.22155 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9736c33c-b9ad-3cf5-806a-c8188780b6e7 | -7.46953 | -42.8387 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa56885e-ed8d-373e-8fe9-0e6810f61be4 | -11.76199 | -44.95691 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0d4957b-4804-38b3-ad11-b7a14667d9bb | -6.95858 | -45.28767 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2d2f695a-5d0c-377c-9459-d8799ec072b5 | -12.02582 | -43.47523 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38c487e4-9667-3540-b762-237712b602a8 | -13.80998 | -44.19125 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6a64b8a-e72e-35a4-92b9-468112ec3d7a | -13.62933 | -44.42453 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b99ede8-cab0-3dfc-b669-b37a420fcaed | -11.99564 | -43.47053 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9145c93-5b99-3f86-8ce2-dfc60dcf47d7 | -7.33984 | -45.30813 | 2026-10-09 03:45:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 435fedf2-45e0-362c-bb60-964f0999e319 | -11.82677 | -43.59705 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ded9517-9736-35dd-bbd9-6313eead0367 | -13.35075 | -43.97028 | 2026-10-09 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eed571e-f224-3797-9df6-099d6fb9517d | -11.01191 | -45.43547 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b7daa810-2743-39a5-9f7f-710adea14171 | -7.47821 | -42.85016 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 112d7e2d-2935-3c2c-b50e-2662caf86a92 | -11.65163 | -43.68293 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fd90676-eca2-374e-8365-0c6ea8f726ef | -11.00779 | -45.42574 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 94d9d36f-1da7-32d3-bbd2-f74033403155 | -8.90779 | -45.22147 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c23b055-bec6-3be1-8cee-5811ad92cc2c | -10.90484 | -45.52667 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e16aa1d4-0ae2-3522-ac03-1aee46ff2515 | -9.88758 | -44.79907 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16d7bbd0-1d1b-3bc9-88c3-77beb9fbb88b | -10.86957 | -44.8069 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da317fde-844a-3651-963b-0e4f740a4e9a | -11.67554 | -46.77554 | 2026-10-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1aaf0b42-987b-3573-9ce0-c5457f62e285 | -11.85489 | -43.53191 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efdf4d1e-2195-3131-8951-3fd7c15f3373 | -10.59376 | -46.41979 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 748d475c-38bc-3fc7-bbd8-d6efe7669f6a | -8.74216 | -45.15261 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bdc3524-98e7-3eb8-bf8c-444ad1a21427 | -9.34676 | -46.58527 | 2026-10-09 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d45172cd-fd55-33af-9e39-a1b6969edb22 | -11.1964 | -45.32037 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 905b0252-ca60-3a53-bbb7-949945523555 | -11.00402 | -45.41588 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 29727582-5935-3064-89e5-e657e54d4374 | -13.49758 | -44.37274 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8720a05-25c9-3a62-9711-ba38ed4a674b | -12.58194 | -42.22577 | 2026-10-09 03:45:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5c08981b-5081-3dc5-8f6d-6f61fb00c1ba | -8.73289 | -45.13708 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bb6ffbb7-337f-3f57-ac18-6bae07934d39 | -11.26321 | -46.26748 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0aabe4b7-e0c3-3bef-b6ae-da34a26f74b2 | -6.88246 | -45.90126 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 04623d7d-cf83-3fa6-b6d2-6230324c1bfc | -12.20937 | -44.6195 | 2026-10-09 03:45:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 050d073c-e9a4-378a-8b91-12a77bb8fefb | -11.7856 | -45.59016 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74a95c18-49af-3e3d-9bfc-b9dc9d23e6d1 | -10.87511 | -44.80805 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 757a13ca-73f8-3be9-9ce3-3ac3e6cb6ed4 | -11.60849 | -43.71515 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4294c0bd-fc34-3d5e-b8e5-fed2374472ee | -11.61714 | -43.69748 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0c86ac8-410e-3e04-9ff8-eb72972caabe | -8.90911 | -45.22702 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7abe9cdc-ebbb-3bb4-b046-96d8b4fb1031 | -9.86763 | -44.87269 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d24598aa-2a7d-3818-85c8-e871309c1c0d | -6.96091 | -45.27476 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a36becd2-a31a-3201-9b75-54cb88f42544 | -10.59473 | -46.4148 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18fc7143-fc69-3333-931a-f0e9c1b384be | -8.90272 | -45.216 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a70da067-a028-3a47-827e-92a3c1063b50 | -11.86159 | -43.60686 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e7e1b47-cfbe-3ff4-9662-4951e628d0ee | -7.48097 | -42.83459 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3cd040e1-65ff-3c77-80d5-4c7754359f2d | -7.48041 | -42.83771 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee981255-7049-3952-93fd-0bea243eab65 | -6.96024 | -45.27754 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 72392583-9ed8-3e24-84d3-0b32da7a78d6 | -11.75024 | -44.92941 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c462b0ea-74ed-3002-81a4-4792a2c258ee | -8.74379 | -45.14395 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 560659ec-3726-303e-aad9-d7f5139b9925 | -12.0264 | -43.47209 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ab4fad-ab4c-351d-b578-63fe9609fcdb | -7.41509 | -44.76596 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 88dcbf89-9e4f-3773-babf-d4acc2d9abde | -11.72118 | -43.63654 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d3fa04bc-e1a7-3085-b065-1e2e177de128 | -8.90695 | -45.22583 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b281b454-c421-31a9-93fb-abf54f9f9a53 | -9.2966 | -47.42427 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc18077d-8006-3e52-b347-eb7d79a07acc | -11.01302 | -45.43086 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 14be7945-1391-3cfa-937b-4ef27ebeba26 | -12.00562 | -43.47249 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c245d59-d3a6-31ca-a24d-f2352358f084 | -9.29371 | -47.47438 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fdbf019-15c1-327d-a9fe-569b516f6b46 | -12.02555 | -43.44901 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ffe4f6d-458c-34d8-863c-1ddffd0e1320 | -14.25733 | -43.66758 | 2026-10-09 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 144265f0-ab7d-3fde-9fb6-36f061348b02 | -11.21701 | -45.24496 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd3eab7f-f371-3400-9de7-c0503ce166cc | -11.25438 | -46.28035 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e836bbce-8dd0-32c7-b3c2-014386d24763 | -11.29808 | -44.82685 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47981b34-f1e0-3d77-9ec6-47f2e6bb3e5c | -12.01738 | -43.49268 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffd5b10d-5daf-3761-a07b-7ce2420414ab | -7.50919 | -47.33867 | 2026-10-09 03:45:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eb2111a4-9a2e-3a0c-b19f-95af7a346331 | -9.29303 | -47.4424 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f7b85349-3754-386b-8f2d-8d5dc293b7e3 | -8.98474 | -45.90732 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd7615a3-e287-3acb-8de6-1a6ae5036941 | -11.74647 | -43.64194 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44393236-7a44-3650-ad4a-db33d0e623db | -12.81487 | -44.64853 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README69.md)
