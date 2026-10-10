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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 392712ee-881a-3082-ba58-b1fe0ead1769 | -15.58419 | -48.1854 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e603f884-96b5-363e-b930-9499aaa5c0ca | -18.91748 | -47.91545 | 2026-10-10 04:49:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c01d506c-a113-38ac-95fb-a846038921e2 | -16.07128 | -44.32334 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb18a1da-1841-3ef3-bc8b-fbe0ee8a0816 | -14.75536 | -48.22935 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 667177bb-ddcc-3dd8-a478-2ad1d5e581f9 | -16.56375 | -46.80178 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00f0ac1f-a5b5-38a8-bdf5-9916d29b45ae | -18.61972 | -48.2565 | 2026-10-10 04:49:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5740e577-d142-306f-892a-610ec2b1ce49 | -16.76184 | -47.07653 | 2026-10-10 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f403cac3-69c6-399d-8182-a81253247846 | -14.70025 | -49.79222 | 2026-10-10 04:49:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71edc34a-bb2b-34fb-932c-0ed28ab4a329 | -16.12046 | -43.75294 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03773fd9-d34d-330a-b6da-7b44d76cda91 | -19.55272 | -43.58849 | 2026-10-10 04:49:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12a01b1f-d31d-391e-9938-c274eb76dbc3 | -16.58336 | -46.76896 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b41295da-f9c0-3093-9a75-4981fcb8a78f | -17.34591 | -42.68624 | 2026-10-10 04:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68607cbb-bad4-3b6d-9b84-fc7b01585232 | -14.34083 | -55.0059 | 2026-10-10 04:49:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1755ba2a-637f-374a-991b-fdc3f9d59192 | -15.55554 | -50.4925 | 2026-10-10 04:49:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30eadd36-9a27-3cac-bfad-29ec5dce3784 | -15.65734 | -48.13873 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d82bc0c1-d85c-3a94-bd9b-95629adcbfe0 | -14.71751 | -48.22687 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7e612b0-f241-3ee3-acb8-86f910984bd6 | -16.56011 | -46.80119 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1407807d-896b-38eb-8f0d-ffef06ce0d34 | -14.71354 | -48.23013 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462d6e63-772c-35b7-8bd4-01dbd44b8273 | -15.65251 | -48.12708 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 440fcab4-5481-3347-b956-5037002858e8 | -15.45317 | -48.06009 | 2026-10-10 04:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| debe483c-aa53-3009-a77a-4795a09d9dbd | -17.34845 | -42.66556 | 2026-10-10 04:49:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b594f690-75a6-3c35-8a7a-c04d96922a5b | -18.64627 | -41.33249 | 2026-10-10 04:49:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6667e16a-2818-3876-95ec-595ab8649b35 | -15.90076 | -46.00015 | 2026-10-10 04:49:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3140f2d-6e82-31c0-9eb6-1471b2aa69d4 | -14.7435 | -48.21599 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc23bcc1-0fca-3151-a5a3-888c02bf0882 | -15.45353 | -48.06088 | 2026-10-10 04:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d5efe04-315c-3b33-a094-e041be867807 | -18.84796 | -41.9651 | 2026-10-10 04:49:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5961cccc-b1b8-30ca-9a28-0de143329def | -15.7498 | -45.707 | 2026-10-10 04:49:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80c76965-ba47-3a11-a04b-37fa309428b3 | -16.5938 | -46.74831 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c2c4c7b-06fb-3a35-86ea-422c382a050a | -18.91453 | -47.91076 | 2026-10-10 04:49:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13ab5fa3-ba5a-36eb-82a6-1fe534e4a2c2 | -18.85305 | -41.96576 | 2026-10-10 04:49:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 48a80f1f-b373-3198-910e-06cd00c1b332 | -16.60351 | -46.75867 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bbe9395-d5e2-35d7-8e11-185c19ca1d19 | -12.29679 | -63.37181 | 2026-10-10 04:49:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4563eb0d-a25d-3e69-a49c-f3c9dee571bd | -15.74027 | -41.90029 | 2026-10-10 04:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76ab10e6-33ee-303d-95a9-7aaac0fa1b80 | -14.86861 | -50.30593 | 2026-10-10 04:49:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f6aaba7-c290-3bb4-b077-950a3d32ee75 | -15.82027 | -48.19124 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38242e2f-3a46-310c-91b5-b95041b243cc | -15.65761 | -48.1396 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcac0acc-f112-358f-b8f6-983a5979016f | -16.9385 | -49.38097 | 2026-10-10 04:49:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 248dbcb2-2dcd-353c-8109-f92c15e9c2d1 | -14.34014 | -55.00963 | 2026-10-10 04:49:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4f0ece3-70af-3e8d-8dd2-c9bc62974b2b | -14.76998 | -52.8205 | 2026-10-10 04:49:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69a8617c-84c5-3479-a74c-142930fbef87 | -17.46381 | -45.06936 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 711596cb-257f-3393-8fcc-bc3903e8a10a | -15.24547 | -48.57939 | 2026-10-10 04:49:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b14bb2f0-a1dc-3404-8a14-4c2707cc18c5 | -16.60289 | -46.76296 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0c7c38c-9d3e-306a-910a-149cb514d4f8 | -12.29526 | -63.37899 | 2026-10-10 04:49:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 91b3d3b4-7926-31e4-aca9-70a193aa24b7 | -15.6619 | -48.13163 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a716332-a8fe-3e39-a502-e702d4611a90 | -12.28865 | -63.38323 | 2026-10-10 04:49:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b77e5b3-41a5-300f-89e9-182b01ff165a | -16.13853 | -46.03094 | 2026-10-10 04:49:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c298bbdf-0a6f-3747-aa27-bd8745bb4700 | -14.87253 | -50.30291 | 2026-10-10 04:49:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f20ba7b-b912-3715-9590-a31e736310ae | -17.10319 | -41.57577 | 2026-10-10 04:49:00 | NPP-375D | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fd36718e-3742-3d9c-a76a-d4b3161446f7 | -14.79358 | -47.97883 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02526af1-f299-3dbf-928f-6f24b741a528 | -16.01028 | -43.60276 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b5961ba-5355-3851-b358-c72298e7db94 | -15.39896 | -41.9026 | 2026-10-10 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3d8049fa-6046-3572-9252-1748465e1871 | -15.58078 | -48.18482 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d15cfcaa-2fa5-3e77-8ae0-9c8e192f36ac | -16.64014 | -40.59605 | 2026-10-10 04:49:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b7b0a366-d9e6-37ea-aff4-98fa4d381241 | -14.87195 | -50.3065 | 2026-10-10 04:49:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| edca2ab4-3fa4-3c49-ac3d-2bb0dad70701 | -4.1039 | -54.0164 | 2026-10-10 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ba7744e2-9193-3020-975f-b67187b88df2 | -3.9912 | -59.356 | 2026-10-10 04:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 669fbc1e-a982-3ea4-a1c7-61bd4e48ed9d | -3.5689 | -54.3745 | 2026-10-10 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d0c4aa52-c2c2-3614-8204-71ea7712c0d9 | 2.727 | -60.2586 | 2026-10-10 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0ff84a7f-6bed-3088-96b3-dcba24340be2 | -22.09214 | -48.98966 | 2026-10-10 04:51:00 | NPP-375D | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22700aee-eac9-31e2-be0f-a3520fe9d45d | -21.23028 | -48.6135 | 2026-10-10 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a90bdd20-eb72-366c-a4fc-b2cb3f5d6d40 | -21.93386 | -48.96514 | 2026-10-10 04:51:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9782c334-091f-33b1-824a-6b5f94ae86c3 | -22.7648 | -49.35773 | 2026-10-10 04:51:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e66cd42-caad-3972-87bb-01f1578369cf | -22.07812 | -48.98742 | 2026-10-10 04:51:00 | NPP-375D | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5244996-67f3-3f74-b04a-1efbf61aae1f | -20.93538 | -48.51497 | 2026-10-10 04:51:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5548d187-5004-3eb8-8399-8b2dd18d739a | -21.10222 | -48.49997 | 2026-10-10 04:51:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32d64389-c47f-396b-8158-18ac668a0303 | 2.727 | -60.2586 | 2026-10-10 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e1cedeef-10e7-3f6d-8960-1d35a79d5ed3 | -3.9912 | -59.356 | 2026-10-10 05:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f352f5a4-f62a-34c1-aeee-f45aced05952 | 1.1779 | -53.04345 | 2026-10-10 05:01:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0098480-4f6b-3490-a6cd-0cb8515b19d9 | 4.27467 | -60.89051 | 2026-10-10 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48cbfe15-9523-3ea4-a9db-1265bfde4709 | 3.73139 | -51.61557 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32757c19-3f79-363a-ab24-c415774b73ea | 0.36223 | -50.95566 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6120be1-deea-3d26-a4b7-82b7e564a775 | 0.3682 | -50.9473 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75d66d77-0024-35c9-9d0a-425cec6a9cd5 | 0.93898 | -50.19547 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43188bcf-bb6d-3dee-bec4-70ee366e16f3 | 1.67314 | -55.62215 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 038edc9e-8e7f-3a23-9c3e-ae643c4fed45 | 3.04018 | -60.54182 | 2026-10-10 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d059539-9660-3038-b10f-89780b5ec626 | 1.67609 | -55.61748 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5197400e-50ae-3992-a719-f0379318a8f4 | 0.30663 | -51.3809 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 470bc3ec-93fe-3111-a86e-918eae0892f2 | 4.26939 | -60.89121 | 2026-10-10 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 415ccbae-ccbc-30be-afc6-beabbaf6dde4 | 3.98239 | -51.63178 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3292b7c0-f8ee-318e-a3a8-c43055656065 | 1.16344 | -50.1502 | 2026-10-10 05:01:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef799cf-6797-3d70-a4fd-16d6547c3e96 | 0.82009 | -50.76849 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a9d991-b9b4-3168-9e29-0029b09a3da1 | 0.48658 | -50.78886 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bd1bcf87-5390-3d53-91d8-8cfee0649abb | 0.28756 | -51.41326 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1b37828-ca9e-3f5c-9b81-27cd56a7bfa7 | 4.68667 | -60.58811 | 2026-10-10 05:01:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac115ee8-a5b0-3689-a9e0-d2d1b3d945b9 | 0.36507 | -50.95145 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef6b1b2d-9e76-34e6-ba33-a129289a65a1 | 0.47285 | -50.79101 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 888cbd26-336d-3375-bdfc-f8c24849e4eb | 0.94835 | -55.75181 | 2026-10-10 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 173221e8-77c0-370c-ab38-4d644be5ad35 | 1.6784 | -55.60867 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89829258-55fa-395b-a37a-ca947a6ea46a | 1.41174 | -50.67414 | 2026-10-10 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a369951-c0c0-3473-92cf-7d56434585e6 | 0.9431 | -50.19879 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 865f51d0-d22d-39dd-8fec-4a1e24b0cbd9 | 1.16693 | -50.14965 | 2026-10-10 05:01:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cc3ce49-bde3-3cbe-b21c-2cb940aa4578 | 1.72607 | -55.5844 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47624449-0085-3b76-b73b-4a8d9dc1bf5c | 1.67081 | -55.63089 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafc87a5-b4ac-346a-a7e2-0d995e1ac75d | 0.48255 | -50.78568 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e3f731b-620a-3117-98b7-97683c11abee | 0.57028 | -50.22599 | 2026-10-10 05:01:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04d1aeff-b10b-32e7-8d29-efb79e2528ac | 1.83231 | -55.52256 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 641f889e-6296-35b8-b32f-693ff30a2f4d | 1.67186 | -55.61392 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b86c697d-367c-35d9-923b-789db4dd3e39 | 0.29373 | -51.40863 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8757c979-098e-3e49-ba39-5444f6d14de5 | 3.04063 | -60.54475 | 2026-10-10 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f6a10e1-a927-3473-8b71-848f787c6bfe | 2.73136 | -60.26109 | 2026-10-10 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.4 |


[Clique aqui para ver as próximas entradas](README90.md)
