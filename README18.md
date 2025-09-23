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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b615eb2-af7f-3a55-80cc-b828a73fcf8d | -6.39166 | -50.91594 | 2025-09-23 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd7d83e5-ea99-32de-a9c8-e81168a2390c | -4.5953 | -46.59177 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebfe98d1-852e-33ec-b0f7-45061728376e | -3.78832 | -57.29421 | 2025-09-23 05:10:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d6747e-14bf-355d-b90a-43774b3fe600 | -6.50416 | -54.88982 | 2025-09-23 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4d98fc9-7b42-39e6-808b-1afa4152e015 | -4.00879 | -43.27218 | 2025-09-23 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfe404be-7ec3-365b-a963-a460535b1e5f | -6.59214 | -44.54862 | 2025-09-23 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c1027430-bfad-3deb-a70f-e989c2779d25 | -3.24635 | -52.85551 | 2025-09-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 122b9f35-ab4f-33bb-ae0d-573b64e3ae8c | -8.00288 | -45.72647 | 2025-09-23 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baba7a5e-2d0e-3ba6-b5ea-8ea14885a8ce | -7.88302 | -44.01822 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3f42b620-44fd-3008-bfed-5d22776ace08 | -4.51359 | -55.76242 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e699b25-0b09-3950-a157-449e3d01899e | -3.62698 | -51.90959 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 12667fff-c64d-33cf-a761-9125a50b4c93 | -3.64786 | -58.16159 | 2025-09-23 05:10:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7370e017-26bb-3635-a5a4-7d7e7648b5f4 | -4.25535 | -48.59721 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff82b197-08b9-3d21-a382-951f06e4953a | -8.14254 | -44.46989 | 2025-09-23 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68df02c7-e8b3-3b25-a83e-403e47d81bca | -5.92598 | -50.05839 | 2025-09-23 05:10:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87bfa498-3869-349d-8a78-1595468e6ea4 | -6.24548 | -55.36493 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a734939-923f-3acd-a7b8-9d65cf6cd7ec | -7.16002 | -48.2875 | 2025-09-23 05:10:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd381e2-8060-385f-b0c8-b1263e7ae90b | -6.77435 | -55.48529 | 2025-09-23 05:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65af1dfa-4689-3ba1-9aec-fa2a1f6d7280 | -6.33983 | -56.19954 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23a08a34-3610-3253-9634-08e495a770ca | -2.53607 | -54.65928 | 2025-09-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c97c235-91b1-3b6d-9d0f-0c36834f4d53 | -8.52426 | -44.97472 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d8c5ade6-41fe-31f8-b277-d2bb9f901940 | -2.16038 | -53.65239 | 2025-09-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b813af8e-651a-368c-b348-93ae4be469f5 | -4.13108 | -48.81871 | 2025-09-23 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50edcd5c-bc89-31cf-af1b-2c9f3ddebd66 | -4.55326 | -50.28828 | 2025-09-23 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086e680d-83b4-380e-893d-e3059efb9d40 | -3.82445 | -52.14886 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 403189c9-f33a-3d9f-a780-0cfd72c99e11 | -4.7868 | -47.25116 | 2025-09-23 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07ad6892-a3dd-3589-85c4-694717da4462 | -6.34209 | -56.20717 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d2adef5-778f-3a2f-bd1d-0ad506205f43 | -4.48011 | -55.57862 | 2025-09-23 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42270ec5-1f06-3ed0-b290-70618ca0f866 | -6.25789 | -45.33458 | 2025-09-23 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c595ba69-fafe-3def-8b43-5a4c51225a03 | -6.34092 | -56.19242 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3e1ada4-b942-3526-a042-e8e85dff3455 | -6.35151 | -56.19042 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710892d5-0902-315a-94c5-ad22ca2cac84 | -7.22661 | -45.17973 | 2025-09-23 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e276cdf8-1a2e-328a-96d3-7e74903c1433 | -3.85567 | -52.23605 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fbad667-78a3-3400-81be-cc4958f3dc8f | -6.33648 | -56.19901 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f65f1603-7141-310f-a404-1b4d9d457f5d | -3.24695 | -58.84782 | 2025-09-23 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9162181-c386-3635-a0f0-e9dc99cff84f | -4.07822 | -48.03789 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0839061a-25a9-331d-b536-70b374bed438 | -3.96262 | -49.29881 | 2025-09-23 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e47149bb-35b8-3a72-9091-052c3e8a01fc | -5.94556 | -45.39676 | 2025-09-23 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa089525-7a50-3f7c-a815-03f11197b0c9 | -5.32972 | -56.00432 | 2025-09-23 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41fb2c58-38a3-3cf0-8a06-e3cdc43b3aa6 | -4.15741 | -48.60307 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c466618f-057d-3478-8f5f-69b4059b794f | -3.33107 | -56.99646 | 2025-09-23 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26657faa-afaf-38db-bee0-27e559b84fe1 | -4.51414 | -55.7589 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37dd49e7-e218-389f-88a3-41cd879dfc22 | -2.52517 | -57.85836 | 2025-09-23 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f56325ed-3c02-3731-aab5-88dc173f2474 | -3.64405 | -51.9048 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 863c0900-9cc6-354c-9c17-184d7a5a5c77 | -6.34544 | -56.20769 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d93b0461-22b8-3748-9823-2e4399657ba3 | -4.96716 | -48.01137 | 2025-09-23 05:10:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05b3ddf3-9b67-3f8d-9bc5-f6e7bf92094b | -6.34535 | -56.18582 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45fb5765-d728-36ec-a6c3-52e14c556879 | -6.35041 | -56.19755 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8369281-5ea3-36ed-9b0e-c0767725c1e0 | -3.5189 | -49.44689 | 2025-09-23 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4b0fdeb2-645b-3e36-94bd-3543b292444d | -4.0725 | -48.04078 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c16b4fef-0233-3415-85e4-295cfc73cf07 | -3.635 | -51.91064 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afbe0212-335a-35dd-8de5-f34bb1f4afcb | -3.03274 | -51.44898 | 2025-09-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b664898-3dc5-3c12-b244-26a7ebc321d3 | -3.64458 | -48.32422 | 2025-09-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c91e9c35-8972-3d23-8802-1226b438e36d | -4.27153 | -48.1842 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c7a97ce-f0d7-3c1d-8310-a51641ff129b | -1.69019 | -48.19854 | 2025-09-23 05:10:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6cde2a-efb5-3069-a39c-de875040a457 | -3.87168 | -55.35677 | 2025-09-23 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8b2670b-c3da-3f26-a79e-06b53bb2965f | -3.59787 | -58.58479 | 2025-09-23 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adb09e35-481e-3dbe-bf40-099b52213df5 | -7.88698 | -44.01906 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3c6cfbb-5e73-3769-9f38-15ed964c8489 | -4.78625 | -47.255 | 2025-09-23 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d6e7073-b598-3bcc-9196-4928084c80ae | -7.89323 | -44.0273 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a97ea6a-eced-3732-9fd3-9d46b253fde4 | -6.59718 | -44.54746 | 2025-09-23 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| edbbd415-e075-3414-8bae-a73333118890 | -8.52215 | -44.97597 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 112859ba-44f8-3155-abf1-42f15e041301 | -6.33874 | -56.20665 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66497630-8464-3211-9edc-4875630504c2 | -2.836 | -48.83516 | 2025-09-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6e7b4c6-1adb-321c-9206-b52942f97e7d | -6.34146 | -56.18886 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5998ca64-411b-3185-a51e-95c931615a08 | -6.35096 | -56.19399 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2ef8153-77d2-31a5-862d-d5b939bef0ef | -5.92335 | -50.06183 | 2025-09-23 05:10:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6768af1e-e215-3298-94b0-ec258a39665f | -8.51739 | -44.9745 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 658459bd-ec9f-370d-80b5-8771c95547a9 | -6.34037 | -56.19598 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33b3c625-4221-3470-a8c5-7f977d6be267 | -3.63099 | -51.9101 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4149f377-738e-3a4b-9ab1-196207839f16 | -5.92178 | -49.29479 | 2025-09-23 05:10:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b19b0625-d29e-3180-8151-d4f5dfa90422 | -6.34652 | -56.20058 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d681d7a-2c1b-30e3-8acb-51cebdc2def1 | -4.3816 | -43.28423 | 2025-09-23 05:10:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21292ff7-8e15-37ec-aef0-eefe5230da50 | -3.64004 | -51.90422 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba88427-613b-3f6b-8214-90b93ea9ff2a | -6.34878 | -56.20821 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 271900c4-f01e-3f73-943c-44fb46c4a8c0 | -4.49149 | -48.11289 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c070735-6770-3749-bdc6-32941cb01d94 | -3.57985 | -58.56705 | 2025-09-23 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6290ce-eeb4-3d90-90e1-c6f213d48325 | -4.08302 | -48.04191 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8223887a-7968-3359-8237-08f74ef06d9f | -6.25903 | -45.3339 | 2025-09-23 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac832daf-4ec4-3ef4-b906-b734cc4e2263 | -4.27106 | -48.18739 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6250e13-71b9-340b-be35-75cab49e8f6c | -6.34481 | -56.18938 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab89910-53eb-3af0-ba70-efe02dddffd9 | -5.64749 | -51.4663 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a3bc730-6a27-3527-a0d5-04daa2b14ce3 | -3.36442 | -59.43373 | 2025-09-23 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f277f71a-601c-3885-bb6e-7e74dda21f8f | -4.32239 | -55.50272 | 2025-09-23 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5126015c-6acc-3932-8149-2a7e5c24be3a | -4.08298 | -48.0425 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca7c2d5-6665-3e39-b45d-6c9b3a7e8897 | -3.87505 | -55.35728 | 2025-09-23 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89652686-26db-33ec-b56e-eb29261d5c48 | -3.09475 | -52.46781 | 2025-09-23 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f893b32-1844-3741-9a06-97dfe7000722 | -4.40712 | -44.37144 | 2025-09-23 05:10:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f5f1e93-1855-3229-9b19-859f222e3ad2 | -3.24552 | -52.85337 | 2025-09-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee76320d-7d4a-35bd-949a-6b394bebcabf | -7.16623 | -48.30066 | 2025-09-23 05:10:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97426af7-9802-3366-aa19-845de66e1c0a | -7.16669 | -48.2972 | 2025-09-23 05:10:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9e90389-6d6a-3b17-b3df-19a2e5f7b1fc | -6.59906 | -44.54861 | 2025-09-23 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea5ff097-dd88-355f-a3d5-36590297c475 | -3.51814 | -49.45197 | 2025-09-23 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb5558f0-b5c4-315d-b8f5-6e6593d8b2d8 | -5.17815 | -56.06017 | 2025-09-23 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fc2d025-ac09-30e1-ad8e-196ba93d766b | -5.55059 | -51.44856 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a48c048a-2c4d-345d-ae70-5e7156d462dc | -6.34933 | -56.20466 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 584aedfe-f25b-3f33-a700-e5b6a945050d | -6.34598 | -56.20414 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36a90a76-2adc-38f3-935d-1e9951219d40 | -6.34761 | -56.19347 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf143143-e6fb-3a5b-aef1-271a50744e9c | -3.74287 | -53.31668 | 2025-09-23 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec0d685e-a2d5-3601-990d-37afcb945802 | -4.07254 | -48.04014 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README19.md)
