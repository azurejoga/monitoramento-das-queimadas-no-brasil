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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd4575e5-b36a-3e3b-9756-669760736df8 | -7.58434 | -45.48053 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d6efece9-66ec-309e-b611-dc66003b9703 | -10.29037 | -50.23792 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 06399d6e-c3cd-3e66-821e-dffa1a5c9509 | -9.1846 | -45.31159 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45e041db-b7b8-3cd3-9432-d4cfb24b6d48 | -9.14305 | -44.85325 | 2025-09-19 05:14:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0178b010-8aea-38d1-8378-623c59b91d2c | -6.51112 | -51.19129 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99873dcc-e1f1-3ba4-a9a9-bb0e6a0acc2d | -9.17789 | -45.31072 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b500e24-81df-3e2d-b89e-298f2a42cf39 | -6.33457 | -56.18016 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae654366-bdc6-347c-b202-ebcc5a06cb33 | -8.13516 | -44.4745 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c2c443c2-6921-3557-a39b-46738b25635c | -9.72665 | -45.91879 | 2025-09-19 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bb5f220-3bcd-348a-b67d-b418383c96ad | -8.03981 | -45.72217 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 232a5afd-e7ea-36c1-baad-9e8d4f4263be | -9.46187 | -63.21338 | 2025-09-19 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd3fd190-8f61-3ce7-a967-9f14428421e7 | -12.08754 | -44.83999 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e00112e0-ddaa-3439-8503-b916a3f6fade | -5.68432 | -51.75149 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 765f503b-1076-36b1-86cc-16e7de927623 | -7.54837 | -45.50239 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3258bd5b-ae80-3570-be9b-7af00e59ebf4 | -8.03046 | -45.74293 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae0dac9-4f08-3b04-a9c4-cf4215dfedd0 | -8.13602 | -44.46775 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ff06257-d464-3075-a9de-fa82dceee243 | -6.3312 | -56.17963 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61aa51e7-0d90-38e6-93cc-a73092122424 | -6.3301 | -56.18678 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b742906-5486-32ce-93b3-e44ccb059ba9 | -11.21374 | -49.63168 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c88140a-f188-34ed-ab2c-2d7f752e0cd1 | -9.45781 | -63.21264 | 2025-09-19 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2a2d847-e66f-35e7-aa53-08a07076a4f6 | -12.09712 | -44.85256 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72226dbf-01e1-3db1-842e-cb769f69f61b | -11.42251 | -56.83361 | 2025-09-19 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7568fd13-53a3-3539-a3f2-5ab99e787f3a | -10.28469 | -50.24285 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c3a2baac-ddc8-3c16-ab54-78f5481ad517 | -8.02196 | -45.70831 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ac67599-6e7f-3b66-ab43-400f118657a7 | -19.57503 | -57.74874 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9c1904ce-7af5-3fd8-886b-53d1c3dfe127 | -14.26958 | -51.34258 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0cb128a-de69-3602-a723-29f4a88141dd | -15.79915 | -59.41087 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a952feb-4f8c-3aeb-9df5-976d9721b882 | -15.3362 | -59.4076 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68adb74b-a81b-3561-b878-06b2e6fbd0f3 | -15.77867 | -59.38901 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64e164c2-c23b-3a08-b094-a3185e5d4a87 | -15.3323 | -59.41063 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af100247-e90e-3df5-8ea4-ae632cd93df0 | -15.79363 | -59.40257 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800402a0-b55d-31f0-986b-d153b0f6ae52 | -15.29616 | -56.8361 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32bbc91e-a09c-3c5a-a7be-600d61301c0e | -19.57915 | -57.74514 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 119c715d-f592-31d0-935b-4a6f0ed10de6 | -15.78369 | -59.37879 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3d264ea-8e94-3d35-bffa-cd0900b1a54b | -17.09058 | -55.49953 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 327335de-5d92-3fd0-bf78-6569f76f01bc | -17.09389 | -55.5117 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0350992b-c6d5-349c-8c9c-ed5ce6fc90c2 | -19.5827 | -57.7457 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 692ea6fd-1fb7-350a-92ad-bad14d8ec7bd | -15.77754 | -59.39617 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d72b6b5-4000-3b7a-acf7-79e993e3575b | -17.09135 | -55.50124 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 172dc1d9-ecdf-3a0a-8382-389e073e5a24 | -14.18592 | -51.38097 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a7bd3f-33e9-308b-84a9-c59a79e5371f | -19.00727 | -47.89421 | 2025-09-19 05:16:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e8ef3c3-81ca-30b2-96f7-79036e5d8630 | -14.83536 | -60.23938 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9736e075-02fa-34de-a8e8-510712d33f04 | -15.03493 | -55.3361 | 2025-09-19 05:16:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4686018c-7bb2-3fc9-834a-a3ddd18f38c9 | -14.27444 | -51.34323 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7efe9e7-7115-347d-9a7d-1d65e92be874 | -15.77636 | -52.16011 | 2025-09-19 05:16:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8fc9ce75-b906-324b-941b-15b0bee02970 | -19.57919 | -57.82166 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9469e1a0-e39a-3216-ac40-5f30513e0328 | -15.28201 | -56.83553 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b337c1c-48a2-3c01-9876-83882fb66e8b | -14.82924 | -60.23463 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87fef13c-df87-3e97-9885-88e4828f9e89 | -19.58978 | -57.82336 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f98b6a2d-3a0f-363d-9ac1-3587aef26da6 | -15.90888 | -59.44347 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d0d02d7-05bb-372a-a9e1-2cf657a40c38 | -15.32508 | -59.4131 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a57bed-6e94-349e-af06-f48c72540580 | -16.01069 | -59.92947 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d936795-bc38-3108-82f0-fdc8fab9fbf3 | -20.79055 | -47.23241 | 2025-09-19 05:16:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36153a2d-2905-3f65-b98f-4ed3e80e01c6 | -16.69003 | -54.9686 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f51c00ad-4a07-3b3d-bea5-43f4452c345e | -16.6933 | -54.97421 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9aa660f3-6dcf-3772-b8d1-c2f1fc51c0c7 | -19.57149 | -57.74818 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 11202b48-7974-3654-8aee-19986fab62d2 | -15.80192 | -59.41502 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28f48524-e96d-3723-a369-5ae01d45e853 | -15.29824 | -59.41632 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96e8291c-a0f2-3096-a2b3-23393b4ecf2c | -15.79695 | -59.40313 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7036c85-fa62-3f21-b92b-4afca07ff31e | -16.68739 | -54.95824 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 317de764-0def-36e4-a8bb-f95713488f59 | -14.83142 | -60.24245 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5021855e-cddb-37a7-ac2c-6b94b79076cf | -14.41811 | -47.38768 | 2025-09-19 05:16:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a8c70157-144e-3f90-b1be-8e8cf2d47689 | -14.83083 | -60.24609 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b44bda4-3c29-33f1-8286-6ee02c69a7da | -15.28202 | -56.83414 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e35ea04b-3bf5-320e-b797-baf9778a8d3f | -15.7798 | -59.38182 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f898f8e-2be4-3ee4-b633-478f12be4ff5 | -15.79639 | -59.40671 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4845ab41-1d24-394e-b421-048442e47663 | -14.74329 | -60.20206 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7c23380-d1be-35f8-a8f5-788bfae58ec3 | -15.79306 | -59.40616 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e59190a-4892-39e0-a299-f7a34a44c0c1 | -15.82556 | -59.50373 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6639bf16-813e-3509-8fdb-097ea794d304 | -15.78313 | -59.38238 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1dff50c-c8c2-3be0-89c1-05fb188a0fca | -16.68672 | -54.96319 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e11d1c3d-cfb9-309b-b55c-0351f9346df5 | -15.81726 | -59.49128 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1ee5e5e-9fc7-3f81-a5f3-046e25c1fc9f | -15.90556 | -59.44291 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0faf0974-4079-3f79-ae83-6a8bfdc5a1e5 | -19.59037 | -57.81921 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8a284efc-2028-3e6e-9381-41b225c4897c | -14.2689 | -51.34802 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ed3a0cc-2bc7-3eca-b361-c99343b7a0c0 | -15.27849 | -56.83492 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91c5b777-1c8f-3d4a-a748-46b47dc1e530 | -15.80028 | -59.40369 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b7d5cef-1000-310c-a7f3-ec2302023850 | -14.26472 | -51.34194 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfa37a0c-c71d-3506-8bf7-23e148e15067 | -15.29767 | -59.4199 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60825d51-f865-3cc1-a299-48122759a76d | -14.74665 | -60.20257 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86fe345b-ddb7-318e-bf7a-1ed3c3ff5f2b | -14.18527 | -51.38637 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1837ed05-d04f-3204-aed8-71eed8f6ca2a | -20.34678 | -48.78267 | 2025-09-19 05:16:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6de1015-8c5d-3f6c-9f3c-3bae57b33675 | -15.27851 | -56.83352 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6372bded-eded-32aa-9bbb-b441b946ee3b | -19.0068 | -47.89955 | 2025-09-19 05:16:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad4731ed-a007-3629-a522-b4310c2a6806 | -20.79722 | -47.23475 | 2025-09-19 05:16:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e6a303d-f69f-3ffd-b46d-06a9995e1d4b | -19.57857 | -57.74932 | 2025-09-19 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ab05cd1f-cc1c-33f5-b04a-76de6549a76b | -14.27376 | -51.34867 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f614df19-cc9e-3108-b5dd-9c0000ad4d9e | -15.33287 | -59.40705 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 013f7134-1078-38ea-873c-c6f5c1915829 | -15.90945 | -59.43988 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c0751c9-2511-3985-b1de-a54fa271e6c8 | -15.31936 | -59.4125 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c118def-c2b6-346a-8faf-e8c80553a6d6 | -15.27789 | -56.83896 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 949f9861-aa60-3d9c-a981-48f320515248 | -17.09455 | -55.50676 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 71a1eff1-dd0d-3287-9dc7-8708d2f8d619 | -16.68934 | -54.97367 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dc11c7f7-3493-3a4f-8f37-0a8b93739484 | -15.32564 | -59.40952 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d0b30ba-ce63-3310-aa89-ea21cc5576d1 | -15.31879 | -59.41609 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b52539dc-6464-3e53-adcd-bce3a200ff6b | -15.41843 | -58.77999 | 2025-09-19 05:16:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e041a402-70a9-3faf-9403-64830240d89f | -15.33677 | -59.40402 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c16a5a1-d213-35dc-b63f-bab320e58bc4 | -15.03427 | -55.34082 | 2025-09-19 05:16:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c578e0d5-1864-3582-aeae-683a0d5bc22c | -17.09774 | -55.51227 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a8b73555-c87f-3f99-bd74-52606449d635 | -15.91278 | -59.44044 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
