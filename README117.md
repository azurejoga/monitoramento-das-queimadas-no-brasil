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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7263cdcc-cbbf-339a-baed-166d4e2d4166 | -8.80966 | -63.17646 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b05b6495-dcdb-3ba4-9e59-daa755732b1c | -8.80857 | -63.1767 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f09f732-f8ad-3831-88b9-0bcb61e12c55 | -8.80619 | -63.17587 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75d4d455-aa50-35e8-ba42-2635c84dfd9d | -7.305 | -64.67572 | 2024-10-12 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd5c0cfb-be06-30e5-a641-d1c33a11a4c7 | -8.80519 | -63.10928 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92b1c19b-7130-3f5e-a8fb-3ae315d47873 | -8.8051 | -63.17611 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c57c59cd-8590-3c7d-8689-dc86ea6df706 | -8.80173 | -63.1087 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34b8f507-0b8e-3784-947a-d0d2f1abd47a | -8.78343 | -63.08994 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a52d9ba5-0596-3291-b565-95500be106be | -8.76918 | -63.2216 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a8a813-88a7-3bba-80cd-645e5be72aa6 | -8.76855 | -63.22546 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0fdd906-e240-3c4b-ad2c-46159ced61df | -8.7657 | -63.22102 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef5a6e16-f691-3a13-8e39-fd5e5bd0cd33 | -8.68831 | -63.09466 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d20c973-3e00-3ee1-a15d-8109f715a177 | -8.68485 | -63.09409 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6a73d82-2c07-3aa9-bb85-0b9398477eb3 | -8.68258 | -62.86805 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c3d87df-7cbe-3c3b-a7e9-783be07bd4d5 | -8.68196 | -62.8718 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 142f69ae-ac99-39ae-a366-2826b298ca22 | -8.67447 | -62.87444 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb19fb8-2b48-39f4-979b-cf63fda2f497 | -8.67138 | -63.33688 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cca8dd06-bad8-3556-acb2-0b48c8c2b4dd | -8.65426 | -63.48332 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12e665cc-2e39-31a2-aa97-e3c6b60afedb | -8.65388 | -63.26297 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b238dac5-905f-366f-af06-2e28a217aa16 | -8.6536 | -63.48729 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0fab1a-5bc3-3e70-bf10-887e98b7ab23 | -8.60595 | -63.51299 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00a12b49-63ea-38d6-94a5-04566e0320fa | -8.60366 | -63.01508 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e82f4633-7471-365b-8348-0798d44cfc70 | -8.60304 | -63.01889 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 829480fb-cfa1-36cf-8698-76a8a1ef43df | -8.60113 | -63.09699 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb22d213-0fbc-3380-91ca-a35e819fab55 | -8.60052 | -63.10082 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b457cff1-5ddd-3c64-931e-8373fd50e243 | -8.59804 | -63.25372 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 974f130d-dfa0-3dbc-a99a-62e06458ad13 | -8.59682 | -63.1238 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0d2d4ce-2dfd-3bc5-9358-fa1f92bbdf20 | -8.59272 | -63.12708 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7830efd-46d0-3cec-8998-dc5148048a2a | -8.58885 | -63.24423 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09b69afd-1d6a-36fa-a750-f7e77579de81 | -8.58032 | -63.09354 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed05febf-86af-3502-af50-7acc0f5601dd | -8.5716 | -63.41385 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bda4f77-5662-3fe2-a16f-8d2576393282 | -8.4119 | -63.83496 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c16c64a-4959-3c21-af4d-2f241d7a5f17 | -8.40831 | -63.83437 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d999906a-20bf-3856-a295-39f2ed9c1c4c | -8.39905 | -63.93479 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16592f56-5b12-3e7c-a972-45058bd31136 | -8.20251 | -62.8386 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a10160e2-6856-3cd0-a743-90ee7a03510b | -8.15347 | -63.93024 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20f2116c-4951-378f-865d-16d78645be26 | -12.16605 | -63.3446 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83257670-fdf6-33f9-baf3-1a3adeb13234 | -11.78895 | -64.24519 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da5f705c-e021-3858-9f92-d9ad20bf3b63 | -11.78475 | -64.2486 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 920ccab7-935a-39a7-aa49-d2fa92350a3f | -11.78308 | -64.17138 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 287e41c1-0441-3491-82f5-ac49a7da4065 | -11.78277 | -64.17446 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56d8daac-9a2f-3516-b0a7-b08e3119d1d8 | -11.78243 | -64.17535 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1410af8-bae3-3c69-8ccb-f2f558591710 | -11.7821 | -64.17842 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 397c3590-f6b5-3282-a800-150f2c3a48fb | -11.78178 | -64.17933 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f0ef088-960b-3ac3-953a-2724aa34302e | -11.78143 | -64.1824 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 025f050e-93c6-3aad-a151-f28ab5d43fe8 | -11.78055 | -64.25203 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28213d03-9dc4-358f-b355-70cfdc1d583a | -11.78022 | -64.16679 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b580353-e4b4-397b-a134-c5771d9d0208 | -11.77988 | -64.25602 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eeb424b7-b938-3092-9af8-c8e5d5a9b02f | -11.77957 | -64.17077 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb21ce1d-4e7e-35c4-b8de-e1a7fc4f5677 | -11.77671 | -64.16617 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46d3a661-0672-33ac-83da-e85e66e0562d | -11.7732 | -64.16557 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f2b8a63-62f2-3803-bb56-a08fc5e97c90 | -11.77312 | -64.29606 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 718e36a4-f961-34f0-abaf-0afab7568af6 | -11.76969 | -64.16496 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 473d2964-5f88-3b39-8671-fc1b58feca5b | -11.76617 | -64.16435 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdbddbd7-7644-3f54-83f5-af83ba2d8764 | -11.76266 | -64.16376 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a757b6d-28bb-3e98-9481-15d6b639b6a6 | -11.762 | -64.16772 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af31e585-6795-39d7-82ed-f604c5b3d2e1 | -11.76039 | -64.0901 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57c5cadd-551d-3bfc-87eb-a66e7e8caec2 | -11.75973 | -64.09406 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec668c0-2b5c-315b-be36-77a0be73e462 | -11.75914 | -64.16316 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f148c564-0da3-32d1-a7d8-83ab180cb5d7 | -11.75849 | -64.16712 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8b83ea-f966-358a-9fed-b76c778d34ed | -11.75689 | -64.08949 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69b94ac5-2122-3cba-9d68-569fb4d755af | -11.75623 | -64.09346 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7711b0a-605e-3419-9e77-ff91e3be5195 | -11.75563 | -64.16257 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e061de3-400b-3045-b8d7-f0bffe60317c | -11.75497 | -64.16653 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba55bb9-6c60-3305-a2eb-10f62509a79e | -11.75211 | -64.16198 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e98da077-63e6-397d-9506-874bfe12f5ba | -11.74794 | -64.16534 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09210de3-2128-3ca2-b9a9-abbce2b4612f | -11.74463 | -64.11994 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 276a6a66-c223-37ea-8bd7-6d805ae3347e | -11.74443 | -64.16475 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 165601bd-4c20-3ca8-89f9-2d724cf38c04 | -11.74398 | -64.12391 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7908b348-6236-3b67-89e0-bdbb550d13d4 | -11.74025 | -64.16811 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d71f5db0-99c0-347c-bb93-b00bb4fa45cf | -11.73674 | -64.16751 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 335d0d1c-4178-3b21-be07-9b2479a0036d | -11.73382 | -64.29439 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd7b8349-9e9a-3714-b84f-23c74e4220e5 | -11.73323 | -64.1669 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eab0e240-c83b-312b-a00f-52ec207f4b4e | -11.73042 | -64.03219 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d201ac67-9905-377b-a8f3-52dcd4c7e95c | -11.73029 | -64.29378 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58dd495a-cbff-3668-b772-11b2a5a2f59d | -11.72977 | -64.03612 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9137298f-3c39-3534-a8df-030f2a7e7497 | -11.72884 | -64.14981 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e9ae3e8-b9bf-3239-a5e4-d690561edaaa | -11.72675 | -64.29317 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 318d32af-6379-342e-a8e5-b1749e972ba7 | -11.72608 | -64.29721 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0a6c037-05c4-349e-aba3-48e8321432a2 | -11.72533 | -64.1492 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0811ba6-1150-326c-8f61-37c86be94a85 | -11.72255 | -64.29661 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0bda2e-11a2-39b0-a666-db8f9f848a92 | -11.72182 | -64.14857 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 332f9589-8d4c-308a-9d8b-7f6bf9c1f558 | -11.71902 | -64.29598 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b43418b4-e861-3579-9194-debbbe33844f | -11.71214 | -64.16325 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1dbcfad-7888-3c19-94cb-0e78eb701cd2 | -11.71148 | -64.16723 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71c19f0e-2d4d-34ed-bbf1-252ab490029d | -11.70796 | -64.16663 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 446e2feb-2f2d-31af-b44b-9137bdd54c11 | -11.70625 | -64.1337 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 195225e4-73da-3eb3-aa19-a3162348dfca | -11.66638 | -64.24155 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bdc8b86-3268-3c21-867f-bf8e5d0f127b | -11.66491 | -64.25505 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 125174a9-32d0-34ef-bb53-53e3b28328b0 | -11.66335 | -64.24239 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 212083f2-37c7-3b03-b0ff-26786bed21f9 | -11.66269 | -64.24639 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7acee79c-de49-3ad7-aa62-93661ee6e9a0 | -11.66218 | -64.24493 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37572a13-e08f-3baa-9a5c-288eaaeca0d2 | -11.6615 | -64.24894 | 2024-10-12 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8782e713-0362-3eff-80e8-bd28c6efd7cd | -11.76733 | -63.81031 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edca13a4-91fe-306d-89b4-74f621fb720d | -11.7667 | -63.81414 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a44458-00cd-3b84-97c2-efc82a7f431c | -11.76641 | -63.79438 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 795e5fcf-de2d-30f1-9d88-695ff96e7360 | -11.76323 | -63.81356 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6892eac-9e43-39d4-81e5-625b82f36319 | -11.76295 | -63.79379 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93d4d856-ddff-3715-a2a8-5d594bad29a0 | -11.75976 | -63.81298 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0c78842-eac7-3235-9b20-f53ed4775e72 | -11.75438 | -63.82394 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README118.md)
