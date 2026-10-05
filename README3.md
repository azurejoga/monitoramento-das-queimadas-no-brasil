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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 670b1f3a-199d-34ae-8f80-b1d4ea499a3e | -2.9141 | -54.0951 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71bf1680-0b96-3a29-8e9d-1a52adc93c58 | -6.1839 | -52.817001 | 2026-10-05 00:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 712f9f86-1b22-3509-b70f-d73670ae9fb8 | -6.9112 | -43.6633 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edfecce9-739f-3324-936c-39be678655cb | -7.6449 | -35.016899 | 2026-10-05 00:12:00 | METOP-C | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36fd9fc1-cc4a-351f-9e9e-979a347c7801 | -4.635 | -46.306099 | 2026-10-05 00:12:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1fd4aa1-61c9-3075-aa87-b33b27d9303b | -6.9031 | -43.6731 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6da2981e-6d7a-3cc1-8dc9-c6ecc55adc17 | -2.7464 | -45.541901 | 2026-10-05 00:12:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df20f8fc-e3e5-3ddd-91e0-2fe88fc63bbf | -7.0896 | -41.762901 | 2026-10-05 00:12:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3de74045-1fdc-3f05-b24c-b9d75afae029 | -6.6087 | -41.553299 | 2026-10-05 00:12:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 415076d2-6c70-315e-bae7-745a0ec2c446 | -3.9053 | -49.695999 | 2026-10-05 00:12:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22eb2f85-0d74-33bf-86ce-758f5c649c7c | -10.9647 | -45.414101 | 2026-10-05 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b66bde7b-bd41-309b-92f8-40c8fb4794a1 | -7.8852 | -44.205601 | 2026-10-05 00:12:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9e48dd4-8f13-392b-aac7-22f31a1b93bf | -5.942 | -41.3437 | 2026-10-05 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2729dcda-548f-3345-8da7-b7f43e2551e6 | -3.8227 | -50.289101 | 2026-10-05 00:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 822725ab-32bb-3784-987c-78562c6d1655 | -6.4304 | -43.721401 | 2026-10-05 00:12:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc59acd1-5ad5-35da-9659-0a9996120219 | -3.25 | -54.154701 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe623b18-8410-3281-8a75-131107f3b293 | -5.5784 | -49.752499 | 2026-10-05 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82efe33d-fdbe-3cda-a4bb-48c44d9ecc26 | -2.7483 | -45.550301 | 2026-10-05 00:12:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 256acc86-225d-30d8-9352-a9a31d51485e | -8.5846 | -41.447899 | 2026-10-05 00:12:00 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 160ac1a8-1c28-3bfa-9a25-b8781827f6f1 | -6.8559 | -41.641998 | 2026-10-05 00:12:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf757379-4926-3228-981b-916bb62ae1ed | -6.6129 | -37.889702 | 2026-10-05 00:12:00 | METOP-C | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 01b61996-30c0-3d2e-af46-7ce4e8ba6a54 | -6.8703 | -43.6642 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8eced62e-81e6-392e-a916-81c8c74ce6c6 | -8.583 | -41.441002 | 2026-10-05 00:12:00 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72431c1e-abdc-3b35-8abf-86f2aa7c7713 | -6.3306 | -38.9258 | 2026-10-05 00:12:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 29845857-ca82-3e20-8c68-57a9b7774eea | -6.895 | -43.682899 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b0bb8f18-1221-307f-8599-c60ed02a11b1 | -2.4597 | -48.039001 | 2026-10-05 00:12:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8811827-9900-3fd8-95f1-efdb402ad0e4 | -3.0506 | -54.164299 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3b2e83-fa9d-3300-aaff-2dd04898aeea | -3.9088 | -49.711899 | 2026-10-05 00:12:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a654339-e9bd-323c-9c70-ee4a42104313 | -3.0602 | -54.1623 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7589d8eb-9b85-3d65-b9e9-92f88289f346 | -5.9667 | -41.316502 | 2026-10-05 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 36af4bab-57fe-38b6-a0ef-401cd9208394 | -5.5747 | -49.735401 | 2026-10-05 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52cf374c-47ab-34cc-a294-6ee1457ffd3a | -11.6805 | -43.634602 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f798d76-3d31-32b5-9421-0bc2c6665269 | -6.8899 | -43.659901 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0646e9d-3437-3104-b008-2995ec62a34e | -5.9503 | -41.334599 | 2026-10-05 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 07b03e82-a7d8-37ad-bd02-e129035f18bf | -4.1621 | -46.439999 | 2026-10-05 00:12:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 734bb994-9fd8-36ec-ac45-69a297cf2e05 | -3.0904 | -53.7085 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d45de481-09c0-30f0-8709-a2ce2ed6bae8 | -8.8609 | -45.383099 | 2026-10-05 00:12:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 802aeda5-aea9-378b-b08e-127316cbddd8 | -6.6108 | -37.8811 | 2026-10-05 00:12:00 | METOP-C | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| aef2be04-a2d7-3f8c-ad70-f08e7f1759ee | -3.8305 | -50.324001 | 2026-10-05 00:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5786206-b637-344f-a61c-2fb77ca039e9 | -6.8818 | -43.6698 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb733230-e035-3309-b650-7c7c97565732 | -6.6088 | -37.872501 | 2026-10-05 00:12:00 | METOP-C | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| b1dd7638-2af0-329c-baea-a43beb0672b6 | -6.3154 | -43.347 | 2026-10-05 00:12:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8d7f17e-5791-3179-ac55-3c8551ba4f7b | -7.088 | -41.756001 | 2026-10-05 00:12:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ab12c77-52e0-3134-b44a-f9c798579777 | -10.9526 | -45.405602 | 2026-10-05 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cecfa9f8-fadd-3a83-ab7f-30c034adc864 | -4.1023 | -49.065701 | 2026-10-05 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca616bd-f46a-3965-b0fa-e8a420fd1c0e | -4.2838 | -50.763901 | 2026-10-05 00:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4540c91-a66e-31fc-a9c6-58ce68d89592 | -11.7381 | -43.426201 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e50c99d7-9709-365d-ab78-dfef1f71afe5 | -3.0339 | -54.1348 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6425a8af-8c9b-3b9e-9459-0406a4dd95ba | -6.872 | -43.671902 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ecc179ff-a669-3ad9-8616-ac665d73d18c | -7.8834 | -44.1973 | 2026-10-05 00:12:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55ade0af-3511-3007-9efe-0d788c122fb0 | -6.2429 | -35.1441 | 2026-10-05 00:12:00 | METOP-C | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e446b1e7-587a-36c5-86a2-e3019612fc78 | -3.1035 | -53.767601 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a99af7-edca-3fc1-8bc5-37ffd72be47c | -3.1193 | -53.702301 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceac0ca3-3e4a-359b-b274-a28b3a6cf0ce | -3.1 | -53.706402 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61d4db9-752a-3320-97e7-5e2b35d1e280 | -6.9065 | -43.6884 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4d122b0-e225-31df-b60e-cd55565ff847 | -3.0969 | -53.737999 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d4269a-6cef-364b-83e7-3f65e1af50a0 | -9.81 | -44.7981 | 2026-10-05 00:12:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3b654ca-03bf-3669-877f-23d30c36c4a7 | -3.0807 | -53.710499 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a556d073-f38b-3a57-9c52-053c6564e955 | -13.6269 | -44.4193 | 2026-10-05 00:12:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cbbaa1b3-956a-3c6f-b543-d2fe6c709a38 | -6.6005 | -41.5625 | 2026-10-05 00:12:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8ff7e7d-a425-30a4-b026-85e72b451b68 | -2.6814 | -49.0205 | 2026-10-05 00:12:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c81ccda-35ff-3c06-8de8-52cbb4b1560b | -10.0849 | -36.214901 | 2026-10-05 00:12:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 199c9259-c5fb-38c5-bf75-85deebbd331c | -4.288 | -50.7831 | 2026-10-05 00:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23b31cf3-426f-3b77-bfa4-2d2ba095d50d | -3.1097 | -53.7043 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1536a9c1-6ce4-313e-b394-050b29a8ad9d | -3.2667 | -54.184502 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74b811ea-f242-384f-82fa-9758fa86a921 | -6.9163 | -43.686199 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fbca6a56-5729-33a9-8ec0-bde3b2f0812d | -3.2647 | -50.391201 | 2026-10-05 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9567c212-9a7f-31b7-8705-a824b22a0b26 | -3.9193 | -38.675201 | 2026-10-05 00:12:00 | METOP-C | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7308724d-9b8f-335a-b3d0-2df62c0852f4 | -6.3324 | -38.933601 | 2026-10-05 00:12:00 | METOP-C | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e2fca84c-24e8-3171-9ef2-43c72eb20916 | -3.8403 | -50.321899 | 2026-10-05 00:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cafb00de-8ca8-3719-b585-554fa98a5437 | -11.6438 | -43.606602 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b39ccf55-7140-32de-8952-c21121cd8713 | -4.8478 | -40.401699 | 2026-10-05 00:12:00 | METOP-C | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| be69f6d5-0456-3ce0-921c-bb5ea6c8b4e3 | -3.2549 | -50.393299 | 2026-10-05 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a47dcb3-8f78-3119-93aa-57f2836f714b | -3.0532 | -54.130699 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc78ea13-8a60-3190-bb59-987f84efc786 | -11.6787 | -43.625999 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93f1f8c3-b267-311d-9093-938515652924 | -6.8967 | -43.690498 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 45a1601e-f003-3f7e-b186-464fb2c77681 | -3.041 | -54.166401 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48c47827-ddca-3626-8dcb-df119d855589 | -3.0939 | -53.769699 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 804dac3a-e362-343e-9f02-4f745f7da980 | -3.0288 | -54.202202 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f10338a-63fa-33c9-a9bb-2e9008dc7d5f | -7.8932 | -44.195099 | 2026-10-05 00:12:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aaae0bc5-88dc-3e4f-acbf-627b9aa3a356 | -6.8543 | -41.635101 | 2026-10-05 00:12:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01d0667b-7fbc-36b4-a8e1-0ad0930103ac | -3.2598 | -50.004101 | 2026-10-05 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c786e688-335b-3662-9126-d6eaff4ec9e3 | -2.7628 | -54.0952 | 2026-10-05 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4e226f-7f8a-3b51-8bd3-baab3d80c05e | -3.1065 | -53.735901 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e6b98f-f5dc-3688-9b7e-fdb90bd16244 | -2.888 | -54.068199 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b40b3f-d7c0-389c-918c-5b5af00f26f0 | -2.4571 | -48.027302 | 2026-10-05 00:12:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21347702-e69e-3c8c-b4cb-5a5f1f6322bd | -3.1031 | -53.674999 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3831855b-22a4-3048-80e4-aa087a9cb0a6 | -3.9473 | -40.924099 | 2026-10-05 00:12:00 | METOP-C | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| abeb379e-ea9d-3d80-8851-98c88a1878c2 | -3.8991 | -49.714001 | 2026-10-05 00:12:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac0e6ec-2e8c-3ef1-8ee6-f61fc9ef98fe | -5.0668 | -40.456299 | 2026-10-05 00:12:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98723a91-fd5a-3676-8bfb-4bf3f68385c1 | -4.7907 | -42.5751 | 2026-10-05 00:12:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 26ce3b03-73ee-33f5-aafc-698dd90608d0 | -6.8737 | -43.679501 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57928bd2-5145-32b5-a3ad-96c71b66a0a8 | -11.6707 | -43.6367 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc4d75ed-9d1a-3534-99c2-7b6b6861d02b | -2.8319 | -51.2798 | 2026-10-05 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 252dd7be-cd5d-33d4-9df9-d054cf9322c5 | -3.0873 | -53.740002 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac4968e-7fca-3bb4-9e0d-e1507cee7b8f | -3.0711 | -53.712601 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b84d54cf-43cc-365c-b947-512df4a4d671 | -6.2526 | -35.1418 | 2026-10-05 00:12:00 | METOP-C | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45e5e972-8428-3177-8ca1-a85abc19ce8c | -2.4695 | -48.0369 | 2026-10-05 00:12:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250bdab9-5ae9-35be-8345-10c65b16c132 | -3.8325 | -50.286999 | 2026-10-05 00:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef0babbc-63af-30eb-8819-ea00ed96be6b | -6.6399 | -39.056599 | 2026-10-05 00:12:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
