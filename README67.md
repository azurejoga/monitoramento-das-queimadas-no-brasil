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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e30b7051-9e87-35e6-8fcb-a24805a075ac | -7.20006 | -45.35283 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d9d455c8-37b2-3a19-98f4-edf22b3b6c77 | -3.27035 | -50.40431 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54f98e96-264c-3da0-9084-39e1c6c8f34f | -5.76861 | -42.05216 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ba1c88cc-e2b0-3e8f-8ccc-c1af55219159 | -3.2094 | -50.55616 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e78dc161-0faf-3626-97b4-80a26ec8005a | -5.26118 | -45.4081 | 2026-10-08 04:02:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74f446f7-3209-32cb-adad-5d99eae7c99c | -4.40275 | -42.12379 | 2026-10-08 04:02:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9131663a-637c-3359-844b-3d763a9c68c3 | -10.96313 | -45.39866 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f468edb4-3280-3de0-95d6-522328eb9008 | -4.83671 | -45.80107 | 2026-10-08 04:02:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce43860-607d-3c70-97a2-8eb286c3d56f | -5.50922 | -42.83858 | 2026-10-08 04:02:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 480423ed-c945-3318-a0a9-4640773ff439 | -3.4655 | -50.08762 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bde248fa-a6db-38fc-ba48-3d4d7e417841 | -6.8906 | -43.68533 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23408b48-ea05-3d28-93fd-3df8b42ec324 | -6.13182 | -47.93766 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22f024ce-e617-3e3d-9964-87b35f7bd2e3 | -3.86272 | -50.41518 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 53e5e61d-7341-3beb-a1a2-dcd98c247709 | -4.35027 | -43.79131 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2446c6c7-913e-3529-9cc9-95cd8c28af06 | -7.86043 | -45.40004 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c91e31cb-afc6-3c13-a338-c6d8990ae4ea | -3.32181 | -50.18602 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4f0e4eff-478d-351c-98fa-4ec8d534862d | -4.15246 | -47.98953 | 2026-10-08 04:02:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e1da6e2-8e1d-3971-981f-bf6fa76c6f26 | -8.2147 | -46.37149 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d3039c0d-04f0-3fa2-bcc3-102ce0f3df28 | -6.15814 | -39.43188 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c27dbec1-e646-399e-842e-1aadccb13f4b | -9.91292 | -44.79449 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24ca04ba-033c-3628-b37d-865b60f5c37c | -7.46832 | -42.84484 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b5e02484-ac5d-3916-aced-ecdc412cea7c | -6.6215 | -37.88332 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5cf73b17-1b7a-3065-8cce-70afd976c39e | -6.1427 | -47.93945 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7380411-3ca1-30b0-8f86-baf0155c3807 | -6.59076 | -41.54795 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f956c3b-cd35-30d9-b25d-33395e331ac4 | -7.21825 | -44.15875 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd08814b-30d0-3787-89d7-c0a49bf711be | -5.73169 | -45.15398 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 00963d63-9eb5-352f-ab7e-d596fb3da290 | -7.77178 | -43.80732 | 2026-10-08 04:02:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fd36cc73-c614-383d-8ccc-718567fa44a0 | -4.34987 | -43.79389 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 8030b65a-fa8d-3a44-8e2f-625a108566f8 | -8.21993 | -46.34169 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee04b64b-7796-3c19-a713-a1d45c288932 | -5.48636 | -42.85526 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 81b45310-6cd9-35a0-8065-0b5dc1595db4 | -11.09879 | -44.00843 | 2026-10-08 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eee15f5c-ce40-37bf-91c1-f5e4ffcc3f5d | -5.23613 | -38.54638 | 2026-10-08 04:02:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2592d45-008c-3a8e-84ff-a4b282ed3279 | -10.94767 | -40.29367 | 2026-10-08 04:02:00 | NOAA-20 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c9a850e6-67be-36b1-afd8-e8c21d939a06 | -8.7255 | -45.15453 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e7997d23-3e00-3a4e-a6f2-f4acb6e81dfe | -6.82818 | -39.5571 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53ab1003-0a86-370a-bcec-e928954f9a7f | -8.98148 | -45.91901 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 531ae394-b01c-32ab-ab89-a08858fe6117 | -9.94736 | -43.49725 | 2026-10-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01f97278-e476-3265-b509-5b7733d709f9 | -3.16352 | -50.60405 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8d21138d-b691-3cab-a8ea-f769760ed224 | -5.98766 | -40.93845 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3d60da8b-2673-3cd0-8814-aa8c1159f38a | -2.78273 | -51.68427 | 2026-10-08 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eec77a2a-2993-38a2-8ab5-4c095f56d90e | -7.31437 | -43.99271 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3bce591-9232-37bd-b482-c3cd3f4de66e | -8.72187 | -45.17532 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6668cfd0-4fe5-3d6b-8918-eaeb141cb6d0 | -9.76698 | -44.78828 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a4c1ae0-d7f9-3ea8-8f8c-f878c4c5759c | -7.06293 | -40.94597 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ac06908-c2d1-3146-9045-593081b1c0e5 | -6.13971 | -47.92435 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2ef0978b-e710-3e1a-bdad-e9794b49fc83 | -9.40048 | -49.00885 | 2026-10-08 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b7ae140-6417-358e-8e2c-b7da33d03a9e | -7.25891 | -45.34559 | 2026-10-08 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ed0ab47-566f-3c34-bba6-cf3629a315a4 | -8.22281 | -46.353 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 995941ad-8638-3332-92d6-1821a7906d58 | -7.46294 | -42.85358 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0153d68c-1fff-33c1-986f-eed3f0d03416 | -7.09816 | -41.74514 | 2026-10-08 04:02:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d76f49d4-0b88-3bba-ac48-050dd477049e | -11.64864 | -43.68042 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3a5e8b4-abcd-39a2-8515-f8ddeac86b39 | -8.36928 | -44.75663 | 2026-10-08 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40fe8148-e467-3ab1-9ab0-ae3276940e3e | -6.31763 | -43.3428 | 2026-10-08 04:02:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11a7497b-546a-39c4-8519-84b3ef379469 | -3.84833 | -51.93832 | 2026-10-08 04:02:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb70faa4-c2aa-3271-b895-87b4bddee566 | -3.19648 | -50.57302 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44a4884f-36c5-38c2-87de-69d1568fe489 | -3.34673 | -50.47763 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5107ffd5-5691-3616-b537-4141093b1445 | -6.88476 | -43.69527 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 9da03abe-6982-3951-805c-718be01c553e | -4.34919 | -43.79786 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 52408d51-2703-3318-8628-0124f9e03c30 | -5.72086 | -41.63725 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6829395e-3873-3dac-b1be-e726bad191d5 | -6.98937 | -40.03523 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ddb5d617-8601-3dd2-9e27-21fee10b664c | -7.30908 | -43.99917 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff2540e8-1ace-35c8-a786-0f2ed075daff | -9.26379 | -45.64133 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ade6b19-a8c8-348f-8938-0c537e8a083a | -4.80827 | -42.74895 | 2026-10-08 04:02:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ef3e88c-cf5a-324b-8916-5f36b6bd68df | -4.85933 | -42.99843 | 2026-10-08 04:02:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec12812d-1406-3612-b8ce-908603c0bde8 | -6.62482 | -37.88386 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3aa2773-669c-3648-9772-a15aaf0f9f43 | -6.32781 | -43.35519 | 2026-10-08 04:02:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a7c4b4d-2602-3b17-b444-6d5604abfc8f | -3.19183 | -50.55983 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c13feb00-46f7-38ee-9917-41b1856c5e7b | -5.11424 | -47.11742 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 466878bf-e1a3-35cd-80f6-5280ff35a856 | -7.18211 | -52.62667 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6e3c4a0-3205-3c94-a401-4533a6ca7f9e | -5.77232 | -42.05278 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d0f7ff5c-df0e-3364-8f70-6cdf0f82f2ad | -3.16228 | -50.45145 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4dfa944c-f4c8-3710-83ad-a3433dfd486b | -6.15701 | -39.43891 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 516263c5-94e1-384c-ac4a-df446a75608b | -3.94557 | -49.01797 | 2026-10-08 04:02:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e52ef504-22a4-337f-a7b4-ab35d4c9453c | -11.26099 | -45.18624 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff4e10d8-dc0a-3afd-9d3d-62fd85988ed2 | -6.05427 | -44.03164 | 2026-10-08 04:02:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8152d2f3-29fc-3e1a-ab98-beecc06b270c | -5.39216 | -42.96148 | 2026-10-08 04:02:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 78bf52f3-09ba-3eff-b104-9c9dff07b125 | -10.28884 | -47.99572 | 2026-10-08 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e15d9236-9dd7-37f4-b3d9-06d07677ee2b | -5.96507 | -40.92288 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bbecaec8-1105-3bf6-9f62-f80bcee296a9 | -7.18011 | -52.61909 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a3f32581-3acd-3542-94ae-e03fee81d6f1 | -11.73674 | -43.64244 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 87d1af01-b171-3f3c-911a-bbcb6583a5a4 | -6.82319 | -39.54555 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 67f68e40-c822-3709-ac8f-ab230f5d6f74 | -6.83206 | -39.55417 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f5d1df3-1db0-3ac9-8119-d8586c3ebf57 | -8.99282 | -46.75916 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfaf848-48ab-310f-9307-1a00e2570266 | -7.34986 | -44.37305 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2e4ced6-cd85-3793-8f75-9d33b08b6cca | -6.14464 | -47.93571 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b6cd88f9-4eb7-3b03-80a3-559286eecaee | -11.6259 | -41.83446 | 2026-10-08 04:02:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9642ff3c-e696-348b-bcb4-d1595a8cdf71 | -3.18307 | -50.57071 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 461a9338-80ab-31b8-8056-c728aaa5b92f | -11.09494 | -44.00773 | 2026-10-08 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eec10b21-39e1-3940-87d9-d20d4e614cb0 | -5.96094 | -40.92619 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d98f0dcf-f0b2-33b9-ade6-729a90f97ff3 | -5.12062 | -47.11176 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f6be80a-835e-3444-bc1a-c32fb60d3006 | -5.748 | -41.67635 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1434487b-9327-34f4-a787-656e841fcea0 | -5.97853 | -41.37111 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 633aa355-381d-3dbe-a4f8-6cec3184507a | -5.73041 | -41.76106 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68649866-2cef-3bec-8e7c-c9528ed8918a | -7.82461 | -44.1847 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f28709b7-2a55-3695-8020-e2821857dfe8 | -8.7182 | -45.19625 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d080c562-4122-3787-9801-0ad4c4ca3581 | -5.75826 | -42.06863 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 341dbaa5-5c58-3a4c-90b9-3a3eff84de86 | -6.053 | -44.03181 | 2026-10-08 04:02:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24ad3af6-805c-392f-af6a-a6cf112f970b | -6.95755 | -45.26182 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cde1ef8-1be9-31fb-bd99-f04dcfd5fa32 | -3.20835 | -50.56213 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e888e855-bb76-3a3a-b3b6-02940f9b41db | -6.94489 | -45.2816 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README68.md)
