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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1554bc1a-f094-37bf-aea7-5ff0096f9a49 | -9.0718 | -49.60368 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc5541d3-f7a2-3a15-aebf-2aa0d4b267cd | -12.49842 | -47.23724 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46091c6d-318e-3993-a4d4-a861a61287b5 | -12.24607 | -45.06398 | 2025-08-27 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e4065cc-f7da-3dae-ade1-eeb02990045b | -11.92083 | -46.71391 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f97296b-c8ca-3ca0-8461-d044101060e4 | -7.1699 | -43.84168 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7a338ce-6a3a-3113-9803-2220a65d06b6 | -6.87992 | -44.99859 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fafa6c7b-2915-300c-a1d3-3dfc51f187bd | -9.08243 | -49.60574 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 432aceb9-7323-3fcb-a4c5-90f89d1b10bd | -6.96739 | -44.10488 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bae7af43-5d01-304c-b810-719f200a791e | -7.73827 | -51.1381 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aee0eae-48b3-3d7e-9599-010e5a96a303 | -10.77211 | -46.38153 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd9d10ff-6a01-35f0-ab4b-5ca8540393e3 | -6.62984 | -43.53131 | 2025-08-27 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf215d34-8749-3a7a-983d-0df135e90f96 | -9.08137 | -49.58121 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b026820e-bf5a-3747-8afb-e76f3a7957c7 | -9.60351 | -40.57695 | 2025-08-27 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00106659-029b-3a0f-aa28-b2b3eb3fcc28 | -6.95746 | -44.09365 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bdc10e4d-5ccd-3f0f-bf12-8f104fbff299 | -11.92056 | -47.10946 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a254556-0345-3868-94ad-09aee6c6a1aa | -9.09201 | -49.57301 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05b7ffcc-a33d-3d7e-80c6-afecafb1e6ea | -12.00409 | -50.62245 | 2025-08-27 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b0453a5-a487-37de-8f7d-05a0563bf23d | -7.63862 | -42.6879 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4cb0389-a1e6-3b9e-b118-31c0f1f61e36 | -11.29068 | -44.9285 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 24c58bc3-b0a4-34dd-ad77-9a45cfe0841f | -12.76806 | -48.15988 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a74f318-4d30-335a-ab36-84814024bd25 | -6.49178 | -44.68067 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 433f4c9d-83d3-3ada-81ad-cf56084d318d | -6.3876 | -45.31391 | 2025-08-27 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 737669f2-f5dc-3650-af57-6d7b0afeb139 | -6.49091 | -44.68596 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c4182bf-d44c-38e2-881e-a572889028e3 | -9.08967 | -49.56564 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62246a4b-91dc-3d94-b0f5-d99d5699608e | -10.78509 | -47.06153 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d89c3d6-fb4e-338c-af4b-3470c4aa2746 | -9.09259 | -49.57983 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15a53e6e-a982-36b7-88de-9a522efae076 | -6.38698 | -45.31765 | 2025-08-27 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ac0da46-d7b1-3d66-b942-68904a887eab | -11.24463 | -45.47666 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d6df3d8-f6f1-3d44-9585-5ffbd372f0b9 | -12.67965 | -47.87713 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eb9b296-1ce2-3fe3-a6b2-b415e317bbe8 | -8.46858 | -43.6788 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 255c3d11-8469-39d3-9f2e-2f5dbffee6f6 | -11.81542 | -46.79571 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 599abc7e-4493-325f-9928-1cb3b2965f0a | -9.08608 | -49.57536 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35abd2e0-c5f2-3241-9670-314f48dc88da | -10.76178 | -46.39129 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e87af8e4-834d-343b-8288-a5d23ed9f16d | -10.78714 | -47.07523 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 53b6e336-2307-343a-a6a7-caf8e033e0f1 | -6.82016 | -42.81165 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0559f310-2325-3a19-818f-40c04e1deaf6 | -11.57786 | -44.64807 | 2025-08-27 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0472af6f-98d3-3c7c-9cbd-40b823b0cc5e | -8.32823 | -44.8057 | 2025-08-27 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070a1136-a543-3652-be33-418d3d2034d0 | -13.43486 | -46.99038 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b4f3a9e-28b2-3227-951b-0c09bf433433 | -6.96356 | -44.10421 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e44cbbcb-5ee5-31c5-94a7-8d7814581fad | -8.27398 | -45.12029 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 849fca7b-d2e1-340d-99b2-996cd2d64744 | -13.4251 | -47.02114 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4c1602c-4b1e-3837-9200-17671f3592eb | -8.86628 | -47.17347 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c2807ed-3e94-3c51-add5-891da80a2307 | -12.74194 | -48.19985 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d20f1a75-3579-3a44-849a-dcb832a69ef4 | -13.41941 | -46.86223 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d4e502e-00a5-3682-a79d-1f67da6c0ec7 | -12.89822 | -44.63708 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b2df92aa-9dfa-3284-82a6-be8e7f266926 | -9.9469 | -46.3719 | 2025-08-27 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04b48de9-2905-3e55-a998-3450b5eaabd2 | -7.59479 | -45.22014 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6119cd7c-5a5d-3fad-8c7b-cb8cf46b227d | -7.63797 | -42.69186 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e96f512-a9f5-3480-b7e7-847e47b113a4 | -13.17479 | -45.29047 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 20ee3fad-fcd9-30e9-8ef0-ef00e1cec96b | -11.14901 | -44.78234 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dbffc51-1a17-39f0-b2c0-d37a2395c2d4 | -12.75196 | -48.19645 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6200362-20f7-3515-8543-4d92e26f5533 | -12.75644 | -48.1976 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d15fa06-ed13-347c-a20e-378b678f1bf5 | -11.74719 | -49.08843 | 2025-08-27 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9c93cb5f-8548-3b74-bef2-e44a8aac4432 | -8.08468 | -45.01001 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de7d394a-20a4-349e-a7e4-9d6fd6e174cb | -9.94201 | -46.37497 | 2025-08-27 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26090734-46bb-3012-a01b-a1f3c6de7a35 | -13.07297 | -46.3289 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5314c88-a8e3-3492-9611-57c65d0a1ec5 | -9.57484 | -45.73211 | 2025-08-27 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb628dcc-0f2b-3f1d-b659-6aba4645ad11 | -13.50654 | -46.86379 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16263f12-3a37-3592-86bf-ed756abc592f | -13.17104 | -45.28979 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eec34979-eef1-3b22-aa67-a65c4c9b5c8f | -13.44874 | -46.98447 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fe2b185-10f7-30dd-86d2-f20e496a423a | -8.72501 | -49.73928 | 2025-08-27 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15b627c9-eb18-343a-a92b-0603c2549dce | -10.31913 | -46.79219 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41f00895-3bd1-3f1f-ace6-8da42d9815dc | -10.3127 | -46.80348 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f5e53cb-a2bf-35e8-b025-7bf6e0a9f9f9 | -8.07633 | -44.98719 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4a6164c-9996-39a5-aaf3-245cf1371a47 | -9.95391 | -46.50749 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d36c38e1-db5c-3a63-bfd7-ac3934eecf9e | -12.74373 | -48.19015 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42c0d5e4-fdb3-39a2-9794-1bf03a44e41d | -9.17356 | -40.60112 | 2025-08-27 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 52d4d32f-b7fe-389f-8018-7b75243dcc03 | -7.89288 | -45.87158 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b10f5f3-f865-3c19-ac3e-8aab9da9e192 | -9.10202 | -49.58844 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a77452d-6950-3dea-b6c4-a441045a7d42 | -7.66201 | -42.65551 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 19a4b242-bcd2-3cdb-843d-9ce82701c39a | -13.40307 | -46.88212 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd7807fb-9097-32bf-bbcb-230c737c9608 | -13.04797 | -46.30724 | 2025-08-27 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc6d5c3e-a4eb-3bff-9c1a-3aaae36a1f38 | -12.76458 | -48.17884 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a9ba9e1-0b6f-3733-94a0-cbc42e22ca3c | -8.25703 | -45.12307 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e50892d-4c19-3929-a3b1-bf495e328d0e | -6.80911 | -44.9982 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0868ddf1-7a11-37f1-817a-e593739c27c0 | -12.89385 | -44.64073 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3853ef53-b384-31f2-8474-f6c5dc8e9b45 | -10.31991 | -46.78777 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac538f07-710b-3973-941d-f284603ebc2c | -7.47919 | -46.00901 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58aa4eab-e98b-3d44-ab75-64b33b0fc8e8 | -12.76181 | -48.19397 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b43f9979-df1e-3378-bbba-8d8227f3500a | -10.31102 | -46.81307 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 429fb201-f722-3a2b-8052-5c4ea33ae9c4 | -15.79638 | -41.46961 | 2025-08-27 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db91e1ab-ead7-3a15-adbe-41ddc2d372ed | -15.89925 | -42.66351 | 2025-08-27 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b59e03a3-5bba-3168-bf88-b66a25b71a43 | -13.61883 | -48.14179 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3890739e-4a80-3057-813b-83883b6651dc | -14.12633 | -45.40588 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ad73e64-04ea-3c10-9ca7-e4fa61a17cee | -15.45245 | -47.44019 | 2025-08-27 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efd16755-d889-3367-9840-de5aef1ca090 | -15.09569 | -48.72632 | 2025-08-27 04:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3945d891-013d-3317-b874-dd8d54ae8cad | -14.34314 | -51.92805 | 2025-08-27 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 539a792b-d8b1-3e39-823a-cc86475e944f | -15.76717 | -43.22275 | 2025-08-27 04:06:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4da4ccc-9f04-3aef-8f28-6967215c5f54 | -15.41065 | -46.5952 | 2025-08-27 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee4bcfd2-ef60-3e91-a867-565115a17c1e | -15.03876 | -48.68126 | 2025-08-27 04:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf4f9a7a-6d33-3080-942a-b25b205d36f3 | -14.1226 | -45.40519 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b562ea82-ae99-3375-a11f-e5ad94c29515 | -16.76094 | -43.10945 | 2025-08-27 04:06:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99eb4d3e-67c7-37c2-9bf5-c1ca0d7369cb | -15.11283 | -48.55801 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc644faa-e593-3ff5-92ce-8381a7c8b422 | -14.83384 | -47.15134 | 2025-08-27 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd83e786-3164-3f47-90c5-d560c37d208f | -13.61163 | -48.20548 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1ecffbd-9eeb-3b38-95cb-90b96e8fb987 | -15.10071 | -48.57354 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31a8e406-39d5-32d9-90e5-187ecc757848 | -14.32122 | -53.26802 | 2025-08-27 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21d94b15-4521-3f55-bdfd-6d43ad8b85ce | -15.10629 | -48.61848 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e10917b-f61a-306b-9da9-1c0a13096e0f | -13.62367 | -48.21546 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ee60caf-470e-3b7c-8a5d-268281790ae3 | -15.12636 | -48.6695 | 2025-08-27 04:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
