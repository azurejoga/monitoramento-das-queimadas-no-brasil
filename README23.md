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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 163d2cb3-72cb-327f-ae51-30b1ac4d3e26 | -2.8773 | -51.379101 | 2024-09-28 01:10:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96017ef8-4c14-3139-aef7-afdf0c799cec | -2.8792 | -51.387402 | 2024-09-28 01:10:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29b0f4e3-a87e-34ba-9c6c-4a8925bdf0b1 | -3.3075 | -53.369099 | 2024-09-28 01:10:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c930964-0ca8-3c81-b61b-f5bca9251178 | -3.4529 | -54.0905 | 2024-09-28 01:10:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a56ce54-82f9-3532-9f7d-78f4873a6a5e | -3.4544 | -54.097301 | 2024-09-28 01:10:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 847f274a-2a12-3bae-aee4-9bd0b456b6dc | -2.871 | -51.662399 | 2024-09-28 01:10:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d45409-b802-3878-8959-38acfc404a5f | -2.8729 | -51.670399 | 2024-09-28 01:10:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9258b6-961a-375d-8465-8f6c6993903c | -2.8747 | -51.678398 | 2024-09-28 01:10:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c811bc85-8d6b-3865-9764-4678716622d6 | -2.8594 | -51.656601 | 2024-09-28 01:10:25 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa8ae3a-6b71-3fde-8c17-fae30b252cb4 | -2.8612 | -51.6646 | 2024-09-28 01:10:25 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 762e71ae-ffc0-3d5b-aa9f-f2bf3234f4d7 | -3.2993 | -53.692001 | 2024-09-28 01:10:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab2faf1-c53c-34ec-8bd0-4671e1530ce6 | -3.3009 | -53.698898 | 2024-09-28 01:10:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9a53f06-e150-3a5a-a4fb-924322111a45 | -3.2911 | -53.701099 | 2024-09-28 01:10:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d1d743-beee-377b-ac78-278c20ae00e0 | -3.2078 | -53.384201 | 2024-09-28 01:10:25 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69c7a6b-9648-36b7-a11f-0a7ca0419a5c | -3.2094 | -53.391201 | 2024-09-28 01:10:25 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 867fccce-b3f1-33a9-bb55-62d6e901aae0 | -3.211 | -53.398201 | 2024-09-28 01:10:25 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4d84862-8716-33ff-9861-b6453a0ac291 | -3.1964 | -53.379501 | 2024-09-28 01:10:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79ec073c-43f1-39f4-a17f-709aa359086c | -3.198 | -53.386398 | 2024-09-28 01:10:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6837a8-350d-3082-bd12-74a63d875528 | -3.1996 | -53.393398 | 2024-09-28 01:10:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a069951a-dbed-3b07-b44d-0d9e2bfdf4ea | -3.2012 | -53.400398 | 2024-09-28 01:10:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48d16ee-2721-3fa4-a11f-6f0de3566a12 | -3.1412 | -53.676701 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff98eb8-777f-3137-b444-07e34ded8a95 | -3.1427 | -53.683601 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50db92da-8136-3969-9863-64d2fb2f6a98 | -3.1443 | -53.690498 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df2f9e26-9444-3fee-897c-5c0209636973 | -3.1298 | -53.672001 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52eac996-36bf-3138-af60-7c71726d24a7 | -3.1314 | -53.678902 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9883fbab-4a01-3051-9e93-a6ab7b70cef4 | -3.1329 | -53.685799 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 525165e4-b7a8-32ed-9081-5a4a4a222282 | -3.1345 | -53.692699 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a12647d-1b09-325e-9a41-b349f64d367f | -3.1245 | -53.738499 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb9af0d4-7745-38db-982f-229d8c5a97a8 | -3.1261 | -53.745399 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4fcf50-8ebc-30e0-a1ae-743dd0826235 | -3.1276 | -53.7523 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4591b403-0a4a-306c-8121-6b82d134ef07 | -3.1292 | -53.759201 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9f25d6-90c8-3923-956b-0b26c5362d83 | -3.1163 | -53.747601 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94cfa142-59b9-3ed9-a26f-d0bab54b23af | -3.1178 | -53.754501 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff794d32-3584-3c89-97e0-f0cdd8e8c0a5 | -3.1194 | -53.761398 | 2024-09-28 01:10:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e435c79-127a-31eb-9c14-eca978c36077 | -2.8504 | -53.309898 | 2024-09-28 01:10:31 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e373ae0-b506-395b-b45a-8e7bcc62bbbc | -2.852 | -53.316898 | 2024-09-28 01:10:31 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39297768-8c71-3eee-8cb3-c36622e1248d | -1.1769 | -46.711899 | 2024-09-28 01:10:33 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf64e52-73f2-37ed-991a-33debb90bbfd | -2.6573 | -54.038502 | 2024-09-28 01:10:37 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3c5034-c927-3428-9207-c012bb027292 | -2.2207 | -53.664799 | 2024-09-28 01:10:42 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba6e3bbd-40d8-3415-81b7-f39d210ad09b | -2.2223 | -53.6717 | 2024-09-28 01:10:42 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa5e8d7-5cb4-30db-b744-7d472da9c07e | -2.2239 | -53.678699 | 2024-09-28 01:10:42 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7b0eb5-047b-324e-8a88-aeaf74d5218e | -2.2109 | -53.667 | 2024-09-28 01:10:43 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 029decf2-bda5-335d-95c7-8eb82e15d131 | -2.2125 | -53.673901 | 2024-09-28 01:10:43 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7e280f-3280-3f96-98af-af8db1d457bb | -1.5757 | -54.761501 | 2024-09-28 01:10:57 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c07dfc9a-8b04-376a-9d32-6789fcb5768d | -1.5773 | -54.768299 | 2024-09-28 01:10:57 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5a94db-b374-36e0-837b-4da5e983e22d | -1.5789 | -54.775101 | 2024-09-28 01:10:57 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b21e73cd-68ba-31a3-b416-5e574030b464 | -1.5462 | -54.947102 | 2024-09-28 01:10:58 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e0ad77c-327a-3988-9041-5f694f3f63be | 2.4388 | -50.7677 | 2024-09-28 01:11:47 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f720101e-009a-318e-802f-0e3d984924fa | 2.4364 | -50.778099 | 2024-09-28 01:11:47 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a2d5fc2a-e8c3-39fa-98ea-20e96c7e28de | 3.1341 | -61.178001 | 2024-09-28 01:12:37 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c38b6a0e-8d1e-34e5-99cb-be3101cae127 | -17.105301 | -56.167198 | 2024-09-28 01:52:22 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52c49e39-ce0d-3da2-80ce-9aa2e0ee3115 | -17.1113 | -56.188999 | 2024-09-28 01:52:22 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6961e49-b8ec-3968-80c2-ef338e883cf4 | -17.095699 | -56.170101 | 2024-09-28 01:52:22 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54d25d33-9aca-3fd4-a337-83bf54430e27 | -17.1017 | -56.191898 | 2024-09-28 01:52:22 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a54f279e-d68d-3ccb-bcdf-cae89a04a599 | -17.107599 | -56.213501 | 2024-09-28 01:52:22 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82df7ee3-dae4-39ef-9a16-b637af7d3b00 | -17.0921 | -56.194698 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05e14856-cfbb-3a07-93d0-c46e770fb68d | -17.098 | -56.2164 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbe99571-9342-3df3-b432-1a7f8b8ff9dd | -17.0825 | -56.197601 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fbd3dd99-8e4d-3750-9178-54cc8044ffed | -17.048901 | -56.112999 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ebff63f4-4227-3038-ba76-0d670703a73e | -17.055 | -56.134998 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1238d8bd-7144-36c9-8405-1f35ba00272b | -17.039301 | -56.115898 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21e6ca42-d01c-351d-931e-55af12cba185 | -17.045401 | -56.137901 | 2024-09-28 01:52:23 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed9a5ccb-55da-3c8f-a51b-79ace03f4694 | -16.988899 | -56.083199 | 2024-09-28 01:52:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79522023-a157-35b0-a4e9-9d78d169da2f | -16.995001 | -56.1054 | 2024-09-28 01:52:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a19d6e7-e3e9-3805-a960-ce78c460516e | -16.9793 | -56.086102 | 2024-09-28 01:52:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 383e8561-4c15-32cc-b30f-c9854342e50f | -16.985399 | -56.108299 | 2024-09-28 01:52:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e01f5e7e-16f5-3c80-bd95-50766a522aea | -16.9914 | -56.130299 | 2024-09-28 01:52:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bda103e3-10c4-36fe-89b0-6d0e255347a0 | -16.7384 | -55.8139 | 2024-09-28 01:52:27 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13f43f08-5eef-3d34-bc69-fa1bdf612544 | -16.728901 | -55.816799 | 2024-09-28 01:52:27 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06779349-5f4f-3346-9406-6f3f52ef07ff | -16.919901 | -57.9856 | 2024-09-28 01:52:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0dba9c31-22c4-3585-93cf-05e83df2322f | -16.910299 | -57.9884 | 2024-09-28 01:52:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c10c4eb3-b21b-3474-b05b-82070d50940a | -16.891701 | -57.9576 | 2024-09-28 01:52:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ae10225-91f4-36b2-8747-c9c2df977dbb | -16.8962 | -57.9744 | 2024-09-28 01:52:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67975ca1-bbf0-3c54-87a0-9b45a9b3a52f | -16.9006 | -57.9911 | 2024-09-28 01:52:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6453f28-c8a4-3be7-81ff-eb0165207105 | -15.5856 | -57.4874 | 2024-09-28 01:52:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44e3d314-51d5-38ec-b4a3-bf7511ac7abd | -13.4816 | -57.238499 | 2024-09-28 01:53:25 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23b5666f-43c1-3b97-a06b-dac5ecb60196 | -13.4719 | -57.241199 | 2024-09-28 01:53:25 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8de8bf-214a-3fb7-8f43-81ae9d4e4d26 | -12.6815 | -54.669498 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b51921c7-1c16-3f7d-81cc-db83b4106781 | -12.6905 | -54.702099 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd813b40-db81-3f89-acdd-997ed75e8f65 | -12.672 | -54.672298 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a00125a9-0314-3de3-b73a-8fb8bf9a6fd3 | -12.681 | -54.704899 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3551d530-f03f-3529-b9ae-5dfb20e7990c | -12.6624 | -54.675098 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6af0836-f5fc-324a-bcb8-f90271154b1f | -12.6715 | -54.7076 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc46479d-2f3c-3ef4-92bf-ce1c6183eea8 | -12.6804 | -54.740002 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9bcd7bd0-06ee-3fa5-876d-e41ffb8593fb | -12.6529 | -54.677898 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9147c7-ba0b-3adb-abda-e7e9da7ac9af | -12.6619 | -54.7104 | 2024-09-28 01:53:27 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56fd9255-f084-355f-910f-a397b74fb182 | -12.9869 | -62.687302 | 2024-09-28 01:53:55 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc004f8-c629-35bc-b29f-e24da4df82bd | -12.9892 | -62.696999 | 2024-09-28 01:53:55 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa121f26-b10a-3e9b-bdf5-4a0213889e83 | -12.9916 | -62.706699 | 2024-09-28 01:53:55 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45d6d9f9-513f-36e4-b938-376a047f3fad | -12.8504 | -62.721401 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43f0c0ca-fba4-3a72-82b4-7e1e1fd7ed29 | -12.8528 | -62.731098 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0413fd35-7089-3bd7-832c-7463976dede1 | -12.8551 | -62.740799 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1509055f-0293-357c-9d3e-99d0ce5e200e | -12.8574 | -62.7505 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2628d69-bb16-3187-a5bc-788c13b4bb22 | -12.8407 | -62.7239 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 485c1d70-b97e-3779-ac76-970583596144 | -12.8453 | -62.743301 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00dccd97-100c-358d-8a32-a0dba843dca7 | -12.8476 | -62.752998 | 2024-09-28 01:53:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf85215d-ef82-3f8f-be67-ad2d7c8f212e | -12.7711 | -62.6064 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3ebf87d-a4ad-3ea8-ba4d-2c57e7b8fc66 | -12.7735 | -62.616299 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3e27c94-38c0-35f1-aeb8-2b476de75775 | -12.7758 | -62.626099 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2a80baf-0183-3f72-9435-1d7cae8f5ec2 | -12.7613 | -62.608898 | 2024-09-28 01:53:59 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
