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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef45bd1c-2bd1-3d61-9e29-046069c1bd0f | -19.7156 | -56.84076 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 1633c049-afc8-370b-9749-eeece6f226d3 | -19.71192 | -56.86319 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 88c125c3-0aed-3658-b4c0-17b67f8bdc64 | -22.3201 | -47.13678 | 2026-01-26 05:01:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3198ed7d-acee-3fe8-b042-947c389b2893 | -20.91743 | -56.38093 | 2026-01-26 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef334cbe-0657-3147-8030-4306cd6449c6 | -20.31396 | -57.82318 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f1723103-b25a-3e65-b303-2857a5c044a7 | -18.82773 | -57.71753 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3202c2dc-1c70-3708-8a3b-e0670b313f4c | -19.62571 | -57.34156 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 181c12d5-6425-3280-94db-2376a5f7850e | -19.61239 | -57.29583 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f1a16dad-fa06-38ed-9350-d4340dd83754 | -20.31462 | -57.81929 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f29e9f7c-c189-3cad-96f4-f582613ed83d | -19.6539 | -57.31925 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 54d9e4b0-acff-3777-a5e8-8a9e84956ebe | -19.66649 | -57.18051 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 38a7dab0-6078-3154-adc2-fea906fab746 | -20.30989 | -57.82644 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5cf63b32-6553-3877-b127-50d525d81298 | -19.61048 | -57.30725 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 574e5d09-bcb7-3e0e-ac03-1ca178ef3dbd | -19.64923 | -57.26342 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8b6f0085-e8e6-3b2e-935d-312158b0ab64 | -19.60753 | -57.28315 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8aee4577-fdcc-3eaf-9161-7914e395deea | -19.66088 | -56.85003 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 704c06d6-9c9e-34d0-ad3a-ed9d1083c271 | -19.65496 | -57.35487 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f9ddc45d-479a-3568-864e-a4825e641bd9 | -19.6921 | -56.83647 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bf8e4917-85b2-3560-bd65-8538df234cdf | -20.31804 | -57.81993 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b14938ff-3df5-3d55-b263-f9ef16eb9b83 | -19.66619 | -57.3294 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 68fc2ca8-aedb-3cff-b0e1-1692fde851c3 | -18.82429 | -57.71689 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 92b2cd6f-26f8-3d09-8187-b0a0d81eb2b7 | -19.64267 | -57.28181 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 662b935f-a33b-34bb-8493-73391271cecb | -18.82151 | -57.7123 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e26eff94-0920-37ad-bf58-cbfb7cbf89f8 | -20.31055 | -57.82254 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8cdb48df-c912-382b-aa56-a08bab3510a3 | -19.66407 | -57.32113 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 217e2e85-7f7d-3503-905b-34f48e4d8617 | -19.61681 | -57.33204 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5f61617c-dfeb-305c-b9cf-e66151ad0595 | -19.61387 | -57.30788 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc9a91cc-c981-3a88-80f5-9d06e2390cd4 | -19.65517 | -57.31162 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 035a49ce-ea53-3828-b562-7598144a1c01 | -19.6522 | -57.2875 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77e1be45-af1a-3450-b1ae-12380a121e8a | -20.3187 | -57.81603 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0f6a95a6-10a7-3532-8c03-669c8c834379 | -19.66958 | -57.33002 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 44e3161a-b226-3a43-9130-1889446ec4d4 | -19.70553 | -56.83892 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 11f48f2b-f380-3d51-b31a-5d68dc419b02 | -19.61451 | -57.30407 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2080bd02-96d2-3c5e-9203-4db86b67b4c5 | -19.70278 | -56.83458 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 59bfd1da-cedb-3052-8e46-46d11c0d057f | -20.56268 | -55.55808 | 2026-01-26 05:01:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 793fdc6f-6bc3-3754-96c9-7072ec3b75c0 | -19.65897 | -57.28876 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d0a5f0c5-bc45-3bcd-ab04-e799017e98e7 | -19.61342 | -57.33141 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b740f512-cdc6-3099-85eb-d5cd0afb83d4 | -19.65835 | -57.35551 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e84ebd36-4b49-3314-be5f-1a5c2b448587 | -19.66424 | -56.85064 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6be74ab5-d7e1-3640-be57-15a466fc3250 | -19.61028 | -57.28759 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3cc3af6e-ba8d-3d55-acd0-9ae3f7e46a97 | -19.6647 | -57.31732 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 00d38d7c-39fd-3719-ba11-2e798cf146f4 | -19.67217 | -56.84439 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6e2bde90-e9c7-3c8e-a207-86f422d1d19b | -19.67388 | -57.17797 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a1238d15-52ec-36b8-a244-d6c7d2b6817e | -19.64478 | -57.35298 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a3b0ba75-9498-3f14-9464-b7ed04a66576 | -20.32146 | -57.82058 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7b0f2dee-2c7f-3f31-b4d5-d8f504d54ec0 | -19.63524 | -57.34728 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f40176d9-724f-38f5-afc8-1f1c46ec720b | -19.61092 | -57.28378 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d180dbe8-a2b6-3c40-af7f-34911358817e | -19.71224 | -56.84015 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| d28e4fab-c1f8-3725-9ca8-d2565c4448c6 | -19.71253 | -56.85946 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6ecc7479-f8d0-3142-85e1-a4edd5b62939 | -19.65432 | -57.3587 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6206e733-ece4-3200-9c4e-8c050ffc5a69 | -20.31936 | -57.81213 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 088bb8a0-4d67-3688-a030-58c642bc2595 | -19.61323 | -57.3117 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 26fce12d-49f8-38b1-a2f3-c7b0ca6a78f6 | -19.71621 | -56.83703 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 9ce023e0-14e8-3eef-b35c-3e1a9c56f0fc | -19.62846 | -57.34602 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e7bdfc22-54f8-3e0e-bcf5-27f347761dfa | -19.66174 | -57.35614 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d297c417-1ccb-3a85-a75e-fc552d2ab309 | -19.61956 | -57.33649 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 79416e06-bfa8-378b-a96d-05ac8b4120fc | -19.65283 | -57.2837 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cb27c972-6a53-37dd-9004-c419414d2a5f | -18.77599 | -57.65624 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9ac53cd9-3139-370f-ac66-973d7893d579 | -19.67431 | -56.85248 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2ae86af8-a727-316c-a307-9e278b336252 | -19.69607 | -56.83335 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 28f3447c-51ea-38ea-83ff-86c2c8af63bd | -19.71896 | -56.84137 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 5c568fd2-3363-31ac-acc5-ee15de02c19c | -19.61067 | -57.32696 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1d65f5ae-01b6-3790-a5cf-c9370742cffb | -19.64817 | -57.35362 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8df7a30e-4945-3f3e-b8b4-de9cfefa9195 | -19.66236 | -57.28939 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e3ab8700-b354-3852-8442-bbc74f0ae69b | -19.72048 | -56.8532 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c25ac746-3c33-3087-ab9c-e6761e6914df | -19.66881 | -56.84377 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 502da4a6-3cdd-33ae-b8c9-0bd8c0aa6c5a | -19.64584 | -57.26279 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 712a507b-2020-30fd-b1b4-8b2ecee36d7b | -19.63461 | -57.3511 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9ed4e34f-ed96-3e5f-878a-a28cc6d9e1f4 | -19.62232 | -57.34093 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8256da25-724b-31f0-b5b8-f9d81bffa7d7 | -19.64944 | -57.28307 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e38548ca-02e9-3539-91b6-aa8f58ef40c3 | -18.77534 | -57.66017 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 27a1d17b-49aa-3c68-9103-c5939c09ebb8 | -19.63185 | -57.34665 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5aee1b2a-793d-376d-9944-5730e9c54ccb | -20.91861 | -56.37352 | 2026-01-26 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4ee533c-3c06-30da-a752-3ed91d39d750 | -19.70889 | -56.83953 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 2df75db7-c997-3cef-ab61-763314de047d | -25.20592 | -51.3891 | 2026-01-26 05:01:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08022bc4-e239-3bfc-b6e9-abb8df295790 | -19.638 | -57.35173 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 99794923-6016-3903-a5a7-389a7cfb8d61 | -19.65093 | -57.35807 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 70a19ba4-d003-3ea3-9cf9-a5431c3835fb | -18.81806 | -57.71165 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bcfe35ae-8af0-35dc-8d0c-3080057f315f | -20.32212 | -57.81668 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a65b1f3c-2260-3c0b-a31b-e398d1f0f095 | -19.64606 | -57.28244 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| be9395c6-93b0-3657-8610-7270074db164 | -19.66712 | -57.17672 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 851d523a-2a5b-3009-83db-358d605863f7 | -19.70614 | -56.83519 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 62f001ac-558c-33a1-ada5-a5a3e9b131b7 | -19.70733 | -56.87006 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 370828a9-b0e1-3f64-8520-daee7b3d01d3 | -19.68126 | -57.17543 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a0522b4a-03e9-34ee-965d-437047edb3f8 | -20.42198 | -53.22631 | 2026-01-26 05:01:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d74094e1-e5f3-3130-bca4-8f5a489a9764 | -19.69546 | -56.83709 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3c680bfc-261b-359f-99e0-6374c199c1cb | -18.82706 | -57.72147 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| fbf44b31-210f-3d94-9099-f060b4793811 | -19.64542 | -57.34917 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e6ac3280-1c05-34b1-b0c2-2785dab74ec8 | -19.61617 | -57.33585 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3b0c50aa-9426-3005-92ae-f0a2d863af6e | -19.67788 | -57.17481 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ad119bd0-6b9c-3e1c-aee5-f72987db7fde | -25.47353 | -52.75692 | 2026-01-26 05:01:00 | NPP-375D | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a673375c-9fed-31ee-a0ca-fe8656643e68 | -27.33058 | -48.87384 | 2026-01-26 05:03:00 | NPP-375D | SÃO JOÃO BATISTA | SANTA CATARINA | Brasil | 4216305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dcb434a3-416b-35f5-89da-83388bd3ee63 | -26.90504 | -52.88252 | 2026-01-26 05:03:00 | NPP-375D | NOVA ITABERABA | SANTA CATARINA | Brasil | 4211454 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbfcf0d4-c47f-339d-92f3-9b67e78c5e12 | -28.10522 | -50.50182 | 2026-01-26 05:03:00 | NPP-375D | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a621043c-8b89-38ad-90b2-34821a449292 | -19.7242 | -56.8408 | 2026-01-26 05:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 3869d675-0d41-35d5-855e-0764576efa2a | -19.7041 | -56.8436 | 2026-01-26 05:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| a7f84070-92b2-33b8-b8da-95bd935ea826 | -3.00264 | -52.87276 | 2026-01-26 05:16:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2cc10a1-2910-3297-a811-e083ebb56ce3 | 0.87291 | -59.61633 | 2026-01-26 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce14049b-2c47-33bb-a1c4-adfc11098b22 | -3.00321 | -52.86908 | 2026-01-26 05:16:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebc343d0-73f9-3c99-ae8a-da63f3ba89ac | -19.7041 | -56.8436 | 2026-01-26 05:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |


[Clique aqui para ver as próximas entradas](README6.md)
