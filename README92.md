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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19338295-5037-35d4-869d-6d2b9c79cb62 | -4.5587 | -42.9523 | 2026-09-18 12:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 66d417c8-7343-315e-b68b-9cda1e49e392 | -10.6533 | -50.4991 | 2026-09-18 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 140267c0-81a7-3a3d-92ca-dfdfd427fda7 | 2.18431 | -50.88546 | 2026-09-18 12:21:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6ac05cc9-5af1-3ab1-b9ec-7b7539ce227f | -1.6133 | -55.56857 | 2026-09-18 12:23:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d4fa2727-f44a-3253-9a51-52d127a7f9fc | -4.4816 | -54.98164 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f09e326d-f160-31ab-a95d-751ea94de771 | -2.36235 | -55.2318 | 2026-09-18 12:23:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| adc584e8-2a0c-3047-8f9d-e8a50bdd97e5 | -4.38246 | -55.03114 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5483b2c0-1449-3b97-8089-97ccb4b11232 | -4.44243 | -55.51757 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 90ba19d4-9c2a-3065-b0e6-f6940b7b40d9 | -3.73398 | -54.64822 | 2026-09-18 12:23:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 735beb25-1322-39ee-b5cc-ea488514b6c9 | -2.69764 | -57.60046 | 2026-09-18 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f534056a-ccae-39b4-87cf-e623ed3869e1 | -1.65865 | -54.92521 | 2026-09-18 12:23:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2138cf1a-722b-34b7-ac78-36687c819439 | -3.27931 | -57.91888 | 2026-09-18 12:23:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3efbc3b1-0080-3c0c-a0f6-ed788fa2e313 | -0.79821 | -48.67248 | 2026-09-18 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 4ce9ce47-f505-3612-bf68-13c7ec11d38f | -3.70691 | -54.17701 | 2026-09-18 12:23:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 54aab631-4450-3104-b885-ac12207f718c | -4.50874 | -54.97114 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4845b0c2-7582-3862-9844-824be53c8225 | -2.90637 | -54.18346 | 2026-09-18 12:23:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7db1e4c0-caa9-3238-834f-a6bd78ecda45 | -3.48614 | -54.71706 | 2026-09-18 12:23:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7afb7d87-ae5a-33db-b9f7-d5ee49a8f71b | -0.80161 | -48.64779 | 2026-09-18 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d7a4fecf-7e14-3830-97e0-91098af56c37 | -3.73537 | -54.63812 | 2026-09-18 12:23:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| f10d3842-49dc-31e2-9bc7-a451bb47acb8 | -0.78607 | -47.54625 | 2026-09-18 12:23:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| b818fa92-46c1-3e84-b5e3-0a2eb6bd9a04 | -4.48298 | -54.97188 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 587546cd-0d1a-3718-84f3-52ddacd07985 | 1.28505 | -50.87003 | 2026-09-18 12:23:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d52d3e51-2ea5-3e8a-b677-a39a35b87bcc | -2.89684 | -54.18215 | 2026-09-18 12:23:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 4ca3486c-1d16-39e2-a661-eb2568f0e383 | 1.20076 | -50.76327 | 2026-09-18 12:23:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 173c4af0-e9aa-3418-8063-c1a0f4f71480 | 1.25819 | -50.75516 | 2026-09-18 12:23:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a136d6c7-46da-3475-a20d-f39b63f80fea | -3.92137 | -55.74671 | 2026-09-18 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 31395ea7-78f3-3f9e-9b5c-8c7fa2a38815 | -4.43337 | -55.51627 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ff61e1a0-c0bb-3f1e-9b5b-fa34c094a6b9 | 1.23636 | -50.92945 | 2026-09-18 12:23:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f322e858-679a-3403-9616-1a749081aa85 | -3.74335 | -54.64952 | 2026-09-18 12:23:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a332a363-bb4a-3ef6-ba58-5fd945fc712d | -3.13894 | -59.21522 | 2026-09-18 12:23:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3fa7b9de-ccd3-3db2-b1f6-308a68fbd408 | -3.21644 | -53.94234 | 2026-09-18 12:23:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fd2b5942-2519-3678-baff-644b8764ba29 | -4.42476 | -49.19379 | 2026-09-18 12:23:00 | TERRA_M-T | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 36403c05-fd59-3dff-bb51-bb4f07e19234 | -4.49172 | -55.4958 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 55287f47-8254-30a0-a4a9-99687494659a | 1.39457 | -50.91039 | 2026-09-18 12:23:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 36530d0f-1cd3-3801-b694-ccdbc5175acf | -4.13809 | -54.00813 | 2026-09-18 12:23:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b5fdb298-9e42-367f-b72a-cff75331db3d | -3.29558 | -54.82803 | 2026-09-18 12:23:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 34aaf29a-c6e7-3864-90bd-f1f02f1b32ba | -4.5528 | -54.92694 | 2026-09-18 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 01267a9c-d4f4-3e35-9ec9-596512ba3980 | -1.14822 | -54.16688 | 2026-09-18 12:23:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 89383ad2-f196-3663-b5b5-47a2d6c85cfa | -3.30379 | -57.87595 | 2026-09-18 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3a0a009-60fe-301f-a25d-8cc791dc342e | -3.26314 | -54.26723 | 2026-09-18 12:23:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c924a583-c437-345f-a7e0-68c0d53c8e1b | -0.7975 | -48.64173 | 2026-09-18 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 4d8368bf-0336-3447-addc-a07794867c5a | -0.79393 | -48.66639 | 2026-09-18 12:23:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0fefd430-0615-3c8c-9496-571bcc1705ad | -1.03439 | -53.73597 | 2026-09-18 12:23:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cabf25ba-9a4e-3be8-a0b9-9d85b02655a6 | -4.43207 | -55.52557 | 2026-09-18 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 38aa7f49-9673-332e-8a15-3696ede6b851 | -7.49787 | -55.01175 | 2026-09-18 12:25:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6ab69214-f605-3f52-bdbc-7c19d555f4aa | -4.88247 | -56.05787 | 2026-09-18 12:25:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3eef9894-b4f8-37cd-b15f-4492b6980700 | -5.73476 | -52.24374 | 2026-09-18 12:25:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 996db085-5dc5-3d64-b412-373462dbafbe | -6.54702 | -56.02376 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cd577235-5718-3394-b6e6-b993d0a8062e | -4.80978 | -56.12156 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d88852e6-9071-3289-9272-391462815845 | -8.31047 | -47.46653 | 2026-09-18 12:25:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 6cd4a969-c2b9-3bcf-ab8c-38e310a1427f | -4.71377 | -55.75267 | 2026-09-18 12:25:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 84a8282f-5349-3007-9de5-57a9c034516c | -4.51887 | -56.08427 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6d39bf90-a83e-342c-9b5b-8b21df08454f | -4.77636 | -55.70168 | 2026-09-18 12:25:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 74aaa863-3ebb-35ed-8a55-cb127a5bfa15 | -6.09879 | -57.68932 | 2026-09-18 12:25:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a914e8b6-9aa7-35d3-a11c-b5fe9d54fe24 | -8.15902 | -54.81282 | 2026-09-18 12:25:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ee23886e-28bb-3312-bd20-dfc9998550f5 | -6.10005 | -57.6805 | 2026-09-18 12:25:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd55cc7a-3c12-3c03-9431-122f2d047a42 | -4.80851 | -56.13061 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc73ce26-7e16-3b8f-bfc9-06a0b991c0b4 | -4.77509 | -55.71083 | 2026-09-18 12:25:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| fa03ee91-7afd-3500-99ca-6bb8783b8273 | -8.30716 | -47.51444 | 2026-09-18 12:25:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 9a0883f5-ad42-3fad-858f-56f99fad085b | -4.52016 | -56.07522 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2a0fe133-98aa-317b-abf6-436d4068e22b | -8.31178 | -47.47372 | 2026-09-18 12:25:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 295.8 |
| aac7a4d9-5258-3c64-bf0b-12278384cfdc | -7.8685 | -54.69875 | 2026-09-18 12:25:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d1ea5335-c251-3e79-b279-7bbd81958171 | -6.31801 | -55.27929 | 2026-09-18 12:25:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9a0e3e33-0729-3043-b492-93102cfebd0a | -8.30559 | -47.50718 | 2026-09-18 12:25:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d0ea80ca-6952-3e32-9623-6bd75ebb0aaa | -6.34342 | -55.83081 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ededca59-8980-39c5-b84f-9cae17e6694c | -4.79924 | -56.12291 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9b020202-52f0-380b-ac74-ef561557233d | -5.84474 | -52.10567 | 2026-09-18 12:25:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9d2bc77b-5e69-3423-b7aa-4cd43b183c07 | -4.80053 | -56.11384 | 2026-09-18 12:25:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| de44d00f-d928-302d-9ad1-aa919615ec7f | -8.16884 | -54.8141 | 2026-09-18 12:25:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6a8c4b6c-0f97-3320-90f7-9967ac3bb377 | -4.88119 | -56.0669 | 2026-09-18 12:25:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2a811330-d834-3fe8-b72f-eee74efd7203 | -8.90273 | -62.40547 | 2026-09-18 12:27:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 666117fc-0a96-3195-8847-d748f63c1323 | -10.69984 | -50.26108 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 18004f2d-1bcd-38f5-bf23-76baac0f2f56 | -11.07263 | -48.29416 | 2026-09-18 12:27:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 2e141ace-fe74-37fe-a390-42a2056d5101 | -9.71039 | -54.8237 | 2026-09-18 12:27:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 59918f11-29f7-3981-9b84-b265458e66cf | -11.91791 | -50.05326 | 2026-09-18 12:27:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 7b5bcc8d-b583-3516-89ad-cf107582ae40 | -10.82646 | -50.19348 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6b919365-1743-30a5-ae5b-d555bfeff0f2 | -10.62415 | -50.24015 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 9629ff35-41cd-3750-a0cb-98cde11e6345 | -10.65282 | -50.5144 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 10047a45-a8be-3f53-922b-04885f7c68ff | -10.58158 | -57.69208 | 2026-09-18 12:27:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a7ed8b3a-953e-3ecd-b2ee-4ccae5cdf0dc | -10.8305 | -50.17199 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1844bc36-19ab-3bcb-b94d-31ed5a4df4dc | -10.67328 | -50.4647 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 654d7375-36cc-3909-b2c5-6a560ada2c14 | -10.65889 | -50.49598 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f484a54b-a2fb-36b5-be4e-6caa1b8fc687 | -9.84389 | -48.41183 | 2026-09-18 12:27:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| f9aba626-b8af-3724-bfa7-d18185aca51d | -13.42898 | -51.88524 | 2026-09-18 12:27:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| cf3665bb-1c9a-3c9a-827d-35aedf41bbc1 | -9.83154 | -48.37368 | 2026-09-18 12:27:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b4c6a331-f9a7-35cc-9cb1-22bce2f25247 | -12.20649 | -52.85971 | 2026-09-18 12:27:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 661aa049-d70b-3837-b63a-7c9852152410 | -12.44238 | -54.99924 | 2026-09-18 12:27:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3ae17f28-4c79-3414-bf59-92e3e8635a78 | -10.82978 | -50.16617 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 21e7fbf7-afea-378a-a8e7-13cab407093f | -11.07731 | -48.25154 | 2026-09-18 12:27:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a248ea32-5f36-3ac3-9d7e-c7eb829ec731 | -10.62554 | -50.24566 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 9d8615eb-054f-3e2d-bd8b-6ce012083207 | -10.68524 | -50.25937 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b79fd74c-ef93-3add-a8f8-a263637143ea | -14.16289 | -48.74151 | 2026-09-18 12:27:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 48d5d921-1c6c-3d7c-ba56-9f59ad2f7277 | -9.69167 | -48.31221 | 2026-09-18 12:27:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| d2419bbb-cc6f-3359-8a99-2113822e7603 | -12.55763 | -50.70972 | 2026-09-18 12:27:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 01dc1a26-8638-3f4e-8a44-acb8fcfb0dcc | -9.71193 | -54.812 | 2026-09-18 12:27:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fbcf14d4-7240-3a69-82c6-5805e189944e | -9.72194 | -54.81337 | 2026-09-18 12:27:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 51e9220b-b292-3875-9444-7ce6ecf0b430 | -8.4968 | -57.62907 | 2026-09-18 12:27:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2da434c8-2802-3f50-aac9-743f4a3ba74b | -12.62952 | -50.88363 | 2026-09-18 12:27:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 2d30644e-312c-32cf-b9ea-23e4d74933a8 | -11.08038 | -48.25892 | 2026-09-18 12:27:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 32ecacd5-2231-390b-93ed-fd291101bccf | -12.21089 | -52.86686 | 2026-09-18 12:27:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |


[Clique aqui para ver as próximas entradas](README93.md)
