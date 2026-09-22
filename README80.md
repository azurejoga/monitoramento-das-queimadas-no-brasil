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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60079598-178f-366e-a2f5-7afe738721c2 | -11.70696 | -50.99991 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ce1d8d83-06e8-3cd5-8035-9c32a8e259ee | -6.57267 | -44.15786 | 2026-09-22 05:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9ffe4c88-a8e4-3595-90c0-f3ceeb097032 | -6.12944 | -55.81512 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34a9f1eb-7adc-3851-97f2-e75d430ab5e2 | -6.06106 | -57.86487 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb3847ea-eee3-361d-8a37-7522d85ea2c1 | -5.60315 | -48.22574 | 2026-09-22 05:23:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90af9420-00bd-3f79-bf00-bb146ca817a8 | -10.90481 | -53.9609 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50614cd3-7edb-3cb0-af52-0c0817b0c264 | -5.87696 | -52.06247 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d67f5af-a9a8-33d6-98c3-8077da0960f1 | -7.56816 | -57.68373 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70790188-4146-34da-95d4-189a9aca8cbe | -5.96956 | -57.78241 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e3fa75-3139-3e61-98df-6db4abb37abf | -5.76247 | -45.08437 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 183bcc49-5455-313d-86c5-22b620879085 | -8.82782 | -50.49047 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca6b7b9f-7883-3b56-ad6f-109eb197bebf | -7.58257 | -57.67889 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bb48624-7797-3c3b-a320-c3c154e5c2eb | -3.40647 | -61.29328 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aebe581-fc2e-3cb7-8f04-8cc77ca3eb22 | -8.79784 | -44.27922 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fa7d75e7-ad00-34ec-9f57-8e9fb3241f3c | -6.44865 | -59.97297 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 283a6afd-4459-36ab-b869-a397a4d89330 | -6.13663 | -57.77675 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0269d3d8-8354-3ea3-9fd0-c33e9705ca1b | -5.93804 | -59.98325 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e29080d5-29b8-38f2-81e7-68fedbf1e7a4 | -6.78224 | -48.67205 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54c01d86-1921-395d-aef9-f09141e65d66 | -9.56024 | -66.02287 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aafbc426-bb80-3560-99b4-5353c599a562 | -6.7244 | -55.0785 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 733e2ebe-d5b0-3ae3-b2f9-06f87a0bd50e | -6.00731 | -57.67421 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1e92d85-cc50-304a-9569-970becfb9517 | -7.24509 | -55.58778 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11a21c1d-1f93-3859-b964-2ba0d41193cd | -3.48897 | -59.57788 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8210567d-562e-31b0-a349-6d52d9f84fde | -6.11064 | -55.68988 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8212494-5631-3c75-a14b-d5d1177de140 | -6.66402 | -50.88807 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1fb9017-e6f7-3d91-937f-750d92c80169 | -6.78028 | -58.60891 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a20cdc92-1d4b-3437-8bb3-0d488f529224 | -6.28519 | -57.77518 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07485e2d-211e-3f3a-ba2a-1d82f4d920e3 | -3.92941 | -56.05082 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 129331c0-5a9e-3585-8732-11f0959900c4 | -7.13435 | -48.43843 | 2026-09-22 05:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59956379-8dfc-307c-b12c-4c561f58eeba | -7.055 | -49.91993 | 2026-09-22 05:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9aa6eb50-38f9-3728-90cd-48aa261eeb3b | -6.92797 | -59.63042 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a3b011c-ee09-36aa-a23c-d1b427334bae | -6.64514 | -50.06496 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7dcac90-cb17-3038-bf88-e3732ba98bac | -1.18805 | -55.67545 | 2026-09-22 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cdab3e7-4b57-39ea-ac60-7c79c530f12c | -3.38402 | -56.93456 | 2026-09-22 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e5648a5-d8c9-3fe0-ac5b-a5d93ddc1f7b | -6.7449 | -59.06296 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 271d4b68-7f4f-3e46-a1b2-5f37e117c875 | -9.5661 | -66.0184 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9c1b596-f688-3761-9956-0ac9d3fd19dc | -3.45543 | -58.21177 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 643aee38-342f-3571-a5f6-af68aa1a8f5f | -1.84606 | -54.95647 | 2026-09-22 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a09c34bc-dfb1-322f-bc1a-250323d5a2fd | -11.32054 | -54.03522 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c333032-180c-36db-a871-d591c822a5d7 | -4.0552 | -56.33115 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4240158-8988-3b80-a707-fb5d2927ac0f | -5.98512 | -57.70633 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bc174c1-3d29-3f6f-90d2-679ec71987e4 | -6.09499 | -57.65234 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa861416-eded-3b7c-9547-6f39874e69d0 | -7.45513 | -44.74356 | 2026-09-22 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fe77a33-2962-3db3-b109-f5a9a8454556 | -5.87389 | -53.65017 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c4baba-d95d-395b-984a-7018f5c43363 | -2.73879 | -51.37089 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b02c6a89-73f6-3e57-b428-b8046b77fc12 | -3.40345 | -59.26386 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1843cab0-f39e-3cd8-80d0-22a248fa7837 | -5.37755 | -55.89584 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db227550-5193-372a-adbe-36fcb492f7a7 | -13.52327 | -51.50862 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 6984e4d6-79b1-3f97-865a-01566c956994 | -6.44931 | -59.96901 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2e2b29-03e2-3669-80f1-76b0aa1229ad | -3.20689 | -53.94662 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15ccd73d-8ffe-3861-95fc-c47d0bae104a | -6.84254 | -55.26941 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e674253-fd4c-36dc-a4de-57bf202a9678 | -3.45649 | -58.4026 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d0aa7aa-40c7-3445-9e18-de63db9d8778 | -6.28276 | -56.03879 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e411efe8-721f-3686-a62f-9be99165f2e6 | -6.3494 | -59.96109 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ccbd740-c34f-3c44-bfac-b665acafee5b | -9.60484 | -66.1176 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1bcc4ed-c151-38bc-86a5-c7055e8bf9a8 | -4.65108 | -50.99361 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a76ce6c-a5bc-3bef-a8e2-11e8deef95aa | -5.84407 | -49.78259 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cffae70-80f5-3154-a6af-f65e17ed4f37 | -6.46277 | -59.97531 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e15f867-994d-3a99-bc40-0803f58c3556 | -14.64849 | -52.08498 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77f3041f-279b-3bfb-822f-1b60343aa499 | -8.10238 | -55.34668 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4e513ed-8c28-3c9d-b3ec-fe9ffef5e19f | -12.80098 | -54.0402 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc78ef8b-9a20-394b-82e4-bb4b0d8b0a98 | -7.4204 | -49.85326 | 2026-09-22 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f80cea12-2d1f-388c-b020-29d99e5538de | -6.34076 | -59.94753 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 034d06d5-b62d-329d-99f3-7fd9c4e013ce | -6.19251 | -57.78557 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72cdf2b2-5e74-381e-a05c-4ada53ac32f2 | -3.28432 | -57.8616 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69bbe18a-7386-3cb2-b0c4-42e89da03c23 | -11.87456 | -46.84903 | 2026-09-22 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1b03550-9c69-3f54-9ab4-455dcc1f5872 | -8.11387 | -54.80166 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff32172-a7e2-3a36-b07e-a6ef09b8511e | -11.04149 | -54.14908 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ad686b9-39d6-3254-80c5-c6570f37b47c | -6.13935 | -59.96561 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cabc01c-df75-3f8d-b2a1-bf04fbc276ff | -3.06217 | -54.41343 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e51fbbb0-48aa-3dde-b321-498b71515152 | -1.33307 | -54.66513 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 485ac8c1-6800-38e3-9e4d-64bb1861d45f | -11.95772 | -46.52072 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed0ad28f-fd64-3363-9449-864245ad4a1a | -14.17361 | -47.875 | 2026-09-22 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a6a6ef0-57a2-3964-bfe0-03867b4d89df | -3.23468 | -53.95487 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0724e644-5959-393f-9efc-19fbed19d001 | -5.37925 | -55.90706 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8115fd1c-2a19-3562-a7a2-6a148f8bceb9 | -12.30381 | -50.70133 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67c5dbd9-14e2-342f-b22f-7de6843b70e7 | -6.44644 | -59.96446 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f131eef-6b5f-3a7e-be8b-dec5d1d0c92b | -6.99837 | -49.93794 | 2026-09-22 05:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c690567-0e16-314e-8e85-2a4866540701 | -12.93355 | -51.04585 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ffdeccf-92f9-3294-a052-d3e2a99a2181 | -11.70765 | -50.99467 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| f7b70143-40ab-3c1e-8622-36d896c1b9ab | -6.73885 | -59.42691 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 054fc85d-fe4e-3596-8184-f082b17bd35f | -12.84124 | -50.97694 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5c35ab7-7ecf-30eb-b0fd-6925f3594351 | -5.60714 | -44.84132 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4d37ae2-cb84-3de0-a95d-08f794dd77ea | -6.8176 | -55.83102 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32463cda-94f3-355d-a70c-821158e1097a | -5.81785 | -53.51241 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c69e2ee-cb27-3cea-b9f4-7b4a83265df9 | -7.57148 | -57.68426 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ed5f85f-e4ed-3518-b593-56f560ae5820 | -9.55922 | -66.02846 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f1cc386-0bf5-3411-9fe7-d3ec4c0c1a1f | -3.4591 | -58.32035 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a80c663-0cdf-367a-80a6-067792ef0873 | -6.7291 | -55.07125 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba7765e3-723c-36c5-917d-6ee2ebf14aeb | -10.87722 | -54.09658 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5d911c1-58d8-30d6-8d2c-bff4fcd31f92 | -11.99488 | -58.0747 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b39c59a5-58f2-3227-a60a-d9f6895cd8dc | -12.95975 | -50.97816 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ff3cd2f-f30b-302e-85d2-d79bba0151c9 | -3.07117 | -61.27164 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96d13d10-87da-39ab-a147-ed9832490480 | -3.01913 | -54.18013 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32d16897-3980-3d82-8c12-ce68db9322f3 | -3.08723 | -61.17156 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 247a8235-befb-3ace-92ec-5a8be12233e3 | -3.66502 | -54.27056 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb5f536b-3665-3b69-a8b7-52a43cf0f514 | -6.31048 | -60.00486 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 387ec6e0-063e-3970-a86e-1a1ce5438ac5 | -3.82105 | -59.33544 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c529a8-fa35-32e7-8407-37b03392f428 | -14.75474 | -48.43027 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00d1edf9-d989-3e90-97ef-772b1c9e662a | -1.70575 | -54.89125 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README81.md)
