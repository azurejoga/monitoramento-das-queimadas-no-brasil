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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c47603f-058d-3ba8-9511-293ef5640457 | -6.09989 | -57.69032 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8efe8b4-5542-31f0-9041-b6880f581b8f | -6.79752 | -58.78763 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39883c7c-4134-3991-9f7c-402e386067be | -3.06696 | -59.30496 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ec99d4ab-0d36-3c5c-976c-66adc032272b | -6.79958 | -59.13777 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad6677d9-7b12-3fb6-bd52-5b4814a4c9d4 | -3.06802 | -61.27395 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6162589-7afe-3035-bd1c-ab9107f47406 | -4.34697 | -55.65665 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f994c1ae-6c9d-391f-91e6-f27b61272763 | -3.23209 | -53.94893 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8af75515-7dbb-3516-a9f8-dbd068f4e1b6 | -3.47424 | -59.60069 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e70f572-11cd-3c36-bf96-93aa2e817f4b | -3.20668 | -53.95514 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab6ab88c-c07d-385d-8a61-523424892e13 | -3.46397 | -58.33236 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 036df6f7-de84-3867-b45e-cbe01ab3c689 | -3.11419 | -61.26976 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 135d1169-b639-38f3-890e-86d8254e632e | -6.62153 | -59.92019 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| ec30b619-8b83-3aeb-824b-3339d88b397d | -3.60624 | -60.57312 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c86f540-c139-3d1d-9bf4-9ce6f1777bcc | -2.22096 | -60.08364 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41ba2392-7de0-3dba-b924-ca15421e6f6e | -4.4112 | -55.24594 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f286afa-db4a-3cc6-a1b4-66b76f1319f9 | -6.78147 | -63.13303 | 2026-09-22 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22c8045c-6f60-3b99-aa93-fbb7f28c0de1 | -3.77021 | -61.19598 | 2026-09-22 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dfd599e-bf9a-3418-bd7e-c68028668bdf | -6.69627 | -59.96184 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 79be7027-a37d-3cc6-b025-11f16df9282a | -6.62458 | -59.92294 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9dc6ed27-5930-342f-8fad-4b79be59b03a | -6.77744 | -55.4874 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f206da7-ee50-3205-89b0-e111fcc36270 | -3.46189 | -58.3992 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5a74c0-a766-3b10-b0c1-ec4553fa0f70 | -6.06273 | -57.87119 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28cb85d-d72f-3f0a-ab55-019a5b550cb1 | -5.72912 | -53.46679 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aa16da3-7e4b-37c1-9186-f8fc2365642e | -6.35276 | -57.77032 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1c301fa-c6f9-37fc-8c7d-011194d49eb0 | -3.34073 | -59.86138 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fc6f786-3731-3ddd-aef3-4b3b60c73c80 | -5.7297 | -53.46277 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a5a435-1479-3d1f-91ab-256c61c9f151 | -5.97647 | -57.78463 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528abb85-6eb1-3df7-81a2-738d869f8664 | -2.85639 | -57.81427 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63ff5ac2-4ca6-3257-be59-d837268e78b0 | -6.38941 | -60.02121 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ead64c2f-42ed-330e-85dc-123146a417bc | -8.48712 | -57.61831 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb2ece11-076c-3508-88bb-12712d8ec083 | -6.43221 | -55.61772 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e4074b6-fffd-3d21-b24c-a5a970e451fe | -8.25741 | -55.26696 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e505fb0-7609-39ea-9b35-3c4616ed6783 | -6.42777 | -59.97359 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cf8524c-bf80-3f6d-a14d-73ee38990c4a | -4.96383 | -55.82631 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8493fb73-32de-38b3-a61b-a57bf314152d | -3.97068 | -59.63776 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b30ffbe-298f-345f-9833-f83505f4288f | -7.08237 | -61.08479 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93af1556-e36c-31d0-a5db-2fe2b08a48ee | -5.93924 | -59.98045 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c5aa45a-2b9a-3281-9225-9413d29c6cb8 | -7.72233 | -61.25008 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24552cb5-f846-3f5e-8b47-9c411c63743c | -3.69145 | -60.56116 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b413146-3c51-3017-a222-591632daf43b | -5.9348 | -59.98442 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47f091ba-7646-339a-a319-f5d7de11c971 | -7.71769 | -61.23265 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6abe9fe-e8f7-3cd0-916e-6967deca389b | -3.66353 | -58.57494 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ab8cdb-5c3e-3ea8-8acf-60584c6d133c | -3.28627 | -57.85893 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfe885f7-74eb-311a-9495-5bb8de24f227 | -6.29733 | -59.94212 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a33f59fb-8ce7-3f5a-bb3b-4d8bfeb53f43 | -3.14168 | -61.22853 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c436073c-fb6d-3c9e-89ff-30595386480e | -3.65408 | -58.86749 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d519683-7f7c-38ec-a45b-af5a4d3ccad7 | -5.94005 | -57.7031 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 896c2298-cc5d-3010-91c8-21ab1de7c57c | -4.34431 | -55.65409 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3337a03-5094-3c3b-85b0-8295e23120e9 | -8.11603 | -54.80176 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a7ed28c-1c27-3b96-9f86-ad2a624d080f | -5.49002 | -60.13269 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c93a2c3-aaac-3ca6-9e74-b637185db716 | -6.09073 | -57.62541 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 578e8659-0600-31b3-bfa5-478428d9bb35 | -8.25869 | -55.30429 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9aa018c-fc4d-34d8-938d-c9ff05836da9 | -6.37573 | -58.29208 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6864f9ce-af6b-38a3-a2e0-748b663d2b6b | -2.67479 | -57.86128 | 2026-09-22 05:42:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b772a503-db6d-3000-86f2-91706c8d2ce5 | -3.34306 | -59.87039 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e17de80-f9a4-3c40-b529-207eba6f4786 | -6.46409 | -59.98851 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 26388139-9eae-320b-903f-dbd601788218 | -3.59734 | -60.79586 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2802814c-7508-34ec-af99-d5acde4978db | -2.54708 | -58.01482 | 2026-09-22 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6730001c-338c-39d4-af38-f27f5674997f | -7.90156 | -61.82808 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2036b4a0-dea2-38ec-b6b0-59a8922f1fb2 | -6.22782 | -55.61876 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c154e3c-fde7-3271-9fd0-ae4144767272 | -8.49166 | -57.61898 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6483c726-8be0-3252-8449-7decb035b790 | -3.83647 | -59.38458 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 954d443e-7585-3794-9039-bf9889adbd8b | -3.92005 | -60.55711 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8601636d-0cb3-316b-84fe-657f89e9484c | -8.61529 | -54.63525 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90b05087-4bc6-3bb4-8d44-c9ceb1ad9870 | -7.72528 | -61.2547 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80f770a9-f59d-3e32-8ed0-9ba8fbf769d4 | -2.40916 | -58.28334 | 2026-09-22 05:42:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ec1224b-f20c-3bec-a8d1-3a1480105698 | -6.29287 | -57.7467 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29a65287-9992-39d5-80e6-543fac1894e5 | -6.08493 | -57.6939 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6677762e-3cd4-387a-b2bc-aaa4ac98d6b5 | -5.45348 | -60.14948 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 684d29a3-5458-30ff-96f2-72bd19c16c5d | -3.46083 | -58.4061 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45f7bf1a-e341-34ff-a7f5-08bf543ab188 | -6.3086 | -57.73796 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a62bcdcb-ffc0-3c78-bd0f-35f7ac863e6c | -6.30983 | -60.01382 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab605072-6f62-368f-bd00-095e30b8e52b | -7.32878 | -55.59895 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8364fea7-71ba-39c8-b108-ae866e8a010e | -4.87176 | -55.84506 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83e10da2-44b4-3718-8dc9-c5fd8ed3ef9c | -8.60515 | -54.62634 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b6944eb-8020-3d76-8b99-0289c332e692 | -4.08878 | -62.09335 | 2026-09-22 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3162ff9b-3443-389b-bd51-9fa70e1b44c5 | -4.96871 | -55.8269 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bc5cd97-068d-37fd-b8d8-e9c53ef3dd4c | -7.71938 | -61.24545 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb41c88a-528d-3258-bd41-21dcec149096 | -6.42716 | -55.61702 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a663895-9c2d-320e-91e6-7cea66ddd892 | -3.50185 | -59.61844 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b69a945-435e-3727-9591-2ce120c95f63 | -3.3297 | -59.81168 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96c2856-889a-32d8-84f2-1d3f2d968cf4 | -4.07288 | -56.22952 | 2026-09-22 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a286a2e5-dbfb-3781-ae9b-03076e40c2f3 | -5.91267 | -57.67824 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 912006b4-f396-377a-8eab-60c05a1aaf3e | -6.19741 | -57.78082 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62e3735e-3492-3ffe-b63c-4c6c5359ee7a | -3.72429 | -60.58137 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19a8e33d-fc67-3a44-8d8c-41ffe92fa88c | -2.65374 | -59.68396 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ec5a048-9881-30ef-8ff9-2f9854a9a4e3 | -3.05784 | -54.40304 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614c5705-da73-359c-abc9-d95ab2e94bab | -6.7542 | -59.11336 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4646778-0b26-3d7c-937f-2e1ad13ca81c | -3.51864 | -56.90845 | 2026-09-22 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b40a595-9102-31bc-bfdc-953f41157503 | -6.13642 | -59.87996 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 410289d4-d9bb-34c7-b686-89de0f9b9772 | -6.63149 | -59.9311 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 09be39e5-655c-3706-b588-8c6ace3a85cb | -6.29931 | -57.74084 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b42bd47-3579-3f7b-b221-7fae273de09f | -5.41658 | -60.21923 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc62dc1-fd00-3886-9621-c9bee6a7b672 | -3.7815 | -60.7475 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8335152-63cc-34d6-953f-8ba0add54aac | -8.91479 | -50.92703 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49fa6eec-916c-3cf8-95f9-1a4536d7e05c | -6.00313 | -57.70709 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c401fa4-3d6f-31d2-a9e3-4f273c228182 | -3.14969 | -61.39954 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8ca64bf-fdca-3fcf-9124-db9097a53933 | -5.8039 | -53.52673 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95befdec-1275-3523-9d59-3c0031e26eb7 | -6.44421 | -59.96679 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f155365-8a3a-3774-9675-4f3d9f109bb2 | -2.78678 | -59.88715 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README109.md)
