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

## Dados Diários - Página 248

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e8e923-061d-3b2b-af40-0dcaadf97856 | -9.8246 | -65.016 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ce31b93f-116e-3e87-96ba-00ef34c2dcd7 | -9.5468 | -64.8196 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| e93b6968-728a-3236-9b87-5946875e5b2d | -9.8059 | -65.0354 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6ab39060-7eb4-36cd-9659-503b2bf49486 | -3.1697 | -58.6437 | 2026-10-07 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| fafb5f3e-44eb-3214-83e8-217a684ec190 | -9.8431 | -65.0341 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 19904d8f-94b7-34e9-b9a8-bdf1af852102 | -4.1223 | -54.0158 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ca4749d0-d900-3382-aa6f-f1bc959bcfb5 | -3.2214 | -53.8818 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 7304c9ce-375b-3479-8c5f-774dbae8551e | -11.7139 | -43.6757 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 29bdb965-df12-34f5-a57b-dfabc8ae50d2 | -7.3744 | -46.2385 | 2026-10-07 18:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 449f8abd-c2b2-35a3-8376-b1fcd1cac00a | -9.9779 | -43.5491 | 2026-10-07 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d0bf143c-68aa-3288-ae8c-e8779edcadcb | -9.0406 | -65.9401 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 58d0eef0-8621-3c7c-a2e7-f17604181406 | -16.1669 | -43.6351 | 2026-10-07 18:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 71c49428-2356-321b-b7f6-d94a77daea96 | -3.6612 | -54.2715 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9fb6cbce-d392-33aa-9d7d-a88d01029785 | -4.0947 | -52.0635 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 27bbf959-0178-3b9a-b118-e21de7de2ae8 | -4.2558 | -46.3855 | 2026-10-07 18:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cf73bd02-37eb-37ab-aa34-3cb55ba3e451 | -3.2577 | -54.0217 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f4a235d9-b8a8-3eb0-ba57-507d873eed81 | -3.2576 | -54.0418 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 236.4 |
| fc8d0410-24aa-365e-b105-3a11e2a8fa2c | -3.0559 | -53.9062 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 340.4 |
| 04648e25-2ddc-3ca9-9da6-dcf8f867fee9 | -8.2181 | -46.362 | 2026-10-07 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 6da58347-ed1f-31a4-8691-cf7dab5d6175 | -9.9787 | -43.502 | 2026-10-07 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 1d19f8e5-3b18-37f3-be6d-5c68bfba98db | -10.9946 | -45.4527 | 2026-10-07 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| f95a7df7-9529-3b7a-9671-3a365bffc476 | -7.6803 | -70.0128 | 2026-10-07 18:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c3be891a-0638-37f3-970e-0f7c8e5bc230 | -3.1655 | -54.0844 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9e2bbb05-b0db-3fa7-850b-9ad9bb0ee42e | -3.8529 | -42.2394 | 2026-10-07 18:20:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| bddb48ee-3fa5-3305-8d75-6f3db3391ac7 | -5.7927 | -45.2626 | 2026-10-07 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 0d174690-62d8-37c7-a2f2-7b74f5187d5a | -3.2211 | -53.9623 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9fb386da-1817-33e6-9a9f-ac82ab16f1a8 | -5.7659 | -42.0389 | 2026-10-07 18:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 279.8 |
| 0b06813a-61ad-306b-886e-dcd103bc6d43 | -9.1356 | -65.4145 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 8334f998-8893-30ea-bbd1-64dc8af6209b | -13.3676 | -43.8504 | 2026-10-07 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| f83cc31f-89c7-3187-9027-41e5b54a6443 | -3.7811 | -41.7675 | 2026-10-07 18:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| ce31c664-7dd8-38ff-9dbe-fb61c8fdb8b9 | -3.0605 | -58.4145 | 2026-10-07 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 09a38c1a-a705-3ab9-81fa-776699cbcd69 | -9.432 | -45.8293 | 2026-10-07 18:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2f575db1-e85b-38a7-bf69-3e3542b27bbc | -6.02 | -51.7272 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 9a9458e8-a1c8-3195-b395-d14e653930ad | -3.7809 | -41.7913 | 2026-10-07 18:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 205.2 |
| 72ad8a98-7b92-30a0-a374-8dd5fa992c86 | -3.2357 | -50.1805 | 2026-10-07 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f37cdc8f-f5a8-374e-aa5d-ec45c8365565 | -3.6197 | -55.5089 | 2026-10-07 18:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| aee5b52d-3ae2-33d6-91ec-a24e48443a0f | -11.7143 | -43.652 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 287.0 |
| 12d98661-e293-38f8-b023-c494d30fe9d7 | -3.8786 | -44.1265 | 2026-10-07 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 6aad0730-df8b-3dce-8ebb-cd035e08d442 | -1.4771 | -53.6134 | 2026-10-07 18:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| eb79e8ab-2150-3887-91b1-fbb216af7de7 | -3.6603 | -54.512 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4ec48967-3103-3faf-8515-9d53ef699f9f | -9.0591 | -65.9396 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 0db02de6-4030-30c4-aa63-142b5944c163 | -5.8114 | -45.2612 | 2026-10-07 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e7c06363-e42a-3b0e-9b7f-f6e03e3ba11b | -3.5495 | -54.6352 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| feaf37bf-c38a-391e-ad86-1e55bb1dbf9b | 1.6937 | -55.6263 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2acd42a6-075f-3a5c-ad80-5815479d9042 | -8.5093 | -70.0555 | 2026-10-07 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 110.8 |
| a5a68e93-2edd-38b5-965b-6471bfc42529 | -6.5794 | -41.5841 | 2026-10-07 18:20:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| ded13ac8-3e8c-376e-8bd6-88b2a1fe8181 | -6.0447 | -53.49 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 437037aa-6e46-3fd2-bc3d-d762cc82f66a | -9.6757 | -65.0401 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 6b06d2a5-c81a-3d78-a9c1-d9d65fbfaef5 | -8.9082 | -49.986 | 2026-10-07 18:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 71ba9c02-046c-3d14-9c9b-a382243ddd9c | -3.13 | -53.7229 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4a617e0c-79f9-3b03-b218-b448509fe6ab | -7.3747 | -46.2161 | 2026-10-07 18:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2294d063-be5f-31ca-8936-38ce7c19c3e5 | -11.6951 | -43.655 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f108293d-0633-35de-85d2-1be264358a4c | -13.885 | -44.1365 | 2026-10-07 18:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f6cd42e0-497e-3843-8b98-50782ff0655d | -3.0374 | -53.9268 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 439.5 |
| 2243812c-9e90-33cd-9f6b-8db0cf04e6f7 | -9.0988 | -65.3596 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 4df22971-ff13-33d5-97f3-6efb1b522a28 | -4.5782 | -54.942 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 13b62751-207b-3711-a8e2-6f6f315003d0 | -3.2717 | -50.4102 | 2026-10-07 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 72f86635-baa5-3a81-837e-91ba6e3216cc | -4.5345 | -43.7219 | 2026-10-07 18:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 32d7df03-bffe-37a4-88ab-596db0c710fe | -11.8508 | -43.5361 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 670bddce-f4a6-3111-935e-9403b81e8372 | -5.9647 | -40.9383 | 2026-10-07 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 317.3 |
| 37808cdb-b466-385b-97bc-870174445526 | -3.1116 | -53.7234 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d03ba9f8-b4db-35a8-a47d-0a7ea0b2e8c0 | -3.295 | -53.8597 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 4966f921-7321-3c2a-8662-9c77e27dd6ca | -6.9328 | -43.6799 | 2026-10-07 18:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9ae43cb9-c9f0-3f4f-87f8-920a402ab0cf | -5.9833 | -40.961 | 2026-10-07 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| dcbd2a8e-53dc-34c1-a867-2accedc31ca9 | -2.1361 | -54.4671 | 2026-10-07 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 71ac17b0-b600-3d8b-b227-2f80c1bd3a0a | -8.2181 | -46.362 | 2026-10-07 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a2e66548-bdaa-3aa8-a497-76a7c3d9c96a | -4.1407 | -54.0152 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3982eb00-0969-33a1-893d-a085ceab43d1 | -9.8059 | -65.0354 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 15a21708-b425-3756-a500-c125a4ab3ae4 | -7.2011 | -52.6272 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 86da930b-deff-3d2d-ba05-7ba90716c98a | -5.9835 | -40.9367 | 2026-10-07 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 179.6 |
| 8f7e7adf-1923-3707-9e3b-557cdd68bddf | 1.7121 | -55.6063 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ca97916e-a38a-3048-b3bb-ae5bf200a15f | 1.712 | -55.6459 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f258ba3a-1bd7-3935-8b1a-89bdc39cbc01 | -9.5177 | -67.0987 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 62785f8f-fc42-35a0-9b6f-7542d13d53a2 | -2.951 | -58.3201 | 2026-10-07 18:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 54d15d11-3291-386c-9f83-38982473d256 | -3.2957 | -49.1202 | 2026-10-07 18:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b5906fe3-7624-37c4-b1a9-5d979786559e | -7.1827 | -52.6078 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 82bfc83e-236e-3849-913d-9b35487c1247 | -5.9644 | -40.9627 | 2026-10-07 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 178.9 |
| cfdf87fc-a3b2-32ea-a1f9-c9a7cc115f69 | -5.9699 | -53.5953 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c317c201-2e9a-348a-bc8d-154d84033341 | 1.7671 | -55.5859 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 02c16ed1-5341-35db-a972-1a0c98c20d71 | -8.0837 | -70.831 | 2026-10-07 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 681a8f5d-179f-328c-9753-6337f6ea5ad0 | -3.2214 | -53.8818 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 630ce965-15d0-38c1-ac01-b04cf38885f1 | -8.6292 | -67.0111 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 199d6ab1-8f7d-335f-8b6a-a2e4f1739da1 | -11.7362 | -43.5068 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8f12c82b-505c-32d8-a1f3-07635b24cf9c | -3.2199 | -54.3038 | 2026-10-07 18:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a3f5971d-ff17-3cbf-b430-51a4623b2f24 | -3.1973 | -50.5382 | 2026-10-07 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 636a73ab-1031-3fb2-8e63-eb659c5a1e71 | 1.8768 | -55.7227 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 03ef1f35-9082-3f54-95c7-462131abb1b0 | 1.7121 | -55.6261 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 8f38b745-c646-35bd-b051-5889b0d2b317 | -7.9178 | -70.9245 | 2026-10-07 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 672721ed-9e18-3df1-a107-ddfae7b2cf5f | -9.5468 | -64.8196 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| f61d9982-18d2-3e26-9339-33d5b2836bc9 | 1.6937 | -55.6461 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 6b4cb931-efa5-332d-8a58-33a74076af94 | -11.7139 | -43.6757 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9b813d41-c0ff-3bdc-b3a5-788890ddb4a2 | -3.6612 | -54.2715 | 2026-10-07 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 48bcbf71-cf58-302d-b944-96c2e231243f | -11.8503 | -43.5598 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| f4b7d9b9-595a-33a8-b192-7c8c2a6e3589 | -2.0026 | -56.9575 | 2026-10-07 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a51636bb-d9e1-304e-b6dd-f06fec6c79df | -3.295 | -53.8597 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 928821e4-87c4-38fc-91dd-5c265b6cdf73 | -6.02 | -51.7272 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9083cbfd-7ad2-33cf-aad5-15dce9a8912b | -9.7126 | -65.0951 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4a4cec16-e3bd-32ce-b5bf-c3df47751280 | 1.6385 | -55.785 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 49cf02d0-2226-367b-8731-ae3f9ed62699 | -13.3865 | -43.8708 | 2026-10-07 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| dbf2f2a8-ecb7-3228-9f29-b89ce1aeb594 | -3.1655 | -54.0844 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README249.md)
