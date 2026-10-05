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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a3d91c7-9c1a-3234-96fd-fda187dd0abd | -3.253 | -57.87892 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4bbac99f-4ff6-3d20-bfed-2ff22008d04e | -3.01233 | -57.75306 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3586ed8a-4770-3b65-a9ff-c7272cca5e11 | -4.10403 | -58.77015 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96f61df7-dc17-3a98-b1c4-cb22b5f477de | -2.98436 | -54.03277 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 84c325f0-a0ff-302f-a761-d047e05da1b5 | -3.51457 | -54.60863 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7e566e92-e3c0-3730-b42e-7c8ca2d65fd9 | -11.37667 | -47.6288 | 2026-10-05 17:34:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b181a507-5123-3a12-beaa-1ba99ab7f1c8 | -2.93986 | -54.10592 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d025dea5-5ba6-37c9-b034-2bfa941c35d3 | -3.28529 | -54.18335 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c442d5a5-dfd6-3a9b-b543-d4354823f2f3 | -3.51897 | -59.56148 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c06ada72-5149-3698-b8e7-0345d2aa65d9 | -3.69502 | -55.96227 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a9715ae2-28b3-3261-9171-92592bb0d8db | -4.13428 | -59.8974 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 33d2b6d4-aef6-32e0-bd9f-910f9cc9a1d7 | -3.79353 | -59.31976 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 451bff97-0aae-30fa-af46-f2e6304bf0cc | -4.11945 | -54.41829 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 715b90ec-af79-39ec-82e1-aff2c048bf55 | -3.21578 | -57.87622 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 018ca460-9af4-327d-a2ec-10f8fa63d0d8 | -4.00345 | -55.67871 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 5a8f4470-c455-3d94-9099-d047e3281bc5 | -3.82265 | -55.61674 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e962d839-79a6-3dcc-844a-f9a2c1b1fe45 | -3.06355 | -54.17064 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7b2887ed-988c-3184-bd95-8b46ce9572b3 | -3.87921 | -55.81137 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f17bbdf-772f-31e6-b3c9-0af01849c5cc | -7.58509 | -46.08046 | 2026-10-05 17:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fa082531-ef2d-3cec-9d64-57f9cd041612 | -3.61305 | -54.60337 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0c399f6b-c2c0-3d43-b420-697b0b3cbbd3 | -10.95746 | -60.90492 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae4f1562-09b1-34ab-ab1e-225822c06722 | -2.98404 | -54.78417 | 2026-10-05 17:34:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 89a59c17-1b4f-3910-82d0-14e07f35d0ec | -3.37441 | -58.1909 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7660b578-6611-3938-8178-fce3c2571c15 | -3.64965 | -60.92282 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad99e388-76c3-31f1-bc71-8942a83409bd | -8.23454 | -73.117 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 841544de-ec22-30aa-b8ec-6034fe4d55df | -3.06733 | -54.16525 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 48e7a1c6-c5af-3835-a95c-9f9194f1080e | -14.3051 | -57.4684 | 2026-10-05 17:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce3e43d4-504b-337c-9a5c-db53a379e0c6 | -3.17224 | -58.63594 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d82ff8fa-6714-38bd-914f-dfc79c24db3c | -6.18049 | -55.35056 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29daa15b-890e-3519-a921-b12f98af7403 | -2.80608 | -54.0921 | 2026-10-05 17:34:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b177b06c-2e70-3b71-ab2e-9e171bf33833 | -3.6259 | -58.22517 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89c3bd07-35d3-3545-90e4-bbd622270bcb | -3.54551 | -59.48805 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e9accfd2-525a-31df-aca4-caa222921769 | -2.90473 | -54.12103 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 72e9416a-42d6-34ce-a462-0a4e0a3f6cb9 | -1.86263 | -50.59936 | 2026-10-05 17:34:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cf4cf6c-4ab0-3207-b4e1-3f22ee5577c8 | -3.63304 | -59.64169 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8dbc263-88cd-3eb4-af34-343beb047b6d | -3.4785 | -55.42707 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| dc0da0f2-d775-30a8-a067-ae80420e6f2f | -3.67593 | -60.53814 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f6a381dc-4ef3-32f8-bef9-ba7574a534a3 | -2.93935 | -54.13099 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 682dc2cb-89d8-3952-b71f-c0c6cfa24eb6 | -3.28088 | -54.17626 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 382f91b8-5d27-335f-a8e0-283a764d912d | -3.07219 | -54.1722 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 80956149-a3e4-391c-8d49-a90ae11d7504 | -3.05306 | -57.4199 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 432f26b1-1148-3a03-869a-98d90873073e | -2.78852 | -56.49371 | 2026-10-05 17:34:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f44b7e1-19de-3e6d-8f43-7f22bf62f92a | -4.18059 | -59.40271 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6416c6d9-d5ab-3c2c-962f-774457b6361f | -2.67553 | -49.03041 | 2026-10-05 17:34:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 33d6ffd2-6e55-31cc-b0c3-7eb343424a83 | -4.13149 | -59.9014 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| dfb17596-be4a-3f65-ae35-7772e5a1c701 | -13.52054 | -61.11284 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 135.7 |
| dd13ed62-567d-367d-a3fe-dff66197b3ca | -3.67918 | -60.62575 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d07dba78-3a65-36db-9e72-dd2e57dc8b93 | -6.83064 | -58.59125 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a3631fb8-e9e0-36db-aa84-61c5d29f47f0 | -3.28617 | -54.18016 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b8f14d9c-1425-3bb0-81bc-d5cef5e570c5 | -2.80533 | -54.08739 | 2026-10-05 17:34:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5e26f8e8-67ad-35e2-9396-7ef1d1544b37 | -3.90712 | -58.67777 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25129088-6277-3f72-a737-af8d0797d3af | -2.94353 | -54.12917 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 254b7b03-e218-3896-add8-f28d69f259fb | -3.51526 | -54.6129 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3ce6b4ba-99a8-3e95-b19f-638a4be0548e | -3.84355 | -59.55362 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14f05c85-47c9-32ce-86d2-54731f34cb92 | -8.19604 | -70.15771 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f787b9f8-c504-37e6-adb4-cbbd6e0343f6 | -8.78533 | -72.80721 | 2026-10-05 17:34:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d07cd4ab-145a-377f-89d9-ff7fae733c29 | -7.40961 | -70.11074 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e2f31432-9c53-3590-8370-36e603d84d30 | -8.03501 | -72.30784 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c48cf2dc-660d-3081-a102-281b63d7031a | -13.51523 | -61.12585 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f00d39bc-4c70-311f-a872-e684af72b802 | -3.65404 | -60.26226 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| adcf770c-3eeb-335d-9169-9cd8c6564510 | -12.43372 | -51.32922 | 2026-10-05 17:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 72532be3-9a61-35af-942d-a2838e11d2d0 | -3.37502 | -58.19488 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| a44bbe39-bdae-3edc-b700-e597a38b298a | -3.17165 | -58.63211 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c66fb683-5e3e-3544-9c7e-5ff98009236e | -13.52461 | -61.1163 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 37de6fa2-1544-3a61-98ce-4328992d0b83 | -9.51295 | -46.81641 | 2026-10-05 17:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d0cf86e2-5a4b-35db-a736-bba02a680e64 | -3.378 | -54.10999 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e643689-a119-3d58-b5b5-afff543c9236 | -12.02881 | -62.54061 | 2026-10-05 17:34:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 0119415e-6c44-3b16-8b8d-47b605dc9bef | -3.46286 | -54.59485 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9b655ae9-2cbb-303c-9134-d9f5b880008c | -3.09081 | -54.16626 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 7e7b8675-9e69-3c0a-bc2a-9d18fe6448f4 | -3.0674 | -58.40623 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8c8548d-bfad-3359-b36a-eb4b25281d02 | -3.67646 | -60.54159 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 439ec10c-35d6-3a60-b072-2fa1fce1f39b | -3.54888 | -59.48753 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d1244f03-2c27-36a3-9cbd-16b7144421d3 | -4.07104 | -55.76579 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3020991a-8ae6-39f0-b1be-b8c5c6c51538 | -6.20633 | -55.2727 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c53f4f4d-e476-3a91-af50-bd31504be457 | -2.48682 | -49.40671 | 2026-10-05 17:34:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 82c9b51c-40aa-3ea5-ad29-dbde9bf107f3 | -2.92821 | -54.15069 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 669e28c0-4ad0-3958-9463-82b3c94d5866 | -10.19152 | -52.56025 | 2026-10-05 17:34:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eddee607-4382-363f-955e-92dcf23b9b01 | -11.2023 | -46.27496 | 2026-10-05 17:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 04ff94ed-8ffb-3d08-9910-f654117577ef | -3.3296 | -59.47408 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ee253fab-a2c1-3606-8ec0-148a921e47a9 | -3.48326 | -55.43019 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e3f83176-2653-323d-8687-0628d5360f3f | -3.29717 | -59.39801 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f8f10727-9a6d-328e-97c2-09f8c0d26df1 | -5.96444 | -55.35499 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fb4ae4ac-512d-3877-b7ad-d82c1b2fd228 | -3.51663 | -54.62137 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 644f20ac-202f-36ff-ade2-651f576ebf83 | -8.10396 | -70.132 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb7fda27-1a57-32de-9ea7-939f650004e9 | -3.72165 | -59.68887 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f58e00e2-cbd0-33ac-be10-b64a62075a22 | -7.75893 | -73.07203 | 2026-10-05 17:34:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3f1c9fb6-03b6-3ce5-8217-e5446ffb87a3 | -1.85644 | -50.63495 | 2026-10-05 17:34:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40b508f5-00bf-3e0a-a7e1-a112d08f16e3 | -6.83402 | -58.59073 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e34c5e27-cad7-3f90-8cca-978ecb0bf6e9 | -3.67587 | -60.62625 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 5a55add9-aa36-3a2d-b71c-6f07c2c15642 | -3.3738 | -58.18693 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| bbdf3b5b-c614-315c-b9dc-9c1961f6f52e | -11.01647 | -68.51516 | 2026-10-05 17:34:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 1b3e8ced-a342-3136-91ee-b9d7aa2b4f96 | -4.06338 | -54.04816 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a1d0c3ce-1148-364a-9f4a-15c63b873b89 | -3.4602 | -57.48354 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f6358fd1-6ed1-38e4-bb1f-00c166901fb9 | -7.78437 | -72.15132 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f16aa2e-bde1-3d60-ade8-fd5f3d9b2f46 | -4.20753 | -53.46402 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| da625580-221d-359d-a27d-27da452ba70e | -5.96272 | -55.34421 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 73a5d96f-5051-3a7d-99e8-c5eb0049181c | -3.06237 | -54.16903 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7cf71cdf-9241-3e6f-9d3c-7cf9a89b2235 | -10.49588 | -47.24308 | 2026-10-05 17:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7bade808-8d57-3e86-8a99-ac0c3b6d484d | -6.04702 | -59.93067 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb55115f-d217-3ac8-87e5-d0e48a10a60b | -3.49241 | -57.64323 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README135.md)
