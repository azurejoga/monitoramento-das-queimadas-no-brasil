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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df56d885-515b-3e38-924b-8d75a971110e | -11.85955 | -46.87338 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 662f8c4f-06e3-3849-aeb4-302836232b6e | -11.7399 | -54.56487 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8396e550-ee95-3258-86ac-fba64dfba92c | -11.01746 | -54.13472 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d678f2e-8d17-3617-a755-85ccc36e57cb | -11.88487 | -48.99264 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01a0755d-c3c2-303d-b8ef-ecca788d1e68 | -16.53826 | -49.10115 | 2026-09-20 04:21:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 294b203b-6b24-39cb-a135-9cb61f1fd59b | -11.83788 | -47.64927 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f8594336-3fb1-3b41-a6a5-07436bd9c9c6 | -11.10105 | -54.02998 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3d1ed5e7-54d9-37e3-9740-3e43e36d8e26 | -11.84975 | -46.86208 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a70e7cd-761a-339d-9c97-88c37204f8b5 | -14.1381 | -45.5572 | 2026-09-20 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2143d326-2dd2-33db-bf05-d8e5bfd877cf | -12.75728 | -46.145 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 928d2cb9-fe4c-3b04-9da5-fdf899e3fd29 | -13.38503 | -49.44679 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d795eaf-3012-3fba-8658-c71e970133bf | -11.86303 | -47.67014 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 01450ac9-9f5c-39a0-97c7-cb50fb2e4ab1 | -15.597 | -48.09317 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca2e42d8-19fd-3a15-ae41-f66af1400223 | -12.74218 | -46.19025 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a372fa15-cbf2-33f9-8ded-2945acd659a2 | -11.86387 | -47.67183 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f57852a1-9b26-3593-81ce-c216b7c58f30 | -18.57566 | -46.85872 | 2026-09-20 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f43d57a-67a7-322a-a2b0-a0ad85195a8d | -18.00246 | -48.03687 | 2026-09-20 04:21:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e060eed9-fc79-3edc-a5fe-f16270f8e683 | -11.05072 | -54.18329 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 142153fc-1e7b-354f-85b3-c70f32c97820 | -11.39014 | -51.41718 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89874719-1dc5-3072-b8e4-0098bac91e1b | -11.21832 | -54.07664 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8d96a85-7e48-33e0-83af-87ec35508a9e | -13.23806 | -46.95746 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38734cb2-9006-3eef-89ab-a0a6e93be9a6 | -11.10199 | -54.02901 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cc8505ac-2113-373c-b1ab-fae254514c82 | -14.108 | -44.83176 | 2026-09-20 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 406bf660-09cd-3e52-82db-b60b8d0aecdc | -11.83619 | -46.84994 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73649b09-0a70-3f45-906e-ee9027cbc164 | -11.74613 | -54.56614 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c681d6b-9c2f-3ca6-b347-805db8705636 | -11.85995 | -47.6642 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ad711ae-9dad-3cef-af84-58fe5e24bc01 | -16.58029 | -51.62574 | 2026-09-20 04:21:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0195d25c-b0e3-39ab-810f-6d4b237cdefe | -10.8829 | -53.98303 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2af3c971-a976-3d85-bc7d-cd6946cfacaf | -11.75038 | -54.56418 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4990c99e-2b61-332b-9d67-bb672d8d8569 | -11.87191 | -47.66632 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f43bb3d-1d52-3e2f-95ef-917ce883a4b3 | -12.37046 | -45.80276 | 2026-09-20 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4c7ad0f-a908-3343-a2d4-8e47c4fa29d5 | -12.37587 | -46.99868 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e863be67-048e-3f58-aa89-e18f7fdcf714 | -11.23568 | -54.08504 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2a74491-9594-33b4-bc72-a6b3abd8193d | -11.2182 | -54.07904 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 413c2f61-0a35-32fc-bcef-cc82109d6e6f | -15.62014 | -47.84027 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 26a3eaa3-742b-3a11-af35-216793555ffb | -11.95687 | -50.10535 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fed6564e-48dc-3548-9cbe-87fe3ffe3ae9 | -14.5987 | -48.09601 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1e7c4cf-8b08-3300-b7ea-77d55596e240 | -14.67443 | -46.69109 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a9d2b92c-36c8-38f0-96eb-8a619db5bbf9 | -11.19673 | -55.03866 | 2026-09-20 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0aae77-f7df-373f-9ba4-e0a1fded8bd5 | -12.28774 | -47.12001 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00c30d8f-8450-3911-8461-6cf161eb5e26 | -12.65367 | -49.47353 | 2026-09-20 04:21:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ddc5351-38e2-33a3-b7c0-16e1b864cabe | -12.15656 | -47.03654 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3b33754d-729f-3be7-a477-c4a8c67e472b | -11.85505 | -47.66874 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8361a11a-7adb-33cf-864b-71e4cbacecff | -11.38988 | -51.42385 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b1c884b-83c1-3adf-8b24-970add392ee6 | -14.92941 | -49.90812 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03d1d4fd-0f97-3334-8ec6-d33b8654e307 | -10.87681 | -54.0837 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01464667-1700-3939-b4ac-2ed34fad4df7 | -11.05272 | -54.18274 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4eea5e7-7d92-3793-bbf2-73c0c2c84586 | -12.74794 | -46.17823 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 23a2e3d1-95d5-35ec-a8b5-929fecf9b73c | -14.78449 | -48.53788 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea5d3572-ffac-3ad3-99e2-140f0e70ff5d | -13.87908 | -48.58498 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6ed9e5d-b862-3a63-850c-1172fe348799 | -16.09871 | -49.64616 | 2026-09-20 04:21:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74cb2cef-0092-3bc0-9e1e-0226759ffe9e | -15.67697 | -52.72914 | 2026-09-20 04:21:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef8c0961-018b-3927-b483-26905c81f1cb | -10.88022 | -54.09073 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f84d39dc-bc55-3f2e-b1c2-eff6e7a1fb1c | -12.76447 | -46.12443 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 807e839d-f20a-39f9-a7ed-0dd4f9bb028a | -12.76304 | -46.13289 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a1db052-3340-3bce-b274-cd7177a2f6c0 | -13.03176 | -46.91949 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6834184b-4e10-3805-85ef-eb3b615c6ddd | -11.72849 | -54.55709 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2138af11-9fe2-369c-88b2-b1f12a632176 | -13.02355 | -46.92226 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7dc9b34-cd94-34a9-a46f-cbf698ea8105 | -11.86274 | -47.65522 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 538eb606-49a0-34a2-8b58-f618ce8da04a | -13.01688 | -46.91614 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba50b0ab-0118-3511-9d81-e8d53ecd9007 | -10.91715 | -53.97045 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f00afdf-e706-3932-bbf8-3a2859cca302 | -10.87599 | -54.08005 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 151d186f-f2c9-33b9-a4e5-8c56a73832da | -12.75084 | -46.18313 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 61f7c4d5-b1f8-3d8d-b4c1-7a32ee9f5bbd | -14.18578 | -47.87156 | 2026-09-20 04:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d032025f-74ba-3309-a42b-a1edfe8e6dcf | -11.22626 | -54.06873 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0be6ab7-c8fb-3528-b156-608932c22b91 | -10.91623 | -53.97506 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 004467d5-7c84-3858-b124-f82d7ca470e7 | -12.75366 | -46.14439 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 986ef7af-2b0c-34ba-87f1-b67331bdea27 | -18.37793 | -49.39714 | 2026-09-20 04:21:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f916b1ed-5921-3269-a039-44415a2890d7 | -14.10893 | -44.84726 | 2026-09-20 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c59896a-9afe-3970-8aa1-57992e428fcf | -15.86758 | -49.91168 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea9654ca-c5fe-37fe-8cdb-78a23bb2252b | -14.9233 | -49.914 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df7c3a8c-eee5-3a18-8d55-82e0f447c679 | -12.75379 | -46.20984 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6d1a8ae-8265-3fab-bf4a-50bbc8900c3c | -10.87786 | -54.07077 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b94f8cfb-6b6a-3160-92e9-acfc78563d92 | -15.46827 | -48.42535 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e638a033-fbc7-35c4-a03e-45711c4be969 | -11.837 | -46.84525 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c33c9c1e-7e06-3b53-aeae-45f0fb56d935 | -12.73999 | -46.18112 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93e2732d-26d8-3e75-b4ab-48b94b3a636e | -13.02064 | -46.9167 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb6a2c19-6656-3b06-afa3-1c1cdc153e1a | -11.38898 | -51.42339 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e13beaa-b3a6-3f57-92d2-cdce122f9e10 | -14.67806 | -46.69176 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ddcd08f7-f723-3c0f-ab8e-0ba1ac2d30f9 | -11.86957 | -49.00275 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6b588dd-485d-331e-941b-5cda0b6efbce | -14.18269 | -47.86633 | 2026-09-20 04:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f495f82e-2a71-355d-a617-4be8032d7a2c | -12.52376 | -50.04385 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d29ba842-83b4-3295-a57a-2f16b477a177 | -11.37763 | -51.39859 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c79553d3-5f72-3d19-9436-7977b6d3fcf5 | -14.68968 | -46.68945 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3fa765c7-ecd6-344b-9d04-634bf5d73fc7 | -12.52099 | -50.0418 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96be04f0-2a06-36e6-8786-9e66cf47f2b0 | -13.03255 | -46.91494 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d48cac79-8d2d-3030-a615-bfcb17e7c140 | -14.69544 | -46.69937 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23d7d364-3c28-3f42-bad5-173d42b5bc9b | -17.01776 | -47.15146 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4511eae-5ad2-370a-a240-aa4d28f18650 | -12.75724 | -46.12321 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 472fea2f-cdc2-3309-9aaf-692b98d18ea4 | -12.87976 | -51.00191 | 2026-09-20 04:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1786301b-d82a-3095-90ae-bb47066c64bf | -14.9234 | -49.91623 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed095af5-42fa-3f65-8306-0237efc8cfd7 | -10.92416 | -53.96713 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93ca01a7-2c01-39d7-ba5c-098edbd48b4d | -10.91721 | -53.97385 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a665e5b-385a-3c23-95ff-1beea2953f66 | -15.4566 | -48.44474 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3d0eba2-0b7d-3d5b-97a0-f71a25f0a04e | -13.88394 | -48.58145 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 24738d88-ca24-3c9e-9476-f9a20bea48bd | -11.22534 | -54.07329 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e9a8ccd3-beb0-3147-94fe-99efe751f130 | -10.86794 | -54.08825 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59dda52c-0fb3-3419-b0a9-34531b4cf5c2 | -14.05617 | -52.09417 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dbeb46a3-fe5a-3469-bcbe-32dfb3004c2e | -13.96039 | -47.85254 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0e3acae-170e-3e9c-9797-45430a4c47f3 | -11.86213 | -47.67537 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README48.md)
