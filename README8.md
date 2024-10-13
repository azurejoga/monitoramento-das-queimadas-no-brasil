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
| c98df09c-9b72-3f20-913f-006a3c09513c | -8.05503 | -44.81697 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a2dc5389-24b6-32d7-954d-cf3ef9d19635 | -7.94049 | -43.18483 | 2024-10-13 00:39:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8fed49d7-d7b3-3990-95f8-935fb252ff8a | -7.93924 | -43.17595 | 2024-10-13 00:39:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d787edd7-6a76-3fb8-b958-d92bc28ad1d7 | -7.90039 | -44.62923 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 25de1ec0-5c76-36bb-bc33-9b1632fca3c4 | -7.89914 | -44.62011 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a661ef6e-5763-314e-9ad4-13b703d11911 | -7.8979 | -44.61103 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d2e5bf86-3ae1-3a10-b310-ec856cd52e32 | -7.89019 | -44.62138 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d89a9414-8dcd-3255-88a1-97e87ca1470e | -7.88498 | -39.15465 | 2024-10-13 00:39:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a8c5b36d-6c82-37de-a491-145f8f3816f8 | -7.73498 | -43.30558 | 2024-10-13 00:39:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c8b367d9-63a4-3ab8-ae10-6bca5fadfbe8 | -7.73374 | -43.2967 | 2024-10-13 00:39:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 844a28ee-81c8-33f4-855f-c18c0fc41cc1 | -7.7249 | -43.29797 | 2024-10-13 00:39:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f9ec45df-4704-3491-9fb2-43e689c20e02 | -7.7163 | -43.17219 | 2024-10-13 00:39:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 502da2d8-fb01-3bd5-a5dc-f6cae98d2f47 | -7.16601 | -42.6014 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 99a3c6f5-e150-3df7-a2d3-1d9d9a941adf | -7.09621 | -39.86185 | 2024-10-13 00:39:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 87d523bc-537a-383e-afe3-f5699a57a08a | -6.82101 | -42.76935 | 2024-10-13 00:39:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 68eeb708-5c1d-37fe-be84-9fea61364b49 | -6.81973 | -42.76023 | 2024-10-13 00:39:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e91ef543-2dc7-319a-a2a1-15bf5f2df681 | -6.73007 | -43.5623 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6f39a997-46a3-3d34-ba29-ccd799e8814e | -6.72883 | -43.55345 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 860bc439-6a19-3118-95d4-44a838319078 | -6.72123 | -43.56358 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8c8d0f3b-fd98-337a-b93f-92ae87e6870f | -6.71999 | -43.55473 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c893b89c-e1ef-39d6-93d4-b77cb404e8a9 | -6.43158 | -43.93598 | 2024-10-13 00:39:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e19b2f0a-d3ea-3184-9c9f-f12d120a240a | -6.38808 | -41.60276 | 2024-10-13 00:39:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| b0a47f1d-e26d-3c2d-b705-ab56ef9451cf | -6.38663 | -41.59261 | 2024-10-13 00:39:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 3d8b21a9-4b32-3cc0-9f93-8cd7cf24a4b5 | -6.2502 | -42.51321 | 2024-10-13 00:39:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 77647a6a-edaf-3a4e-b35b-e52280c87f7f | -6.24887 | -42.50372 | 2024-10-13 00:39:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3ed1c826-8eaf-36f0-855c-a1c5fa9fdea0 | -6.16375 | -41.79154 | 2024-10-13 00:39:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 660ca2de-ff40-3996-bf56-31c8148f52d3 | -6.07565 | -42.3913 | 2024-10-13 00:39:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e81356cb-50c4-32b2-aa0d-fd2ba32c2ca0 | -5.95922 | -43.19517 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a7ad82dd-da45-3c74-88fc-196ee992fee9 | -5.95032 | -43.19647 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cd479a42-2eff-31be-a5fc-177f56feacd0 | -5.94836 | -42.66082 | 2024-10-13 00:39:00 | TERRA_M-M | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 62ba8478-f82b-3062-a4ad-0c317c2f74d7 | -5.94493 | -43.47963 | 2024-10-13 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7cd64e7a-3127-3ea1-a4d2-6edd646dd539 | -5.85923 | -41.97213 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 58ecad9f-054f-3136-96ca-a994e5e62403 | -5.85782 | -41.96227 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7dfcbe8c-9885-3c07-af82-75c4a1fed597 | -5.79674 | -43.22159 | 2024-10-13 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bca2ef7-b7eb-3720-921f-bb378e275c28 | -5.64327 | -40.69503 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0de5317d-730b-3969-a40c-de70cd73de36 | -5.57464 | -43.93329 | 2024-10-13 00:39:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8121c08-bdfe-37ea-a93b-1d36182636eb | -5.50724 | -39.56318 | 2024-10-13 00:39:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| eba1e4fe-d807-3cad-a133-7c691f2308fd | -5.37665 | -43.51331 | 2024-10-13 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0f45d611-e6f9-3d62-8920-41eecfae7645 | -5.14874 | -43.92535 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e18560b0-99f8-3ab2-9bb4-7e078d412c3a | -5.12098 | -41.69599 | 2024-10-13 00:39:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| dd94a035-8a67-32db-b088-cfe5a19aef6b | -5.11951 | -41.68562 | 2024-10-13 00:39:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0e463796-b95d-36d0-9e1f-f7af3bb96551 | -4.95379 | -41.81684 | 2024-10-13 00:39:00 | TERRA_M-M | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0cee602b-d89b-3358-851f-16064f8ed66d | -3.86552 | -40.63485 | 2024-10-13 00:39:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 85bd1319-97cb-3567-a8ee-4a384511a225 | -3.72474 | -40.73783 | 2024-10-13 00:39:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9a6c01da-c451-345e-8e44-52422d16fe0d | -3.72291 | -40.72537 | 2024-10-13 00:39:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 66.7 |
| a7a49023-4467-3e0d-8c8a-9d3c9684aeec | -3.7211 | -40.71298 | 2024-10-13 00:39:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 1176d251-aed0-34df-8278-c01744e164a5 | -3.71254 | -40.7268 | 2024-10-13 00:39:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 41.2 |
| c28103fd-55a8-3762-8ae1-7e37c3887f4d | -3.71071 | -40.71442 | 2024-10-13 00:39:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 37ec38a7-5822-33bb-a1e5-dcdf86d472b2 | -3.44653 | -40.57882 | 2024-10-13 00:39:00 | TERRA_M-M | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f2629df2-1150-354c-983f-4f5370464c68 | -3.40961 | -43.35338 | 2024-10-13 00:39:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61bd4094-698e-39ff-bd88-8fcfeffe7ab5 | -3.40833 | -43.34424 | 2024-10-13 00:39:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a8b7c365-d467-30ef-b99c-bcd7bde48bf6 | -9.53158 | -47.63265 | 2024-10-13 00:39:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5595ea30-5b26-32ee-b6fe-9938ea225f8a | -9.52934 | -47.81056 | 2024-10-13 00:39:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1209dcf9-5ad4-339c-b1a7-b40cf1ff2479 | -9.51832 | -47.81206 | 2024-10-13 00:39:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 1805ba05-478f-3f77-bf51-1161002392e2 | -9.50913 | -47.82796 | 2024-10-13 00:39:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9f73863c-f3d7-367e-ae27-bceb99b77ff2 | -9.5073 | -47.81363 | 2024-10-13 00:39:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 729350b1-517d-368a-86ed-2273157adab9 | -9.44879 | -48.89977 | 2024-10-13 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7df1e8c9-d463-33d9-bdac-bbeea0faae92 | -9.44662 | -48.88223 | 2024-10-13 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 17370c5f-7d10-3fba-a737-8ecfc9ffd73f | -9.3055 | -49.64877 | 2024-10-13 00:39:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 020f1c54-9133-3617-9f40-45534862222a | -9.23022 | -46.68931 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 004dd137-9f9d-3593-8254-63580d0e7679 | -9.22874 | -46.68366 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| bd7d26c8-0512-3a1a-ad61-7bf776dc8510 | -9.22862 | -46.67744 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 26d50eab-1843-3e6e-9d00-17aa9243a63b | -9.16204 | -47.60775 | 2024-10-13 00:39:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f0bcd529-9785-3f97-95dc-c0be77af33d5 | -8.9656 | -49.034 | 2024-10-13 00:39:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7d337591-fd32-3e81-995a-5794a32b666a | -8.91274 | -47.91994 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ef8125ff-c720-31cf-bb3a-18ce4825b792 | -8.91089 | -47.90577 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f159a19f-2af6-3421-a4d8-941242461a18 | -8.86126 | -47.95568 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 67a16f0d-db6a-3102-90fe-9f8a124d3650 | -8.85024 | -47.95728 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bffa3ec5-3913-3b1b-a762-b339ccd3cdd1 | -8.84912 | -47.96307 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3636068d-f2fc-3098-b1d0-4a863a0d2fad | -8.84724 | -47.94884 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 22c74354-6f16-3dce-be54-5437fa0dc8e1 | -8.70093 | -46.62527 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| baaff010-3a44-3902-89f9-d33f5f40f683 | -8.69946 | -46.61398 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 248.9 |
| fbe84274-5daa-36cf-ba51-c1b515c4b577 | -8.69902 | -46.76771 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9903647f-a39d-348c-8550-27f91d4e947f | -8.69799 | -46.60274 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 302.0 |
| f509834a-2138-39cd-8a9f-836d350ac455 | -8.6965 | -46.59135 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d27a4f52-195a-33c4-b470-ea12fc800719 | -8.53025 | -47.2671 | 2024-10-13 00:39:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 794ce3b3-c15a-30d0-be32-ff1d0b15215f | -8.52985 | -48.77246 | 2024-10-13 00:39:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 14.2 |
| faf9d41b-3b11-30d8-a4c3-041fee22c472 | -7.97648 | -49.46141 | 2024-10-13 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 5e86bb47-d59a-3511-81bf-7ac87af41b08 | -7.70424 | -46.65478 | 2024-10-13 00:39:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 71e6951c-fe69-3a04-8441-bfe421ad4a84 | -7.68348 | -50.24775 | 2024-10-13 00:39:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e417247a-e75f-3cf2-8c99-e2e8b4935ccb | -7.67942 | -47.32218 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 01b21f74-6d07-30d4-9646-d1fdfd1e63a0 | -7.67781 | -47.3098 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 62af8fe4-1cb7-3744-b3de-fb5f6fc87efe | -7.66909 | -47.32358 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 4cd8531a-7e83-3252-8ad9-66943b13d8f3 | -7.66749 | -47.31124 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| f5a36aad-5410-34da-95e4-0a52c795e819 | -7.66056 | -47.31801 | 2024-10-13 00:39:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| f5c3f1a6-6551-3950-ba8e-a13f7421dbf8 | -7.60494 | -47.74667 | 2024-10-13 00:39:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4018784a-2fb0-345e-855a-76b07b0c1dfe | -7.57245 | -47.36763 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3680758a-0100-3dbe-8eec-2c80e7e8abe4 | -7.55823 | -46.2495 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0040a6e3-65f4-353a-b6b7-16bfa455e9ae | -7.52165 | -46.58971 | 2024-10-13 00:39:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a606e1d5-30e7-329c-bde3-a85d21465a20 | -7.49786 | -46.08775 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f2887ee3-5950-3faa-870d-aa261ddf796c | -7.49385 | -46.09416 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 39f25f8c-53fc-39d5-b9ac-adf0315d6f17 | -7.41061 | -45.69453 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6dfd5cf8-8c52-3643-98ed-7b0125e82840 | -7.40928 | -45.68474 | 2024-10-13 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f048ec7a-8c04-387d-b58a-802543359f3c | -7.39198 | -45.62694 | 2024-10-13 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d3ed3b3d-28a5-31ee-9d91-f5fb1cc4351e | -7.38494 | -47.25517 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 0e6a4cf9-645f-3ef2-a55a-f78208ba0e19 | -7.37724 | -47.26244 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5d8058a2-b690-3dc3-8711-1d58ed99a378 | -7.37561 | -47.25043 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| d7b132a5-9091-3982-9865-7d994c4c810f | -7.3747 | -47.25652 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 1942f96c-8cfa-3e0d-8771-71e953c02594 | -7.2756 | -44.97515 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b0fca741-3056-3e17-b81d-9b04eb0c5679 | -7.27433 | -44.96581 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README9.md)
