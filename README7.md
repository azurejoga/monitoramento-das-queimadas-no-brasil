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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6709147-b558-3750-aa43-94353af0b721 | -16.18426 | -55.86086 | 2026-03-25 05:14:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| c20c6254-ca86-341e-b95b-dc541e799826 | -21.40605 | -51.74961 | 2026-03-25 05:14:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f3fa488c-d14c-3b53-9a57-4c80095c3e9b | -21.26802 | -49.48596 | 2026-03-25 05:14:00 | NPP-375D | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| c39f0004-926a-317b-b86e-e2a4f08141ca | -20.2273 | -44.14268 | 2026-03-25 05:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 96be07e3-3424-3b60-bdce-6469786d191d | -19.90246 | -48.68501 | 2026-03-25 05:14:00 | NPP-375D | PIRAJUBA | MINAS GERAIS | Brasil | 3150703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab885bf8-48f0-3ec4-9b0a-8d6f525555e7 | -19.87142 | -47.08838 | 2026-03-25 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d7d1ce5-2711-3b5c-8c1e-d9abbaa67813 | -20.13266 | -44.62181 | 2026-03-25 05:14:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7061797b-48a1-39cf-8d4e-abe40b3ced9e | -15.6573 | -56.42938 | 2026-03-25 05:14:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2583fbd8-5bb9-3cf3-9e0a-d093434aa526 | -16.34856 | -48.67452 | 2026-03-25 05:14:00 | NPP-375D | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe131534-f8a8-331e-a223-1f1c53d6ad3a | -22.05983 | -46.85139 | 2026-03-25 05:14:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cda728b-ce10-3ae8-b00f-7ff0f92cbced | -17.81308 | -48.61797 | 2026-03-25 05:14:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| fe7f75fd-c5a8-3ddb-b2d9-45b16298f0bb | -21.93167 | -45.16054 | 2026-03-25 05:14:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e58606f-1f05-3d25-8a6d-89a60b4bc3c2 | -15.24414 | -55.67336 | 2026-03-25 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bdd49a03-3915-3fcf-8853-df43aa325782 | -18.69766 | -48.30603 | 2026-03-25 05:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c6b0eca-931d-32df-bdec-7d49e5a633fb | -18.6381 | -47.92724 | 2026-03-25 05:14:00 | NPP-375D | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 627ae849-1d51-377a-b636-1e9c3994c857 | -15.66125 | -56.4262 | 2026-03-25 05:14:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 522ac8a1-d73e-36a0-922c-86d82e77956d | -16.66057 | -53.119 | 2026-03-25 05:14:00 | NPP-375D | ARAGUAINHA | MATO GROSSO | Brasil | 5101209 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5b04e8b6-f93b-3212-b757-62f14819d106 | -15.66915 | -56.41981 | 2026-03-25 05:14:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9da5f07-460a-3547-9de3-79c6fe91ba56 | -15.80832 | -58.62915 | 2026-03-25 05:14:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.1 |
| f7cd58cc-c2ca-3b59-972d-e9fba740418e | -22.5161 | -46.08761 | 2026-03-25 05:16:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 46d5a90e-0c01-365b-a863-351fbb82fba1 | -27.31076 | -48.84736 | 2026-03-25 05:16:00 | NPP-375D | SÃO JOÃO BATISTA | SANTA CATARINA | Brasil | 4216305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 00d79e69-dd15-3b63-92ce-fe97f801df8a | -27.87314 | -54.55153 | 2026-03-25 05:16:00 | NPP-375D | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| e107e868-8446-3081-99f1-1e9c6b609342 | -28.25399 | -49.09055 | 2026-03-25 05:16:00 | NPP-375D | BRAÇO DO NORTE | SANTA CATARINA | Brasil | 4202800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a680075-5930-36be-85c2-43753a2b2ca6 | -28.0896 | -51.62891 | 2026-03-25 05:16:00 | NPP-375D | IBIAÇÁ | RIO GRANDE DO SUL | Brasil | 4309803 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| ae3b2b34-4f72-3a01-8ec5-704938d503b8 | -23.01238 | -53.39097 | 2026-03-25 05:16:00 | NPP-375D | SANTA CRUZ DE MONTE CASTELO | PARANÁ | Brasil | 4123303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b0d2123-3da5-3b95-a9f7-a173fbe3d0a6 | -23.81465 | -55.13068 | 2026-03-25 05:16:00 | NPP-375D | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 8450dd2c-5a36-36a4-9ab3-d28da08f22ac | -28.30281 | -53.81375 | 2026-03-25 05:16:00 | NPP-375D | BOZANO | RIO GRANDE DO SUL | Brasil | 4302584 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| dad7cfaf-c905-3c8c-af05-912d18cd7847 | -29.36822 | -49.95484 | 2026-03-25 05:16:00 | NPP-375D | MORRINHOS DO SUL | RIO GRANDE DO SUL | Brasil | 4312443 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| b650d6aa-24fc-37df-93ad-e96ae98dd81d | -23.02046 | -48.44644 | 2026-03-25 05:16:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 276ead32-43d1-3099-9029-6fc2c3a0ff94 | -24.98873 | -48.98085 | 2026-03-25 05:16:00 | NPP-375D | TUNAS DO PARANÁ | PARANÁ | Brasil | 4127882 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f623de12-90e7-35a1-8421-93e231eeae44 | -24.82841 | -48.10301 | 2026-03-25 05:16:00 | NPP-375D | JACUPIRANGA | SÃO PAULO | Brasil | 3524600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 189e3064-922e-369a-86d2-6274b1c5b1cf | -27.67779 | -50.6237 | 2026-03-25 05:16:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4dec1f09-e9e6-35e3-9bc4-e7b1dc2ad92a | -25.40314 | -51.75935 | 2026-03-25 05:16:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57f748f3-c8a4-3207-a78b-915ee84ac1f7 | -24.25372 | -47.16172 | 2026-03-25 05:16:00 | NPP-375D | ITARIRI | SÃO PAULO | Brasil | 3523305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1fb1539b-6936-321d-a976-cb4068dc4ba9 | -28.97872 | -51.39913 | 2026-03-25 05:16:00 | NPP-375D | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| f2392e8b-a31f-3fbb-b2ce-5cc16eed52f2 | -25.92323 | -49.78199 | 2026-03-25 05:16:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3dd1db1d-73d1-3fba-a832-f2041794fa57 | -22.33898 | -47.18718 | 2026-03-25 05:16:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf974b39-0d50-3ee8-ba0d-297f1f49fb04 | -23.26196 | -46.53839 | 2026-03-25 05:16:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 4c40abfe-b521-3d20-bf75-b08100d15888 | -25.31347 | -54.13604 | 2026-03-25 05:16:00 | NPP-375D | MEDIANEIRA | PARANÁ | Brasil | 4115804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a0b0e90e-b2e1-3919-aa26-d564da38f2ec | -23.27439 | -44.73091 | 2026-03-25 05:16:00 | NPP-375D | PARATY | RIO DE JANEIRO | Brasil | 3303807 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| e64b2688-8732-3f39-8203-024c1ac4fae6 | -23.69417 | -55.35768 | 2026-03-25 05:16:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a85d5ee-2ae1-3ba1-bc0b-a764fcf303d3 | -24.15192 | -48.8367 | 2026-03-25 05:16:00 | NPP-375D | NOVA CAMPINA | SÃO PAULO | Brasil | 3532827 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 28470e56-0e60-3448-ba06-cbf2ab2b25f0 | -24.1429 | -54.30032 | 2026-03-25 05:16:00 | NPP-375D | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 3a43aea7-b4e4-3d9f-bf54-12953e2cb2e4 | -25.6951 | -48.65463 | 2026-03-25 05:16:00 | NPP-375D | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ce09e14-c63e-3186-99fa-b50c2b5e221c | -24.47244 | -49.90092 | 2026-03-25 05:16:00 | NPP-375D | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 23378432-1fe2-3cc1-a1f9-2d9f1fdb3dc0 | -23.0241 | -48.44398 | 2026-03-25 05:16:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d71ccd65-1be0-319b-9838-5d479eb3add6 | -23.22665 | -50.64985 | 2026-03-25 05:16:00 | NPP-375D | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 4eb6eb43-1f36-3d37-9c96-011a783a8c46 | -24.05035 | -48.7871 | 2026-03-25 05:16:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b7a05c65-9641-30c3-8bb2-f58f590833fa | -22.7956 | -46.94588 | 2026-03-25 05:16:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| b41e29d0-1af3-3bdf-b024-4561aad966c1 | -22.15816 | -48.41951 | 2026-03-25 05:16:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ff6a3af0-48e0-3d38-b3ef-2520fb08ecda | -29.44938 | -53.82402 | 2026-03-25 05:18:00 | NPP-375D | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| f86c5925-3c44-3b49-86f7-5374b937cf52 | -29.91101 | -52.98574 | 2026-03-25 05:18:00 | NPP-375D | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| b5a33c1d-9895-3871-b9c2-5933f9206f9c | -29.4294 | -54.10847 | 2026-03-25 05:18:00 | NPP-375D | QUEVEDOS | RIO GRANDE DO SUL | Brasil | 4315321 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 2dc051e4-8c04-3e61-827d-aadefef938ad | -29.81896 | -55.19896 | 2026-03-25 05:18:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 49e0b80a-6545-33fd-b408-9235e3242d2f | 3.85345 | -61.27557 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a46a521-db47-3e76-a36f-b370a497f53e | 3.85514 | -61.28625 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35f51d7c-78f3-37e4-a9ae-255356d5d05e | 3.77247 | -60.76231 | 2026-03-25 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef695dc0-9b70-3798-97c8-dcf885d4e035 | 3.93333 | -61.28946 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 476b5604-990c-3222-a995-683dded9d8bf | 3.85121 | -61.26134 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4988f3c0-f335-38ec-8580-0afd21c87a50 | 3.85178 | -61.28677 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35cd9e26-a851-3805-ac9e-cf17b456cb2e | 3.93277 | -61.2859 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aafaf80-6d43-39d1-b965-d5797f4e821b | 3.85177 | -61.26489 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31e6df41-a6dc-39dd-96b4-b188346cfc09 | 3.85289 | -61.272 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80d2aabf-e51d-3632-bab6-337c5017d731 | 3.92105 | -60.19421 | 2026-03-25 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da28b702-e40e-3638-a7dc-69bacc416ff5 | 3.85234 | -61.29033 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cc36e35-d99d-3427-85be-181edb389ee3 | 3.92997 | -61.28999 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f98a291-b03c-3862-a44f-fd7a002d09b4 | 3.85401 | -61.27913 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6999ae11-43d5-3ab1-b7ac-b145753a8ce3 | 3.85233 | -61.26844 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c14b30f-7399-3fdc-9dce-25387a8fe5b4 | 3.85457 | -61.28268 | 2026-03-25 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dcfb505-0a49-37a2-8007-b60953fb31d4 | 3.76915 | -60.76283 | 2026-03-25 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dca2a8f0-c23f-363a-a604-2e4baf8e5f90 | 2.72275 | -61.34883 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c282130-5ce4-30b2-89b4-5e3025c9fcb5 | -2.83052 | -57.6916 | 2026-03-25 05:29:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53150940-3c6e-304e-8bc2-39afaa5946a7 | 1.41969 | -60.75703 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17019f3f-e824-3e0c-91ee-7f42348e9786 | 2.67425 | -60.24353 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02c0573e-0973-30d8-af3a-1ca681aa35dc | 1.95001 | -60.90991 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21556058-8af3-3b92-9523-363162eb0463 | 0.81041 | -59.35479 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbdd03a5-17d5-3cc4-9f39-2897668d0fdd | 1.94616 | -60.90697 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d54be43c-8b7d-3d08-8f88-86940bb20903 | 0.81209 | -59.34365 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4e40b9ae-8247-3339-9a4e-d1b20cccddeb | 2.70549 | -61.34793 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03a392f3-bbe8-334f-95b7-d8b396259670 | 0.8132 | -59.35073 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 993f4c1a-98d9-32aa-8524-84533b6bd900 | 2.71383 | -61.35745 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3abda79-a9ee-3755-a613-87c4ca4376d1 | 0.82213 | -59.36383 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50da6be7-3de7-3e04-8b6b-f83984b67bac | 2.03873 | -61.10471 | 2026-03-25 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a6e9196-57c7-3e1e-a4ea-21bf22f18d5c | 0.81543 | -59.36488 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1caa7c15-0b75-3562-86bf-bfbd7e658eb0 | 1.92493 | -60.27692 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c615f1c-0b48-3d80-a411-4a14af1a912a | 0.80929 | -59.34771 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 114dc0e6-5db5-3d29-9d0e-66a264121635 | 1.76816 | -60.57579 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8509bfbb-0cbe-3581-a15d-be059878fe5d | 0.81209 | -59.3654 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| beac6e82-1d02-3847-90ee-39ed4ec91d14 | 0.81544 | -59.34314 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e8dc7f93-6d7d-3179-a9e9-84162e72e0c1 | 0.81711 | -59.35374 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 894eb36e-0796-30cc-9f3b-cfdc7ffd889d | 0.82157 | -59.36029 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f081f909-d4c8-39b9-9a0a-7344d4c7a62f | 1.56336 | -60.46075 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8884d64-e773-3633-9aff-bb9020902cde | 2.7283 | -61.36241 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1d63b55-be78-3b1c-9d0a-611288eeacdf | 2.70883 | -61.3474 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aecd2bce-8477-3eae-b152-06975d4404e6 | 2.7272 | -61.35537 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 877da2fe-44d8-33fa-b804-8da6afcd25e9 | 1.92439 | -60.2735 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3765ab45-d115-3b85-b9e6-c3ba81ac3eb7 | 2.67977 | -60.23565 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18c46460-c642-300f-99a8-ed5ef613e2fb | 0.81599 | -59.36842 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3d3e0d0-2e8d-3ae9-b65b-660f36425f95 | 0.98039 | -59.37938 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 557dd8b7-e96c-338b-98e0-970d1b5e3270 | 2.32487 | -60.39651 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
