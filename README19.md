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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d65f005-b589-3577-8f75-6127c5832f3b | -2.8845 | -54.147202 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7424e78a-c2a4-3979-86eb-8774c1f9e788 | -10.8389 | -50.656101 | 2026-10-07 01:09:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bab7f60-e565-3cb8-addd-a110a47b9710 | -14.3752 | -55.041199 | 2026-10-07 01:09:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8efebf33-4357-398e-adb3-d92b44b212ab | -3.2725 | -54.041901 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea783fd-c8be-317d-aca2-f2827d6f8770 | -3.0466 | -53.9133 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2619cee1-25bb-358d-83b8-4671e5675dc2 | -3.9827 | -56.215302 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839ad292-c2d9-3424-9476-7e83dfc1e4c4 | -11.7331 | -43.6721 | 2026-10-07 01:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a06cf20f-0037-3d3e-bdc0-460b76c94b2c | -2.8808 | -54.1311 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0ebc6a7-b153-3d5c-bb82-6ff18204d1a3 | -10.9956 | -45.453602 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5509943-bf2b-37d7-ac6e-41b71e6903e8 | -3.588 | -54.555401 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f00e5cd-ee23-327a-834e-85e225a91857 | -3.1272 | -53.7729 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d05ccdc-392f-37d4-8dca-d06f134da028 | -2.9353 | -54.1441 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2e9209e-a52f-3c15-a2b9-01d4b1cded49 | -3.0504 | -53.929798 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d8a386-5822-38c6-a46d-2b3a0fa5e113 | -3.4772 | -50.109402 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7079bb1f-8254-325d-a19d-7b00a11a1dfb | -3.092 | -53.710499 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0299dab1-1e2a-32a0-be6c-1c3858a6351e | -2.9787 | -54.108799 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c2d7b2-9a46-3293-b5f8-23179093a4ca | -3.6553 | -55.512001 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 627816f3-aef8-3a49-a0ed-4f4e7d8e54d8 | -2.7696 | -54.096802 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34fc3979-a2ea-3ac4-bb27-270f9f5d84a4 | -3.0427 | -53.8969 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec935731-20c6-3632-a5f3-bb0a594603b6 | 0.4477 | -60.5382 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ea5ac823-2cd6-3b74-8445-e19c35aedbeb | -3.4869 | -50.107101 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3822c354-d5ab-3d72-b397-8bdb49cb8897 | -1.2875 | -54.551201 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91653536-beb4-3603-9cd6-a86cb83da991 | -2.8631 | -54.1436 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8b124a-c279-3f0a-87b1-a6fa507089ea | -2.9726 | -54.127201 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7854b602-6d25-30b2-9f2c-5edd1c683ca6 | -6.4424 | -55.027802 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c71fd7-06e8-3279-b0d1-674abf13aff7 | -1.7969 | -57.115601 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd263db7-fa11-3ed4-859f-9506ce856471 | -3.6219 | -55.279099 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbdeb78-e381-3cf5-8d0f-18fc01de92af | -3.4793 | -59.4692 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d696f5f-36a5-39e8-b01a-4ea8e230d05c | -3.2443 | -53.8769 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c81e758-9409-3e08-87f7-9f02a5d2e08f | -3.5059 | -54.646 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e348fd38-e57a-3fdf-a974-4686443fc191 | 0.9407 | -60.412201 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea60307-04d6-334f-897f-9cf32829bf5e | -12.1663 | -44.6982 | 2026-10-07 01:09:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9bde645d-604d-3e66-887b-cc0f37e23407 | -2.8363 | -54.073101 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be979944-35fc-3fb7-a103-c54c87ebd295 | -2.9689 | -54.111099 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 845523c0-3292-3f60-9671-c6964a654f34 | -11.1069 | -45.718899 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1f0ebfe-b161-379b-9e0b-d947a68c9098 | -3.1016 | -54.282398 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536215cd-7a34-3cc0-953f-58dba674b1aa | -8.2953 | -50.266499 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c3f0a6-534f-3b5d-963a-8f2994ea12ea | -3.6497 | -60.630299 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7f3990-f5a7-36fe-9af9-39160de61770 | -2.9432 | -54.1339 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7efab8f0-322b-3572-a265-15073caa306d | -7.7541 | -49.1973 | 2026-10-07 01:09:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd09658-cc70-3baf-8340-4e9d163d7d50 | -2.4815 | -56.1021 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbf22a81-931c-330d-a834-8b2e6e303a41 | -3.1936 | -50.558201 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ba52c4-81ea-33cd-ab25-5f09e4f801bd | -3.5683 | -59.498299 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9bddb2-e4ea-3351-9fde-953afd4c6069 | -6.4076 | -52.719799 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f690491-a5d7-30c2-ad4e-79b8fb2590e1 | -3.361 | -59.900299 | 2026-10-07 01:09:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b79defa7-6a99-3850-aff8-5fcdb8a102e2 | -3.3386 | -59.4841 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c534f669-c7b4-3146-b29d-2ff03c2ca122 | -4.3674 | -54.756802 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd30a5c-3cb1-3785-af33-e5722a09f1ee | -3.2977 | -54.0616 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83716ac2-21e7-3752-83f1-91339d0aa665 | -3.292 | -54.037498 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1fc584d-2b17-324e-be5d-f60b29edccec | -3.1414 | -54.364399 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9c74b40-c346-3913-8acf-f2b19feb8cad | -3.0349 | -53.907398 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa200d61-cbea-362a-9ca7-f005670f6544 | -3.9758 | -59.343201 | 2026-10-07 01:09:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3902e433-6a3d-3104-8227-775c9bb04af0 | -2.9764 | -54.1432 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b57dbbf-ede3-3604-a852-7856e1ad7ad1 | -5.6808 | -53.488899 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d15fa7e-f995-3c66-a83d-453b301ff927 | -4.161 | -55.156898 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41272fc2-32a9-3ae7-a594-f3d792fff617 | -3.0485 | -53.9216 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5a3b45-aa08-3047-9d55-5f266c4a9ec5 | -3.5417 | -59.4716 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0dce0de-04aa-35f8-81aa-ab6dca06f6ef | -4.1577 | -55.142399 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e42512-14a1-317c-9857-3bd9c43ad553 | -3.3018 | -54.035198 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eded6cf4-837a-343b-b468-f26e2525c32c | -2.9745 | -54.135201 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3dec1c-d8b6-3ef2-9a30-e014587b008d | -3.4396 | -56.9482 | 2026-10-07 01:09:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e260b8f-56ae-30f0-ae6e-23157133c4f5 | -3.847 | -55.9846 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29d08d65-e9b7-3050-b158-321abb98442f | 1.9771 | -60.612801 | 2026-10-07 01:09:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc70ed0-4fe2-313c-8cfe-247b872df48d | -3.2168 | -53.891899 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48ea36f9-3891-30ff-83bb-7ed40c12d31d | -2.8762 | -54.199799 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e827feea-991c-3578-9006-49983f685af7 | -2.9372 | -54.1521 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab1263a-72e8-33f7-9207-5fea178ef3e1 | -8.2884 | -50.2803 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60628bee-5906-3adc-b0de-e709e9336f5d | -3.0959 | -53.727299 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e316261-f9ed-3ac0-9a13-219fca505694 | -3.0458 | -54.220001 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6c5672f-ef8f-3e85-8b8b-76e1c6501554 | -3.0728 | -54.247299 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32229d44-49ec-3e70-8eba-4b747548094c | -2.9885 | -54.106602 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e191d333-0465-3bc3-862d-a70a6d770e9e | -2.9572 | -54.105202 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2830b68a-be84-3a26-a6c2-e77b7314bb2c | -2.9512 | -54.1236 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98611591-5724-3636-ab70-10094c2b6cad | -3.1035 | -54.290298 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c16629f1-432f-3dd0-aab0-77c7ca4c2b53 | -2.9237 | -54.138302 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7dde22-76d6-3667-87a6-4a311f6a4662 | -2.9489 | -54.158001 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a38460a0-6488-3a44-90ab-ac908afb0cf5 | -13.5131 | -44.3689 | 2026-10-07 01:09:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f1e53c0-3eba-33eb-85b8-b6c51a0f87e6 | -8.7213 | -45.221401 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cbcbc2b-af2e-3d72-b86e-3278af6cb1ae | -3.4965 | -59.272598 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9d29b26-7c7c-3e1e-8df8-ab4774964616 | -1.4636 | -54.777302 | 2026-10-07 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49c4bea8-d879-331c-9980-af203d7c8f24 | -3.2149 | -53.883598 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76ea5a0-45d6-3a6b-aed9-358615c4895d | -3.5665 | -59.490501 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfcc4e8a-c607-3908-91ce-b50eb9f88efe | -9.6374 | -48.886002 | 2026-10-07 01:09:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b57698b-5fcc-3624-8c7a-d6d520a87b13 | -3.969 | -56.0662 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5918abc-531f-3877-a49b-d11c0f71ce72 | -3.5648 | -59.4828 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee58f3c-8833-31b1-a675-7600611e3afa | -3.5798 | -54.653099 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef14ff73-58c8-3af3-8d23-385b66bc2a1e | -11.1123 | -45.739601 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20ce0d57-fb26-3b0f-827d-22818d3c3d24 | -8.7148 | -45.196701 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 414d93fc-f030-39d4-8a7e-e1cedf2b7b08 | -3.3519 | -59.497299 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 820e69d0-db13-3fac-a72b-3b597936a31a | -13.6342 | -44.4338 | 2026-10-07 01:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec125689-50c5-3b3a-aebf-8b77585adca8 | -2.9143 | -54.0979 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a831eb8e-262e-3209-9fe6-93123717732b | -3.2864 | -54.013199 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b04b0098-57ce-3706-a062-156a24eed70e | -2.9391 | -54.160198 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d64f7a8-50ea-39e6-853b-988c720e8de4 | -3.5487 | -59.502602 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1d8563-8fda-3ed2-b044-2c16466e002d | -3.1673 | -58.641102 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08216269-b4b2-3015-90fc-abe582f2a11c | -1.2992 | -54.556999 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4572b9-e426-3c04-a6e8-cafee370c52d | -3.2822 | -54.0397 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6033ce27-bf1b-3a23-b6fe-888382c6b62d | -10.8487 | -50.653702 | 2026-10-07 01:09:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bea3aed3-0b0c-35b1-a5cf-eaf4f19a8f4b | -9.1493 | -65.957298 | 2026-10-07 01:09:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec9c1c5-cbb1-3ac3-ac69-691f8a8377b3 | -6.2053 | -52.6936 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
