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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a61ffa-013c-35c7-be09-28dafcf3924e | -11.06392 | -48.27912 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00d987f5-5148-34e8-9339-b14589d90b8e | -9.71839 | -54.81334 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ee674c47-aad6-3ff6-9141-7ea0b02711d4 | -8.49818 | -57.63197 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b572b79-3ada-3d43-9126-8e64fe2cc32d | -9.7091 | -54.82522 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7d12e4b-4ebb-3aa4-a96a-1bb4b617244e | -10.62556 | -46.06673 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 000e6f23-901f-3957-af3d-2591a82d82b6 | -10.02354 | -51.10666 | 2026-09-18 05:18:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203aad28-07c6-3f1c-8552-e3dd42e412cf | -8.4832 | -46.87786 | 2026-09-18 05:18:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6a8539f-8706-32a4-bdaf-33acfef52448 | -8.15666 | -54.81767 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44174be4-22a2-3767-8424-52edccd404d2 | -11.07194 | -48.30131 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28a21511-0eee-3c55-843f-c30d25ec72bb | -12.27309 | -50.78498 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a120ffde-87b5-3894-b3e4-c3d5a7e4b74c | -9.76749 | -46.59645 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 544ab540-ac9a-3f7c-9594-179796709cbe | -10.64145 | -50.24124 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a7759e36-95f1-3597-b916-43be7ef05412 | -8.93041 | -51.46429 | 2026-09-18 05:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e93a1d38-3e7a-3a8f-84e3-e0ff81605819 | -8.67687 | -45.31277 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86386464-9007-350c-a05c-470a9687031e | -11.88298 | -47.57835 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09cd52b8-15dc-3938-9b97-faae6139f821 | -9.9524 | -46.60577 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c032eb2-1313-3b27-9224-17503ae678d4 | -9.94112 | -53.98735 | 2026-09-18 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9d62568-e643-3b61-a6bd-eeed7bf9a5a2 | -9.70974 | -54.82093 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a50339f5-2c3f-3c6b-a457-3617213872c3 | -11.88174 | -47.57975 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c76888e-e73b-3361-8f08-4bbba9f7ba2f | -10.86553 | -53.99039 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10795c60-8fb9-3408-b73c-00965f6c9888 | -10.79898 | -46.65388 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac06a849-88e5-3510-8f33-8053b93bdc21 | -10.6515 | -50.24259 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 4f6b6f6a-1660-31a2-8e14-57aa02065451 | -12.31052 | -47.96454 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 294e5254-da78-3817-af52-5ab1593ccec7 | -12.25617 | -50.75254 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8da54a19-3d49-3a6a-895e-991320d8a5f8 | -9.93985 | -46.60358 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 364bdb82-1b89-31fe-95d9-659165ddfc9c | -8.6729 | -45.31275 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bd17b81-eba7-3402-a3d3-3897d71feec1 | -8.51507 | -48.49846 | 2026-09-18 05:18:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8938aec4-80c4-3f04-a4f6-c3359204c6c3 | -12.44368 | -54.99491 | 2026-09-18 05:18:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdf471df-34c4-3c57-8e7f-0dfc88677ade | -9.91169 | -46.54623 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18953a4d-02bf-301d-95c1-839f523a6110 | -9.70674 | -54.81589 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a7b84fd-94af-3f81-9be2-1f14e9748221 | -10.11543 | -46.30045 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb50b7b0-8569-3b2b-bbde-f1f85353bf2a | -10.40454 | -48.68237 | 2026-09-18 05:18:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ed4cee3-280c-3cd6-a5b8-743390bb2436 | -13.6197 | -48.3132 | 2026-09-18 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce9e9270-c3a3-3ca7-a29a-17d18496c14d | -10.66424 | -50.26215 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 348f376d-ae80-37ef-88ca-e9365f81f0bc | -9.09109 | -45.7254 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d05b731-6f1f-3bac-a6d4-8ed96ff43bd5 | -8.91182 | -62.39946 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f66e36d4-52a9-3fef-82ca-06fd4ddc4781 | -11.55808 | -46.89239 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e2981b9-2c86-33c4-855a-0343ddcdbf7e | -11.31248 | -46.7765 | 2026-09-18 05:18:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 431457ac-cc7c-3f4e-a3e2-dfdbfedc1762 | -8.56329 | -64.05147 | 2026-09-18 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f2e3a3e-4ae0-363b-b5bf-e34fa936dc1d | -9.73449 | -46.12407 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdd99b09-8df2-3420-8883-84cc0ebd2f2c | -9.6893 | -54.33322 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b1ee9e-232a-3636-9d4d-4283fb4da29a | -9.94067 | -45.32337 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7c8efe0-80ef-38ea-9f09-8d6f9ed35849 | -8.67361 | -45.3069 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 087f3893-df44-367c-9db5-e0038df1cd08 | -12.43422 | -50.67954 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1dce325-4dc2-341b-b0f3-fb2af2ea856c | -11.06921 | -48.27719 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b32a73c8-5ee8-3d3d-b113-144f46210203 | -10.6573 | -50.23742 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51bc57e4-1d18-3d9e-9d3e-1539695723a6 | -10.66887 | -50.26572 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 87f8475e-28b2-32e5-901d-128063e7dbda | -10.405 | -48.67874 | 2026-09-18 05:18:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867afa75-b6f4-377e-a2d2-4b908ecc755a | -8.94603 | -51.4642 | 2026-09-18 05:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab093722-219a-30a4-bd24-9a23705286e2 | -9.75105 | -46.57447 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6cf2d6c-cfbd-32db-ad6b-fdd30b7656ae | -9.74349 | -46.10516 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4a49144-969c-31b8-85d3-60d357d32514 | -10.65829 | -50.46884 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31ab1924-dc08-3477-a957-6eb7926eebb8 | -10.80975 | -50.19778 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cbce4f1-9539-36f4-8bb3-762ab0512f19 | -12.43497 | -50.67373 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 336adebc-d76d-3d2d-9ac8-52faa1cfc160 | -12.28737 | -50.75211 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaee0b7c-1dc0-323d-9a84-04fe55ad009b | -10.41101 | -48.67588 | 2026-09-18 05:18:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 817da700-fa77-3475-9e17-3eed595910a3 | -7.83214 | -55.4138 | 2026-09-18 05:18:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82bb2db0-c112-3d80-9e48-8ea12a0907bb | -10.66891 | -50.46456 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3554ece6-8892-3c10-8847-10b7427a8796 | -10.99986 | -57.06416 | 2026-09-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80ef37ab-fc36-3e1f-b6f4-24ffa22c098d | -10.66 | -50.25563 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d55e2f0a-e4da-3324-b9b6-7b53f338ab16 | -10.91863 | -53.98274 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae530cd-ee9d-38cc-9e05-2439b6ade8d3 | -10.51895 | -46.74314 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b1d3a06-6b14-3db8-b0d7-4c661be05c9f | -9.84176 | -48.39822 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beb59cf4-93b0-35eb-8a46-78c8468ca899 | -7.57464 | -57.69551 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0532fe26-7f69-3da4-a393-70b7cdfd47b3 | -9.9119 | -46.56992 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a8c6b0e-2c23-3833-8948-e5e1fc3ff89b | -10.66463 | -50.25923 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff6c01c7-1169-38d1-8f02-9a1f6602b406 | -13.74333 | -48.8077 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e00519a-0c8d-3bdf-a5e1-65fadcbe637e | -10.01629 | -45.50625 | 2026-09-18 05:18:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0d385c7-2553-3f5b-9632-d54d6e251bc6 | -13.42534 | -51.90053 | 2026-09-18 05:18:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d8b060a-1fc5-304b-a908-d7655f2687ce | -10.64724 | -50.23608 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 41304e15-cb23-3484-a30f-f6fb37982fd3 | -12.31704 | -47.96068 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be223742-b911-3606-aa01-34c721c930dc | -8.51007 | -48.49411 | 2026-09-18 05:18:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 839f599d-e60f-3720-96b6-0149bc4575a0 | -10.65922 | -50.26147 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7aef001c-0424-38de-8588-c34717da46fa | -12.39683 | -48.47549 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e36383a-07cf-307d-8b5a-084fd369d19b | -8.88511 | -45.89427 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc2c64b7-61e2-3edb-af39-b19110970aff | -12.39634 | -48.47945 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8054068-86d6-3296-a8aa-a9479066a106 | -11.55414 | -46.89862 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73128cf0-817f-32a3-804d-222a7930a866 | -11.87689 | -47.57762 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 84d0e561-b383-3a13-8630-799211a8ca33 | -12.45711 | -50.69978 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bed6e7c-3556-3680-a22d-389c7a0ad7dc | -11.07349 | -48.29669 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 194b1255-8000-3d77-b86a-525f41d67d46 | -12.16873 | -46.98 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5b335d3-e8c7-3b64-8e04-9c5fd7b387b3 | -9.70965 | -47.0974 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9294ae0-5ca5-378f-9df7-a0f3be397370 | -6.92048 | -63.02823 | 2026-09-18 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3817657-394c-347d-b1ba-b6a2f7544d07 | -9.53942 | -55.11102 | 2026-09-18 05:18:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6d9a9c-5321-3eec-b26b-6efb3e6e57f8 | -11.06292 | -48.28054 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2198a501-eb2a-381b-91ac-233bd457fd80 | -8.48808 | -46.88754 | 2026-09-18 05:18:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ea4f09a-c7a4-3fc3-9479-cf83168ba892 | -10.64183 | -50.23832 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5db30935-dbb2-3a40-8b42-1c35bb559947 | -9.91046 | -46.55584 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9568e22-a72a-363f-bde7-a3d447275a07 | -12.62565 | -50.89307 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2794c067-0f10-342b-ba53-b9cb39123795 | -11.55469 | -46.89411 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11c5f4ae-b434-3d70-9f5f-818f002142ce | -12.55902 | -50.7369 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b531c31-87c2-3304-b2e9-95cae4092d36 | -12.55206 | -50.71241 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a183506-2c86-34db-92f7-6b92a9c701e3 | -13.24408 | -46.90805 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d16fc657-f841-3130-866d-1a88899bf2a9 | -10.89294 | -53.99439 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edd2385b-bbc2-337c-80e9-1b0c0079548b | -12.42997 | -50.67307 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9833bd8-542b-3c68-957f-d3175522f326 | -8.11695 | -54.81168 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 480a9612-cb2b-3f6f-9a24-3190e8078d43 | -9.91106 | -46.55112 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc0618a4-0cb3-35a8-ad89-fd11e8f75545 | -14.1707 | -47.863 | 2026-09-18 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9d18551-141a-362a-b549-9fde61e8e673 | -7.8795 | -54.71972 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d7bdc06-9d02-32a5-a891-1c7f4ae13301 | -9.946 | -45.33615 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README84.md)
