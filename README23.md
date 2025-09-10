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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c184f84d-2acf-345b-83fd-0cbd4dbc590b | -5.75195 | -40.95388 | 2025-09-10 04:14:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7198598-8259-31f1-8925-962368146a07 | -5.41139 | -43.45095 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7d8ea1a-24ea-3600-9f1a-a6d8549dfd2c | -7.09345 | -44.13457 | 2025-09-10 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b958eb4-4237-3c38-a6a9-a99aa764cbf2 | -6.20108 | -43.29693 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8de0452c-4348-3b06-a3df-f36b472d8c30 | -6.46786 | -41.79699 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43c1e917-89a0-35cf-adad-1ef578dff444 | -7.09014 | -44.15553 | 2025-09-10 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5598a0fa-f579-3a95-9898-77f461298266 | -6.2022 | -41.03477 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5a85f7c-66b8-3649-b44f-895d177493f3 | -6.00768 | -46.68068 | 2025-09-10 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1275bd6-a156-3d2e-b96e-7d3e66050ebc | -5.79739 | -51.67329 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb8bd85b-eef0-3b1a-9176-190eee8b6003 | -5.73214 | -45.60319 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b866f781-bdca-3044-a0d4-c305d1fe1ad9 | -6.49303 | -41.76788 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04ed2b67-0d57-3ba4-96b2-8b351b9dcbf2 | -8.84953 | -47.27427 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9faaa980-4192-35cd-ba5b-df04fa2fba7e | -9.68997 | -46.86874 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c45f9d7-1264-35d5-8178-48c1e6365e6d | -6.05577 | -43.13649 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 38773237-4ce7-3bc1-97aa-53fb5f8605f6 | -5.74234 | -47.46938 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8d4c26e-c8ee-3bec-9b0e-9e986c995202 | -6.29449 | -44.21552 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de066c2c-635c-302a-838e-46a52f64199b | -8.87356 | -51.04009 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d05cb124-c22f-3aa2-b47f-d0aceab38016 | -8.37254 | -45.04 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 546538bf-8078-3498-84fb-67b29b659be7 | -9.71266 | -48.09188 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 775cf7b9-6581-3353-a881-0d18b55d2c34 | -7.9851 | -46.32782 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5e1d313-65ee-359e-87d7-49c1abfc1433 | -5.93674 | -45.95431 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94982099-1b15-35ba-b712-7a4e3cf4752c | -7.85359 | -46.04161 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc726511-1dec-3e1f-b080-b7e7d6be5df9 | -7.99572 | -46.32925 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f062126c-b2e9-3144-8afb-5879e738bb63 | -5.75482 | -40.9581 | 2025-09-10 04:14:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 627f5545-8120-34f7-b9a0-57c4bca8efc8 | -3.43489 | -42.46902 | 2025-09-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7cb1df94-3681-31e1-8d9c-e9f10a85121f | -6.87901 | -47.9034 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfd10f9b-82e3-34a2-ae36-eed61dd06d76 | -8.41616 | -49.1074 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39d0f63e-d84a-3e24-8558-42290283f7a5 | -5.79494 | -43.88849 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96fa4821-2696-3468-9adb-3efb38b463db | -7.08263 | -45.2027 | 2025-09-10 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3b1e5e06-85e6-314f-9106-c42e7a3403a1 | -8.02477 | -45.50433 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62606c1a-553b-3ef0-b3f0-91704f5ea475 | -7.86656 | -46.02774 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f85d62a-7831-3fcf-86b9-77b278ec4675 | -8.34585 | -44.8414 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a60fc230-b7f9-3e34-99bd-972e3758f25e | -6.86127 | -47.88988 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d19c80d1-2c29-3457-9c70-41433ef07a6d | -8.70837 | -45.29742 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 936dee8f-6f3a-3588-a9a3-2917f7b68971 | -9.31469 | -46.72145 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 94c412e0-898a-35e0-a377-f1ba341b1fb9 | -6.34608 | -43.65253 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc7c4244-c382-305e-8139-f6589d9866ee | -5.57208 | -42.92577 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c2a75eba-17d4-3435-8e4f-60729a0aeecd | -5.65871 | -43.91013 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54facc74-979c-3d09-b9c9-6014249f2dc8 | -7.84753 | -46.01287 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7544cb70-9197-3323-8498-52c4b4b8b2cf | -7.78772 | -46.06297 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56958cf6-0450-3f09-b1dd-3aa46083fdfe | -5.86752 | -43.2335 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87cd8c96-01ce-37a6-b642-1ed8431c7b9a | -9.60883 | -48.03824 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7d0b340-9308-333d-aa35-688123d81753 | -9.06527 | -45.72001 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0edaeb6-4eb9-33f9-b11d-a233fecabdc0 | -6.20274 | -43.502 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd96aeea-6aba-3b1c-85d6-a47fe9c1f1cc | -5.72325 | -45.41578 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5ef2ffb-9df2-3445-957a-bc1dd1b40625 | -10.30518 | -43.39229 | 2025-09-10 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b198afa0-91d3-3668-a01d-6e447c583be1 | -7.79045 | -46.09922 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a700be11-64b0-3405-a70b-97a90ed93bb9 | -8.2117 | -49.51202 | 2025-09-10 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac247398-5fde-3fbe-b55c-a478d30d501b | -8.20127 | -47.15249 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ace4bc03-4289-3893-8d70-777fe5020d81 | -5.54197 | -42.65981 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dce60bb8-b3f7-3958-8aab-4fddd86206bb | -7.38655 | -48.16928 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4af92fc-6d09-3809-adaf-a11629802d52 | -9.83386 | -46.05103 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d07c8b59-531c-3d96-a85f-633e124f6de3 | -6.8528 | -47.94024 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9958fc7-03c7-30b4-9295-6041f00e1ff3 | -6.67854 | -44.11149 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e9616a2-bcd4-391b-afa8-c1965372bd65 | -8.07485 | -48.6538 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01eb9c9c-6e02-32bf-b8bc-69167d77a7b5 | -9.21482 | -50.55619 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8e8397f-fa1b-347f-bf9d-43c30315e0b5 | -9.69221 | -46.81083 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd91051b-6e9e-3792-b907-dd353f655b37 | -5.41361 | -43.45838 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a8678293-7a87-37c3-900b-98858b0a7bcd | -5.56189 | -45.4855 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3328b7b7-911c-32bc-a95c-1f11fce79d48 | -8.42234 | -47.38441 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11c5f146-14b4-399a-ac2b-2695cfe5d1a6 | -6.44563 | -44.05632 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ee504c5-2236-3941-b7a9-f73a2dacb37e | -9.7538 | -45.39947 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 77c0c662-22c5-3dce-afb9-f63a06e23f1d | -8.04729 | -48.67034 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b75c6324-af89-317d-bfdb-04bf556e6c51 | -5.77537 | -45.53441 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0bc8138-ebab-3370-afff-509a8ba0a40f | -6.16173 | -43.37548 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 799e0992-f8c0-33ab-a8a1-ca303e01ec1c | -5.78583 | -45.40223 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81fa2854-31b0-3008-b1db-6d9420d11377 | -8.34899 | -45.0582 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a15b039-1145-32e1-85f1-1de6e1a980c3 | -9.06275 | -49.82284 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52a16ebf-a6ba-3470-a56f-7dd15ea3bc8a | -7.8688 | -46.036 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8aed8fc2-b6ed-35d2-90cb-916d71ee2963 | -9.69381 | -46.75703 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 074c86cc-1ac5-316c-afcd-d9b74ca29d02 | -5.74268 | -45.25586 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6276c07f-7003-3e28-bfe8-70d3b2a328a5 | -5.70441 | -45.45282 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90ae32e4-0979-3dec-be85-1ae8fa9e5edb | -6.41903 | -44.39802 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33665b56-c24f-3ed9-877d-94c0b6ea7b74 | -9.70351 | -46.80835 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aa7ff9b-0442-35e5-9948-1963d06ebf5a | -9.06794 | -46.98074 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2136396-ca32-3c2a-9fe4-ac6b7ce17e55 | -8.04942 | -48.68208 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e682449f-9189-3109-9380-909f89ebada8 | -5.34831 | -44.79736 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ead991ba-60f0-316c-a994-9b07aafca6cf | -6.39448 | -44.44503 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6bbc4e73-5de3-35c7-a7ef-63a10faf46fa | -5.70727 | -45.45722 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc38bf93-a8fa-3176-8871-d90587ea84d4 | -5.48741 | -42.65844 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d4ca2eb4-4fb0-3f28-b016-2aeeabe6cbbd | -8.42852 | -49.10929 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1dba806-6a91-3136-a91e-32f26e59637a | -5.85785 | -45.12739 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f22436dc-9e07-350b-a430-b2a276410518 | -9.05881 | -45.73817 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c795a4d5-1d91-3292-b34a-be3d7c619055 | -8.74491 | -47.09111 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd58e3ec-d5ba-3abe-bff0-8a09b660c09e | -6.39728 | -42.6063 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9affae94-bc25-3d34-a090-ddaafd55603b | -8.42054 | -47.28026 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e13c9b4c-4269-38f2-8fbc-0da7c240b525 | -6.33979 | -47.10119 | 2025-09-10 04:14:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5bbe17d9-0434-3f97-92ec-62ed98201953 | -7.80194 | -46.07299 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7ed4ac5-c909-39a8-b8e1-86b6535ee0aa | -9.13457 | -45.57183 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 698ac758-b3b5-33ab-8b59-b3ad946c398b | -4.94277 | -45.2948 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20990c9f-a32f-3aeb-9e30-7aa726d908b5 | -9.10283 | -46.97045 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 93e45748-1d44-3344-97c5-72fd83bb261f | -6.31292 | -45.66553 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c41ea7ac-70f2-3bf4-855f-110a3205adef | -7.70825 | -45.1522 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ed2a1dc-d967-3b79-b01f-b8231203408e | -9.35824 | -49.00391 | 2025-09-10 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d85d79ef-a625-3441-8029-f1840f080bb7 | -5.84421 | -44.81878 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 456aa00b-71ea-390f-be1c-3b8ac5c067ec | -8.65446 | -45.73878 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ff76c40-c6db-3dbd-a033-a56bf472bb96 | -6.08853 | -43.36391 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 398b7993-72f3-34b3-a076-80eb97023b4c | -8.75147 | -47.09644 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fa0644bb-c102-3722-b105-5568276651ce | -5.65684 | -51.26578 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f4818ca-5ec8-3c4d-ad84-4b29a41e1440 | -5.66204 | -43.91064 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
