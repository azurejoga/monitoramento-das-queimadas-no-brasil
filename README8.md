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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95413761-7e8b-3a9c-8d81-d891947c5dae | -5.7939 | -45.1267 | 2026-05-22 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 4a23f32e-2c4a-3bba-8d23-440bc388257a | -6.17 | -44.917 | 2026-05-22 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| bffa0b23-1721-30ec-88e9-7423734781f7 | -5.7939 | -45.1267 | 2026-05-22 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| fb2b5d43-ae8f-34aa-ada0-fb0e0a4b60c8 | -10.6642 | -49.7054 | 2026-05-22 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d87269fc-9fca-3162-89bf-9a24646f5369 | -5.7752 | -45.128 | 2026-05-22 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 4ed1b7b0-d47e-3bcf-8866-0ed5b8fec111 | -8.9266 | -46.9157 | 2026-05-22 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| dc6f4081-23e5-344f-9caf-9ed23db6b2e7 | -5.7752 | -45.128 | 2026-05-22 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| ebe4aaa0-e9f8-3398-9911-4658ded782f5 | -10.6639 | -49.727 | 2026-05-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1df9557c-6c7d-3b95-86d2-4ae8e4faf45f | -10.6642 | -49.7054 | 2026-05-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 89eb8f34-f784-3a0c-bd88-11e54397eece | -5.7939 | -45.1267 | 2026-05-22 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a083f7bb-19e0-39f2-bffc-4b228c7ba017 | -5.775 | -45.1507 | 2026-05-22 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 410d9c90-8d67-3f08-b155-e6df9701cefe | -5.7939 | -45.1267 | 2026-05-22 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| f089f984-16af-349c-a3f0-1ae7af061468 | -10.6639 | -49.727 | 2026-05-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| ddddcf79-9097-3317-9a9a-e03a486e2778 | -11.4534 | -52.9212 | 2026-05-22 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b03b0e48-b75b-3dea-88e6-669c329a6ad4 | -8.9266 | -46.9157 | 2026-05-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 894a2848-3f1e-376b-951a-37d2b6b8842d | -10.6642 | -49.7054 | 2026-05-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| da71469b-5242-308b-b67c-3f2af17a61e8 | -8.9266 | -46.9157 | 2026-05-22 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 84372097-889d-3ecf-8bf8-09cb27890885 | -10.6642 | -49.7054 | 2026-05-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 2d274b00-c68e-3012-8f55-fab5da7bba1e | -10.6639 | -49.727 | 2026-05-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ae6bed2b-7ad9-3216-ae5e-6da5bd13068b | -5.7752 | -45.128 | 2026-05-22 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |
| f094b774-df75-3e53-aa0c-1849e7d5e278 | -11.4534 | -52.9212 | 2026-05-22 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| edbdfee6-ac53-3e08-ab1c-691e425596d7 | -11.4534 | -52.9212 | 2026-05-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 22ac4317-5664-325e-80b7-23389901c398 | -10.6642 | -49.7054 | 2026-05-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 80deb5b7-0aae-3fd3-bfbb-7734d9c0a49c | -5.7752 | -45.128 | 2026-05-22 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| f45ee2eb-3c44-3d52-80cb-1b43bf01fdad | -10.6639 | -49.727 | 2026-05-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e472b666-e4d1-3b8d-85bf-4cbb9350c599 | -5.775 | -45.1507 | 2026-05-22 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| acf72024-4a90-3e1a-b4f1-cc6ac550e7a7 | -5.7752 | -45.128 | 2026-05-22 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| ab1c650b-eae5-3376-81cc-e6b4cc2ed015 | -8.9266 | -46.9157 | 2026-05-22 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b93c4ee3-d885-3b9b-acc4-fd055dd83fca | -10.6642 | -49.7054 | 2026-05-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 680f21d1-199f-38af-8b90-2fa5ef13a9f0 | -11.4534 | -52.9212 | 2026-05-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 333b06e2-b943-338f-9847-59c84dd123f9 | -10.6639 | -49.727 | 2026-05-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 73beb2b7-e910-308e-a585-d59b7f6268c6 | -10.4535 | -49.8999 | 2026-05-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 35b49782-797d-32a8-8d14-07e42197d2b0 | -10.6642 | -49.7054 | 2026-05-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| f8a2870a-aca1-36f5-9b49-7277e2a57f03 | -11.4534 | -52.9212 | 2026-05-22 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 2ce9f374-4444-308e-adef-1e80a1ad2f3f | -5.775 | -45.1507 | 2026-05-22 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d40dad91-bfef-39f9-9256-230d779c731e | -10.4346 | -49.9019 | 2026-05-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 87573719-4be1-3470-a12a-4189c6263485 | -8.9266 | -46.9157 | 2026-05-22 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 1865a45c-0fb5-3256-b3e7-4fa9a68c6ef2 | -8.9266 | -46.9157 | 2026-05-22 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7feacf7b-2f2f-310b-9d06-4359f631b3c9 | -10.6639 | -49.727 | 2026-05-22 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9a8094e6-44c8-344b-ad31-376448aaa525 | -11.4534 | -52.9212 | 2026-05-22 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 2afbaf26-d6ae-387a-be25-87da88aa5c0a | -10.6642 | -49.7054 | 2026-05-22 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 18659425-3a25-3f70-bcca-2424cc1bde3d | -11.4534 | -52.9212 | 2026-05-22 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 70df4d18-918f-3a45-a28f-b00f5127810a | -10.6642 | -49.7054 | 2026-05-22 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 500d739e-d59b-3420-bd56-6220032dd922 | -11.4534 | -52.9212 | 2026-05-22 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 4c10dadf-e3bb-3515-8bc6-4da1ced26566 | -10.6642 | -49.7054 | 2026-05-22 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 2b46b5b2-5e09-315e-a88f-febee1885f0b | -11.4534 | -52.9212 | 2026-05-22 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| ce25a5ec-4411-3187-a768-c0b337cd6385 | -11.4344 | -52.9231 | 2026-05-22 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 0c7e9cea-3d40-30b1-ab75-f1157c02c36e | -10.6642 | -49.7054 | 2026-05-22 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| c035ef3b-44ac-34b2-89a0-8036bdf1a2b3 | -10.7939 | -49.9064 | 2026-05-22 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 33da0240-99b5-34a7-821f-8e94d32b2cfc | -10.6642 | -49.7054 | 2026-05-22 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 4de4ecfd-1608-39bb-976b-3bb290bea5e0 | -10.6642 | -49.7054 | 2026-05-22 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |


