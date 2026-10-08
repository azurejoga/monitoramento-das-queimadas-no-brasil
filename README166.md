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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e039178-9fd3-3f03-aa2a-88c5b48d6898 | -2.99637 | -54.0733 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a58d6399-2e1c-3230-a6ab-1ff57b218001 | -6.19894 | -52.78901 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13cf285b-7a1b-35b2-a6f2-edfd1ae8d6dc | -5.69108 | -53.49257 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61cd51fb-eb48-3273-824a-e5d1e2a2c906 | -3.51701 | -54.65636 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce5346cf-43fe-384b-99a3-8023ab33ddb5 | -3.05578 | -54.22068 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ef2ba02-f106-3235-bd7f-0b072e6caace | -6.94991 | -45.28253 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7c2d1cc4-655b-30c7-9d9f-4d79aa819a57 | -3.17912 | -50.54623 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70c696b0-c7a1-358c-b8f0-d1bd361f8d5c | -2.76506 | -54.10189 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f05dfccd-bb99-39e7-8163-ed286bd71788 | -2.75581 | -54.1092 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d8e4d68-d780-3d5e-9776-e561c89728ea | -3.03097 | -59.14974 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf29b2c4-d3ce-3112-b6a8-eb591f4e7844 | -3.00348 | -54.05056 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72d2bbed-21db-3cb8-9901-58f1509c7106 | -11.35384 | -51.87707 | 2026-10-08 05:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30cf7bdc-5a89-392d-9951-7ad795425f1a | -3.07493 | -54.14485 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99fb7c59-6be3-39d3-beec-91839dacb827 | -2.58352 | -56.17281 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40c1c330-358e-385f-acbc-db119ebe7d39 | -6.14222 | -47.92665 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a974c3fd-8304-3edf-9f01-2edf4b68b4ff | -3.01051 | -54.74627 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17ce9878-512d-35b3-aaf6-e5b591afe8e3 | -4.45736 | -47.92188 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 275e3dd2-4962-3a93-a9bf-69bd0c60863b | -3.31017 | -54.04815 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d3725046-eb69-3dd4-8be1-2223c5b5aba9 | -3.56159 | -54.48604 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a192d63-62c0-378e-b449-2f5cb6cc41da | -9.97337 | -57.52486 | 2026-10-08 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91f545c5-bf88-3a0e-ae5c-7346c6e459d9 | -3.09217 | -59.19511 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8777d7bb-2683-31f3-85d4-08e75880c33c | -2.78903 | -54.08591 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2082ebe-37dd-3b51-b370-1125f0cd6ef3 | -2.99738 | -54.76311 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98c86957-8111-3cad-9dcb-1a6b7b65622c | -3.28282 | -53.82942 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4cc02d-6d53-326e-98f9-ab15c2b661e3 | -3.84781 | -58.89702 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2203fe19-c75b-3961-b1d2-9eeb529075a5 | -2.49964 | -56.12795 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0ddbd4a-301a-3b9e-8640-a2d025a5116e | -2.62858 | -56.65838 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51503c15-3826-35d4-8026-e17d68dc42f2 | -5.72763 | -45.15571 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dad1bd07-ece1-3e4c-8456-865bacbe1daa | -10.6238 | -53.85905 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f995f781-fc6d-341a-bce2-be22bb267c54 | -3.54175 | -55.52154 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 281732d9-2bc2-3314-a644-fb9a77311d86 | -3.55054 | -54.661 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2565770-2a9d-34f6-871a-6670e2597bd7 | -3.51097 | -59.32772 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec94070-2d2d-3ed5-beb9-ed6f8279f9f6 | -4.77645 | -55.7457 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8b9f932-5020-3a1b-b4a5-854cf647b13e | -9.14467 | -65.30027 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa21a257-0571-3987-b71c-e3faddb816cd | -2.4935 | -56.10218 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9320347c-9af0-35ee-9253-9699b49bfec2 | -2.88228 | -54.08748 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dad3961-d005-3b95-988a-cd997a324d5c | -2.9024 | -57.65757 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25bf90eb-5077-36d8-a6e7-94b92ef16650 | -6.32738 | -55.71405 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a97ca6e5-a86e-3ef9-945e-9953348bb590 | -2.03328 | -55.63195 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 394d6d92-d145-3fc1-aa2f-bad165ce3199 | -3.54518 | -54.65685 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92d4e7cb-ff83-38f5-a37e-cab6d7f79dcc | -3.01662 | -54.12795 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7861e1e2-c3fc-36d4-9d21-a94f5f10d130 | -3.08203 | -54.28634 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80f5324a-38aa-3724-a2d3-e38e77d9fee9 | -7.21144 | -55.09486 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c50a62-91b8-3228-a820-319e4a285d8b | -3.73767 | -54.65114 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07773c8b-7f1c-3a99-bee1-2183695dca36 | -2.48747 | -56.14021 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdbfaa84-464e-3a3f-8029-64842f46fc1d | -3.17723 | -50.55848 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c4769f6-4ea4-3f21-9496-a0995bae5324 | -6.26282 | -55.99632 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac57a141-7e04-3f2c-b7b5-ecf2619ff06f | -3.54303 | -54.62582 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db01f670-56d6-33a9-a72a-d8a8cb86b103 | -5.27032 | -55.95627 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bcb2b8d-6aa3-33c6-8598-dbdd168187b7 | -3.27479 | -54.06666 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29a8a317-481a-3147-8790-2a7273b13cb4 | -2.36173 | -48.88477 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e4f1ae-c0bc-32f9-baf7-9e17a33fe2b1 | -1.10315 | -54.16382 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9590cfba-6f39-3c1d-9f35-87f1b29a1c2f | -3.55341 | -54.66526 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5039c4dd-1f22-3949-b4ec-09a033bf8d10 | -3.08374 | -54.2983 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 69b05e17-c1a0-3fc7-91e5-dec503ec83df | -3.99085 | -59.21534 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31fbb78-15a8-32fc-a2aa-ea14cfbd38e7 | -2.86575 | -59.23469 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5de2867-0c87-3b4a-a71b-691d58cf7021 | -4.53938 | -55.61381 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a585f04-a68f-3fac-91e3-b609605d1312 | -8.38802 | -46.30256 | 2026-10-08 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7d3f46c-5fbf-3530-bf3c-8d832e051020 | -2.88391 | -54.12332 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 439979f5-9157-34fb-895c-7ccccd0ff7ef | -3.28383 | -54.03205 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3db65bf7-bccb-314e-960a-76c0a8c800bb | -2.88956 | -54.17921 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99081996-68b3-356b-9c1c-f4589c83cdb4 | -1.09912 | -54.16698 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89fba24d-002f-3db8-a774-d8ac27688612 | -1.36469 | -56.92136 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4855f401-4157-306c-82d6-d3933d6f78b7 | -4.043 | -55.37224 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4851736d-5515-3704-b989-21e3456c8790 | -4.92329 | -55.85908 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f97d6ffe-3c30-30c5-9e75-21a6de605f4d | -6.20839 | -52.86032 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c989cea3-9f1f-3fd2-99f3-674f5fe08965 | -3.47359 | -59.58237 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 078a53fb-4cd2-3f49-9c86-449f909d1fc8 | -3.54824 | -54.653 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b59b6e93-2d86-3949-af3b-59a6e094f8d9 | -6.67852 | -55.09158 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f679584-0bb7-3e1a-8513-c2f230a1ca28 | -3.00153 | -57.75683 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 261b6a7b-fee7-3ab4-a9c3-073ae05a8e4b | -3.06645 | -54.24862 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4417d0e0-2f61-3620-a02b-a3f2c02fee9e | -3.38151 | -58.2416 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae1e60fc-77de-3416-86e8-35aa9dbc228b | -1.41801 | -55.71715 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b1690d7-410a-3d4c-8e52-a8321ae75fb3 | -10.28445 | -60.54053 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e13ccea4-231d-33fb-a3b1-dff369369c44 | -3.29335 | -54.01744 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e46e31f8-bb7f-343c-93dc-2c353f4d32c5 | -3.00432 | -54.13789 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0458ef4-8c37-3d63-b3bd-a93144366adc | -4.12688 | -54.2636 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e38ffe9a-9354-33d4-8fc6-b4a8f8ac9a14 | -3.65506 | -50.94814 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de610395-621f-3b34-a6ec-c679232f7042 | -8.7241 | -45.15334 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5beec7f2-f248-3e98-8232-e5d7b5db31db | -2.48128 | -56.09319 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 431d0c26-2ea4-3c88-93c5-32720549a4e6 | -3.30495 | -54.67372 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42c4f9ad-3722-3035-b338-800970a0f793 | -2.83155 | -56.6795 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a84e8279-f79d-37b5-a714-829d6be650e5 | -7.1702 | -47.78519 | 2026-10-08 05:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd9510fa-717e-3463-b6ef-87ee08443d87 | -6.66978 | -55.10199 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d7e3a2f-0468-3d6f-94a7-6a35101872ca | -5.6975 | -53.47519 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6895497-b650-35e8-9907-572832dd7a1a | -3.72988 | -58.8602 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb45072f-a0ae-3f4a-99f3-68ccf7a7410a | -1.52616 | -54.53203 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eac4d83-b116-38ff-9171-10c51b6ec978 | -1.48662 | -54.54094 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c6ed54-3f98-3ebb-863f-d07372af6ed4 | -8.73679 | -45.16063 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 642c6002-b0ae-3fa4-9940-ce477747c6ff | -9.10081 | -65.35508 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01a31e47-89f3-3fe1-884a-27660839cbdf | -2.91901 | -54.10505 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e72e660-6280-38e5-9999-853910687747 | -3.24853 | -56.80209 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c150e0d-9c5f-3b50-9434-7a9d87469196 | -2.64337 | -56.54385 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e146a117-9c8e-3d34-a066-dbd2db212235 | -6.09571 | -55.72372 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22c96bab-70f3-3df2-aeff-f3da7644fb3b | -5.69686 | -53.47948 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75ef49fc-1ee8-3907-b405-f06d07d487f0 | -2.72341 | -57.46594 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e9fccf6-11a9-3037-94e0-8edfa8b8bfbd | -3.69001 | -55.9556 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bffaa9b6-5aea-3009-9d31-a5ff2724997f | -3.59027 | -61.63132 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f3d551c-0967-3279-aad8-1bba53f1ce0d | -3.04825 | -54.38959 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bc16c9e-fff8-3cbb-86e7-5977d232931c | -2.98588 | -54.77334 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README167.md)
