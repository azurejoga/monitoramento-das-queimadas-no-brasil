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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 329a7b0b-7bd9-37ed-b00a-0cbb1a67c93a | -11.43417 | -43.44608 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f0690d6-eab5-3c2e-89ea-4a0ea44c1eeb | -10.81871 | -48.73185 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 527d921b-771b-3204-b3c3-26d7232ac1da | -13.1925 | -48.536 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9de477e-eccc-3ed8-9fa2-78935898c196 | -10.81214 | -48.7368 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4d8c58a-e73e-3ca9-8bdb-9b06f26df61b | -12.74287 | -47.28031 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e6337ac3-3c34-35b2-8c9b-2193ee4b2e24 | -9.99479 | -50.26979 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e3bc901-c9df-3ebc-bd05-6e3c0a588970 | -13.11391 | -47.41155 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 018c3396-3817-36d7-be7a-5973bb7c129c | -12.49261 | -44.95458 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a148631b-079c-3bad-a506-f90a912c1b77 | -12.77779 | -44.14946 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76aa4e9a-9064-320f-9a79-96eee40bbdcf | -11.44366 | -43.47314 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06dbad7b-a578-3e04-aa21-53179b8bdf62 | -15.002 | -47.86996 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c5aa6ca-de5a-3b0f-8e5c-f8b8de75c1cd | -11.40303 | -43.42659 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 553775d4-87dc-3ff6-9127-f9973376ac48 | -11.38234 | -43.38309 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6aeddb2-f61c-3b79-897b-1c1a2fb1c4b6 | -11.43531 | -43.46088 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acb7ecf7-f32c-3598-af8b-f749f311ebd4 | -15.4745 | -46.13118 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 598f29dd-6099-3296-8973-6788a679832b | -11.26778 | -43.53255 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5795831d-99d6-3c64-bca3-202d81ef5156 | -9.82781 | -45.27788 | 2026-09-29 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df9b0b5e-4b97-3d3d-8935-423a6431236f | -21.06846 | -48.8427 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 47210bee-c4f2-3cd2-8c55-8f3e76bfb83f | -10.81956 | -48.72697 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d0c30b9-595b-3999-8429-6a466788a0ec | -11.37213 | -54.05704 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aaa6b2c-1d33-3bbb-bec4-98941f4800fb | -11.189 | -44.82832 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f16323e2-583a-342e-bdab-673bdab8cf40 | -10.21786 | -50.0102 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2faf898-d4a7-3857-b3b2-9e40a24137c0 | -11.17689 | -44.79762 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e25fdcc2-306c-38f2-9abf-7e8095528ac6 | -11.54797 | -54.5006 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff43403a-64b4-3f17-b608-ac0e6b7e8615 | -19.00592 | -47.87678 | 2026-09-29 04:17:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72f22eaa-cd4d-37b2-882f-0029e148ae7c | -12.76463 | -47.30052 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c9410bf-ac8d-3370-b96f-cd7d691078e9 | -11.13047 | -50.06446 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 312fed8e-918a-38fd-96d0-0d4fbaea0728 | -11.62169 | -44.14868 | 2026-09-29 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d3ab999-f34d-3017-b90e-148d4f751bcf | -8.66257 | -48.88532 | 2026-09-29 04:17:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c091a17-f77b-3001-accf-24df968c0a98 | -22.16788 | -49.2332 | 2026-09-29 04:17:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37156417-c80a-3656-89de-56e9dea1de3f | -12.03299 | -50.94728 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2158156a-9654-3045-b568-0c4e306077e4 | -15.22656 | -46.17033 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55beaefc-7fc3-3d99-baad-63e70dee5a3b | -11.36321 | -47.44602 | 2026-09-29 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a11a1ff9-8ce1-322b-950e-c0bfd72a0f26 | -11.85038 | -47.11493 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5247ee6-2a39-3bf3-878e-8274bab20449 | -11.43089 | -43.46748 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 37b44bc8-0d7a-30b1-9021-e8de4bc01e6c | -15.25761 | -44.82265 | 2026-09-29 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f55c5f3-209a-3f42-8029-0bf8d0b8c2c3 | -10.81672 | -48.73316 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04df6be6-814f-35aa-b45d-9e02a35caabf | -11.91691 | -50.88784 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf950e49-6189-3978-b57e-40025e525582 | -9.95766 | -50.15297 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae59d5b1-ecfa-3a6b-9328-56f312a8d406 | -14.30686 | -44.99113 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f67ad2fa-9336-3b39-90af-e082118043bf | -15.10066 | -53.87067 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f045c4f2-83d6-3715-a463-c126036a3288 | -10.26587 | -44.63908 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 998f9270-f515-3f2b-9dd2-5be06f7c960e | -12.31493 | -50.29428 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 098fb420-588f-346d-83e7-73e0b61d1ffb | -12.06334 | -46.49603 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2d9e972b-c7e5-3d35-8666-2d6b18579bb2 | -10.26973 | -44.6361 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 707e7532-6156-3e18-b366-904519582b05 | -11.10179 | -43.30658 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 722edebd-3af9-37b1-bceb-db099e7fb354 | -11.44143 | -43.46549 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8641a823-5395-3193-9d6d-3aff108cea98 | -12.00354 | -44.92848 | 2026-09-29 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5f2d447-cf45-3f6b-98c2-eb4baab6c3df | -11.63002 | -43.49832 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e636d1d6-536d-3c78-ae15-ae4db6bab996 | -14.0984 | -46.99382 | 2026-09-29 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c56d880-6ecf-3eba-a922-8c32ae17875e | -11.39147 | -43.45765 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 254ce0ef-c537-306e-8887-9edf385d7116 | -11.3569 | -54.03936 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ca59a5f-8a1c-3e8a-8605-54b3bc01253f | -15.0129 | -51.40302 | 2026-09-29 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3276ca76-91c9-32db-b44a-f410cec45746 | -11.43864 | -43.4614 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 431b653a-9259-35c0-9c65-8fa69f45bdac | -12.76114 | -47.29992 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bf147ee-4140-3482-87f9-f61df7970577 | -11.40915 | -43.4312 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a859fcba-e5de-3a65-b54f-cb12ae65c851 | -11.40528 | -43.43425 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92836a05-ec77-3255-aa29-68326f3f8b80 | -9.13263 | -48.34402 | 2026-09-29 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3401254-b1e4-344c-bddc-f024c97b19f4 | -11.44864 | -43.46297 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 027bc99d-cc8d-30b9-a001-2741f624080c | -11.34137 | -54.12149 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c923c372-19c0-3f5d-81bc-62c39726bbe2 | -11.42751 | -43.44504 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb89d045-49c5-362f-a5f8-59141d553fe2 | -11.40691 | -43.42355 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6feef4b0-9e80-3e9c-bfdc-ce789bdcd46f | -11.12913 | -50.07224 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 101f905c-5b29-3fb4-86d5-be9ab2acc2c6 | -12.73657 | -47.27511 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b20995a1-938e-352e-b315-14a1ab9efc89 | -16.19656 | -42.8809 | 2026-09-29 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 994c878e-9fdc-3169-a0d8-6c9e35bd0d5d | -14.0705 | -46.32856 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64304b82-c8ca-38b4-8280-cca10188cd4c | -20.68756 | -41.97127 | 2026-09-29 04:17:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b25c9083-bea6-33e0-916b-0b8b85f473f2 | -12.05287 | -50.21975 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4bede61-50d5-32b8-b455-5c2c49023fab | -12.00943 | -50.97842 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac7895e1-5af1-34a3-b482-c29124f11851 | -11.6834 | -44.5172 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3013763d-cc34-3cab-8e4d-a4a7498aa77c | -11.42193 | -43.43686 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24b3f1eb-d907-3ff5-a966-9035dcd52864 | -12.61783 | -47.26851 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f02ee411-7775-3fca-abb5-d1ea8682959f | -10.70807 | -44.42393 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0abb3ba-2f4b-33cb-986f-41cca61111e7 | -12.7618 | -47.29593 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50cb47b0-8134-346d-bcb9-1633c60d5500 | -12.56015 | -47.15399 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c8db37b-6084-339f-932e-85f937171176 | -8.74428 | -47.87262 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1737c84-0318-3149-8254-e3b7b86f0086 | -13.34355 | -46.81636 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c9aa0e52-eb08-3dbc-891d-b5cdfdbe9c19 | -12.01712 | -50.93554 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 750ecba5-57a0-3830-a11d-1bfe325e279c | -12.71601 | -46.99862 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dfed64f-ac27-3ef4-93a6-8f209020ee20 | -11.45201 | -43.4854 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e05e643b-d712-396f-a46d-fac352928d41 | -11.42248 | -43.43329 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 77051025-230b-31ca-8c96-e8ed6964433d | -9.83344 | -45.26404 | 2026-09-29 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff3e5ba1-ef91-31e2-81e0-c53565c6e2dd | -14.43209 | -42.30894 | 2026-09-29 04:17:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| edc1fa3f-8bea-34fe-9e69-dbd342ee1268 | -8.88533 | -46.19905 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3175fa54-d591-3795-84ab-88a0a22c627e | -12.01558 | -50.94409 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 792f3a3d-36a4-31e7-837e-5765bb407fc9 | -9.7945 | -48.19632 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fb4dc73c-375f-31de-98c3-fa7a3b7e0dd5 | -11.09979 | -47.11114 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9146d7d4-1bee-3453-a7d6-cdad46af0a72 | -15.16255 | -46.16704 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f0b7cb2-6628-3ec8-b524-8b544eeec2af | -14.82039 | -47.28466 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527cbda3-df59-3f9b-840e-24a2014f4ecd | -12.01277 | -50.93475 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e61a2e4a-1fc9-34b5-a878-2169c7e4084a | -8.88249 | -46.19465 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e399facd-9aee-3e19-91eb-c01018d5ec7b | -15.83058 | -42.56025 | 2026-09-29 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b9919e57-aaab-3b95-a003-a465f3af12ae | -13.3253 | -43.94793 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c754801-436f-37a4-99a8-5ad189d406ad | -15.1755 | -46.12845 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e6682de-200d-3fd4-94f8-0b1760a4aa92 | -15.12936 | -43.61886 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f0e11a5-134d-3f2a-b11b-2c1adfa4403b | -15.86952 | -40.45948 | 2026-09-29 04:17:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 0e0bbcb2-96be-3c41-b54d-c8d44e6c2961 | -11.40582 | -43.43068 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9c7b8ae-0c6f-37c9-b651-9c1bdd611949 | -11.39461 | -47.45553 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d921526c-7d99-3dbf-9e66-dc2b8c2e369e | -11.61232 | -44.14359 | 2026-09-29 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 623143e5-4a82-36ef-91af-2d7a134a1cb2 | -12.36998 | -46.40457 | 2026-09-29 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README23.md)
