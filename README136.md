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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 991a4220-a9da-322b-a8b5-8b82f0974a13 | -12.283 | -50.7011 | 2026-09-22 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 67977a4a-a85a-3b81-aa62-c18c2415a38d | -7.1555 | -47.4751 | 2026-09-22 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e8cc5c79-1f77-372b-a1b9-5f7f611bd924 | -6.1838 | -47.5258 | 2026-09-22 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e8322ca9-88c0-32e7-a805-81dbd51bad3e | -8.7706 | -45.8567 | 2026-09-22 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 17f3be57-44c4-3bb5-b4c8-1980983a4680 | -11.4209 | -47.3603 | 2026-09-22 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 10815779-07bf-3f9a-aab7-458097cf99f8 | -7.4765 | -45.4872 | 2026-09-22 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 1a727ff0-2533-3820-9111-146de2d6dc5f | -10.2793 | -50.2177 | 2026-09-22 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 2e0c6b4d-4d5e-3b43-b402-095615558af4 | -2.9709 | -57.7197 | 2026-09-22 14:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 722ac8cf-a03c-3a0f-a16a-03777dfcb8be | -8.4797 | -57.6282 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2b01a972-1a0c-3794-a332-5bbc45cd2725 | -6.3842 | -55.265 | 2026-09-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| aade28f4-f0be-3b4b-a18d-a5566e25b344 | 4.0579 | -61.4095 | 2026-09-22 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 4381a2b5-97b1-357e-b026-427899c40ddc | -12.8 | -44.2073 | 2026-09-22 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 21c87280-bc56-3a06-af12-162cee405575 | -6.8383 | -45.5205 | 2026-09-22 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5bafac94-d749-34f4-87f5-dba53ab4ffa9 | -11.156 | -51.1051 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 3cc3d862-bcc8-35d8-b686-d9792391d396 | -12.6796 | -50.974 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 82b8a423-1dd2-3724-a8e6-4329a48edf68 | -6.0993 | -59.9076 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 33df8616-b554-38eb-8484-9a42fd5dc15d | -11.44 | -47.3579 | 2026-09-22 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5ff4bcd7-5e9f-3a0b-bf15-ceee73b55be7 | 3.7681 | -60.468 | 2026-09-22 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0b1a2a33-8c0c-3a08-a832-c97020bd561d | -5.5717 | -42.7414 | 2026-09-22 14:20:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 08711f3c-d90d-366a-b659-7f0645825137 | -8.6508 | -62.4776 | 2026-09-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d11c25ff-20b8-30aa-a93e-f1cfad1e09df | -11.8559 | -49.979 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 2b8ba7d2-44e0-3fa0-a192-0a000161e81c | 3.5482 | -60.6623 | 2026-09-22 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1a6d4782-0a6a-30fe-9f93-f4fb04ac4531 | -11.7079 | -50.9811 | 2026-09-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 35ffef5d-4a7c-3209-a713-654be6cfc37a | -10.8851 | -50.1539 | 2026-09-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 476e927a-cd23-3e04-bae4-f52cd8f997b8 | -11.155 | -42.7885 | 2026-09-22 14:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 230.6 |
| cfff9a9e-b8a6-30f6-8d72-95f8f5a75702 | -2.8608 | -57.8188 | 2026-09-22 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9fe8c2e3-0278-3318-827a-23cb61128689 | -6.9871 | -47.4885 | 2026-09-22 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| fcc6ecb3-1251-3a99-9277-6fe5df651c2d | -6.4671 | -59.9711 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 87dcda88-86bf-3f38-bcfc-a942e105624c | -13.2791 | -51.7737 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 9cac7a15-5124-3aa4-878b-7c11856013a9 | -4.6587 | -42.0964 | 2026-09-22 14:20:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 79d76af1-7f6b-3987-be85-a96891aefe0f | -8.6173 | -54.5924 | 2026-09-22 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e9d20b0a-9bc3-36b7-9459-b06aee310f72 | -11.3229 | -51.3626 | 2026-09-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| fdda7a46-40c7-3d40-938c-588d12ac59d9 | -3.3309 | -59.8673 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9525379d-9ec2-32d4-98fd-7a339b0b9319 | -11.3226 | -51.3838 | 2026-09-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 69ac070f-3a09-318f-a7d1-50c6da4fad90 | -7.4311 | -49.8516 | 2026-09-22 14:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5457f447-62ba-3597-afdb-c80b38253c6b | -6.3135 | -57.7342 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0041fb86-2100-321c-83fb-30fc612395ae | -13.8952 | -45.4913 | 2026-09-22 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 280de35f-3666-3638-b191-d0c41268cb5b | -10.4536 | -51.325 | 2026-09-22 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 13736f0f-7b1c-38a9-a727-009d644aaa6d | -8.7916 | -44.2778 | 2026-09-22 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 453659d6-4583-3474-bb8b-05b9da7e3fba | -12.3293 | -50.1802 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 06df9675-4443-33b8-8ff4-42ca37c25c32 | -7.1745 | -47.4517 | 2026-09-22 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| df6b78c3-09e7-3cd3-94cf-c76ba01a93a3 | -4.2042 | -56.3215 | 2026-09-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| cae52754-46a3-3ca7-b75c-47ad8450d2bd | 3.7498 | -60.4684 | 2026-09-22 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 55b8c92f-6ec9-3b5b-b395-7fde9058332d | -3.7856 | -60.7335 | 2026-09-22 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 6dbc2edd-85d8-3ef3-9ec6-f5924d42d61a | -12.3297 | -50.1586 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| c5162100-bfc7-3146-9721-922942aa22ad | -12.1027 | -50.0355 | 2026-09-22 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ba348089-5e38-317e-adfd-a9719d9914a4 | -11.137 | -51.1071 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 4ebafb9e-4c85-3067-81d9-c4aa3b155f6a | -6.2396 | -41.6634 | 2026-09-22 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 19ee218e-5141-381c-8ae7-fb378b1eba8c | -9.9058 | -48.4867 | 2026-09-22 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 076ab4c0-0286-3faf-835c-4f9f7c127d4e | -13.0301 | -50.5874 | 2026-09-22 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b18fafce-b003-3d5d-a8d3-13d2899ffa5a | -10.8909 | -54.0882 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c5263b0c-bb22-395d-9012-5337823b543a | -3.7547 | -58.8622 | 2026-09-22 14:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3beb936d-5307-3803-a155-24f86615d0d8 | -10.5908 | -53.9713 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c2dcdd8c-42e6-32c8-876e-5568d76efe3b | -6.5829 | -58.9851 | 2026-09-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b3ab7a9a-16a6-39cf-b594-e5641d27ec35 | -5.9333 | -59.9899 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| bf316232-28a3-30c1-bfb2-56563b86db45 | -11.175 | -51.1031 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 29494e93-275e-3297-92d2-9ef5298c697b | -3.3493 | -59.8479 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1a9b9ccc-3e98-3212-93e1-0d916ea2eef1 | -3.3867 | -59.5223 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 8bc032fc-f704-3982-a432-190a4e37fa53 | -13.2787 | -51.795 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 5cc3a8a8-fa2c-3d8f-a9de-f89d67655083 | -12.2834 | -50.6797 | 2026-09-22 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| a8eb45bc-c8b5-3bc5-a746-3ccea9440fd2 | -6.3382 | -59.9566 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b4b35ddc-b417-3b60-8683-a7a796925322 | -3.405 | -59.522 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 9c8524ad-2479-3ab8-8834-153f60a27e5e | -12.0839 | -50.0162 | 2026-09-22 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1de489ee-5c56-3a46-9c46-145f2f2d2daf | -12.2827 | -50.7226 | 2026-09-22 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 217a46af-220d-375f-b447-56a77ac8a5ab | -9.257 | -46.1873 | 2026-09-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 0ebce74f-c09c-39d4-8d84-3d274ae573d9 | -8.0466 | -61.3237 | 2026-09-22 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bec64673-60fa-3bb1-a4bd-a4dcb483e145 | -3.2396 | -53.9417 | 2026-09-22 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| fe0f1112-c9f6-3009-afc7-7ac0cd7d206a | -6.4301 | -59.9916 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4c1731bd-31aa-3249-872e-7b122b2248d0 | -11.269 | -54.0334 | 2026-09-22 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4b643c06-d3ef-3aff-979d-b88c83f2a6b1 | -3.2818 | -57.8491 | 2026-09-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| b5b30723-297c-3e7b-b491-d7b40a1fa308 | -2.8608 | -57.7994 | 2026-09-22 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 5fc692e2-d85a-32cd-b25d-40efc2b2dcf7 | -11.4527 | -50.2409 | 2026-09-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 5aca03d6-c7c4-3220-9158-807496e4931c | -6.3436 | -55.8243 | 2026-09-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a45b253a-00dc-3c58-aace-c6d51ad5c5c0 | -9.6108 | -43.9477 | 2026-09-22 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| ec6cdef6-a82a-35fe-8bf2-8c1fbcf16c33 | -12.3676 | -50.1755 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0ba7a884-9ce5-363d-9cb2-5b02d4067f4f | -10.0295 | -52.0991 | 2026-09-22 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| c3f95cc3-7f31-3e4e-be53-28b7c0f2cb98 | -7.5548 | -48.6843 | 2026-09-22 14:20:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5eddd9f4-f047-304f-a514-7443bf59aa27 | -2.8716 | -60.9203 | 2026-09-22 14:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c6a170d1-c6f7-3d9b-bd71-a857f4cbc8fd | -11.4404 | -47.3355 | 2026-09-22 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8ee23d01-7f21-30a6-a17a-0f743a75662d | -10.6875 | -50.7722 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 88717421-e365-31f6-b42e-f4e33197bef2 | -11.0054 | -53.9755 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| be14f8bf-6432-3242-b295-42938196562a | -11.1545 | -42.8124 | 2026-09-22 14:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 53e6df0b-7625-3464-81cd-74663835004a | -2.8791 | -57.799 | 2026-09-22 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| aa5e8c54-f5fb-3b9e-9191-4d341c5f3ba2 | -6.8985 | -41.6976 | 2026-09-22 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 215.3 |
| 6be33e00-1152-36c0-a247-b0fc4c69aea2 | -12.8246 | -54.0442 | 2026-09-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 82b7d2cb-c48f-3518-b61e-b0ac6b8cf43a | -6.295 | -57.735 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 9a7685da-6df7-3355-ac98-5d334e2f42d7 | -3.2899 | -42.6683 | 2026-09-22 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5543f2a2-c309-395b-8bb1-2a9c7aab7af8 | -9.9061 | -48.4649 | 2026-09-22 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 804f132e-1552-3ef7-bd47-e6e00f2f9061 | -7.1747 | -47.4297 | 2026-09-22 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| c5f0da38-8b36-3b38-a5d6-74530601a45c | -6.8216 | -59.1686 | 2026-09-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c202df39-e048-3f0d-a167-669a99941c2d | -5.7873 | -43.7758 | 2026-09-22 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 132d5d61-e8e8-39f4-b1dd-4bdf9d20f623 | -13.5911 | -51.458 | 2026-09-22 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 116a07e5-82cb-3ba4-8e4d-97776b1f8f6e | -6.1653 | -47.5052 | 2026-09-22 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 71a78b6e-93e6-35c9-adad-93cf861868be | -2.9391 | -50.4832 | 2026-09-22 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b0340af9-fe82-32e4-b023-220af5f05d66 | -6.1176 | -59.9261 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2c813448-f1e7-3672-8ad9-f188dc2480be | -12.1444 | -44.2665 | 2026-09-22 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| b7cd784b-7c55-3a7d-946d-aec100d8bb98 | -10.5425 | -43.9649 | 2026-09-22 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 08417721-0a63-3651-8c6f-132fb79f3875 | -7.1392 | -42.0811 | 2026-09-22 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| cf7833de-1db7-3588-86a2-22671a77ec2b | -6.1651 | -47.5271 | 2026-09-22 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 589f8b51-b9e2-3d0c-9099-c6c670a16dc8 | -6.4302 | -59.9724 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |


[Clique aqui para ver as próximas entradas](README137.md)
