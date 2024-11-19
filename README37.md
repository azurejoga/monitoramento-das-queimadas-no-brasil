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
| 261a4ae8-c7bd-39e4-8cb2-d0d1d3d37bc0 | -23.9567 | -54.12097 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f1fee33f-c586-322f-bb39-8c4f37ca8d5b | -23.76162 | -49.00623 | 2024-11-19 04:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4467f5a6-c4b4-307e-9bf6-e618d78dd4f0 | -23.91809 | -54.10227 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c34dba95-0971-32e5-85a9-cc977abfa57e | -23.95278 | -54.12426 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 87bde135-09d7-3d46-a7d6-e653cb5602dc | -23.95449 | -54.11263 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cfbf2b21-7d8c-3e9f-8c5d-4515111052ff | -23.97343 | -54.14775 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c7dcbac2-aced-3b4c-8666-97a018b795db | -23.91703 | -54.09836 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b6c82f4d-27db-3a19-83ef-8e5b7ccdb735 | -23.96342 | -54.12215 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 2c1063cb-27e2-3011-aa5c-68f124a27eab | -23.96006 | -54.12156 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 323f98d1-1b72-32a2-ac03-ceaab70e9db0 | -23.77542 | -54.49554 | 2024-11-19 04:53:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8d02401b-8d98-3da6-9768-6fc42c2b342e | -23.77876 | -54.49613 | 2024-11-19 04:53:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ebd3bf9c-07e1-31d7-b346-8fbf7d25d318 | -23.97679 | -54.14833 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| d7cd132d-adc4-30ba-9797-9ea52c127b63 | -23.97457 | -54.14 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 691d6ebe-6c94-3579-89f1-368ac00dbab5 | -23.96564 | -54.13048 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f5c4b463-c16e-302d-9bec-34d09de31239 | -23.91645 | -54.10224 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1c7a9d39-8353-326e-8558-00e8dd292fb1 | -23.974 | -54.14387 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 386a332e-fd64-38c5-9748-e6cd09db63a6 | -23.96064 | -54.11768 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 33202e94-0232-3ecc-95a2-d7fea658082d | -23.96399 | -54.11827 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2083c9f2-5a3e-36d9-8937-a38e30663a62 | -23.91367 | -54.09777 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dba465a1-6608-3ba6-b7fe-51feb5acbdda | -22.3053 | -49.75784 | 2024-11-19 04:53:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9cd688b6-98a4-386e-80f8-6d9868251937 | -23.91752 | -54.10615 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ae51993-286d-3d6f-90f4-23883c7e46b6 | -23.91588 | -54.10611 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5e106d2e-371b-35ef-9b0d-f7e401fe6455 | -23.95392 | -54.1165 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ebf27b25-3871-3dd3-a6f9-4cdf767e63ab | -24.01271 | -54.22107 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3a04442b-fd05-36ad-a3a8-a99fcff34ff5 | -23.92481 | -54.10345 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2761c15a-54e0-3667-9144-41d3374f3bb5 | -22.30439 | -49.76521 | 2024-11-19 04:53:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f588b4d0-b352-3f5c-929f-5af2b1000335 | -23.97236 | -54.13166 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2fe03934-1d20-3a5d-9797-a9b36e800651 | -23.94497 | -54.10698 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a95158c3-cc95-3632-b899-70872e1d94ee | -23.92032 | -54.11062 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8835a11-c4f9-33b0-bbd0-06f6a0b338f1 | -23.94834 | -54.10757 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 09fd4825-c0ed-3789-94a1-886ff4e25631 | -23.92089 | -54.10674 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19b08c7d-a180-3c4b-87ea-61e246157c7f | -23.96957 | -54.1272 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fc312bf9-97ad-33ba-9346-7ad0fa7a6cb1 | -23.95727 | -54.11709 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 9bc44a54-447b-3735-9776-da5987566ff5 | -23.96121 | -54.1138 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e3526e46-383e-3076-9ab5-ad3b1f6a0920 | -23.96843 | -54.13495 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 35830eb5-f155-3456-931e-f57c82ad0bfa | -21.36229 | -55.89746 | 2024-11-19 04:53:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57c14673-a03a-3b48-a62a-a6dfcad119f5 | -22.53976 | -48.81332 | 2024-11-19 04:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ff8861-4e96-3fda-8c70-d6ceb9bee4a0 | -23.75734 | -49.00573 | 2024-11-19 04:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27a52e49-7383-33b0-8047-0e5ea6351d82 | -23.91252 | -54.10553 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5d10c81f-edba-3ba6-919f-7b827efa0d7c | -23.77266 | -54.49113 | 2024-11-19 04:53:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 359640c7-bafd-3110-a22b-bfafddd737db | -23.9517 | -54.10815 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 168cd5f3-66e8-3165-b8e0-9929d3b0c87a | -22.30885 | -49.76212 | 2024-11-19 04:53:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3174ffe7-1b8f-3b83-9355-a027cf6f5aca | -21.35894 | -55.89687 | 2024-11-19 04:53:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9228c2e1-ab46-3ea2-bd97-7a7756d2d0d3 | -4.5614 | -48.0141 | 2024-11-19 05:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 173b35f6-abde-3bc3-a6a2-edf99b5dd306 | -5.9788 | -45.3621 | 2024-11-19 05:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| befc5920-2339-3469-adb2-d61e905611c0 | -4.58 | -48.0132 | 2024-11-19 05:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1de31656-1005-3db0-8870-d35d2a9db870 | -4.5429 | -48.0151 | 2024-11-19 05:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| f4ddd51e-b9a0-3735-820c-acbf3aefc705 | 2.58618 | -50.85154 | 2024-11-19 05:05:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0af7c301-6ec5-3983-bcc9-27164ffba10f | -3.11231 | -53.70307 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba3f4540-1107-3325-a934-1d8f65e0f4df | -4.5471 | -48.01693 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0425ee17-ac76-3958-bfae-10f691238735 | -4.38997 | -47.77082 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44734d3a-c712-31bb-91ec-3e1ce7c14fd0 | -2.0206 | -52.07834 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bc5adb7-ad69-3eda-a406-100bb7c2595b | -0.60046 | -58.05159 | 2024-11-19 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c28ca225-fae1-36d3-8e7c-c3123a7aede8 | -1.47381 | -51.9726 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5901c1c4-be49-3a62-8371-b00524509e49 | -5.97163 | -45.36666 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 43957dc3-a5cb-3344-8e51-fc73af4c290b | -3.77312 | -52.41241 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1901e32-4f2e-3b75-932c-c91ec5c9caf1 | -4.49003 | -46.71566 | 2024-11-19 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ea777c2-2522-32a8-8936-d54508579b60 | -2.85392 | -53.97569 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9992317-8d23-3e7f-9efa-c00d7a2fc52c | -3.10003 | -53.10213 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 842cb6b5-3357-3bd5-8270-85eebd4c1e6d | -2.43667 | -54.61616 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45eba296-3147-3a9e-8e66-5e32468f03e5 | -2.54713 | -47.10354 | 2024-11-19 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 776eeaab-914a-3a86-8701-2b4d4e324e59 | -3.51566 | -53.79757 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 40985ac8-a10a-34b1-a844-60f7d90de1ff | -1.16538 | -53.38245 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76d6dfc6-e8cc-394c-877e-7a69bc116717 | -3.31719 | -54.07952 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb347028-bed0-3a23-8d2d-cc6c7bec2260 | -1.59029 | -53.80188 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b0b0e460-2291-32c8-a345-38731d1db6cf | -1.95057 | -53.33478 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8743ecb-2e4c-3624-af00-12d2eb697935 | -1.41078 | -54.92736 | 2024-11-19 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| feb0861b-3173-3d56-893c-8b40efa5fa14 | -1.37604 | -52.07906 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b24a2d7c-45f5-39d5-bd05-d6171682df93 | -4.06315 | -50.00875 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2decb08a-5839-3018-a0a9-aced0707053a | -4.38858 | -47.78062 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af0cb6b4-54c5-3655-90ec-7390e96e83c6 | -1.39114 | -52.42589 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14d649e9-c966-32dc-88b7-f421dfb86b90 | -4.39145 | -47.77129 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bafa5c4-a9fd-3203-b457-d424fb9c6861 | -1.2222 | -51.74514 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 111f50b9-caff-31bc-9952-6fc4a14c7eb2 | -1.54612 | -51.11533 | 2024-11-19 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 471f7a27-28af-328b-9fe8-d229c25709f5 | -3.05455 | -51.33577 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23fe42e3-be52-30b3-95bc-089466834d79 | -3.48265 | -48.24812 | 2024-11-19 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3afa78d4-4c6f-3808-8057-f1c5a46f658c | -1.21049 | -51.76088 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5dea382-eefc-33cd-a012-8fafeb7687ff | -2.53719 | -47.3349 | 2024-11-19 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4abf1cea-bbdf-3e31-8050-19898ed4cc44 | -3.1091 | -53.74753 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0e78572-b6f9-3f1f-abca-5e15b1d93245 | -1.37503 | -52.08114 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc44112d-1ac8-3b86-821c-6b65f68c342f | -1.20586 | -51.76508 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1730d202-b372-3704-9deb-9f76a8f79caf | -1.38855 | -52.0003 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dba22a48-30c4-3cb8-8546-8dd61a536d62 | -3.75061 | -54.72032 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abad0014-2d55-32ea-b8b2-176b002b7aaa | -4.57991 | -48.01194 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5dc78aa-d802-3a96-b895-53d8cb759e49 | -2.7153 | -54.59911 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5cf5c9b-e0db-330d-b1fe-57e2d9edc581 | -2.33161 | -53.57404 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9af7c16d-c393-3111-85de-6df5a7ae6f60 | -2.69117 | -51.88336 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 314ddd0f-0599-3a83-9596-bd61e995b71e | -3.1037 | -53.10269 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e37b03b9-4a69-3826-a6e1-c4b2f58867b9 | -2.38313 | -53.66328 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b8ffc97-d4df-38cf-9557-e28059e888b5 | -5.97235 | -45.36151 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8dbc3289-c6b2-3046-88d3-c2ce010caa29 | -1.20744 | -51.78003 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e1727c7-c9ed-3d0e-ad9a-3d3bd066a597 | -2.81468 | -54.0211 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 501f10df-1450-3dbb-980f-2ec4c3dc37b4 | -3.57359 | -50.1575 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f7f3bf8-30e5-33ec-b226-76f9bb15e2f5 | -3.66097 | -50.44048 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c244df53-bb6c-373d-abba-8c17eed3fe94 | -2.76908 | -54.05431 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd0b7f0a-bff0-3be7-a695-ec47383d7b6d | -1.53639 | -60.33499 | 2024-11-19 05:08:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc6fedb6-acab-39ff-96ab-d0eb04942db3 | -4.38516 | -47.77708 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9977a6c-dbe9-3132-918c-d0a97f227a6c | -3.66471 | -50.44528 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a2c0019-7570-331f-a388-a7e291e3a72c | -2.69195 | -51.87841 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6542e0b5-5de6-39bd-831c-596e1fbeb82f | -1.72807 | -52.69789 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
