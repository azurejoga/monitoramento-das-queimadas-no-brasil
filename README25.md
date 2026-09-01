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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f72b86c5-d215-32dd-b6b2-747b64045b14 | -10.05291 | -36.21123 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 95227884-cfb0-3e70-b8a8-1eaf47551dbe | -11.23016 | -51.27719 | 2026-09-01 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9396708f-db30-3285-9208-fe8161d280fc | -9.33658 | -40.49349 | 2026-09-01 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08ec9f82-a9fb-3205-aef6-e970b9fdc5e6 | -11.48892 | -45.10077 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e2d62a3-48a8-3d69-ba30-02271467cdf5 | -11.06412 | -51.52938 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efc22c1f-0532-37b5-94ea-fab1939097e1 | -13.37822 | -41.34712 | 2026-09-01 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43e1696e-33f2-3f3f-ba4e-9cb119f9987b | -11.66864 | -47.61426 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 004d2655-1ac4-3da0-98e1-c42a3e6baf99 | -11.51994 | -46.92794 | 2026-09-01 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a2357f5-2f8a-3113-b348-36627fe40049 | -15.19073 | -46.22678 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94d8d2e6-7dee-3b14-8505-434d40a20377 | -10.86057 | -45.36346 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6341b03b-77a4-33b4-b37e-4821f44405a0 | -11.21824 | -46.09468 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fad9ca1-07f8-3fde-9a57-cc03e47a1a9f | -15.18906 | -46.2319 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b1909bb-0a17-36e5-944e-dd9d0adf0a2f | -12.95834 | -45.96775 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1db0cf60-c90d-39dd-a3ec-80995aeecccf | -7.88417 | -47.08117 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fc21de6-7413-3073-a190-76b52e069d62 | -9.42263 | -45.63688 | 2026-09-01 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6aa7083-6f45-395c-8cd2-7598ae0be3ca | -13.27751 | -48.55578 | 2026-09-01 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 065224c2-4966-381c-95c2-ba7cd7183da4 | -11.27856 | -50.57748 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 5ebfe764-bbfc-370f-adf8-1c82fa12b4b0 | -11.8114 | -46.03733 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3054828-9881-3beb-a5d4-a61b2a6961fd | -11.21624 | -46.0922 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6be6aa74-1228-3fee-bd6f-f6d5939d6a86 | -11.66838 | -47.60155 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03e12ab5-b575-3791-91ef-f40bd034011d | -11.92043 | -45.09324 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7310cfba-5eef-35d4-8a4b-b1cdd6e5a37a | -11.2922 | -50.60917 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfca77d6-cff1-3ec4-8a51-fc43588f0336 | -11.19343 | -45.03854 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04672cdc-b656-3b14-b75b-6c132e273a3b | -11.93856 | -45.07102 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89064050-b7d3-35ae-8510-8a268a8617ca | -11.25747 | -50.58324 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3e9cc08e-af29-3057-a492-0d611237518a | -13.19188 | -44.07231 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd39fa8c-38e8-33bf-9140-de00f2279ecb | -11.9233 | -45.096 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6784453a-f08b-3a88-9292-0b5210a0e8fa | -10.0074 | -46.44509 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fd1af92a-f13e-3fa1-aa59-a4c2169c8237 | -11.92414 | -45.09835 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5bf31c1-8028-3c78-9438-7235de92680b | -7.52151 | -47.33508 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57513dd4-1cb6-3137-a4c6-dac03502bbd6 | -11.24232 | -50.59148 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 546316c2-76e1-3d37-8e14-b5cdfa0b1f29 | -10.7427 | -47.98803 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc4a4433-7794-3e4a-a319-fea57c6ef0a4 | -8.41421 | -44.99791 | 2026-09-01 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9964b9f9-fe20-3d21-9ae8-c4a4fbe854e3 | -7.40792 | -49.73869 | 2026-09-01 03:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24abf367-addc-3943-94e5-7e9ebf1f5993 | -9.45706 | -45.62651 | 2026-09-01 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2fb34f8-4167-3d93-8a6c-b7e13cd5208a | -13.19748 | -44.07668 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef98484f-ac17-3693-82eb-ed98a79f0c15 | -8.76878 | -46.44864 | 2026-09-01 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acabab39-4367-3281-8d6f-7afbd75b5dd9 | -11.66034 | -47.61473 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 055b104c-7386-37dc-bfac-156fba6eee7c | -11.26615 | -50.57362 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9bb1e21b-0e01-3326-a609-d532c87c584c | -11.11199 | -51.53971 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1c2ce9d-f663-3deb-aeb7-772cd352c1cb | -10.19742 | -50.31181 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50814258-2718-3139-87e3-ef85275bbab2 | -9.98757 | -46.43814 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebc2069c-cffe-3538-88c4-71f8b67e530b | -15.18178 | -46.2491 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eafe5f63-4c7d-374f-942e-81df115e627a | -11.31983 | -45.17221 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1388f1b1-d7ae-30ac-ab63-7643f1f7c278 | -10.74827 | -47.98911 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba894a09-69a8-3a93-9f59-bb74b050bdae | -6.71816 | -50.46553 | 2026-09-01 03:55:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fd9262f-0322-3767-af4a-f2a8cc3e8a8e | -15.53932 | -43.18304 | 2026-09-01 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 267a2cae-5f8c-3c64-886a-4b934ef70797 | -10.32145 | -49.95486 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4880f15e-91b7-3b58-bfb7-b7e18e8064b1 | -11.22345 | -51.27571 | 2026-09-01 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3fd272b-2143-3d02-a897-01df0edaf4f0 | -10.95235 | -49.76683 | 2026-09-01 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c57cec-56d4-3636-86ba-83f2cc3a42ba | -11.52386 | -45.49425 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e782e455-41cf-3096-ae0a-86b8ca42d5f8 | -8.76413 | -46.44463 | 2026-09-01 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4f0c792-2feb-3a70-9943-a2268ae435b7 | -10.15784 | -45.76213 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 688146b7-8eeb-3760-907a-c41940212d4b | -10.3512 | -50.00486 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 30bdd6a4-8cba-33f6-ad2d-3e15b3930c46 | -11.20963 | -46.14033 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0de7d12d-de34-3067-ac56-30d17bee2757 | -11.67741 | -47.59785 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8862b4ba-83f4-34b6-aa24-44a69c4c98c6 | -11.20769 | -45.11477 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ffc7e0-fecf-3174-b6c1-cdfbb8929076 | -15.21374 | -46.22731 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ec31826-6623-38aa-85d5-57fd8592c95e | -8.48848 | -44.74327 | 2026-09-01 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a321e571-9dc1-3e5f-bb00-d558218d1a29 | -10.74596 | -47.99147 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb2ce2f8-2945-3a47-b090-aa7ef634bb42 | -11.66772 | -47.60503 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e12825a-3c3f-3a78-9a76-2c66dd99209e | -11.65568 | -47.61005 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb8fd80e-388b-3285-8086-ece37c144083 | -8.49141 | -44.7541 | 2026-09-01 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e681d86e-3b33-3ac7-ad98-0e7be0df65f2 | -11.79316 | -47.67401 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f240adc-9c61-3dec-9a48-a791441d349f | -13.19942 | -44.07791 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6cf57fe8-d23d-3d77-abc1-a9bfddffb7ff | -11.32069 | -45.1675 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab2c6815-88c2-3050-a565-9ce9e24be844 | -10.45103 | -46.74039 | 2026-09-01 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb4c5d46-a657-3c50-9ded-f753e3d62eeb | -11.28528 | -50.61241 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b20fba8a-3538-3e31-9a70-95fd4e2d198a | -11.20852 | -46.07916 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d1aa8e6-d2f9-3e88-a8e3-2c6d76947917 | -12.95368 | -45.96672 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 78f52c26-8209-34e2-8963-adbd699ed068 | -7.88364 | -47.0803 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 397b3895-7f88-36e4-88a0-fcfa72184452 | -8.49228 | -44.74911 | 2026-09-01 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89970312-bfc3-39c4-9d9d-5fb66708e489 | -11.90856 | -45.0744 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a423f005-b679-3572-8bfc-c59f2bd933da | -10.16273 | -45.76292 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 88efedda-ffc7-3c2d-9163-3bf30a9a6baa | -11.19602 | -46.13192 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b951f31c-ab50-3327-aedb-b98a3ac859c7 | -12.89688 | -45.83052 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be1468ac-aab9-341d-b4ca-fbf54a4a44bb | -13.34643 | -43.67099 | 2026-09-01 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 454bd9d2-136a-310a-97d5-1b2818bc8dcd | -10.85191 | -45.30514 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b265b050-3705-3fef-a0a8-e033c08b82dd | -10.39823 | -48.23374 | 2026-09-01 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d32518c2-e7c8-3153-a9e4-17cdc5c40e53 | -12.1046 | -45.01201 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb0c031f-dd2c-32c1-aaa1-6ea960b8fc65 | -8.94479 | -38.00377 | 2026-09-01 03:55:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 288a3894-9bc0-3ad2-9c81-c185c77c8db3 | -12.06671 | -44.99197 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe0ce0e7-7a62-3d55-887e-33f6e7e91e64 | -10.19661 | -50.3143 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 495f7687-c9ab-3411-8420-0f00937d1f8c | -15.20559 | -46.22029 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 655f04a8-1aa6-3b23-a568-4ee9df6d241a | -11.27904 | -50.57644 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5b83f98c-ce61-340d-871b-da6ed7579a16 | -11.68198 | -47.15768 | 2026-09-01 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdee9e3e-c0ef-3d69-9ca1-fdc1260713ce | -11.27627 | -50.58848 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1d8e6659-d312-3466-86ed-6bda2bb41e4b | -8.86249 | -38.6449 | 2026-09-01 03:55:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1420fb4-4147-3cd9-a441-205c4c63f1fe | -10.82834 | -50.71525 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be454784-b1c2-38a3-a2d9-561b5b0aaf11 | -10.72531 | -47.95788 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 799b39d8-276c-302a-9d75-b7ef0ab70f3a | -15.18439 | -46.23522 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dabd85e3-44aa-3016-a80e-1f1b47ab9579 | -11.93614 | -45.10232 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f23f7b3e-61fe-380f-8563-a54c82634a97 | -10.75302 | -47.98491 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cdaa5ff-270f-37d9-9d1b-b2d79a48c5e4 | -10.83603 | -50.71093 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8c518a2-3718-3789-94cb-e6108242c3b4 | -10.81964 | -42.36633 | 2026-09-01 03:55:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 68d62c95-6321-39c5-abab-eafe24e57a9f | -10.74959 | -47.98205 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92d344c2-8db3-3a4f-b0f7-856d779c680a | -11.31402 | -45.20407 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eb55da55-8572-3457-a696-a0b5eb05db25 | -10.35268 | -50.00639 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f8dbdc40-fdf9-3859-a76c-6ab503b2cac2 | -11.05729 | -51.52788 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63ed9232-a0e5-3c05-981b-1579d05789ff | -11.66706 | -47.60856 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README26.md)
