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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef033a02-4b94-3ab4-a396-eb2614fc7c79 | -23.41964 | -45.71733 | 2025-09-21 04:40:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e200e65c-b44c-3eae-a147-35ba600a53d0 | -20.4588 | -43.2531 | 2025-09-21 04:40:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f4cf633e-54f4-3b91-a92e-ec252c69ba6c | -21.28997 | -43.88698 | 2025-09-21 04:40:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b5fea0f2-d5c0-396c-b52f-d79720e0c33c | -26.17696 | -51.73419 | 2025-09-21 04:40:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 74554a51-b1a8-32f9-992c-ab5998b30d2c | -24.75382 | -48.82227 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6a544dc3-3235-32e8-ad4a-48c2124f4126 | -23.13706 | -47.24029 | 2025-09-21 04:40:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8949df11-a464-3c71-9f89-236dd5a366ee | -23.41477 | -47.61779 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 938e1c86-58c0-36b9-bd17-20de045c331a | -24.96748 | -48.58743 | 2025-09-21 04:40:00 | NPP-375D | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 743a603a-2057-3a75-a4dc-c999de6b4c83 | -22.47856 | -48.21697 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 29.7 |
| cc4372ab-c3ff-3f87-b0dc-c6ad96e616f4 | -22.46762 | -48.2152 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb651071-d2d0-3834-9109-45fc10eb2b0c | -22.78117 | -55.37008 | 2025-09-21 04:40:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fc3af77e-8577-326a-8238-2b2e9e028ca8 | -22.47067 | -48.22024 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a65cb837-daf9-3b83-91bd-97352f207f37 | -19.84057 | -57.29952 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a37f64d5-5a7c-3e1b-a9f4-2a98c6d3d95a | -24.72659 | -48.86285 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3df32076-7449-3faa-aab3-ed57397d93c8 | -24.7586 | -48.81429 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0b9f5a70-45c5-3d5a-8b3f-a95b1d64c8c0 | -20.54134 | -56.1469 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f6d4d0-1d9a-31c3-b792-297fe3907638 | -22.13681 | -53.85527 | 2025-09-21 04:40:00 | NPP-375D | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b92caf7-7a2c-3e1e-a9df-125e4e06ec05 | -21.12432 | -42.9874 | 2025-09-21 04:40:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 150d9bf3-385c-3515-ade0-fef1e8f407ff | -20.44755 | -45.24057 | 2025-09-21 04:40:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3686edfc-9412-3f8e-96e4-22929d52f02d | -23.41681 | -47.61582 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2cb1946b-c297-39ee-8bfa-ae923d6b2ef6 | -25.05635 | -52.19379 | 2025-09-21 04:40:00 | NPP-375D | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf12236a-835a-3963-b599-244a8160fd44 | -22.27072 | -56.01516 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91c0561f-8ee1-3a8d-8568-624b69eb81bd | -24.75829 | -48.82123 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 16b5e96a-4384-32fc-8034-b4dd2922c1cd | -22.47552 | -48.21185 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3faebcd0-44e3-36ac-bb07-133ac6151ff1 | -23.15167 | -47.62078 | 2025-09-21 04:40:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2efcfb04-e4b6-3466-b86e-909b2ae133cf | -24.79288 | -49.46787 | 2025-09-21 04:40:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07972f28-753f-3377-9f5b-b58d75694752 | -23.36704 | -47.14764 | 2025-09-21 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d4a50093-9413-3839-b903-f5b1a253bc54 | -22.46638 | -49.01656 | 2025-09-21 04:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 057edddf-eac5-37b9-beb1-177ba80f7e4d | -22.47668 | -48.21 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1b5829ad-9cfe-377e-96c3-3623712f14a3 | -20.6098 | -56.71958 | 2025-09-21 04:40:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f22bcdf4-1721-3ee5-9be4-3e15b497ed20 | -25.05695 | -52.18998 | 2025-09-21 04:40:00 | NPP-375D | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 58969b05-6d1f-3b78-a1b2-1db8828f3646 | -24.75584 | -48.81196 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6ca0a269-b508-34d5-be35-28cdfa45f6b6 | -23.48547 | -45.42776 | 2025-09-21 04:40:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e45a6485-3ddf-3084-a7ac-9423384eb6ab | -25.1528 | -51.97182 | 2025-09-21 04:40:00 | NPP-375D | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6d76727-384e-3925-8e18-a62e4dc321be | -23.14344 | -47.62453 | 2025-09-21 04:40:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 796e03e7-f097-3dc1-8a3c-902a54c682fb | -22.47612 | -48.20739 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 434a4889-268e-3dbf-b9a8-98a86fffa65a | -20.25139 | -44.36453 | 2025-09-21 04:40:00 | NPP-375D | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c954630d-0efd-38a1-95a4-eae9e054a801 | -22.47303 | -48.20942 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d63993c8-f831-32ec-a4de-ad74bef13ee2 | -20.56213 | -54.657 | 2025-09-21 04:40:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d38f0fbc-bc19-3930-9d38-edbaef076eec | -22.26693 | -56.01427 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b154aa6-fe89-3a2f-bb77-a58183070429 | -22.70185 | -51.55844 | 2025-09-21 04:40:00 | NPP-375D | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ffcb0c4c-3ba5-3262-bb1e-58f4d67c3498 | -23.55214 | -50.86141 | 2025-09-21 04:40:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5adfb60e-ebca-3b02-85dd-2c91a323e813 | -23.54541 | -50.86021 | 2025-09-21 04:40:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eee91a69-b71f-3d4f-9ae6-8b690e254de9 | -22.74178 | -47.17059 | 2025-09-21 04:40:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25e91b0e-1aeb-3537-99a3-b543a094cc16 | -22.47432 | -48.22086 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 99318154-c34f-3f0f-8bf6-811e7ed9a4e4 | -20.54745 | -56.14528 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c12c66-3100-368d-a2f7-41a3f9ee3cda | -22.46821 | -48.21072 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b3edb57-d35d-365c-85a7-03f0949c5b82 | -23.44636 | -47.61377 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2fdc4f8c-0cd3-3fef-aeeb-6c7c033b88fb | -23.97282 | -46.47118 | 2025-09-21 04:40:00 | NPP-375D | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf5dc0ad-1d4e-37fa-b765-ecd4e42cecde | -20.54528 | -56.14772 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00da28eb-0409-3b1e-a1e1-6d3de48f6b13 | -23.15655 | -46.64817 | 2025-09-21 04:40:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a41ca618-7848-3cda-abd2-e492eea95b47 | -23.54877 | -50.86081 | 2025-09-21 04:40:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15bedff7-537c-37dd-bcb3-af53d1fc086a | -20.53346 | -56.14521 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f5c3017-d7c2-37df-8613-3455afdf3188 | -22.72025 | -51.4189 | 2025-09-21 04:40:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0374ea9e-813d-3542-875b-4e4a0c71a3c7 | -23.01484 | -45.42214 | 2025-09-21 04:40:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00cddd35-9be7-312b-96c8-7878901a8d9f | -23.42237 | -47.61916 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 856b6e70-9038-37fe-89bc-42df60a3731d | -22.47606 | -48.21448 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d0a14519-5021-3584-bfa9-14ddd71b22aa | -22.47492 | -48.21636 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 533e16d5-679d-3b23-8cc5-0a1e162e74ad | -23.67982 | -46.10251 | 2025-09-21 04:40:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e98d7fc0-7519-3b4b-8a1b-9ebb42ef7d70 | -19.8363 | -57.29858 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 922f5c61-828e-32d2-b0e1-2a5c8dda8b9b | -23.1655 | -46.60903 | 2025-09-21 04:40:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 06d35f5c-2059-3bd5-b4a9-c3eba61415c5 | -23.13836 | -47.23667 | 2025-09-21 04:40:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34bfdefc-c73c-3674-9e91-5da119fea250 | -22.14028 | -53.85593 | 2025-09-21 04:40:00 | NPP-375D | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1ab2bac6-04b7-3943-88d3-42270baba910 | -23.38169 | -46.09902 | 2025-09-21 04:40:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f874c7b-3e2b-3692-bd61-247412ea977b | -23.24567 | -50.85673 | 2025-09-21 04:40:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 105def80-1242-3d48-8be2-3e21043d6329 | -26.70913 | -51.68486 | 2025-09-21 04:40:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 650c96e7-a3fa-39e1-9382-39a9bad7ec8f | -21.29173 | -43.88872 | 2025-09-21 04:40:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3b8a0bc7-63ba-3427-84ea-4900b450aa55 | -20.54037 | -56.1522 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d534f67d-2828-337a-bbb4-288ae9cc6892 | -24.75465 | -48.82066 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 75351570-85d7-3526-9a39-023bc2fb31e4 | -20.54231 | -56.14161 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1ea2ea6-c95d-3757-848e-c644427162e5 | -20.68718 | -43.19697 | 2025-09-21 04:40:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 22c09231-b0f0-3ada-bcbf-c5c513d166fb | -22.22424 | -56.0098 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9a1c476-3111-37be-9b57-ad9e81acd644 | -26.1736 | -51.73356 | 2025-09-21 04:40:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f0478fcb-bdef-39fc-b88d-b87817dc7a44 | -22.2989 | -48.49846 | 2025-09-21 04:40:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e1bb89db-e61c-3ec7-b8d0-410a7ee1a427 | -23.423 | -47.6142 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7aea0a91-8a05-3bf2-bedc-efa5a9815154 | -23.37753 | -46.0984 | 2025-09-21 04:40:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d101f9b3-5831-3143-8b0d-6ffa851575c1 | -22.63676 | -48.25763 | 2025-09-21 04:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 099e3d52-3027-390f-beb1-e3cedf6e8748 | -21.32112 | -51.66425 | 2025-09-21 04:40:00 | NPP-375D | NOVA GUATAPORANGA | SÃO PAULO | Brasil | 3533106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6cb4026f-e037-3373-871a-17865ffa9d97 | -23.50708 | -46.97543 | 2025-09-21 04:40:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 74e8a951-d975-3c61-b5d6-0ea2f0c658d4 | -20.42015 | -54.67609 | 2025-09-21 04:40:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dc56c45-458e-3405-afd6-a49502091051 | -22.47543 | -48.21899 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| df533b51-8afb-3946-9412-b6d12858713b | -23.34496 | -46.88583 | 2025-09-21 04:40:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35555ad0-9848-3724-89c4-e55d644a792d | -22.47187 | -48.21127 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd72a211-7294-3902-80da-83f5e23fea89 | -22.47117 | -48.22285 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4523a82a-e65e-3931-994c-10e715372655 | -20.4126 | -42.93222 | 2025-09-21 04:40:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0a679af-f882-33cc-ad68-5cab8e9dbac8 | -19.84993 | -57.29715 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d3cf50fb-ac9e-39bd-af30-a18533ca8d95 | -28.2823 | -50.35058 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 538f668d-ef01-3e9c-96d2-104bf7f94fc0 | -28.28692 | -50.36949 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8aad4923-6575-3f6f-baa5-2c34ddea5049 | -28.28644 | -50.3468 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 50c030c6-6589-396b-807f-93e5e45666e4 | -28.28875 | -50.3563 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c06f170c-9cb9-3132-971f-e313f77c0796 | -28.28705 | -50.34236 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0dfcfc17-3b6d-332a-b854-20003f7784a6 | -28.29045 | -50.37012 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf3947dd-0d36-309b-b192-489cbe6e6817 | -28.29398 | -50.37076 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 604b15d0-7777-381c-8211-c6352257882f | -28.28936 | -50.35187 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b0141d0f-0259-3256-8878-c398e9242c2f | -28.28522 | -50.35566 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d0aa1874-6eb8-3230-ae09-c694c0d03d72 | -28.28291 | -50.34615 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 304fee14-6fa0-3470-8793-647edfda83a3 | -28.28583 | -50.35123 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9bbd1666-17bf-37c0-820e-625c701c3e6a | -28.28631 | -50.3739 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 218f93b1-c6ad-3230-a3fd-af2dd4d33846 | -28.28461 | -50.36008 | 2025-09-21 04:42:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ba84981b-16ba-3047-befa-5d530352da98 | 4.32852 | -60.7449 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README33.md)
