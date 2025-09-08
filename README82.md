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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74a9b049-2da0-3ac0-b04a-3a68a1fcd21c | -11.61788 | -47.14816 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 517b6ab3-b06e-3d56-a1b1-e07940afe773 | -6.82111 | -52.79594 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e33ed3b4-3b3d-3d0d-a495-b6a1cb50c064 | -9.20202 | -46.04203 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ec00976-a89f-31ea-bf38-da934bae71cc | -9.846 | -48.8545 | 2025-09-08 05:21:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3d01b9b-7076-3fe3-9d92-f80720a0be8f | -6.87659 | -47.91102 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c0a4ed9a-70e4-3fee-b19e-9e5e76543667 | -10.1415 | -46.21795 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa7bc350-e3e8-34eb-84ad-7aa208736ca3 | -10.77361 | -59.85238 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee0a61e5-0908-383a-a6f9-ea77746638b5 | -8.60473 | -54.69076 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36dca853-4e6c-3f17-9179-fdf42a2bd411 | -11.41325 | -50.37709 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97a05fdc-5e9b-336b-a116-b9219df9c618 | -10.50516 | -57.79981 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b606edc-bb61-34d5-9683-0d6e160aeb11 | -7.90636 | -61.78213 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac5f15fb-36b2-3f8b-8fec-8dc2d3684db7 | -10.15456 | -61.14379 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7012e04-7581-30af-b232-46bd9892fcca | -9.88247 | -46.53328 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 436004dc-76da-3674-a596-c23e5c6acc19 | -11.81359 | -61.53548 | 2025-09-08 05:21:00 | NPP-375D | SÃO FELIPE D'OESTE | RONDÔNIA | Brasil | 1101484 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cdd4b6e-c1ca-3f90-ab3e-1d9d1a804840 | -11.40958 | -50.36176 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87e83acb-b668-3dcb-b8bd-f95861be1033 | -13.81279 | -46.2752 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 818bade4-2c35-3019-86ec-26af34b45ad7 | -9.96408 | -55.03492 | 2025-09-08 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a47bd8-ae52-3f7c-a488-424bc84503f2 | -9.62512 | -64.20515 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 551a1a29-73f1-3cfc-8330-c16259524f60 | -12.89589 | -47.99905 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30c2ed9b-87fd-3bfd-a2a7-3191c6be3911 | -8.88607 | -51.05692 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e7b01a9-bcc6-32f5-b9e6-7a0c47c31558 | -6.17138 | -51.51942 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 271a604e-92f9-3f25-96e0-8fce3efe1b5a | -13.82199 | -46.24666 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d20a45e0-2f37-3c34-93a3-0133e602610e | -10.42732 | -59.60608 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb92e2b7-d338-3768-870f-95c38adc88ab | -7.90284 | -61.78154 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af9c93fd-62f7-3c84-afa8-bb87e1785b35 | -6.27676 | -53.41813 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b21d64b-9ca7-3191-aa4b-a5091bccdd62 | -6.95398 | -62.92605 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92b79f74-aa9b-3059-8d47-d76b9660af01 | -9.7074 | -57.79289 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78bbe947-38d4-354e-8416-f6719921521c | -12.93957 | -54.78289 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a21e60f0-793e-3ce6-aabb-19e057fdcdf8 | -11.62465 | -47.14912 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efdcac9b-0333-3b2e-8332-7748ba8ecbfa | -11.31995 | -55.11616 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3471b678-d119-3391-b925-2f66234735b7 | -9.82045 | -47.77068 | 2025-09-08 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56042942-f1b6-3d7a-be80-cede15f80479 | -11.40911 | -50.36541 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70f89064-0b79-3366-a64c-8bfa4e4d8abd | -12.19532 | -53.913 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c25fce12-6bc0-3309-abd8-01f6a736b45e | -13.74253 | -46.9027 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63418d56-edb1-381a-bd3b-d12a5d2abc22 | -9.16889 | -59.37275 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f2e8b16-b161-3a65-9390-bd1429d1ad41 | -7.39216 | -61.63702 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e08cf82b-e8c7-335b-8fd9-87ad6ae938cb | -5.97264 | -53.59483 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b44ed196-9b20-3dfd-9d19-e737dd2df6db | -7.12282 | -63.07219 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0f95158-599e-3a2c-917c-6c64b86dacfd | -6.62676 | -53.35389 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6792b8b-0bc1-3686-8436-f5a4248ec080 | -10.21538 | -50.5219 | 2025-09-08 05:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d22ffce4-e926-3fe6-bfd2-2af64244fca8 | -13.81046 | -46.28585 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0bfd20b-3471-3c38-b496-ee77047cb405 | -13.64412 | -47.91682 | 2025-09-08 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb073e40-848b-36fa-af50-e4a5a569cd31 | -8.88553 | -64.21735 | 2025-09-08 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41d71e96-3a04-303d-b86f-a44088f5185f | -9.94507 | -60.14727 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae5e18e1-7d48-300c-89bc-e8fe06c41c61 | -8.70291 | -45.30524 | 2025-09-08 05:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b717dcc3-fd86-3f6f-9485-c05aa1f06d4f | -5.97212 | -53.59843 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a190ec-13c8-3b4a-a5d8-2fa780816371 | -10.58377 | -61.23244 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 746769b0-fe84-35ef-b60c-0903d911f14a | -9.85361 | -48.84218 | 2025-09-08 05:21:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28d84cfb-4adf-31a8-a3cd-ca415d70172f | -9.66483 | -67.74657 | 2025-09-08 05:21:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc46460c-b97f-3a9f-b837-e246b36a0c85 | -9.20819 | -46.04992 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 00dcfc66-de12-39c4-837a-ab8ca5f7711c | -8.92726 | -45.81071 | 2025-09-08 05:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c66f587-6cae-39f8-b1f0-4541501c2507 | -9.58024 | -48.29454 | 2025-09-08 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2341ce64-8f96-39d6-a6e7-7569371a7265 | -10.88678 | -55.71373 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e1df96d-ef6a-3e6f-be1f-dbd743e2a0d8 | -7.42521 | -49.26302 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49d60f83-ef13-37ef-83a2-e31b5e468e1c | -11.19883 | -55.00794 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc67282f-3935-3b29-b4db-96a4bf23f6af | -9.48128 | -60.48885 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc2ae503-5112-3b89-9f29-c206c3171876 | -5.76779 | -56.5173 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 336d73d5-bbf6-3654-8cbe-f80b6a6db327 | -11.22403 | -55.00436 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ab9fc69-2bfc-3e3e-b7cf-89e5108b7653 | -6.82488 | -52.80072 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6604153-040d-3648-be53-6b4a502c8ace | -12.89477 | -47.99479 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ca97f4c-d325-3e83-b281-868faadbceb8 | -12.94113 | -54.80274 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2241f186-e2e4-3d3f-b19c-ca2296531444 | -7.47156 | -61.59369 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f569b5-aaeb-3118-8c32-814a2c66d9af | -10.89062 | -55.71428 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3359746d-0394-3f75-af90-69307afbb6aa | -9.81703 | -53.32197 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9f7abb6-77ae-325a-81e1-b9acc9e043e9 | -7.2295 | -46.21161 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f8de52c-2a27-31b4-bc8a-99e8c57bafe2 | -9.96688 | -51.1961 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa559c1-8b3d-31e7-bdf5-5bca44bab35a | -9.86875 | -46.58588 | 2025-09-08 05:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ff51cb3-244d-3a36-8a49-900b740b5792 | -13.80597 | -46.26958 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5f626b7-f1df-3caa-8421-09c2328be4a8 | -11.90807 | -50.98239 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5753d54-bae5-3fba-8547-d0528df6586a | -9.17111 | -59.38027 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac372c1f-4bd3-3342-9ddc-5bcdb842391d | -9.63053 | -63.10147 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed506ec1-8fdf-3e24-b4ae-cc7ee3cee073 | -13.2922 | -51.73958 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd18c85c-e582-3a28-bce7-149affdb90b1 | -6.62618 | -53.35774 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec8a799c-024d-37b6-8145-81c8221c0832 | -10.46174 | -53.63109 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc5b9b54-8678-3ebe-8ac7-89c6988dcb9e | -8.69617 | -45.309 | 2025-09-08 05:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c175f4a3-86b7-3473-894b-8fe5f867ae7d | -9.44516 | -61.8223 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7c6d15cd-7aac-313b-8e66-514c99b393c3 | -11.65643 | -46.8822 | 2025-09-08 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa31d44c-4fbf-328f-8957-46afc8a22e2c | -10.14016 | -46.19565 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f4283e1-2263-33ad-bf71-c2e5e315c400 | -12.93485 | -54.78612 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5cc82b7-2c56-3766-9a53-81c8bbc29c85 | -9.2777 | -60.9086 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a977ab20-f6b6-3fa0-bfc9-25d1aa3ee580 | -7.40334 | -61.63483 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 369cb1f1-7d6f-3fb8-8f1b-c07dba6288df | -6.28093 | -53.41875 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6d7711d-dc8a-3036-8ed8-3159872f92a0 | -11.20939 | -55.02045 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91b0a227-0a51-3837-990b-ef6b7d4c160e | -9.50703 | -57.78157 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 485b3121-b02f-3b60-93c1-8c049237fb82 | -6.86333 | -47.91733 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5348bec-bbab-3678-88fe-22d9a429daf3 | -8.09097 | -54.76167 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8be0b4fa-b304-381f-a444-79ad82594364 | -6.62446 | -53.36929 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad5caf2-cbd8-3578-a785-3d490d0a1027 | -13.81471 | -46.25587 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdd4c51a-31cc-3709-993e-436f1306d589 | -6.95021 | -62.92541 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d954b50b-0541-366e-8ade-9ed9358cbdcc | -10.29263 | -48.80996 | 2025-09-08 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1de6c8a7-1fc1-3661-9bad-49bbb9bf5e54 | -10.46212 | -53.62891 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f90bd3c1-4a10-3cce-a7f6-fd673bd47deb | -13.73058 | -46.90018 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9416f0d5-7c1c-31c2-9229-a7ff6411fe10 | -13.73633 | -46.89351 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77a92a93-31e6-3e52-b4f6-c55c841e17f5 | -9.37255 | -65.93842 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40e6d455-cef3-30fd-9b7b-a8618e06b4d6 | -6.20407 | -53.27298 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f0f5c8-3bc1-3798-b18e-327bcd12b683 | -10.50861 | -57.80035 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1b6d34e-b760-3d43-80cc-a9ab4b7b77a5 | -9.47622 | -60.49897 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a7f54dd-f176-3613-84b4-ea0f11b6d716 | -9.96097 | -51.20142 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a19962db-3a8c-389c-99ee-d3a23130d943 | -10.51265 | -57.80846 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c90d6dd4-d2b3-3c7e-a617-9849e89ca130 | -9.07689 | -46.98652 | 2025-09-08 05:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README83.md)
