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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90531891-b9ca-3cba-85df-8d30aae332cb | -8.11981 | -48.26577 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8fff5d3e-62f6-39a7-a2eb-e9457b9633de | -10.78989 | -45.9763 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01a776c4-49dd-36d2-ab2c-68bddea9eb8f | -9.04835 | -44.85058 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c4d448c-74e3-3c2b-a134-37c9129dce1c | -9.80293 | -45.61264 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3beac2f2-cba9-3857-af4d-31616d8b7a0e | -10.72137 | -46.48722 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8c2fced6-1b46-37e6-87aa-ef818cf9121f | -9.74677 | -55.37252 | 2025-09-16 04:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 84be9c14-d6ec-34b2-9f3e-403ed8467f5a | -8.83189 | -44.21347 | 2025-09-16 04:29:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52c218f5-01f8-3cf2-a0ff-2cb4eef925c5 | -12.05672 | -46.55436 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48ee29ce-3b2d-370d-840a-5378a397e3b6 | -8.20177 | -43.75754 | 2025-09-16 04:29:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d00c78d-c65b-3295-bb62-867c56fada7e | -9.05525 | -44.85163 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c72f46f-8639-3ffe-b294-022e77abb1d8 | -9.45512 | -48.60478 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3909288-71ba-35dc-9c8b-91b7d260ead0 | -7.444 | -46.17216 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb2a174f-b283-36f8-9230-1f8ed2925200 | -7.98507 | -45.65601 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 564da52d-365d-3219-8ad0-ed2a1b2dd0c0 | -12.17475 | -44.09772 | 2025-09-16 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dcbddb2-df0a-35dc-ab7f-47bb9c1332d1 | -12.80212 | -47.25872 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7771f1e6-d8ba-36bc-8611-4bd53907dfff | -11.12127 | -45.12086 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9c18793-48ee-3850-8de5-fd9993a68a21 | -7.8107 | -46.12301 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4ed76d7-a561-3eed-9607-8e5286f504cf | -8.03537 | -49.83153 | 2025-09-16 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f43f861c-66ba-38e5-8f96-caeddb6f49c0 | -7.80737 | -46.12247 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4f7e1141-429e-3999-859a-ee67b972717e | -12.796 | -47.25412 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56733697-2612-353b-aac7-7b9ccd3a4fe7 | -10.72082 | -46.49075 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| df8d5a01-144b-34b4-9c66-4f3829d22821 | -11.43947 | -43.54244 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff27a6c9-42e4-3859-84c7-9b7bf64420d8 | -12.62693 | -45.76265 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a7e2f9bf-97fc-3826-a2fa-038ca15d6d07 | -11.46334 | -48.69546 | 2025-09-16 04:29:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70785b83-04fe-3287-accf-cc5ca7fc25b3 | -12.66979 | -48.01142 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a29b0a1-99e2-3344-a934-590118fd2269 | -10.36524 | -61.26525 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51480e8d-05f8-37cf-b794-936c30121156 | -8.12602 | -48.27055 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c649d35b-4c59-39f6-bc27-fe9c06ffe4f4 | -12.66088 | -47.72287 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d945c3cc-feff-3e6e-a28c-f0bb33fb1757 | -12.82325 | -47.23299 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e989006-ca10-35a3-a897-20c6a321958e | -8.5857 | -46.35279 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4900d456-d922-3537-9772-45b4225d4231 | -12.11409 | -44.83264 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c296393-8820-35c2-9d95-73cb49f9a742 | -11.96756 | -46.77507 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ef85f93-24a3-33dc-bad5-c83a87308f18 | -12.76913 | -47.95829 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15122757-8704-3a54-bf0c-8004fd3b9c13 | -12.61661 | -47.95901 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 402bdc32-6562-361f-9089-80088480b558 | -10.72928 | -44.75657 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8426462a-8055-3809-a2be-401919a67a10 | -8.76345 | -46.10361 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50657965-bc09-34ec-874c-37875b608e71 | -11.4554 | -46.9198 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 594d34b3-c603-370e-b9d6-783d1a3de139 | -12.79032 | -44.74593 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd531bb3-9151-3aff-abea-7f0c0d6d52d9 | -10.71748 | -46.4902 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d6690922-d9e7-3801-8631-1a4c2726f507 | -8.88443 | -46.17655 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe0074c8-38d6-3332-94e3-456cd1279119 | -12.62541 | -47.98955 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e84df953-7cf3-323f-bb56-a85f0f1a009a | -10.71527 | -46.50438 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 30ffb077-67ba-35a0-946b-00ee9f0946b7 | -11.46152 | -46.9244 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50bdc2f2-06fe-3c8c-91e2-b6eeb8080e83 | -12.97463 | -47.96304 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3e7d4dd-9b51-344b-b7e0-48d1840a9f79 | -10.77965 | -49.14112 | 2025-09-16 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f7f491f-df21-379e-943b-46b5133b21d5 | -10.05991 | -45.50601 | 2025-09-16 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcab61b3-ed66-324a-8685-529b3dd2682c | -12.78301 | -47.95694 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e1e8cc-a4ca-368d-a39e-a6a5eadab908 | -9.94066 | -45.89725 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2565bd97-4064-3593-b9d8-00a6be8c9684 | -11.45874 | -46.92033 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdbbcd75-2e3d-38aa-8c93-8ed12a80bcdc | -8.97131 | -44.19184 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64b1fbdb-5d0d-3202-aaa6-c0e9e40a9b61 | -10.72485 | -44.76069 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 19edac9f-6bfc-38f6-93da-1aa2b91d6637 | -10.44571 | -45.15031 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b1c2300-b8b3-3a4d-aebd-1f9016af2253 | -8.60852 | -46.40307 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 676c01e6-7428-31a5-aebb-d05869ccc0ed | -10.05934 | -45.50969 | 2025-09-16 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cf7c6c5-9382-3be0-bec8-0a9827bd4ad1 | -12.6298 | -45.76699 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb805cb0-fef1-362e-9760-136295760359 | -10.47493 | -45.15873 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f4bde8d-c0ef-3b16-9f07-a281b8a8f524 | -11.12256 | -45.34822 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1f3308d-e66c-3da7-a383-1823e4825692 | -8.67278 | -46.37717 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42cffa52-8a97-3080-baa7-da58d3e2e493 | -8.07263 | -46.83987 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 225644fa-a83d-3fac-9566-3f5abcb853e3 | -8.61296 | -46.39657 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8917933c-72e6-3aaa-9626-18cbceaed2a1 | -11.43701 | -43.53267 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f249b2fe-56db-39ae-9992-313a461f5361 | -12.97847 | -47.98183 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd18d7f-a0e7-3a64-9394-2c7288e11578 | -8.45015 | -47.67137 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.1 |
| f76fff4a-b18b-3129-8ddc-e9d77b3e542a | -11.23946 | -49.94711 | 2025-09-16 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87b76ce0-364f-3d89-a037-6e558adf7f78 | -9.23433 | -45.68085 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae55526b-37f1-36ae-ac86-2382b11e7599 | -8.70577 | -49.41878 | 2025-09-16 04:29:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c83eefc-0441-3b13-bdcf-82e65ac281c7 | -8.88108 | -46.17604 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c81965c-9f40-3c68-81a5-b373f526e2b7 | -11.43762 | -46.94603 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 051730d8-a5d4-3f27-a8fa-5f025f3b1bf4 | -12.61954 | -45.75071 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9878ecb2-a3b0-3237-9764-b1b94c446a34 | -12.11349 | -44.83663 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68111967-351a-316f-93b0-8d1e33a19365 | -10.72692 | -44.74821 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67794053-0da5-39db-8aa1-eb6d1af19cbc | -8.63672 | -45.68438 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28e23ef5-ed07-36a2-b494-5c642e11cc21 | -11.43818 | -46.94248 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82653d4e-4696-38c0-8a06-951eb702d220 | -8.87385 | -46.17852 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd6a39d-33bc-39f4-afb2-ddf7e0381cee | -12.80434 | -47.24455 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3b18b2a-72e3-3d4e-9e92-9dddcbc4fa32 | -7.67953 | -46.28469 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4e772eb-5561-3295-8b86-9a068398e568 | -12.54114 | -45.87396 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1d07d6ba-8fff-3dcf-afe7-7635afc78e93 | -11.12486 | -45.3563 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11854afd-e1e7-3591-a84e-cab90bfe37e0 | -11.12199 | -45.35199 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eea0b6db-8db6-3d06-9cf1-174bc67e645f | -11.45429 | -46.92689 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f53cddb3-13d2-3132-9e3e-f938e3161fc8 | -8.00309 | -45.66284 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afe6cd16-6f20-3132-8c92-8681a378ab6a | -12.05839 | -46.54356 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9df560f9-3cb0-36a4-98d5-cb4f83e66156 | -8.49899 | -47.99811 | 2025-09-16 04:29:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07e07a34-1d23-3ac1-8e21-061628e21a07 | -8.87553 | -46.18962 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 511bb39a-d42c-3741-8134-ed4b5e9230f6 | -9.05244 | -47.01782 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a67f9e8-fd04-3424-9b92-81cd30a2bed2 | -12.66032 | -47.72641 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b41da128-003c-3f17-9520-697bb5afcc42 | -12.76135 | -47.96427 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 199b9963-38b0-3680-9060-2e220b598206 | -10.78762 | -50.65344 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1db4c67e-9e7b-3aec-b303-0a88e103484c | -8.97811 | -46.24582 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c12779ba-8511-31e1-b96b-a6f83944af78 | -10.11163 | -45.66731 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44731e62-8b3c-3804-bf1a-6cc22997ec02 | -12.80889 | -44.74448 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69390183-6c8c-36e8-bc8e-6cab3d92ac73 | -7.83485 | -43.85953 | 2025-09-16 04:29:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e59d4a6-56f9-3fc9-9718-cedd4c1dcf71 | -10.71248 | -46.5003 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92a3b13b-edcf-3064-8498-5925cacd5b24 | -7.53006 | -47.65564 | 2025-09-16 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60828365-920d-3a99-96c7-902ee7731866 | -9.14488 | -46.94661 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b836b62d-d781-3df8-a45d-0e79d35bedc0 | -12.61209 | -47.98736 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 648e00e2-697b-3e2c-9eef-adf1ccec562b | -10.0365 | -45.2937 | 2025-09-16 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfdf42a0-774f-3a47-974e-0770c9b3b776 | -7.69181 | -44.67133 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd41b4be-ed66-341c-b69f-97396e23ff42 | -10.63787 | -48.74395 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26d8ee2a-35b6-3996-ad99-9e36111c3dfa | -10.36255 | -61.26467 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README46.md)
