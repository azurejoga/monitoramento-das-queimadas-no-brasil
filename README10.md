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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aaf2bd9-49c6-3ea6-80d7-0614bd9b2e7c | -7.7593 | -44.75092 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 73f459d2-1c00-3824-951f-a04dc7d59038 | -8.08427 | -45.90797 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45e34fe6-55e7-3a4e-a64f-e923fd3f632d | -7.28929 | -44.08992 | 2026-08-26 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d018070f-c278-3340-af93-34bde380bdde | -8.07706 | -47.51106 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f00159d-a1f0-386b-90e6-2f191e1adfd1 | -7.14487 | -43.16967 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e729830-7b92-3322-aa10-6f56635a75c4 | -7.45014 | -43.11032 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99a94dd4-c6a7-331a-99a5-04379b89fb4b | -7.13999 | -42.77208 | 2026-08-26 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c588ad71-2b43-313b-92b5-42fad8e70461 | -7.32234 | -42.98153 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 853b8d1b-afb1-3e97-bf1f-c098d610857c | -7.76277 | -44.76546 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 123aa26f-2133-3abb-8823-074c3e5ab994 | -5.00695 | -37.5276 | 2026-08-26 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d5bc01e1-c0ac-3e99-bf0c-2c71117ba7e1 | -7.31129 | -42.99118 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9c8aef51-58ff-3cda-8ffa-76f7e22d6e96 | -8.08829 | -45.90684 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac16d183-fe19-3e01-8d85-a3f2e527b8c8 | -10.36994 | -45.06635 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 8d02bdcd-0583-36b3-8424-e3149d1844bb | -7.45134 | -43.10368 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5de4698-33e4-3c5f-bf16-0cd0e93ce8ad | -8.09729 | -47.56412 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f887b1cc-a6f8-3266-a084-af2ccfcca87b | -7.2764 | -45.36053 | 2026-08-26 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aede414b-5162-35b2-a8f7-fc2d5a03f873 | -7.31895 | -42.97877 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f1fa1a57-2615-3f5d-a900-80bacc4b8d4c | -7.45309 | -43.09404 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f87ce66b-7c0b-3d6e-804a-254cbbf07609 | -4.46409 | -38.51013 | 2026-08-26 03:47:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e0493f8c-3bc9-3488-8f85-5320f75b7ce4 | -7.45192 | -43.10047 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6311df32-117c-3401-b942-ec9239b8e851 | -7.15395 | -42.8144 | 2026-08-26 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b74e0e5-02a3-3c7c-aea9-d20ff497f94e | -7.75859 | -44.77167 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| db89268a-a347-30d1-9ba6-acfe84be2a9d | -7.75698 | -44.74784 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 65fc4e77-7154-3d06-be32-d018e3d5c737 | -7.76009 | -44.74654 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49f2f4bb-0df8-3056-b48d-eebb55c32cc4 | -8.06768 | -47.53092 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18fc5d87-9288-3ef6-bc52-7c68e039da6c | -7.76207 | -44.75319 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9faacefb-5a5f-3652-a970-d0dc0e526220 | -7.76189 | -44.77033 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d74d02e1-db14-3a62-bafd-48e245a1b926 | -7.45074 | -43.10699 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72603e31-f4f2-3ea9-99cb-de0d3a78e5ea | -7.2843 | -44.08496 | 2026-08-26 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 817bd150-14ca-354f-b5a6-f515bb8c7dd4 | -10.3768 | -45.06042 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 92516d1e-51fd-325d-92ee-dd849bba712e | -7.13763 | -43.17907 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c83d6450-2d2c-3268-b673-df16837f6443 | -7.31519 | -42.9906 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f6abbb19-98bd-3542-8846-0af979a0c2b0 | -7.75099 | -44.76311 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f150c2e-6647-32ab-a771-303e61f90b40 | -7.29001 | -44.08595 | 2026-08-26 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3af51dc9-b8cd-3dc5-aac0-c43fc1b3ebbc | -8.08733 | -45.91208 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d96385c9-ba35-3c08-9f06-3629d33fe957 | -10.37031 | -45.0632 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6f3e0c69-e7be-31ec-96eb-803d1a888d3a | -8.06893 | -47.52441 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d42f2b64-f40d-30e9-8510-c564193caade | -3.96752 | -43.10742 | 2026-08-26 03:47:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d59fef9e-81fe-346e-b2bb-d06a523276b8 | -7.45427 | -43.11796 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 802b2f9b-fb47-3bbe-975b-3fca911825df | -7.4525 | -43.09726 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15731642-dabf-330b-b04f-115adf3d6f9a | -10.04275 | -46.05062 | 2026-08-26 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6da3066a-75bd-3dfa-adc0-9cb7975862a3 | -7.75951 | -44.76678 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e13ccb76-9934-33be-b1a2-56ceb046557d | -7.75418 | -44.74553 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fdf3e210-ff30-365e-a255-577302cc8903 | -7.20276 | -42.75377 | 2026-08-26 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8dc6acf-44df-320e-a8af-f4b9a9631ad5 | -7.31826 | -42.97393 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15bdfddd-d428-3578-9d29-00284903da72 | -7.31954 | -42.97546 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6e06700d-5f82-3292-8f1e-d0b2ce09f63b | -8.75631 | -44.25404 | 2026-08-26 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a33c2b7f-0c0a-3d88-ae86-ff97a02f206c | -7.15337 | -42.8176 | 2026-08-26 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25fd8f36-a1b8-31e1-b314-c585d5336d0d | -10.36954 | -45.06724 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| eb13e537-56e6-31fe-9f85-cff0988357e0 | -7.26936 | -45.36406 | 2026-08-26 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e729f618-2d77-3bdf-99de-df7ea21ea62d | -7.76289 | -44.74883 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfdb5186-d095-310f-9101-09c43201ad38 | -8.06752 | -47.52288 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cff74d6-afc4-3d93-ba08-61db43aa6d92 | -7.75851 | -44.75531 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c28940ed-6201-33d5-89bc-c81df74c0199 | -7.29411 | -43.02636 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 119de160-62fa-3c43-bce2-7a36f32404a5 | -7.28878 | -43.02545 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e2889cb-eb70-304d-804f-47969629b430 | -7.75179 | -44.7587 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81cdafe3-9965-3b45-a723-84b4bf739a26 | -10.37567 | -45.06759 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 88d9a263-dbfe-37d5-bed1-4d7789293a74 | -10.03659 | -46.04948 | 2026-08-26 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 762e549e-c475-3c06-b7ec-f12da05b9f0b | -10.37073 | -45.06232 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 57b093fc-a1b2-3d7a-97f6-5c75231c74d5 | -10.37646 | -45.06355 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 95876a39-d175-328f-8f58-1ffb223158f3 | -8.08528 | -45.90276 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbe0f429-2ee8-3c65-ac22-857fc335030c | -8.09445 | -47.56863 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52f219c1-53fc-3cc9-a569-b103fcdf38ff | -10.0182 | -46.42236 | 2026-08-26 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a52ec3c-36c4-3183-b72f-e5d2767531a5 | -7.31581 | -42.98726 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fba6f949-116b-3f4c-b40d-f2d4f38ab1b8 | -7.27731 | -45.35565 | 2026-08-26 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a63b2828-3085-345c-9f52-d1fe0568efde | -7.19754 | -42.75282 | 2026-08-26 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d5063110-6b83-3353-ad62-60f016d9c0e0 | -10.37604 | -45.06445 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0c074661-a914-3a16-a493-bc5248b83353 | -7.31705 | -42.98054 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 155a3cf8-36dd-342e-9dfe-9c2bbcf15d8e | -8.08326 | -45.91324 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03009444-9f81-3b6f-b11d-997f2afc2703 | -7.31766 | -42.97721 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64b4d325-9cb8-34c4-adf7-3f37968e9ddd | -10.02453 | -46.42342 | 2026-08-26 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a080317-73ce-3f46-a774-8f65f6436706 | -7.75449 | -44.761 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 033b3de1-d328-382f-b2d2-f2844da655d6 | -7.27931 | -44.08005 | 2026-08-26 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e7c513b-fd67-3834-8a2a-ad2c40fbb76b | -7.75532 | -44.75661 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 385f9604-2953-3344-a2f9-297b06423f3a | -7.76125 | -44.75756 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 450bbfb9-3170-3383-ad2a-91155224caa0 | -7.31777 | -42.98552 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 666d2bcb-e04d-35cc-8540-3df940b632da | -7.31836 | -42.98214 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 43748011-cddd-3053-806a-87fcf222ceaf | -8.09609 | -47.57043 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a17efbc-6ceb-307c-b697-af9e4b1b009f | -7.13701 | -43.18253 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4cda46c8-5bc8-38ea-9a05-0c1bb62b9a70 | -7.27359 | -44.07915 | 2026-08-26 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28b412f6-c6b2-3a29-b32f-39f641a64969 | -6.91201 | -44.66693 | 2026-08-26 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dda28423-cadb-31ee-b05b-df901fc5d3da | -8.08195 | -45.90586 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e951de1-bda7-3a08-a17a-457baa7cda68 | -7.27552 | -45.36533 | 2026-08-26 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6ca667c-8ec8-3e2d-ba82-a923a9a514d5 | -7.7578 | -44.74346 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cc7069ef-6bed-3c35-a60e-34a45192863f | -7.76361 | -44.76081 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a91c6f0-a383-364c-b29c-ba1a58ab3671 | -7.74858 | -44.75995 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5373b758-63f1-3545-bae7-42c56df1eaf6 | -7.75615 | -44.75223 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0a6cde7a-f99d-3eab-b43b-d0ae872f1d82 | -7.32296 | -42.97816 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 27fc02e8-3ad5-3064-b5e5-5c0d05faa3f6 | -7.28348 | -45.35683 | 2026-08-26 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0106a884-5847-3e0b-890d-e72ea881afee | -8.7577 | -44.24658 | 2026-08-26 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e88acbc-a9cb-3c9a-869b-8d10b7f74791 | -7.45961 | -43.11889 | 2026-08-26 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b84fb7f-309e-361f-a461-a5d085146f0a | -7.76041 | -44.76199 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0fdba3eb-9702-38f0-b245-bcb9b8a594d1 | -7.14425 | -43.17312 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e6823a0-fd59-30be-a7cd-fe7e936fade6 | -7.29073 | -44.08201 | 2026-08-26 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3970a536-2f1a-39fa-ac26-fee87098e1f1 | -5.01077 | -37.52824 | 2026-08-26 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 095c2266-12e4-3c95-a21d-2c7382d739fb | -10.02301 | -46.41974 | 2026-08-26 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bacbb7d3-ee03-3e50-a109-d2e8a53a0077 | -7.76089 | -44.74218 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b780f15-4b94-3514-9aae-dfc5cfa66418 | -7.29499 | -44.09095 | 2026-08-26 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38548a0c-756c-3365-a524-bbd82c4b3e0b | -7.28502 | -44.08101 | 2026-08-26 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d7371cc-fc9e-318b-9a07-41a1444029c1 | -7.27025 | -45.35925 | 2026-08-26 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README11.md)
