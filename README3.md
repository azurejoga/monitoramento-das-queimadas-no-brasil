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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7be39e18-43a3-3767-8d63-fa08181bb4e9 | -11.46091 | -46.62524 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66394af6-9191-33ac-9d5d-7a920349994c | -11.38866 | -47.83876 | 2026-07-06 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0befd13e-3956-3bc6-80e5-087f89d225f5 | -11.91824 | -43.37845 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dddd5951-71ff-3889-a1d2-770c45c35aac | -13.24708 | -54.31711 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a00590-a76e-36a9-9aee-1c0ff681d65b | -11.91768 | -43.38199 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36120c6c-4c9a-3879-88e0-25c2e0ef2ad2 | -11.4662 | -46.54927 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 539e14c0-d55a-3ffe-bb7e-2afbb170725f | -13.24019 | -54.3204 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ec9d3e-6bce-39ed-9f21-0b8887bf7cb6 | -12.34012 | -48.22051 | 2026-07-06 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a12050a-8081-38b3-a970-6878d3250b85 | -11.42986 | -46.62214 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28422f7a-b05d-3f86-9a82-edde071c216f | -10.45691 | -49.97709 | 2026-07-06 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0c3b6932-1c2d-38dc-81ae-0250e1925aa9 | -12.3434 | -48.22075 | 2026-07-06 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8f575ed-a34c-3be3-ad38-fc8579ca4e45 | -12.34273 | -48.2245 | 2026-07-06 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5b0f7b6-be7d-3108-84f9-8272d89068b8 | -11.9188 | -43.37491 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51e0ac95-d781-3e66-862f-1e3ceb96f9d7 | -13.24888 | -54.32051 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 279adf4f-b5c5-39da-a579-f224fc97e08b | -10.45216 | -49.97622 | 2026-07-06 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ec2635-a9db-3a05-ae5d-9b8d54d930ae | -11.92155 | -43.379 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05bd7b55-67b6-3270-9194-a84e799c7620 | -13.20607 | -54.30453 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 325dba31-103d-379f-8339-8660cbd9f53c | -14.16608 | -43.64761 | 2026-07-06 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ab9250c-fe0e-3244-955d-2064903613ee | -11.61226 | -46.83392 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7f01d5e-53c6-3e34-b7fc-798a0613cc21 | -13.25072 | -54.31166 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caa88f27-b99c-3a67-874d-bf1abf2da428 | -11.60094 | -43.83083 | 2026-07-06 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9eac075e-0365-36f9-9047-05b12ee1b929 | -11.62658 | -48.44572 | 2026-07-06 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 881b7847-f0bb-3d91-96f2-0906bbef7aff | -13.24796 | -54.3127 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 600455eb-9091-32e4-8bf1-dde2ec7d0229 | -13.24619 | -54.32155 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5de70649-c824-3c30-b740-36d0c096c13e | -11.44241 | -46.59785 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aed8bba-bf32-3d8d-bb72-78c64f2ef1dc | -11.63078 | -48.44645 | 2026-07-06 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 824ac1a6-6131-38b6-a327-e6aad481c860 | -14.43883 | -48.99721 | 2026-07-06 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 943459bf-45f6-335a-b84b-65c3e06cd746 | -11.89084 | -43.82678 | 2026-07-06 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 365696a3-0dd6-3354-97f1-19657c476803 | -11.92486 | -43.37954 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c649f622-41fa-3a79-8cf4-50aaa8adfe16 | -13.2498 | -54.31608 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e617922-9699-3cb3-b1c8-711156411889 | -13.24381 | -54.31496 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7a19593-2425-37fc-80cc-756c4cc1a4c6 | -13.25578 | -54.3173 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8af18c6c-d69c-31ff-9a6f-48aed9872723 | -11.45636 | -46.62922 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 202148ce-3d1c-3ea2-b561-b4892bfd10a0 | -13.24289 | -54.31937 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e970094d-fe23-3c0a-a84e-2f306a23aa02 | -11.92542 | -43.37601 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 03079073-f502-3607-94bc-5d1bb9596c38 | -13.25306 | -54.31827 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76f372f5-d631-3435-8a55-d347283db936 | -13.30029 | -54.3736 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1477895b-be4d-3a6c-b8fe-ba366a99d5f3 | -11.92211 | -43.37546 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e7902fd-73c8-36b2-a2f1-0a53b0678ed5 | -13.30124 | -54.36892 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8415f5a5-4323-3c04-b6ab-7575f5b88469 | -11.91493 | -43.3779 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05caf147-4ec3-3d6a-a7e8-36468994681a | -11.45555 | -46.63394 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33c68f64-9c5c-3eaa-885a-b6a4e58442bf | -11.46013 | -46.62983 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be2a7e66-96de-30df-9a76-4fd1f42b9879 | -20.20712 | -40.22331 | 2026-07-06 04:12:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dfbed58a-0b5d-3e5b-a044-39df9f5cda7f | -20.50392 | -45.24963 | 2026-07-06 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f84823ce-f7f5-32e9-a2e3-730aed255e3f | -22.04188 | -52.89788 | 2026-07-06 04:12:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 728dbcbe-8e08-3db8-bfa3-c52e2bd3160b | -21.41586 | -45.29328 | 2026-07-06 04:12:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 92202700-c133-344a-b1ff-ee36f97649d7 | -21.46766 | -44.32409 | 2026-07-06 04:12:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8629301e-a865-34d9-9c93-1748bf8b6410 | -21.12735 | -49.17989 | 2026-07-06 04:12:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ffbb94a0-6a8f-3098-add1-fe4df574e45b | -22.97305 | -49.17749 | 2026-07-06 04:12:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd6199fe-5a41-3867-8f6d-5161bc1bb23a | -21.46435 | -44.32352 | 2026-07-06 04:12:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05ce4780-be91-39e9-b3b7-f611f16a87a7 | -20.50451 | -45.24593 | 2026-07-06 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| eea53223-69d5-3557-8a1c-a58673a93372 | -21.59639 | -41.89375 | 2026-07-06 04:12:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a6a7c06-d498-3ff5-aab1-47bfa5f1a4c6 | -21.13928 | -43.95549 | 2026-07-06 04:12:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef531fdd-2a8d-33f1-abc6-41c0a0c90b5c | -20.20778 | -40.2183 | 2026-07-06 04:12:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 537e3c53-43e2-37d8-a97c-269639c16779 | -21.59282 | -41.89315 | 2026-07-06 04:12:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dddd34ff-1afd-36fb-9fb3-27f9fc5425d6 | -21.12712 | -49.18163 | 2026-07-06 04:12:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 68f8e998-f2db-3bb1-98e0-89bb3ffd4947 | -20.39661 | -42.90501 | 2026-07-06 04:12:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eca78871-59b2-3e67-a2bf-eda66b1606a1 | -18.93732 | -47.44309 | 2026-07-06 04:12:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdcb2abf-0fc8-3d6d-913d-081c5304de38 | -11.9305 | -43.3812 | 2026-07-06 04:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a77bf606-7fea-3a85-9571-e424879b7b1a | 0.71645 | -51.37534 | 2026-07-06 04:42:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc28cab0-88f7-306e-807a-0d5957a8135d | -2.9667 | -48.9898 | 2026-07-06 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6407cf1d-0419-30c7-9467-7565d48aa0fb | -2.96329 | -48.98927 | 2026-07-06 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91ba76f0-6bc5-3878-96bf-897ded3c1e41 | -4.34517 | -47.7649 | 2026-07-06 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0e90ddc-3578-3ada-ba04-6ef44853a335 | -2.96318 | -48.98962 | 2026-07-06 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf723b4-b368-3211-a2b3-371f812c170e | -6.90487 | -43.71326 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d8312ac-53fb-3fce-a46a-69f30b13f33b | -5.67238 | -48.09945 | 2026-07-06 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfd08495-c186-39e2-b2b9-182000166928 | -8.71742 | -54.54214 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 571dc89a-a1df-3140-882e-5a6140e5f50a | -11.926 | -43.37582 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 84a8d36d-ffde-3b23-99e5-4cca8da54a8f | -11.92116 | -43.37934 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50598966-11ee-3a2c-927a-87f88c17d569 | -9.7516 | -48.1895 | 2026-07-06 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99cb7f93-9096-3daa-a2fe-561be84b2cd2 | -8.11702 | -47.12106 | 2026-07-06 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a19564c-d54e-38c9-8bee-5b083a01a28f | -9.49924 | -42.99173 | 2026-07-06 04:44:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee031ec6-8c9c-364f-a274-6653378ef7b8 | -10.92718 | -43.06363 | 2026-07-06 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f6d0c4d2-f24d-30c7-b19b-091b84f4799b | -6.89707 | -43.71202 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584292a6-4f58-3c30-a489-1ebe6ede689c | -8.77439 | -47.4066 | 2026-07-06 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdd07eb2-1408-3796-852a-c9da9fe97e84 | -11.92546 | -43.37989 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 34062d99-0dd4-375b-a510-9f547852ae67 | -10.92775 | -43.05949 | 2026-07-06 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4481a71a-33ff-3c18-a05e-ffbe97127ee3 | -10.39262 | -56.77332 | 2026-07-06 04:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bd5cbe61-9aa0-3f0f-b731-2a42c9c18d8b | -9.49979 | -42.99306 | 2026-07-06 04:44:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8cffe69-c6eb-3703-8ea5-9071a365aab3 | -11.42953 | -46.62334 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f25b051c-9cc4-30b2-98d7-e98bc26d9f9c | -6.90878 | -43.71386 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96134f34-f91b-3539-96e8-8b53c8ad0620 | -11.9195 | -43.37685 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cdffd717-8883-3dc1-acfc-3efad2198440 | -10.45576 | -49.97767 | 2026-07-06 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8885e326-d6ec-3ab3-8928-fd5b0e7e9b36 | -6.59256 | -51.69866 | 2026-07-06 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 905f44d1-2967-316b-a3da-0a5f7fc30be4 | -11.46504 | -46.55001 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 70fb7b06-a9ef-3259-a73a-cdacb803e59c | -11.91632 | -43.38286 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 63b0bfab-1d42-3618-b9f7-10be00a207de | -8.37477 | -46.87764 | 2026-07-06 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7afed888-8230-3d47-8909-cbd23af1c0f7 | -6.94008 | -43.71535 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d27846b9-2266-340f-9d43-f5c7c4e3cbf8 | -11.45743 | -46.62627 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f759bc35-ce49-3212-bd92-010de5a8943b | -11.46209 | -46.54546 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db7ef6f3-0601-3d06-823e-82da89f198cb | -11.89073 | -43.8261 | 2026-07-06 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dfbed51-cec2-3cd5-8e83-b6484d48ce9f | -5.6757 | -48.09998 | 2026-07-06 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b224dc-421d-3607-a1b4-1f2d8a2fa333 | -9.27379 | -48.21452 | 2026-07-06 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73aa805c-55f6-3714-9bf8-dd0df58d51e2 | -7.90141 | -48.25432 | 2026-07-06 04:44:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2aa0a196-c738-376f-b121-c4b007d49fb3 | -11.45273 | -46.63364 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18e41aee-2d4d-3a4d-a29f-55b485cb901b | -11.62819 | -48.44616 | 2026-07-06 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a358d543-54a1-3e33-9001-244c4c312b3e | -8.71811 | -54.53814 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fa29e0f-4640-372b-a6c5-efab0c263692 | -8.64221 | -46.97439 | 2026-07-06 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4293aff9-a8ce-35e7-bf3b-4dcf94ab6248 | -11.92587 | -55.91484 | 2026-07-06 04:44:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd1ac697-f79f-3f87-aac0-f2336c1d5df1 | -12.33864 | -48.2266 | 2026-07-06 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
