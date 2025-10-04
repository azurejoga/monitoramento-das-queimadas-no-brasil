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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c22a029e-f0ce-344e-a30f-bffe5235e5bf | -8.22307 | -46.80563 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f950763-d753-359c-9733-657452487efd | -12.9327 | -46.38649 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35938c67-7ede-3cf8-a44e-f2c375fd24fc | -11.95682 | -47.88566 | 2025-10-04 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd072b0e-85d7-3c2f-85a9-ceda328bf615 | -11.91334 | -46.3932 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e1db25c-921a-3e87-abfa-92d20c88daa2 | -7.85926 | -48.19887 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 21945061-b9d8-3dbd-bad3-84b23ac172da | -11.83008 | -44.9102 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f29c4875-9f70-359c-ad14-bd9fcb3ba9ed | -8.17947 | -44.15419 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28a25152-2d73-34c0-bb45-b583b4285c24 | -12.41281 | -45.15559 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5c4badd-2349-3bce-bc43-c12461288f89 | -13.4899 | -47.26347 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53a39f85-fab3-3c09-bd51-907696d03d31 | -13.68378 | -48.62607 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb4d2fba-624a-37f5-8a2e-d44d42dace62 | -13.34525 | -47.21797 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0f3bba9-b6c9-33ee-9750-a74003b78c4a | -10.29151 | -45.17826 | 2025-10-04 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35b27d54-17d5-3c69-a2a0-94fce79237a6 | -12.87325 | -44.63207 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d365ae67-d6ed-3236-a875-da8ba044da01 | -8.35252 | -46.83959 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f49dde10-39cc-3991-82e6-c20aeb179ded | -9.90067 | -43.73348 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae683365-cfbb-3aa7-b2c1-4824eabf9159 | -12.91382 | -45.08151 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6f758bf-5660-39fc-8040-a58b961b2a07 | -11.84059 | -45.03581 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c5927c8-f57a-321f-a195-1de9ec2892f4 | -14.20228 | -46.06872 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df9b116f-5863-3839-a14d-876e208d5ae6 | -11.87955 | -45.00586 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62775892-df5f-3c37-af13-3c9d0277064e | -13.84719 | -43.96198 | 2025-10-04 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3faa77a6-1700-369e-9709-e04f1a7d75bf | -12.30814 | -45.38042 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ae8c39b-ba4c-39ba-a3fc-b5de11610e7a | -9.34137 | -54.52873 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2989e691-67c3-3328-a987-028355d492c9 | -8.0552 | -44.79875 | 2025-10-04 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7743fb04-7eb3-3f50-8ae1-e83a6771f5b3 | -12.93859 | -46.37212 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf137a43-8c56-3f4c-a924-39109771a90e | -13.11744 | -47.94268 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 24c4b88a-33e0-3053-ac7d-852439d76405 | -8.91538 | -46.60561 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aa771ad-9ab3-3a78-b8a7-babead959524 | -11.84766 | -44.94933 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2181db25-413d-3a63-8720-767ffd70c5d2 | -11.12722 | -55.45431 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f33ae89f-bb7b-32d0-be9e-8ff9d4d15706 | -15.2646 | -44.12287 | 2025-10-04 04:14:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0302b779-d0d5-39a0-a9e9-476a5bd90d8d | -11.48503 | -44.98397 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c2f5f36-8ca2-35de-b210-3286b9cc4821 | -11.81225 | -45.0421 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4cb11a22-2ba0-3fbc-a5c0-dfae8fa61835 | -8.16919 | -43.3637 | 2025-10-04 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d07ef181-9ca1-3f5c-b9db-1c88d11f3c82 | -10.99998 | -46.69015 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f75076bf-0ba2-3c0f-b6bb-fe49bbf8a662 | -13.11455 | -47.93764 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0945d932-0728-3f1e-b8cc-9df8fcb25497 | -11.79954 | -45.01784 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de07783-172a-3867-80a1-5115d938b695 | -11.12788 | -55.45405 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0d98f20-97ad-3c72-8384-708d7b46fb30 | -13.3174 | -47.2545 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1393ed7-b85f-3628-bd1c-3723192b04ef | -12.68584 | -47.5635 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebedbca5-a761-3372-9b11-7c1a3b26b98b | -13.38941 | -47.28009 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18f2ec7f-0d24-34a9-b5a5-1275d23ea9ac | -11.505 | -43.50469 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe6c538-f9b4-358b-b1f8-86fdc64748d0 | -13.05111 | -48.62336 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db45b729-3164-3918-b50c-5a2d9ef23e93 | -11.17196 | -47.75522 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 153146d7-d34b-3a70-9b81-13f1eca2143b | -13.33096 | -47.62997 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 09a35098-9cd9-3e6f-8495-538c1dca79a0 | -11.92467 | -46.36772 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1871776f-1e6c-3515-b9da-320cbe2ff5c8 | -11.07562 | -47.88403 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 828fa700-7a07-3b85-9f39-01d040dfd2c0 | -12.72291 | -48.56578 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0db23b5b-301f-3abd-833d-73bda7fd1f81 | -7.73847 | -46.31227 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ede0a24c-3484-3199-9958-769c93331133 | -7.86606 | -48.20715 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c763ee4-095d-3f69-967f-2d244fae8fe8 | -13.4769 | -47.23322 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21f6c33b-1031-3e46-bd17-1c1ed7a0d02c | -13.99566 | -48.20647 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cb7abe4-13f9-3939-a20f-18de407b79e1 | -8.84283 | -46.84313 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27f73015-c2c5-3467-8354-3a7d78df37ef | -12.38632 | -46.50734 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f898a06a-c335-3dc9-8463-00cbc30048eb | -14.41386 | -46.16893 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de3af9a3-6532-3849-ac18-0efdecccc718 | -14.22002 | -46.08695 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6669e8ef-747b-3512-87d7-dbcaf09b9e91 | -10.57495 | -48.69523 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d09b23e-6967-3c82-8a6d-fda362e17ef1 | -13.2924 | -47.5965 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 41c3af3a-fd24-3491-a4b3-cffb77c1991b | -8.8735 | -47.8172 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c785697f-b880-3a0a-857d-ac84d623a476 | -11.48265 | -43.49759 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c45a8c3-9eee-373b-9b60-a7265ae8bffd | -8.22602 | -46.81052 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cf876ef-a828-340e-8d63-a4e335ff2956 | -10.59707 | -54.35231 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ccba744-5e0f-359c-a48c-caaf66f511df | -12.3886 | -54.45177 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a72405f-211f-303f-a739-0e8892b5b2f6 | -10.0491 | -54.33168 | 2025-10-04 04:14:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cad12abf-b288-3a33-8ae2-255abe2e38a2 | -10.03168 | -44.02238 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf9a05db-912e-3bdb-9914-8595f916b06d | -7.9953 | -47.72813 | 2025-10-04 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f732cf0d-407b-3129-a2f3-1f3576e40870 | -13.7795 | -47.82443 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 601fe4fb-752b-32ea-a393-81d6b2e341c9 | -8.54094 | -47.21272 | 2025-10-04 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b35c9890-f202-35f4-ab72-aa1c1c7c66cd | -14.68414 | -48.068 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a826f32-1b55-3064-8a08-de05b698d436 | -15.31921 | -46.30374 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4527e60a-a63d-3a6c-9678-131ec41a3292 | -8.84995 | -46.8227 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d21a9f3c-290b-3c3d-b698-31ddba241e77 | -9.66222 | -42.93475 | 2025-10-04 04:14:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ead0b632-921a-3143-86fc-d38e6f13ef54 | -10.59402 | -48.72596 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a04f60d6-47e7-3ff3-aa77-fe05d0db2ec9 | -11.09786 | -49.851 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94e5f67-d508-34ba-b1b2-b03d31d0910d | -9.90121 | -43.72999 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b719d9cd-68d0-31ee-89a7-3887032444cd | -11.43327 | -55.04977 | 2025-10-04 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1607985-0952-36d5-a4dd-e2386af45a66 | -15.9109 | -43.34536 | 2025-10-04 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1940972-00e4-3770-922b-5737372c5f19 | -13.33037 | -47.62413 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fa5b2a9-a3d5-33ef-83b0-322dbe850ec5 | -13.14061 | -47.80677 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a70d87cd-bcf7-316f-90e9-76f1db3460f9 | -12.48047 | -54.41605 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f0279f-e06a-3858-ad0a-ce2e88000665 | -13.32528 | -47.61977 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 602f3640-f3f3-3e4e-b855-463bb7cb0212 | -11.86995 | -45.04444 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeb2bc90-1b98-3d8f-afb0-a5ad95e8d67e | -11.92376 | -46.35194 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6904f00-594f-3798-be2c-1e10d2cdc194 | -13.99799 | -48.19107 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| adc605b7-f39f-3836-b5d3-3b12b0885498 | -12.5503 | -41.30339 | 2025-10-04 04:14:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb3f1938-7876-3e0e-b3cb-9d7237624c80 | -8.61719 | -54.97864 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3da6ad42-0057-3ab8-88cb-34e6966e5108 | -9.99904 | -48.27546 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0b27c01-5cd6-3e40-88a3-eaa73abe7785 | -9.38559 | -40.45869 | 2025-10-04 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f669b334-39ff-3f5f-85ed-e24bf5b3f6d7 | -14.92222 | -48.3391 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c84dc66-a2b6-32b7-89a5-ddfc82005bac | -12.91668 | -46.92138 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d72ec210-8ed0-35ad-b83e-063aaf11a333 | -14.65739 | -48.30791 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d0bf02f7-6fef-398b-8e20-382bd95bbde0 | -14.10259 | -44.30704 | 2025-10-04 04:14:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb04c8ec-6f6e-3a2c-96ce-47299f17f7b8 | -12.66346 | -44.24001 | 2025-10-04 04:14:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3518161-f814-3d84-9fd6-a4887b1e08c1 | -11.85665 | -45.04216 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6917acf7-9c25-3fd4-bf40-dd980d3da6a7 | -13.57468 | -48.18513 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f87a63e9-4bcf-33a9-8652-15306afa30b7 | -14.65125 | -48.23568 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed628ee0-9318-3e5d-b67b-8088c6c4b037 | -11.49313 | -46.75424 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 736af03e-f54a-3e0a-bf62-40bccbf6370a | -14.86751 | -48.13104 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d7cf840-831c-38f0-bd6e-c85049f758af | -11.88574 | -44.98845 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6facf7c-3e57-38bb-9946-0eedcb4569a6 | -13.26915 | -46.47399 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 045e3914-8203-3341-8eb3-124cbf897290 | -11.91236 | -46.74165 | 2025-10-04 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40a81ca7-9b7c-3cac-8d10-02311426755f | -14.89866 | -48.38905 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README79.md)
