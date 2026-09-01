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
| 74deee6a-0e3b-3d90-b515-c0ff2a376e40 | -7.2005 | -60.6897 | 2026-09-01 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7162fb47-b42a-3059-978a-f5b8b8bd4bda | -7.571 | -60.4643 | 2026-09-01 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| f03cf1b8-5ba1-3b37-a68b-61aa179e1f50 | -4.7734 | -41.8026 | 2026-09-01 00:20:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 14259bc4-56d1-3b13-b5a4-b060cdb309c0 | -16.4773 | -47.9381 | 2026-09-01 00:20:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c142bed6-6fca-3158-9d65-12463e448bcc | -10.0173 | -44.6849 | 2026-09-01 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| edc49313-a408-3ca9-bbeb-efd89157c994 | -18.4888 | -50.901 | 2026-09-01 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 2db06e16-7278-3ab7-a0e1-50a6eacd881f | -6.1844 | -57.7395 | 2026-09-01 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f8d3ba54-3dd1-3d83-853e-96b63bc74fde | -3.0425 | -39.9355 | 2026-09-01 00:20:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 61.4 |
| c3ae0801-8c4b-3607-acd8-3220c086c818 | -14.1266 | -52.7895 | 2026-09-01 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 45fcd932-0fcd-3fb9-99f5-7389dcd5a7a8 | -17.4122 | -42.3445 | 2026-09-01 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3a18358e-0cbd-3c3d-a2b8-53f7abb59ce6 | -16.0547 | -54.3908 | 2026-09-01 00:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| befc325a-59b5-396f-8c29-026c410ea1a6 | -17.372 | -42.3544 | 2026-09-01 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 56f60e90-3215-3451-84b4-29c01325f2c5 | -17.3713 | -42.3794 | 2026-09-01 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 3eaca6ef-7efa-3005-9ec3-ad8405430086 | -17.3914 | -42.3744 | 2026-09-01 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 144.7 |
| ec7b4605-cf08-3826-bd34-79c0ee245def | -7.3487 | -60.5883 | 2026-09-01 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 108f1ae3-bd48-3888-8fad-4e21a12aeea4 | -6.9551 | -55.655 | 2026-09-01 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5fcc71e3-8c40-3ba4-b08c-cb49c3421e47 | -11.258 | -50.5836 | 2026-09-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d993f926-b2e3-34f5-ad1f-eadd75ee4fa7 | -7.182 | -60.6904 | 2026-09-01 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 601c59d5-454e-3129-a3f0-d8b6cf116ed4 | -7.5709 | -60.4835 | 2026-09-01 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1e466b07-e0f3-3319-b5dd-2757663a032b | -6.6036 | -58.5972 | 2026-09-01 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9de82cc9-8ab1-3dd8-bc60-b5a54134a692 | -7.3488 | -60.5691 | 2026-09-01 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d13606e5-d6d3-3029-a42c-dabc0c1c5ada | -11.2577 | -50.605 | 2026-09-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 5c07e5a2-ff03-311b-86c0-4d0cd2832d34 | -6.4245 | -52.2005 | 2026-09-01 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a0410c08-0459-31a7-9276-11693f9de4d8 | -17.3921 | -42.3495 | 2026-09-01 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 5f670e19-7b2c-3346-b90d-75e5be2a8fcf | -21.5306 | -48.63547 | 2026-09-01 00:22:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5b49c0ba-50e1-34a4-a3ce-0754f46b0eda | -20.9108 | -49.25836 | 2026-09-01 00:22:00 | TERRA_M-M | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 2323e216-d414-3f88-80d9-187121bbae12 | -21.52855 | -48.62286 | 2026-09-01 00:22:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 45418c3d-e1c9-3d92-8a32-e7f9a1a045ef | -20.4788 | -45.67559 | 2026-09-01 00:22:00 | TERRA_M-M | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 97f55e3c-5b63-34b8-af12-dd9da533bc23 | -15.84961 | -47.67991 | 2026-09-01 00:24:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7bc1a771-e001-3079-bbfa-6d9302f7f6ff | -13.47487 | -57.03278 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d837e9d4-f3ad-39e4-9d67-199c9d6fef62 | -17.37654 | -42.38458 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 283.0 |
| c6c791bb-2857-31d5-a036-639dd4ce64a0 | -17.39361 | -42.38065 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 91745c0b-4212-395a-aca2-d996a343c8b3 | -14.67749 | -53.55026 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47ef388f-eb46-3eb3-8e7a-8bf6f7b85767 | -15.74743 | -56.0924 | 2026-09-01 00:24:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b4787669-e63c-38be-8901-18e6940e230e | -11.24563 | -50.57457 | 2026-09-01 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7dc5cc95-f104-36a7-9630-207af127f0a4 | -14.447 | -52.5107 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7b02cba3-79bc-3dd1-abb6-e64e0a45c343 | -19.20064 | -57.3548 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| bfea7e83-014e-32bd-a47f-fed8f03caaa0 | -15.25138 | -53.8504 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 714d6b93-3d77-3c40-89b9-7b1e587a9e4c | -13.45085 | -51.8797 | 2026-09-01 00:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0b849936-ebb5-3d4d-8f77-90706d3b6d2e | -10.1451 | -50.29848 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 64a868ac-fd53-399b-b90c-66be3ef2c1e1 | -13.45672 | -57.04662 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 75e48dab-019e-321b-bfe9-6c607bb8782e | -14.58824 | -54.11114 | 2026-09-01 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| babbb8ec-7f69-3726-b6a8-b9f4fceaa6ea | -13.47768 | -57.03753 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f42b689-1dc5-3f06-ae0b-57327507c1c2 | -14.70264 | -53.53724 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1332ca53-2ac6-3971-8d88-2a27390d4bd8 | -18.50329 | -50.90559 | 2026-09-01 00:24:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 0700fc4d-1bb7-3592-ba15-2b996aa9149e | -14.45871 | -52.52823 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 04662bb6-d289-39d8-a437-f2e6960b8352 | -10.17103 | -50.32276 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 51f13498-b48b-38cd-bbca-d2d2729dfd40 | -11.24757 | -50.58737 | 2026-09-01 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 9a272e17-e1d5-3fae-9e8a-02fb96979c96 | -14.50667 | -52.22178 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3fc441ba-6660-3146-a6e2-5a8a242e06ca | -18.94177 | -47.10507 | 2026-09-01 00:24:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| feae64da-53df-3ad0-b54a-88633419db0f | -15.39722 | -52.70427 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b21f2ff5-2b45-32c8-a5f8-83bee50a7309 | -15.64369 | -50.10103 | 2026-09-01 00:24:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e23cc411-7843-3d35-986c-67780044b2dc | -11.47679 | -45.08171 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a8a30607-eafd-3c87-957e-e209532e0fdd | -19.24993 | -57.37177 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 02289289-ff9c-3367-bf63-22dabadcdb02 | -16.54864 | -52.50874 | 2026-09-01 00:24:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9fbb4904-a0c1-3f01-9dfb-41cd6779be0b | -14.422 | -56.2777 | 2026-09-01 00:24:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f5b3500a-7d63-323c-af13-9ede454e8d5c | -19.20308 | -57.34823 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.6 |
| b75c2893-1111-3683-be51-65d8f173bef4 | -10.50816 | -57.44508 | 2026-09-01 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5388f900-e249-367c-865f-e6341817aa8d | -16.14301 | -52.37698 | 2026-09-01 00:24:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 59f1fe2e-a0c2-3e0b-a8c3-ffb3f01c2cf6 | -15.45601 | -52.79898 | 2026-09-01 00:24:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0da75ea2-678a-3426-a72e-49a8fbc4f473 | -16.54995 | -52.51805 | 2026-09-01 00:24:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e001929b-deac-315b-b729-a62fc67e7a9b | -17.38706 | -42.33482 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 139.5 |
| a78b56cc-a91f-3b82-a25d-dd04c6e4eb52 | -17.37459 | -42.3899 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 2974a2a7-fc98-3ef9-9778-5b683d2ce165 | -17.49009 | -48.87067 | 2026-09-01 00:24:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ae42ea33-26cf-338d-8360-c9cd570d7a7f | -14.41918 | -52.51114 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a19dfb05-ed04-35aa-9279-49bcce4dab41 | -14.41379 | -52.47329 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 850cbffc-b475-3366-9efb-e7377afb7ced | -10.8378 | -50.64371 | 2026-09-01 00:24:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| eb1e790b-3d2c-36e2-88bb-1eb17b2e9da5 | -14.68629 | -53.54895 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 02239e88-36a1-3fd9-8257-ab562962220c | -10.18183 | -50.32104 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| c597d103-9852-31b3-970f-9878382cf960 | -14.43802 | -52.5121 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 89750aa0-d0fa-3637-a4da-70536dd1320d | -19.19894 | -57.34033 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.4 |
| 84f35f07-30c2-3645-84f2-936887b5a7d0 | -10.12828 | -45.88093 | 2026-09-01 00:24:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a9d8e100-800d-383d-9016-e4802c298c0c | -19.22484 | -57.34547 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 36355af8-80ca-3945-aee9-8c1717cf8c88 | -10.75242 | -48.00383 | 2026-09-01 00:24:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 87004d01-fe81-349c-a19a-36af2e15e4ed | -14.69509 | -53.54762 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 1c5bf6e4-0601-3026-8ae8-54f9ddd292dc | -11.48248 | -45.11488 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 2b68673b-fb5a-35fb-8986-16545dfb00e1 | -11.32113 | -45.1837 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 7b67180d-536d-3d00-82c7-8bbb1f7a1e5a | -11.10384 | -51.54257 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 367169b5-faad-35df-bb54-414244d6a271 | -10.74377 | -54.04257 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 44095947-a191-320d-b549-bc85de609784 | -10.20761 | -50.3452 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 447.1 |
| 7eb6e4c0-242b-35e9-8199-67c502d38e04 | -14.50808 | -52.23141 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b440024b-414b-3ddf-938d-e1d3ab03ddf5 | -14.45597 | -52.50924 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 631c944f-4b47-3ac9-a067-f0870bd15ddb | -19.21396 | -57.34685 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| f3009876-bb1b-3a03-8e86-5a009b04fe2a | -14.42817 | -52.50972 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 517a8396-7202-3b8e-a0f7-8224056c2926 | -17.22703 | -53.2637 | 2026-09-01 00:24:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e88d9408-0866-3c2e-af1d-f6e10f6f2075 | -19.23408 | -57.32959 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| b7dc4890-913b-3035-b292-133430cea06b | -16.18699 | -49.31812 | 2026-09-01 00:24:00 | TERRA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2d2ae2ae-4014-3c84-a88f-cb2239e91c30 | -13.48046 | -57.06007 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 85078632-25ee-3529-a410-709be18ac01d | -14.3824 | -52.5748 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2195d31-96c3-3ade-af0f-4dce4b5fee01 | -14.12937 | -52.80453 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3a72eb57-2713-3e2a-88d2-81f280e300f6 | -11.47916 | -58.52091 | 2026-09-01 00:24:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3144ec16-e49b-3ecc-bc8c-5012344a4654 | -11.21146 | -46.13146 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| cc7c2fa4-0a3f-3e8e-b340-3f8b38e09032 | -19.23572 | -57.34408 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| ce177a3b-a7d2-3185-aa39-a50ddbd7cec6 | -10.75135 | -54.0323 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 55087599-2fb3-360d-b24f-8f7caf3a7920 | -15.6297 | -56.38665 | 2026-09-01 00:24:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d1acdfac-11fe-3244-94ed-7c7bb013af59 | -18.51251 | -50.90404 | 2026-09-01 00:24:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80c72e0e-de5f-34d2-ae83-8133718072b9 | -16.05176 | -54.3861 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a5757edd-b04c-3b0b-855d-0267a647d91e | -10.75509 | -54.05924 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| eee77a0e-b523-3d61-808a-f1710cbdd781 | -14.57278 | -52.10655 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36dec073-e08b-3fbd-a01b-0af61c62016e | -16.05301 | -54.3954 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README6.md)
