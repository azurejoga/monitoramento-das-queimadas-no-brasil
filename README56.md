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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f0edff8-bb39-3cc8-969e-004708c1a734 | -14.00529 | -53.66788 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b6a2fda-bb39-32f5-a530-db332fec67a7 | -18.76649 | -43.80235 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b911030c-7b05-3d49-94a4-59ef8e795603 | -12.95218 | -56.6399 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3474b8a7-c7a4-3fd6-b166-efa333dace91 | -15.31378 | -53.79953 | 2026-08-22 05:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f2a6230-cfaa-3ef5-8959-6f420e49377f | -14.04556 | -54.1035 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c78f6d19-6f7d-32f8-ba6f-085a81decd77 | -14.12536 | -48.06543 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d4f432b-a81c-3e1e-87d7-1fee652c2ee4 | -13.92563 | -58.25847 | 2026-08-22 05:06:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9d91db8-d5b5-3331-9733-20eab962ba99 | -13.95344 | -53.85468 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d73ca12e-9285-335b-9dbd-4a0108df0d4e | -18.52878 | -48.24736 | 2026-08-22 05:06:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f3e0d5c-9330-39ca-8eac-2a8c4e9f94fb | -14.01422 | -53.69876 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7397c57e-2745-37fd-b554-78cc401a092f | -15.2371 | -52.8326 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7012d562-b345-3835-a588-527cb8cb6501 | -14.56483 | -53.01701 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d60a1016-2931-37c9-a854-aee240b6c0c9 | -13.95067 | -53.85055 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe40238e-0cdf-3c6d-bf30-ddbd48be8a9f | -13.98533 | -53.67231 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05ab9b22-de1d-3037-958f-74f0e9bd3482 | -13.92935 | -58.25915 | 2026-08-22 05:06:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fe0ab4e-57e7-3c64-b207-947ba8690f1d | -13.99257 | -53.66982 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12f73be0-b326-3840-842e-c40dbf492c03 | -13.94734 | -53.85 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbbe47e5-780d-31a3-9a91-edb62e6106d2 | -15.63853 | -47.72681 | 2026-08-22 05:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 068c9167-c032-3108-bd96-b3cd8f7c7314 | -15.17841 | -48.74425 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1bf90c0-6e72-3979-924c-3613d6703d09 | -13.40356 | -54.35946 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a4ed299-badc-35eb-8beb-4998f22065b0 | -14.30885 | -51.83239 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba0c9ca-c53d-343e-8a61-33f730e12cbd | -20.63367 | -47.43724 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 27.4 |
| df3e2cb5-5095-3a98-8933-bd9b0b077903 | -21.06202 | -47.34621 | 2026-08-22 05:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19fa7e4a-c147-37e2-b99b-67ba7c9025b8 | -21.59592 | -44.00562 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2a23eb3-18c7-3167-9d14-fc224adc29dc | -21.60176 | -44.01155 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5895f3d-bce9-31dc-8d0c-da163f9ccf12 | -20.63445 | -47.43736 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 6310ee20-367d-3a86-8314-a759d8dbd11f | -20.62803 | -47.4424 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 25.5 |
| d1c14fab-478d-3f22-8b81-95167c0f6493 | -20.6381 | -47.44369 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 1c37a369-fd1b-3512-8e0e-6eb01784d73a | -21.06233 | -47.34314 | 2026-08-22 05:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 776dd6d8-b82d-311c-846f-b337676edd10 | -23.82768 | -48.71341 | 2026-08-22 05:08:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 880a608a-97da-3a3d-8e00-390b124c1c79 | -23.82285 | -48.7128 | 2026-08-22 05:08:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7be6911-59a8-3128-a3f9-27604924bc58 | -20.62941 | -47.43672 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 2592fb1b-d474-322f-a491-2b0501333112 | -21.06742 | -47.34387 | 2026-08-22 05:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ac25dbc-9f3d-3c1a-aa64-7b5f178b6e87 | -21.59894 | -44.00688 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 506daede-cbcb-334c-a80f-618919b878b3 | -21.06711 | -47.3469 | 2026-08-22 05:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d9e1c6d-d815-311a-a5d8-4cc73027294a | -20.62864 | -47.43657 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 782a00b6-0a58-3035-8f30-496efca411e4 | -21.49456 | -48.03914 | 2026-08-22 05:08:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a528c3-22c8-37ee-ad50-3e18291f3879 | -20.62876 | -47.44257 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 07dc46a2-929f-3a55-897d-47b1dc0caec4 | -20.68122 | -57.2025 | 2026-08-22 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08c79e6f-e344-3e23-a24e-002d8109d15e | -20.43929 | -54.69039 | 2026-08-22 05:08:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30ea0e9a-6f12-38ce-8b03-4fa8c8f94096 | -21.60222 | -44.00642 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b962dea-053c-3083-a75e-137117fc2c2a | -20.63306 | -47.4431 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c890c5e0-dd0a-3d7b-89c6-b667d280b4dd | -24.05567 | -48.84209 | 2026-08-22 05:08:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a1f6929e-34d6-3040-a8ce-36b9ef840c03 | -22.09806 | -46.65496 | 2026-08-22 05:08:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d64bc7f1-d873-366e-afd3-00289a4db4e2 | -22.09841 | -46.65139 | 2026-08-22 05:08:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c33309ec-ac72-3dff-8dc3-d9c92a1cb5da | -21.59263 | -44.00615 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| acfc54c3-e20e-39c9-9c5c-ec26a8981234 | -21.5985 | -44.01221 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 99e0ded7-5c6c-3a0c-8312-ff524ec4427c | -21.59544 | -44.01104 | 2026-08-22 05:08:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d23b8d00-c9f8-35d6-88d9-182e623f7d03 | -20.63379 | -47.4432 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 1fe678e4-4004-3a14-86e9-35b1c676075f | -23.96572 | -55.26684 | 2026-08-22 05:08:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dc41243f-58d1-3cbd-a346-f884ca3e7648 | -20.63315 | -47.4489 | 2026-08-22 05:08:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f3cb369e-5447-3e93-b12f-efbf8390c767 | -25.41037 | -49.9459 | 2026-08-22 05:08:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d690a117-318c-3684-9134-3929038cd211 | -21.55004 | -53.77878 | 2026-08-22 05:08:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb77a73a-510f-3616-865f-161cb1754013 | -8.9042 | -60.5385 | 2026-08-22 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b1eab3a0-2d6e-35e0-83f2-5964e634d370 | -8.5406 | -54.8197 | 2026-08-22 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 781a020d-2fbb-3864-8374-1668f05fed01 | -9.1909 | -59.4619 | 2026-08-22 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 5523e014-a393-38a3-b060-c0273eb6018e | -6.7691 | -58.6873 | 2026-08-22 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6fe97ef9-053d-3866-a8f4-42ab68171ea6 | -20.6358 | -47.4322 | 2026-08-22 05:10:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5ceeded4-9331-3fab-b972-d7225c979d58 | -14.3937 | -51.8012 | 2026-08-22 05:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| d97db0fc-5348-3eff-8359-161d74e8fb2d | -6.8188 | -59.6696 | 2026-08-22 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ab118278-c6a9-3163-9987-cad8e971a701 | -6.7507 | -58.6687 | 2026-08-22 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6b9a02f3-704c-352d-bfda-c3eb0546af02 | -9.1722 | -59.4629 | 2026-08-22 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 97110eb1-12ef-3cad-bcba-df6b2fa48545 | -6.7692 | -58.6679 | 2026-08-22 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| fb6cda0d-8615-3b0b-ab2d-b2e77277a6f0 | -8.522 | -54.8209 | 2026-08-22 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 09a5e6d3-f350-325c-a092-9d0265181284 | -9.1724 | -59.4436 | 2026-08-22 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2c0eb344-2c5c-38e8-99d9-368adc99d2fb | -8.5404 | -54.8398 | 2026-08-22 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3c381fa7-1ccc-316a-8603-f78918db7762 | -9.1909 | -59.4619 | 2026-08-22 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6518a88d-7630-37ba-9a32-08fa793e3eba | -8.522 | -54.8209 | 2026-08-22 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 11ddde9e-82c9-3308-84b5-d7848666a8d9 | -20.6358 | -47.4322 | 2026-08-22 05:20:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ca0ab43b-7ec1-314d-82d9-b13557c4fa64 | -8.3904 | -62.6774 | 2026-08-22 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d64fb82f-8aff-3ab7-bba0-1afe5314e9fb | -8.5406 | -54.8197 | 2026-08-22 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ca40474a-7650-3830-810d-b4acf957a088 | -8.3903 | -62.6963 | 2026-08-22 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fa51fa47-8d74-3594-a331-55ef50682e9d | -6.8188 | -59.6696 | 2026-08-22 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c9eb4ef4-c2f2-3477-887a-ad82c0e23ac7 | -9.1722 | -59.4629 | 2026-08-22 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 4ca3af94-844b-3ac2-95e9-8a9c31e2f7c4 | -6.7875 | -58.6865 | 2026-08-22 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 683c9984-3366-3af1-ab05-1bd26075d256 | -9.1724 | -59.4436 | 2026-08-22 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2348cdb4-a252-3f2a-82ac-e0cb46c0d457 | -8.5404 | -54.8398 | 2026-08-22 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0a9a5a79-dd07-3161-b702-9bf19b7b7f3a | -8.9042 | -60.5385 | 2026-08-22 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1e6797b9-6250-3c3a-85d2-9eaf90c23b5e | -6.7692 | -58.6679 | 2026-08-22 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f4ba304b-6b67-37e7-b574-55fe3e14dea3 | -6.7507 | -58.6687 | 2026-08-22 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 50553220-20c1-3dd0-a2e5-9b3470986bae | -14.3937 | -51.8012 | 2026-08-22 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b735170b-5096-387e-b442-d3de089ede36 | -6.7691 | -58.6873 | 2026-08-22 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 7cf1cc2d-ec5c-3e49-add8-5d53c2754e11 | 2.7928 | -50.93048 | 2026-08-22 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a6c2f2-8c91-3b2a-8345-34132c092ea3 | 2.79348 | -50.93463 | 2026-08-22 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 600fda61-a733-3e69-a41b-567ab7988a84 | 2.79782 | -50.93393 | 2026-08-22 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4cd4e03-6c00-3350-98b6-1f61c64e05dd | 2.79714 | -50.92978 | 2026-08-22 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecf8bc67-341f-348c-b4fd-8826d063a4ce | 3.59192 | -60.95839 | 2026-08-22 05:21:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a864d39b-01a0-347e-9f81-fff5ab288d8d | -6.00999 | -57.79783 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8917dadc-f2f9-3637-8b2e-af0038cab713 | -6.43419 | -54.96116 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d12470e0-2073-3ea4-93e5-560a3a6a15f2 | -3.82554 | -55.67014 | 2026-08-22 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa868a3b-2194-39d5-8978-7b5bb57839be | -8.53059 | -54.81772 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b96e4a19-9cda-3c9b-b986-e012ba6675b8 | -8.52359 | -54.83776 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812b8e5b-6627-34c5-bba8-892705512855 | -7.17925 | -60.64489 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3dd141e-a2c1-341d-b04e-1b7711425358 | -6.77711 | -58.66639 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e151fc2-d63a-39d7-b8ed-b335e6c4be74 | -1.98579 | -56.45948 | 2026-08-22 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c552c02e-0df1-306f-a81c-98555a786160 | -7.10414 | -59.77676 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7118cd8d-f5f9-3a2c-a3ee-057f89e47fee | -1.98804 | -56.4673 | 2026-08-22 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60f66947-52d0-35f7-b6d0-399a0577ae18 | -6.26988 | -62.52453 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42701f00-fd9a-3138-8696-6506cccca5df | -13.99466 | -53.70897 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9421578-2b60-310d-90d4-e119bda72be9 | -6.86817 | -59.44444 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
