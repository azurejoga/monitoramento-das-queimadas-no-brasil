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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0404e4fc-f75f-343a-92e3-aeb956e649f3 | -3.49557 | -60.45106 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9eddec2-1a3b-39f9-9931-43599c0107ef | -4.37319 | -55.43319 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a6522c3-aaee-3fda-ba5e-a8d4554190a3 | -2.56183 | -47.19621 | 2026-08-31 16:52:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d60e3b81-0460-37ee-ac4a-30666c309eb1 | -5.1635 | -56.90017 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 05ad83ca-5132-3856-8cd3-68d979c9a379 | -1.87918 | -47.48558 | 2026-08-31 16:52:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ac196860-73af-3cf6-8def-1cfac3c25d9f | -2.10512 | -48.9647 | 2026-08-31 16:52:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 233ef90a-c7b4-33b1-b508-1bfc6d9687da | -3.21205 | -61.18354 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5dbe137a-06c8-3f47-be54-28f7e05d1ec2 | -6.30924 | -61.9309 | 2026-08-31 16:52:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| fb9bc38c-654c-33ef-8413-a847c0b46d83 | -4.85224 | -55.83114 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 203a116e-ad0d-3af8-adcd-d8b3b6044729 | -4.47617 | -55.45912 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f08abb6-2f3f-3791-ba82-c48f474b04a0 | -3.32779 | -59.3972 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fed6c399-187c-3422-b8f3-3f919550b96d | -6.27897 | -53.33298 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0cc2d7b8-a6d7-30f1-a433-a7606a7def22 | -4.25053 | -43.94173 | 2026-08-31 16:52:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e730b6a-bd8b-3f1a-8a25-df93f83269af | -6.77881 | -56.29479 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6671eb72-4bde-37aa-a473-4e6d4aed61f6 | -4.42473 | -55.42885 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75072439-e284-3296-af35-5154830bf0b2 | -3.88018 | -59.56511 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c6b6d769-06fb-3064-81f5-9f74a57d027b | -3.61467 | -59.08112 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 194349c5-3394-311e-a792-79e9b23702b4 | -4.15833 | -60.71574 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 15af58e8-e787-3922-ace1-053bf27e14c3 | -1.86668 | -56.28596 | 2026-08-31 16:52:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c718d9d5-87d2-3d71-a136-4eb03e802910 | -3.3972 | -59.37245 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68f9084a-ffbb-3293-938a-51dfe503cbf3 | -6.79517 | -59.39333 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7846fc00-d4cd-32b2-a2a1-060a5c4721c6 | -1.91963 | -48.28605 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2054817e-94d8-33b2-9e73-adfbf0ab0a31 | -3.35148 | -58.89048 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a42f23d-8f74-3e48-af3c-00b6dce053b6 | -4.22458 | -59.87207 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| ac6a01ee-2bdf-374c-ab97-b0d7b56fabdc | -3.51124 | -56.31192 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d639d71e-e4e3-34b0-98a3-5ae1dce6a10a | -3.40821 | -43.37235 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 49d6436b-75da-349b-9c99-f8711b8774f8 | -1.95883 | -44.95043 | 2026-08-31 16:52:00 | NOAA-20 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 65958069-3707-3eb0-b911-fe12b42ced47 | -6.23298 | -55.46868 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c746049-3ea9-39c5-b62d-b389b30721d5 | -3.38884 | -59.39195 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ded1f6e7-46a4-3546-aca7-9f8274d5c8df | -5.99149 | -55.72601 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cac0911b-e9a8-38e4-93f6-3e7e3d25890d | -5.96006 | -57.68237 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 60f49dd5-4d95-3974-8133-e601ac138637 | -5.95237 | -57.70138 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 98b760ed-69dc-3999-b88d-03e64f1d2231 | -4.74053 | -56.2701 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| dfece1be-f54c-3047-a4e1-e8feb9cf1e39 | -2.70548 | -56.54353 | 2026-08-31 16:52:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5a252bf1-0c6d-3082-8911-4183ecfc1d24 | -4.30204 | -49.10041 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9365172e-51e1-3bf1-8e84-3a974e37f81d | -4.30151 | -49.09694 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 50a256f5-a3da-36b2-ad75-50ecf1cb0761 | -4.2352 | -53.5224 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c8109628-43f9-35fc-8db2-52c4527fef47 | -6.34179 | -54.68471 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bdb67d93-08f7-3ca0-bef1-8d28d50a41b1 | -3.83569 | -55.56164 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a79ab365-e5eb-36e9-8db1-a110607d8507 | -6.26711 | -53.35873 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6ca0c040-1259-375d-bfd0-b829f892e536 | -0.85485 | -48.67218 | 2026-08-31 16:52:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1adcfb65-725e-3cab-aa59-473c2708f5b8 | -5.95879 | -57.67348 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09ff4c66-f3eb-3d65-83d6-ea1a7b013b62 | -6.4113 | -54.96012 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 88613ec6-5f5c-3325-ae1b-ee5e46076b28 | -3.57388 | -54.55594 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 763ca19f-1f28-3e39-9ca4-d9ad8b9269c9 | -6.60453 | -58.61193 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f1e1bfa0-8d2b-3f2a-9d39-b1432162bd8b | -5.69584 | -60.23778 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a5f511e0-22d1-3985-acf2-cf98927da218 | -3.8346 | -55.55878 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b4b15e55-5c72-38c6-9cbe-158479e01950 | -5.91539 | -52.38359 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 86b0e496-17dc-341e-8743-39cf15934dbd | -3.17911 | -52.18536 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 717c589b-dcf8-37f1-b3ed-496be78e6e82 | -3.50217 | -59.04188 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1f52b3e9-c422-35eb-95f3-fc7b303131fe | -2.83758 | -58.22419 | 2026-08-31 16:52:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49a4240b-c8d3-3649-9d25-b654e620acf6 | -3.78279 | -44.3967 | 2026-08-31 16:52:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 42afe95b-3c91-3530-a477-3a8b84af0792 | -6.80962 | -59.77016 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 96083d04-e752-3337-9f1c-2fb0445a0d1a | -3.24532 | -60.80885 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7a79318a-7ffb-3715-9be0-76bb00fd06be | -1.84152 | -55.19123 | 2026-08-31 16:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d60d3739-8f31-35be-a5d1-1cfcff853d07 | -3.55973 | -56.84297 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 1f874896-bfd2-3d2f-9f2b-b5f9c50b8d63 | -6.79355 | -59.78571 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 060f8a0a-e45b-3eb9-ab06-9c4029b57a5f | -1.41873 | -48.9533 | 2026-08-31 16:52:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b237ee1-0bb1-3d33-b453-8faf86bb8c69 | -5.9503 | -57.68682 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0e6dcaf8-a2f9-3692-b71c-15423d213bc9 | -5.94009 | -57.68808 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f817a57b-149d-32b6-bc61-465c63285337 | -1.14558 | -46.33993 | 2026-08-31 16:52:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28110ed6-6485-3c22-a0db-d4f4d4df05c8 | -5.84937 | -52.08435 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a5b58558-45a4-36d2-b522-ba31a6b4a0b9 | -2.73996 | -49.29485 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| be8781d9-d0c9-315a-ac9f-28414f5ed641 | 0.25556 | -51.48574 | 2026-08-31 16:52:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2ff76b1-76cd-3350-8633-e61debc35248 | -6.38029 | -55.21891 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 277bcb02-6ec2-3127-b1fa-15b749b84cff | -4.09224 | -54.09969 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9056ed66-930b-3f84-8628-40d9227fa679 | -1.17862 | -50.11641 | 2026-08-31 16:52:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28b3775a-f97d-37ed-b9de-58be03e279f2 | -4.3376 | -48.71373 | 2026-08-31 16:52:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a77a6c1-e438-3d54-9128-d0436a73b376 | -3.48356 | -54.66516 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1ae52090-1e87-3334-b878-2229a161cf9f | -5.91662 | -52.39191 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 8b49820e-8a56-3854-ac08-4a4705ce3cb3 | -6.77693 | -59.43318 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e01ceada-dfce-36f2-a839-0d9fe69bf746 | -6.90764 | -59.48292 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 74003a0d-0bfe-35d9-8442-57d4de1ecc06 | -3.61368 | -59.07418 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 87377f7f-3c29-3f1e-a67c-c549a622473a | -5.72344 | -53.72765 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5b04311b-1c57-3b56-beb7-b08d4386c99c | -3.78219 | -44.39303 | 2026-08-31 16:52:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 693f37b2-25e5-31c9-9662-9586f3942e93 | -3.59833 | -62.11452 | 2026-08-31 16:52:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 971bdd09-c041-3ee5-89fa-eeeed97c3c89 | -5.35939 | -49.13471 | 2026-08-31 16:52:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2772018-e7fd-3af6-9906-51b1ba42cba2 | -7.5211 | -61.37297 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 32f24302-ca05-3d7d-ba42-94bde05d43e1 | -6.16145 | -52.63443 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6e26b93b-7f6d-397d-8b76-2a164e6e88bc | -3.32285 | -49.86603 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6abe663d-4167-36d2-aee5-16251fcdfe1e | -6.91346 | -59.48205 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3d9a1efd-dda4-3731-9110-5781e5c39757 | -3.01103 | -51.05183 | 2026-08-31 16:52:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 57fa9860-5d63-36d4-83fa-ad0fde814274 | -3.47616 | -44.53627 | 2026-08-31 16:52:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b66c32d3-226b-3c91-8331-e149b35cb21d | -5.88536 | -52.0581 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 9fec61b1-4d6c-3d95-9c8d-b9076a17debc | -4.86103 | -55.82968 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a3dac734-36f7-3491-a2c0-0818d934a11b | -2.61867 | -43.9248 | 2026-08-31 16:52:00 | NOAA-20 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e51b3699-c974-33b7-9438-4d78c8e73b75 | -5.49035 | -57.14167 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| af5df65a-69ac-3ae7-82a6-bcb0c37df6f6 | -2.03703 | -48.20745 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e4f4dd29-8081-30dc-a255-bcf86e81af7f | -3.86608 | -49.11289 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a72b42f-28f6-3115-b8f1-8268e85e1006 | -6.65263 | -59.43359 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 250c6d3d-b9e7-3231-8b84-0aab9bff5135 | -4.58458 | -42.82783 | 2026-08-31 16:52:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e38b2993-7822-32f0-8c80-faa9b3b02f0e | -6.18431 | -55.44512 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db954412-fec1-3577-aa17-dbb96e7ac10b | -6.37969 | -55.21483 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5685de7c-f36a-3b8b-a9e7-fb7ee7c49974 | -6.11755 | -57.68424 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| d391cf0e-567c-3c88-94a3-f3eac2eb86e7 | -1.16848 | -46.31302 | 2026-08-31 16:52:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3597da85-53ad-3b77-993e-d548dd58a2d2 | -1.77694 | -47.76474 | 2026-08-31 16:52:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3925153a-5139-3cf6-89a2-b29c150d1d31 | -2.72706 | -49.14381 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 646cd9cd-e3cc-3298-8f20-70a7ea5600ae | -6.84068 | -59.7317 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a3ac391e-f329-3a7c-a407-772d9b2c1089 | -0.80555 | -49.20512 | 2026-08-31 16:52:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 585703b7-4d12-374a-b98e-f86a809cc1c8 | -5.07397 | -62.44468 | 2026-08-31 16:52:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |


[Clique aqui para ver as próximas entradas](README174.md)
