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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d01a75-8a42-3681-a515-b42a0babcab9 | -12.59887 | -42.74173 | 2026-09-21 16:01:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 23c1c7fb-a71d-34a9-962e-538dcfee5521 | -11.82657 | -46.81939 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 090b89de-6486-308d-b533-3ffd7773215b | -9.03567 | -49.83156 | 2026-09-21 16:01:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 5d3ccef5-36c9-3298-ae2e-588f055231c4 | -10.25558 | -45.49659 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a61e312f-0f2c-31fc-91c3-b7f22cddca4a | -11.66408 | -47.77409 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b824526a-a98d-3540-8948-a1eba8251325 | -11.15757 | -42.82831 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| bff0077b-1779-36b1-aa01-0a78cd2e7a64 | -11.81869 | -50.02999 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 6a410773-7d8b-3349-b9e7-4439bb0c2a29 | -9.2806 | -48.22739 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0fb29e35-55ef-3e9f-995d-ccb42bbef643 | -12.10762 | -47.04774 | 2026-09-21 16:01:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 88527b01-bc7e-3355-b457-269c2379aa13 | -10.76076 | -46.34499 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77aaf717-3e4b-360d-befd-1eb804d4eeb2 | -14.10017 | -44.83844 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 985d6143-aff6-3f0a-a41c-5dbecde002a8 | -11.80524 | -49.84149 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3bfbbe8f-8add-3f38-87b6-b1ae08f7cc2a | -11.05047 | -46.57919 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2ced97d3-00ac-311d-9cb1-49f945568ae3 | -10.01334 | -45.20509 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ef9126cc-f627-31ce-bf9a-e3a6f1e14651 | -9.89015 | -48.43613 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 9d2aba0d-587b-3c24-a1f9-c916e20d0ba3 | -11.4693 | -47.6358 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ddba65cb-c10e-3d7a-9600-36412fbb0444 | -9.87356 | -48.40141 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e7f4426c-3545-363d-ad5c-bbb031a90255 | -14.21546 | -42.18736 | 2026-09-21 16:01:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4f1761c9-93ca-3dc9-a0c9-37d06959f1b5 | -12.06161 | -50.07485 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| a0fdcc06-0984-3254-9035-18408ac0963d | -10.73049 | -50.78337 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.6 |
| e997bd0e-2050-3704-a1cb-562c24170b27 | -11.4364 | -45.35186 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f10a8a65-1023-3326-afbc-c80206ed7447 | -10.12912 | -45.93484 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e651ee93-1a8e-3604-9035-45123fa4b678 | -9.39038 | -48.326 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| cd7ea0b5-461a-3029-be1f-0b7608b53687 | -11.4827 | -47.64794 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| c6615635-6bca-3e71-97ea-4bd48220b1f1 | -11.65914 | -47.7832 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3cbf32b5-d51e-3382-af82-8692447f556d | -11.78423 | -46.83275 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3a73f95-69e6-3af7-b90d-60152911ec72 | -12.06687 | -50.06369 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 516f9f7a-a83c-3f18-afbf-c488ca716fcf | -10.13388 | -45.93099 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 43d4a24a-f608-3c84-bd41-e40565f55ef4 | -12.39265 | -47.00425 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ea7a476a-3b33-3751-98d9-be22cbff2629 | -9.40834 | -48.3235 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cc85a702-2b26-3d43-ad67-514599c550f6 | -11.90903 | -50.08566 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| d3d07db8-53b1-330e-af26-77d97710f5f8 | -9.16136 | -50.00691 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 04d4f5f2-b08c-36f5-a2b0-ad93f48defd5 | -11.15254 | -42.82505 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |
| af93429a-a443-3576-a3cf-3e89bbbbbc5c | -10.03574 | -45.53361 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f27d0e73-3391-3a7b-8643-b0b123d2b427 | -12.55371 | -47.57023 | 2026-09-21 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6476f183-74ef-3926-a800-3dd6b2d20693 | -12.04765 | -50.07856 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 08c40ece-289c-3e8c-a8f3-c9d6f5257a2e | -8.76057 | -45.85741 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 751215dd-c03a-3745-bbe0-39bc9846ab07 | -8.75952 | -44.28204 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7b08fc5c-832d-3d86-bbbf-4bc34d3caa94 | -9.5426 | -46.52893 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e87fb80-7794-3e1f-b46e-e412177459cd | -8.72919 | -44.88274 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b13cc5ca-4002-31f1-a609-941c35fc7d4d | -11.67089 | -43.43476 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0004994e-337d-3e48-89ca-417f3ce3a939 | -11.65367 | -47.78797 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a879deb3-27b5-395a-bb4f-f4f80e57351b | -9.61542 | -43.93293 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 41fcafa4-c94f-332b-8430-b860a5b60cbe | -11.42926 | -45.37685 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3d41c3d8-9290-3417-8ed9-4995adbca0b5 | -11.64225 | -47.79371 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9c2c4aef-ab7d-33e6-b3af-2681f163008b | -11.38096 | -44.23576 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2ed87df6-1329-37b7-955e-8f37f9bb8525 | -10.11514 | -45.55557 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2dc8778-cf4d-38ff-b49c-50fb0c035d96 | -9.39092 | -48.3305 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c1dac054-b48f-3583-bb71-0648c51f61e2 | -7.13493 | -35.10517 | 2026-09-21 16:01:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e8d5b831-d888-3193-ab51-1adbf46cfb0d | -12.40989 | -47.0512 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 06afc506-a0a4-3ff4-8c86-791254b4a605 | -8.58436 | -44.54776 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d7131ca2-5cb7-3b0c-8348-bd8f27c3c2b8 | -10.873 | -50.1663 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 25318db2-03af-32a0-919e-1ce08dd99035 | -12.39554 | -47.02851 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 92e26286-9d09-3323-924d-b271906098e0 | -9.38303 | -46.41209 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 559ac351-c64d-3549-9534-04d88593bae2 | -10.73909 | -50.79644 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| b4bfa0a1-0c5d-33b4-bfef-f8a2c329ed74 | -10.86202 | -48.06773 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 11483ea2-3866-3346-9903-806e1992de29 | -12.44625 | -47.0497 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b8f5364-4251-3883-8358-bc60a3830eed | -9.6218 | -45.80829 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 400b1e3b-4257-3708-a30b-6bb3158244cc | -10.56204 | -46.54611 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d252a98d-1c23-38d1-a654-b17f9970483b | -11.67383 | -43.44754 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| c13a1980-13b9-3f15-a0d2-5b9a9dd9f5e2 | -11.65313 | -47.78355 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c99ff95b-fb57-3c81-ad91-a324535bf3ef | -9.53595 | -47.96378 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 50526df6-df95-3672-b206-833342a622a2 | -10.83439 | -50.14626 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 89384822-566d-3dbf-9820-819e6ff7054b | -8.80424 | -48.74432 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 62a0195e-c8c8-3cdb-88a9-77b49b186602 | -5.03409 | -43.0403 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d65eb646-56d3-392a-af6e-c92671424476 | -3.38345 | -50.40657 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| e8ad84eb-0981-3f22-bb9b-24ee639c8365 | -8.43959 | -45.82177 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1482a226-c294-3ad0-87cc-9ba94b2ed6ce | -3.88074 | -38.43899 | 2026-09-21 16:03:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8fea8761-2258-3f88-9db9-2e98cefb7b37 | -3.24684 | -42.80215 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5426218-61b7-3daa-98c4-1385417c0f2d | -6.56614 | -45.54171 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9130d8f0-78eb-3c44-9770-7508fa1722e3 | -7.41147 | -44.80378 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a242646d-cb14-3751-971c-7d315c38e009 | -3.90143 | -51.89143 | 2026-09-21 16:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9dedd8b2-7218-3008-bbfe-38490438ca71 | -8.31357 | -45.98674 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 40a309ab-7a72-3bb8-a3f1-6b50123d9bad | -7.40163 | -44.80049 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| e5d053c7-db71-39d7-b76c-40817bdaee43 | -8.32097 | -46.00333 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 49d11569-3f17-3246-99f8-611528a08378 | -5.66341 | -45.4924 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5ff1c42f-4275-3b1a-aca1-08b40aa80522 | -8.60284 | -47.30577 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1175e5b4-5213-392b-8915-23729436f212 | -6.0515 | -45.32569 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a47f02d-41b9-3782-a4db-dc083d751b42 | -3.64151 | -40.5814 | 2026-09-21 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d4153edd-1d7a-378d-9258-7b0cef2ff7bd | -8.49717 | -47.0232 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c5fe058e-347d-31cf-9159-3d51a077f6de | -3.28339 | -40.64714 | 2026-09-21 16:03:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| ecc74998-50ba-3065-adfa-c2f731100319 | -5.13355 | -49.93979 | 2026-09-21 16:03:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 4733b8e9-1d99-31cb-8990-87ac24302aec | -3.81926 | -41.86023 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 49001dd9-ef00-3582-8d65-3925e2f90c8b | -3.58041 | -40.31432 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bb9d1d53-3595-366f-983c-a43a7262905e | -6.71334 | -43.20643 | 2026-09-21 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 44470e54-51f9-379d-9986-3fe4660707fe | -7.56024 | -45.37328 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f278144b-735f-3894-8535-e6d4f1e369d1 | -2.26083 | -48.75723 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 54f82c0d-91e0-36fa-8a8e-496e4884abdf | -7.43477 | -44.76796 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 29475b10-cce0-3e31-b08c-5280bbdf708c | -5.98954 | -45.24853 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e45b823-a1e0-3611-8240-e4b22fd9d294 | -6.63017 | -38.63569 | 2026-09-21 16:03:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 04b0c2e3-e756-3929-a592-a4c5be63cbb1 | -6.61076 | -45.9225 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f17440e8-f6a0-30b0-a030-236db56ffbe7 | -8.72374 | -49.55631 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 67685827-183c-335f-abd6-c0ed00b37004 | -6.55993 | -45.53236 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2e17dcf9-eaaa-3ee4-97ea-c02774ae88e6 | -7.37785 | -44.63151 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6e82c3fe-5ee5-3fcc-9240-ffd18f86556c | -4.39665 | -41.68592 | 2026-09-21 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 325875ad-6538-368a-bb6f-eed8c0a6f557 | -3.39414 | -50.43681 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 66e771c6-ca90-314d-a1fb-74e4c789b06b | -5.46029 | -45.61223 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 669d8697-df8b-3b52-9aee-8c563468bef0 | -6.88961 | -42.92543 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e842ed9f-56ca-36d1-99fc-19ff440065d3 | -3.70758 | -38.70868 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 83c729ce-eb2a-329b-b827-60992db7266f | -7.54712 | -47.32453 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |


[Clique aqui para ver as próximas entradas](README162.md)
