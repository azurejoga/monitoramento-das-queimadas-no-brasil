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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcf75b94-1153-3cd7-8a39-1a7659950b43 | -11.5686 | -52.8057 | 2026-06-05 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 176.7 |
| f5684fb6-2760-3dd9-9f0f-15bd7f653b31 | -11.5496 | -52.8076 | 2026-06-05 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 304.6 |
| 16b5860b-5714-3448-b5e0-f9022b4d919a | -8.7208 | -48.3441 | 2026-06-05 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 6db328ff-ae7c-3bd7-8e84-fa2a0de98a51 | -12.4274 | -58.484 | 2026-06-05 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 98ee2902-7243-3d93-b17e-28e26019703c | -8.7211 | -48.3222 | 2026-06-05 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6889f684-9e3f-3981-882e-c568bc7540ad | -12.4464 | -58.4825 | 2026-06-05 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 9aa31b97-920d-3ea6-a1f8-f3805c351cb5 | -11.5688 | -52.7848 | 2026-06-05 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| d41e6443-9321-33da-9ff4-745777be3767 | -14.4777 | -59.146 | 2026-06-05 00:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| dd56d0a1-15d9-39f9-9d7f-9888615cd673 | -11.5499 | -52.7867 | 2026-06-05 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 15e378d5-8a77-36d9-aabd-c5fa9bde23b1 | -12.4466 | -58.4627 | 2026-06-05 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 745b1d26-99c3-34b4-b512-00ec260c9103 | -11.5493 | -52.8284 | 2026-06-05 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0c72714f-82e4-3c23-8c11-602d04592945 | -11.043 | -44.3167 | 2026-06-05 00:08:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d70981b9-bdb3-3304-80fa-b45884ef7d31 | -9.3719 | -50.527302 | 2026-06-05 00:08:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11983483-5225-3367-81c9-1922b97f7b18 | -7.952 | -46.8377 | 2026-06-05 00:08:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58940915-0158-350d-b972-70eb0bc0e96a | -10.5135 | -42.357201 | 2026-06-05 00:08:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fc7a920e-2da9-3290-8bdd-d320053f251a | -14.0889 | -54.318199 | 2026-06-05 00:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30e90506-adcb-3040-9b3c-14a03794dd0f | -19.745399 | -53.524601 | 2026-06-05 00:08:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 13618df0-28c6-3145-9f4a-6eddb1d28c60 | -7.3465 | -49.824902 | 2026-06-05 00:08:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 766de04f-1812-3f53-83a8-3d81c4fecae9 | -9.3736 | -50.535198 | 2026-06-05 00:08:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c92af4-cea8-3840-82b4-7b718b47c095 | -6.8502 | -47.933399 | 2026-06-05 00:08:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a582a19-77e0-372f-851f-9388b7b61d33 | -7.3449 | -49.817699 | 2026-06-05 00:08:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f09536-7d29-38c1-9bfd-b2f60025f516 | -10.3859 | -49.427502 | 2026-06-05 00:08:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ff6ee13-0a38-3d3d-b83c-1a52120bb011 | -11.0411 | -44.308399 | 2026-06-05 00:08:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 620fad68-7703-3f03-bf40-f88c0c411002 | -11.5594 | -52.7883 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e58834f8-86d0-3cd3-9e57-511eed7da077 | -9.0794 | -50.5994 | 2026-06-05 00:08:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3cdd73c-aebd-344a-a29b-8370aa23025c | -11.0332 | -44.319099 | 2026-06-05 00:08:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3134e54-938a-3b4f-a2ff-ac6fe033a727 | -21.2808 | -48.6105 | 2026-06-05 00:08:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95f02b77-bb5d-331d-b06c-c29bf16d3ea7 | -11.5473 | -52.779099 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3ce406-237e-3a57-8ee8-73e59ed5e6cf | -12.7255 | -54.701401 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd397832-ed20-38e3-8853-2f636225d9ef | -7.9503 | -46.830601 | 2026-06-05 00:08:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 658c71a5-8e56-3731-b5b0-6114f698d66f | -15.311 | -41.883701 | 2026-06-05 00:08:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41347a9c-716d-3fd9-bf33-5dd9e6cfe4c8 | -11.5617 | -52.7995 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0986d9ea-2cae-30cc-9491-578ec75de78b | -5.3 | -47.238499 | 2026-06-05 00:08:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee1cefc-f895-3706-847c-096c5a3d1265 | -11.5692 | -52.786301 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64943441-16f9-3572-a354-ea39e5759d4d | -5.3081 | -47.229 | 2026-06-05 00:08:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c74a0cff-b502-324f-bb5a-b4cf5e5b56d1 | -8.7222 | -48.327999 | 2026-06-05 00:08:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b35a7ee-0683-391e-9bb9-94dd0b451cdb | -10.3891 | -49.442299 | 2026-06-05 00:08:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91cd11fc-b3b3-3a8f-b44f-50724476e532 | -8.3718 | -46.778999 | 2026-06-05 00:08:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5f018d5-c423-30be-9d8c-3a5921c8a371 | -22.6747 | -47.393299 | 2026-06-05 00:08:00 | METOP-B | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 601529fb-cd93-3592-96dc-25f09986d784 | -12.3141 | -54.1059 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8676248a-1131-3524-824e-38ecaf725fec | -9.7614 | -50.004101 | 2026-06-05 00:08:00 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a36eed4-1d1c-37c1-86fa-c85e1ff19b49 | -12.7352 | -54.699501 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a4754c1-eaab-3b23-a3ca-6266c5dbf1d4 | -11.5669 | -52.775101 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 590ebe7a-8ba5-34b9-807d-550ff912ec25 | -12.5334 | -45.666801 | 2026-06-05 00:08:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 492501c7-b6ff-3f3b-b4cf-62148ca6ad9e | -21.805599 | -49.1101 | 2026-06-05 00:08:00 | METOP-B | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3e6d98e-cdc8-362a-a9dd-6abed3444ca7 | -21.278999 | -48.601501 | 2026-06-05 00:08:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5200fb8e-0e30-305b-96f1-8d18f74a6f45 | -5.929 | -43.464199 | 2026-06-05 00:08:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49d41020-0170-3880-b2bc-3aa7aa9fd898 | -11.5571 | -52.7771 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b045328-d52c-3468-9791-12b39777c761 | -19.7327 | -53.5098 | 2026-06-05 00:08:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6b7177-4a2e-3445-9508-57df5abdafff | -12.3238 | -54.103901 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2208c14e-1d20-3635-9e74-8a82f4252add | -9.7597 | -49.996498 | 2026-06-05 00:08:00 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fca287ba-ae63-38b9-9059-862064659b3f | -7.3531 | -49.8083 | 2026-06-05 00:08:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0467516a-d3c6-393d-bf65-19a87f92a045 | -11.3885 | -47.813301 | 2026-06-05 00:08:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a29472ab-ee59-3565-a2c6-d481f2be19a3 | -5.9316 | -43.474899 | 2026-06-05 00:08:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22d04b60-f51c-3c57-9ca3-13a5bce9ef88 | -12.062 | -48.065498 | 2026-06-05 00:08:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd36a4c2-cfc2-33b1-bdfd-87a636cd6015 | -5.2983 | -47.2313 | 2026-06-05 00:08:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 932d98ae-6e58-3b81-a2ce-7eba195c99dd | -12.0541 | -45.9627 | 2026-06-05 00:08:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e57c744-04d3-366b-95dd-e5ac2a4fc11b | -9.0811 | -50.6073 | 2026-06-05 00:08:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8bc6b65-2600-306d-a0fe-24851bc1ac85 | -17.7999 | -49.2351 | 2026-06-05 00:08:00 | METOP-B | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 018ce796-da9c-3ab1-9f69-593f7845243d | -21.2013 | -48.2589 | 2026-06-05 00:08:00 | METOP-B | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5304f89-f808-34d2-a5b6-220707ec9141 | -11.7584 | -47.0709 | 2026-06-05 00:08:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 375f3a31-10ca-3f28-b0c6-165fd6967c18 | -10.5162 | -42.368 | 2026-06-05 00:08:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a69be410-64d6-349a-9375-2b312656947e | -10.3875 | -49.434898 | 2026-06-05 00:08:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80b45e4c-9f98-32e9-89e3-d5829baf995b | -13.5162 | -54.2887 | 2026-06-05 00:08:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b95bd2a6-9e53-322c-b881-cc949101c4b6 | -12.438 | -58.440399 | 2026-06-05 00:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3b6e5f9-84f2-35aa-a8d5-3dce0f292934 | -8.0582 | -50.674599 | 2026-06-05 00:08:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d8e394c-1a1f-3e0f-b5bb-5f8ddab2f0a8 | -11.0313 | -44.310699 | 2026-06-05 00:08:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a65144d-42f3-3b94-baee-cf8040548e62 | -12.3113 | -54.091801 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1210e67-c6b7-31fa-a270-aa2fd8724616 | -11.6026 | -55.326698 | 2026-06-05 00:08:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd524b19-6584-32c7-8a0d-c428405cf724 | -19.722099 | -54.6203 | 2026-06-05 00:08:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2333672c-f06e-36ab-9a32-bd2e464c8599 | -5.9218 | -43.4772 | 2026-06-05 00:08:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd2baed3-a6f5-3ef9-8a8b-69c052d160ac | -11.5993 | -55.310101 | 2026-06-05 00:08:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0320663f-30b3-3e7a-aca3-11eb27ad6869 | -7.8062 | -46.0233 | 2026-06-05 00:08:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8098375-a4e9-3020-a765-0d3591502433 | -12.0864 | -51.977001 | 2026-06-05 00:08:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2647437d-baf1-3ee9-b280-010359f4d8a5 | -12.4323 | -58.355 | 2026-06-05 00:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e390405-a096-3eb4-beaa-5356ba42f04c | -22.676399 | -47.4016 | 2026-06-05 00:08:00 | METOP-B | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3adf2c7f-9e7c-3993-a48c-ba2a18e97028 | -17.7981 | -49.226398 | 2026-06-05 00:08:00 | METOP-B | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7bb11a25-0d68-31fb-86a6-423db7566906 | -11.0708 | -54.4902 | 2026-06-05 00:08:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8495cd13-947b-3b34-92fa-6cd850d0c696 | -9.0909 | -50.605099 | 2026-06-05 00:08:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 276dffc3-8f22-38c4-8e1b-d35775d55b9b | -19.7356 | -53.526501 | 2026-06-05 00:08:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 80cadc4d-7f9b-3bf4-b65e-a6a0f40e6787 | -14.7698 | -52.652401 | 2026-06-05 00:08:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6c91de1-41ab-398c-a3ea-f58309407c63 | -11.3869 | -47.806301 | 2026-06-05 00:08:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d0463e9-8452-3b78-93cb-56540ade0cbd | -7.3547 | -49.815498 | 2026-06-05 00:08:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50271e2e-4275-3086-baff-b777efcc93bd | -8.7335 | -48.332699 | 2026-06-05 00:08:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 632f492e-7868-3572-95c3-968280a1884d | -12.4329 | -58.412399 | 2026-06-05 00:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 790ae75f-3e4f-3158-aaec-6f60730863a9 | -7.3481 | -49.8321 | 2026-06-05 00:08:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99876a44-3947-356b-a4a1-1688f7e97de4 | -11.571 | -54.5546 | 2026-06-05 00:08:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2909087a-be21-3f7b-ad84-bb2173612c58 | -22.4198 | -47.141701 | 2026-06-05 00:08:00 | METOP-B | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 88f38859-d029-3f33-94d4-423c9814038c | -9.0892 | -50.597198 | 2026-06-05 00:08:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5204a5-8105-3127-a392-58d78e0db390 | -12.4283 | -58.4422 | 2026-06-05 00:08:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85f8b8f8-e835-3358-90c9-001db2235980 | -11.5519 | -52.801498 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce0f5fe2-be54-385a-954f-b33efc254e8d | -11.5496 | -52.790298 | 2026-06-05 00:08:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 303f59ad-1c09-350e-8546-7a5aa7218cc7 | -12.5006 | -46.338501 | 2026-06-05 00:08:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61d20835-0484-3964-9c4a-8153c3650f31 | -12.321 | -54.089802 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9e11079-82d9-3199-9454-14fee421def0 | -12.7286 | -54.717098 | 2026-06-05 00:08:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 414ae0e5-a7cb-3417-86c6-3bd3b1f8901b | -8.7289 | -48.312 | 2026-06-05 00:08:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a55904b9-f7b0-3122-bc53-708336642fb0 | -11.5686 | -52.8057 | 2026-06-05 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 184.0 |
| 02f57777-1a5c-31b8-8776-668f2c4e6ff4 | -8.7208 | -48.3441 | 2026-06-05 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ad6ab70a-aca0-3371-9d65-db3348a59f79 | -11.5688 | -52.7848 | 2026-06-05 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| a1149ba2-272f-3c3e-8e8c-e272ebe0e859 | -11.5496 | -52.8076 | 2026-06-05 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 273.0 |


[Clique aqui para ver as próximas entradas](README2.md)
