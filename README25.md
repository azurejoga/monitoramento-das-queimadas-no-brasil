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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40108042-0645-31a5-ba86-923b6854d3aa | -12.05334 | -46.46086 | 2026-08-19 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0afc21be-ef6f-3cfa-92bf-f478d8b6843a | -6.38532 | -51.74626 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4711623c-6be2-3970-a0e6-380ada59a985 | -11.3804 | -46.39336 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a8a8c23-42e6-3e3b-ba57-78e8095fada7 | -6.0181 | -50.20208 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2f63fa0-db1e-3a44-b556-2c18ee7344c5 | -6.34173 | -54.9178 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7650337b-4d44-3d68-b3db-616bbbb542e7 | -11.22301 | -55.08066 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2dfc78f8-204e-3719-b92a-b4276a29f97d | -8.57007 | -54.77485 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 20b78295-6812-334f-8be4-b82ed4dc58ab | -8.58275 | -54.73053 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f664646a-d525-3145-88a4-585366ee0b24 | -11.38113 | -46.3891 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a293f595-b914-30ea-b5ee-52a20f13ae86 | -8.57227 | -54.72795 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94143cfc-10bf-3d0d-adc7-e55b355784d4 | -7.21711 | -43.28926 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b0552f02-557b-3eb1-8606-2a818b43c3a8 | -8.21609 | -55.02319 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4708ce6-1155-319e-9f1a-07d0756753b7 | -13.43956 | -43.84249 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00623ebf-68a2-3759-9355-b90539844dfa | -8.10462 | -51.65681 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f2b1e2-219a-3c4e-8e03-4be17d6b94c9 | -7.55889 | -55.56548 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe2a153a-c1c1-34f2-b156-ae17c3af36e2 | -9.06885 | -50.81788 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70e96541-a598-349d-97f2-d0381c681e76 | -6.33886 | -54.89713 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6defb011-f73c-3a2d-b5b5-9cc4178b78a2 | -12.35701 | -51.20991 | 2026-08-19 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f5dcdb-3d82-3a66-9004-fe83446703d4 | -8.53609 | -54.73841 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f0dc091-32e6-3a56-8271-79c3e46b4e53 | -6.44916 | -52.7337 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da28e0c5-5adc-3564-8d3b-e1b4d46bdcd5 | -7.18994 | -43.45673 | 2026-08-19 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fcc73646-128a-35ce-8f17-22c24e75b746 | -7.18569 | -43.41848 | 2026-08-19 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05c309c1-426e-34a2-8c03-cff7622bf192 | -7.17949 | -43.41373 | 2026-08-19 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68b04402-964c-3f3f-bb9d-de99725ee7c3 | -7.94961 | -44.64108 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7ac218f-3c91-377d-80b5-75c1269ab23d | -9.72674 | -46.79243 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ed872cf-d97b-3a9a-a51f-4845a008825b | -8.21736 | -55.02758 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99563610-e858-3485-aa5f-046984c92d7c | -10.87885 | -57.12507 | 2026-08-19 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32a640e0-efe3-326e-942f-7de95676d620 | -8.21616 | -55.03365 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c1e9db4-f048-34cc-b650-30e063603fa0 | -8.54493 | -54.72807 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9e76937f-2e26-3660-b91a-d7153ee269f7 | -11.21867 | -54.01245 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6413ced-9bbd-3b33-9bcc-e30c0231a322 | -6.40477 | -46.63352 | 2026-08-19 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662ee9df-cdc9-3da7-8477-5c045a419d28 | -8.50251 | -54.85614 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 195f09d5-5a7f-3675-96a5-ee8dc904117e | -6.44668 | -52.74721 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ba91c06-8a09-3d51-9fe2-27c017571302 | -10.24132 | -46.99897 | 2026-08-19 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 672b8c83-8ab1-3b48-a057-baee32992f96 | -11.22522 | -55.06952 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b26842fa-fee3-39e3-b30b-e64ff8a84ccb | -8.55811 | -54.73056 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 706bb311-b96c-3afa-9bc2-24d8868cad0e | -11.05691 | -46.51775 | 2026-08-19 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 118c49d2-63d1-3b8a-94ed-96308dd34098 | -9.46072 | -51.61092 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dff1ff2-55e7-3d9e-b0e9-ea52779c3f6f | -8.35644 | -46.36168 | 2026-08-19 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86d7ccf8-366c-3097-b456-be596bce3afd | -8.08644 | -44.36088 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1de70acc-b33e-37e7-85d8-d96c3286f8a6 | -8.56026 | -54.71947 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0189fbce-5931-3e68-a045-473ca3573c77 | -11.47109 | -46.56317 | 2026-08-19 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81fe7a62-1d00-322d-897c-8ae10c8be2de | -11.1603 | -49.6247 | 2026-08-19 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 756555a9-af52-34a8-894e-c8ce292466cf | -12.24189 | -43.16081 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7d4b6d7-9c20-3bbf-8a7e-c9ae441d7047 | -8.55603 | -47.41184 | 2026-08-19 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e75161a5-29ae-3876-9e87-1295a7d42d9c | -6.34575 | -54.89841 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e00cfa48-329a-3848-93d1-0317d057fd96 | -9.90233 | -47.7371 | 2026-08-19 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dae50b59-1320-3270-a216-917e4e19287b | -9.08774 | -50.80107 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28195291-bab7-3b01-8207-ebb3d85b7325 | -6.35915 | -54.90112 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f36c9d90-0d88-3389-8cda-f02992502bab | -8.5284 | -54.74274 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd22a22c-5b06-3c0f-8c4f-d507df06b2a2 | -8.57456 | -54.75152 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c7eb16f-c567-3ba6-8b76-4a0aac91b835 | -13.43899 | -43.84606 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46dc07d2-4601-3f5f-83ce-afda1daff46b | -11.21956 | -54.00786 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e424d2e-f6a1-3b63-944a-57be20f43c7f | -12.78584 | -48.42423 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a2ee1fd-4455-39a9-8da5-9de77c8db4b3 | -11.1944 | -54.82619 | 2026-08-19 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ef0a72a-ff3b-3846-b011-84530ad3bec3 | -8.57564 | -54.74593 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29ab139e-22f9-3fa2-aa71-39ec3c2f599a | -8.57994 | -54.72359 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dea1f8a-3994-3498-b037-3b076144f16d | -8.21376 | -55.03538 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9d1354f-cb87-3def-b535-a6c860935ead | -7.64857 | -42.75854 | 2026-08-19 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84b4adc5-30c0-3bae-a233-dbb88c987745 | -7.53525 | -55.57481 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28c0418e-844f-3309-b226-6eef4959c81a | -6.66239 | -45.48477 | 2026-08-19 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c561b6b-ac31-365b-b138-7244f392591f | -9.08667 | -50.80695 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 046a00bc-8e6b-3b1a-ac23-a7f316f9ee69 | -8.56145 | -54.74863 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 816c7f86-005f-385d-8c1a-c9e1853831e7 | -12.23857 | -43.16027 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d55bbf20-c100-38e6-926f-60f327403ea4 | -8.57011 | -54.73915 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3bc7e7f6-019b-3554-bbf5-1db103891e3e | -9.72837 | -46.78272 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a08f3c60-a6aa-355b-a30a-92f37dd22fe6 | -11.20574 | -54.01446 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62254a57-5369-3e7f-9625-eafa7166e436 | -8.5788 | -54.72952 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c402a4-4452-3f0e-a80a-b064f0037a80 | -7.56329 | -55.56433 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa0e97ae-6fc8-3ceb-b0f9-cb1bc9b12e22 | -9.90297 | -47.73346 | 2026-08-19 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a597909f-3ccf-3c5d-9e0f-5c76c856ef25 | -11.12653 | -47.28559 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b3c3fac-2ad2-35f2-bb32-37e29a61abd1 | -8.09791 | -51.66257 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eea2c551-8be6-3b25-9169-db48e2dd929f | -9.08109 | -50.80864 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5567dee9-a19f-35f9-b2c5-87496299830a | -10.10997 | -54.28712 | 2026-08-19 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11dde031-32f5-3a10-8d99-ca126eba90ec | -13.44232 | -43.84661 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d10f9dd3-5c1c-3361-b944-9c255e3e4b01 | -9.06061 | -50.83403 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0551b36b-41b3-3169-af97-7bde2093b6c3 | -8.56905 | -54.74464 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7249fb81-3fb4-33b4-ad00-936bfc61ec50 | -11.23069 | -55.07767 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c9510cf-0f2d-3024-b5b4-4986fa33eaad | -6.44477 | -52.72364 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60d51882-49d9-35e7-bcbb-6cd5cc9617ad | -8.17964 | -44.4317 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ebae5fe0-bae9-3f4b-8296-9dd490f5c20d | -8.5734 | -54.72211 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c8d212b-60ac-3235-8f26-2f30053a9685 | -9.73186 | -46.83727 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15173714-2ed3-3b32-9bbc-38adf5d142af | -7.29108 | -44.07757 | 2026-08-19 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bcbc27e7-3f2b-3fa1-8d23-18a5b98a3583 | -6.81089 | -43.20924 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0275278-05e7-3267-a57e-fe1cce1ba736 | -6.35148 | -54.90596 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6302536-0665-3e2e-b439-452a83df9056 | -8.57668 | -54.74054 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea0ecf45-5e3d-3a3b-834d-b0f4684aed9e | -6.35795 | -54.90748 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6ee1cc4-792f-38f2-9c0a-38617581c782 | -8.35559 | -45.97484 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3a13e4e-6a92-3478-8bb5-43c637ddd6d8 | -12.75819 | -48.43749 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f84cdefc-60d0-3ab4-9db7-058ff0d902b2 | -6.0196 | -50.19892 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9a87dc0-4a76-3f3d-9fc5-df78badc5f9a | -11.69023 | -54.56094 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 66161ef6-d20f-3605-85c0-baf5674e203e | -9.81479 | -46.63281 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b8b7c72-1797-3cf0-820c-f8f3c4e2eb07 | -11.23911 | -55.06686 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f0f0a5-212a-34f8-b4f0-131223c28e3d | -12.37337 | -46.44503 | 2026-08-19 04:19:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27268cd3-8b6f-3ed0-b983-858af772e97a | -8.50368 | -54.86918 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d7698ef-11ac-39c3-9235-e919d8bd69d2 | -6.34457 | -54.90482 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 362c2e2f-d552-36d8-8ed0-40f1afb79f57 | -7.2149 | -43.28148 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66ac1025-bbfc-37cd-9627-99e1a6b1f82b | -9.2681 | -45.64787 | 2026-08-19 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8700cb0-3abc-3b7b-8ed5-cdbd42b35a6b | -11.23271 | -55.06543 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffa78b98-3c4a-3fc5-b553-30a362a9bda6 | -6.44834 | -52.73817 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README26.md)
