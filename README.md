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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec88ec1a-e85c-39f5-9ea5-f6e94273292f | 1.2852 | -60.4454 | 2026-02-09 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ecf81b65-ce0f-36d0-942f-60f596467f64 | 1.2852 | -60.4265 | 2026-02-09 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9534e790-b09c-35e4-aea0-3a02c253d335 | -15.55857 | -42.66564 | 2026-02-09 00:07:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c7a09d3b-c77b-31e8-9c70-63373233f52a | -13.49475 | -46.7061 | 2026-02-09 00:07:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f00f2c5-0ede-3b2d-bf88-8f45ddcf471f | -13.50416 | -46.70485 | 2026-02-09 00:07:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 44aebb5b-fad7-3e6c-abd6-1590b1439c64 | 1.2852 | -60.4454 | 2026-02-09 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b5574241-c64e-3122-9940-16a436b77319 | 1.2852 | -60.4265 | 2026-02-09 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7464332f-8ac7-358b-80f4-40f816918f70 | 1.2852 | -60.4265 | 2026-02-09 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b48cd2c6-a1b4-30e7-bb8c-fb9919c10954 | 1.2852 | -60.4265 | 2026-02-09 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 928594c2-6255-3012-b215-ea98a6869865 | 1.2852 | -60.4265 | 2026-02-09 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cd5d2a37-28b0-33fe-a181-2181adf042ed | 1.2852 | -60.4265 | 2026-02-09 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e511d001-a9be-3dcf-ba78-ba9f0cf28217 | -6.5631 | -51.1126 | 2026-02-09 02:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 353a71af-9ad3-3b0c-aaaf-2865f332bb3c | -15.53515 | -39.46125 | 2026-02-09 03:25:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4467363b-e994-3264-a490-ea4cf42cfbbc | -15.90824 | -40.23048 | 2026-02-09 03:27:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 60a31e64-8813-3c7b-ac82-1cdd8a7634c6 | -18.51627 | -44.55314 | 2026-02-09 03:27:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7e7e398-4d6c-3ab0-86b2-af66067a4d1f | -18.52194 | -44.55303 | 2026-02-09 03:27:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3efe1f94-98fe-3958-a1bf-f6e5831e1529 | -18.51616 | -44.55172 | 2026-02-09 03:27:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a868e47b-fbf7-3e3d-9781-94971f943422 | -30.29796 | -50.92608 | 2026-02-09 03:32:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| cb5390b5-40d2-37e8-8563-779cc6983fd8 | -30.29849 | -50.92511 | 2026-02-09 03:32:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| caba1e20-83a0-3233-b0b0-eaa7341b1482 | -15.5529 | -42.6605 | 2026-02-09 03:55:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90805ba3-36af-3f21-a68c-42c124c5bd97 | -15.612 | -41.29755 | 2026-02-09 03:55:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 45daca07-1ff3-3755-bcef-4083d1aac1f8 | -15.53442 | -39.46165 | 2026-02-09 03:55:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0c47025-b09f-3497-95b3-c72a58cbff99 | -13.49631 | -46.70928 | 2026-02-09 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52c5a670-10a9-3315-a320-7f923318366d | -13.50096 | -46.70972 | 2026-02-09 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa271a71-8102-3610-82fa-28b9f9ad1bbe | -13.49605 | -46.70863 | 2026-02-09 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 028a8ea6-f9a7-3a79-b923-546ba7d6fe63 | -15.90802 | -40.23193 | 2026-02-09 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ff41a05-2a83-3458-93f0-0c14156ce86c | -12.71155 | -46.79772 | 2026-02-09 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cccfb4c-8ce2-300e-ba4d-3987cc160f40 | -15.53499 | -39.45806 | 2026-02-09 03:55:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 153fa415-70e2-39c7-ab37-b505a1d3e175 | -14.07094 | -39.49733 | 2026-02-09 03:55:00 | NPP-375D | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1c0e365f-0ac8-3fe6-8d14-d7b4ce812272 | -12.70859 | -46.79293 | 2026-02-09 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9fe2549-a094-30fe-ae6a-1791e8270b96 | -15.42762 | -41.42842 | 2026-02-09 03:55:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ffabd212-5ad4-3713-a2b3-33b93e020224 | -12.15157 | -38.0658 | 2026-02-09 03:55:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92eca1a9-072e-3361-99a5-ca5e869b852b | -12.71214 | -46.79473 | 2026-02-09 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e8849c1-d26e-348d-bb76-2ba385f66e46 | -13.50122 | -46.71035 | 2026-02-09 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6bcf11-e97e-33d7-a3d0-898920c7847f | -12.70802 | -46.79593 | 2026-02-09 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c045e4dc-24af-3626-a6d5-e2745e01711d | -18.51968 | -44.54933 | 2026-02-09 03:57:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13ba7873-93b5-3586-8c05-0795859e9d3b | -30.30067 | -50.9272 | 2026-02-09 04:01:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 04fe2dc1-c46d-3ec9-900f-9f0348540cbb | -2.52187 | -51.82494 | 2026-02-09 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94e1b3f-5e00-3d1a-87ab-595ac73cc841 | -12.63559 | -48.9193 | 2026-02-09 04:16:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 305fda00-7631-3fc4-b026-b8e355fd54e6 | -12.70757 | -46.79321 | 2026-02-09 04:16:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ec5b164-db8c-30ad-85fb-b92b5ecc4a87 | -5.85181 | -44.94232 | 2026-02-09 04:16:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc2707fa-b904-3876-b022-0995db39671a | -14.06957 | -39.4972 | 2026-02-09 04:16:00 | NOAA-20 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da49edb3-bd08-3037-b1f1-a55b23aa2b72 | -12.71101 | -46.7938 | 2026-02-09 04:16:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f23cb804-ca2f-3f95-82f7-28f1ba29ca38 | -12.67666 | -38.80099 | 2026-02-09 04:16:00 | NOAA-20 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 36025dfb-1337-3fca-a028-c11d8b8e926e | -13.39092 | -43.56775 | 2026-02-09 04:16:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86c6d178-6700-3d17-8da4-c686f280eb2b | -18.75423 | -40.35561 | 2026-02-09 04:18:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bab6ba6e-5130-395b-a048-6ee4cd003ab2 | -13.49743 | -46.70651 | 2026-02-09 04:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83130398-ee2e-33ad-8e92-875826130f6f | -17.69516 | -40.06519 | 2026-02-09 04:18:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| febd8ebf-eb4a-33c1-af82-289f66049251 | -18.51498 | -44.55297 | 2026-02-09 04:18:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fa2c3fe-335a-3ba0-83bc-463561711d80 | -15.53267 | -39.46227 | 2026-02-09 04:18:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ed28eed6-db6c-30b1-9a84-eb7e3eda341d | -18.51893 | -44.54976 | 2026-02-09 04:18:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b98d5770-0cf6-3714-8d3e-a2a412f4835c | -15.55204 | -42.66148 | 2026-02-09 04:18:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 545db77a-ecc6-32e1-91ea-2006ff26faf5 | -13.50084 | -46.70711 | 2026-02-09 04:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37d28921-4b6a-3665-a72f-613b8c412582 | -18.51836 | -44.55354 | 2026-02-09 04:18:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d198d14-0444-3f5d-89f7-407dd72a223b | -17.62092 | -41.3322 | 2026-02-09 04:18:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| ba379b20-3df3-30e3-b26a-6a3d72a683e9 | -17.6164 | -41.33656 | 2026-02-09 04:18:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 588b284e-4dae-3849-a4cf-3582fd5e9902 | -17.69935 | -40.06577 | 2026-02-09 04:18:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5f29f9ed-fe56-36ce-a32e-175463370e8b | -15.53322 | -39.45811 | 2026-02-09 04:18:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f552d2db-74c5-3e41-a881-509d06bbc9d3 | -17.69464 | -40.06926 | 2026-02-09 04:18:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 85f41236-27e4-389c-8309-2f0117b07f5a | -13.50022 | -46.71088 | 2026-02-09 04:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f3da636-0c74-3640-aa9b-77aa98e837f0 | -30.30029 | -50.92465 | 2026-02-09 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| a54cf95a-bfcc-3b44-a991-ac16d0d7bd17 | -27.71062 | -51.75005 | 2026-02-09 04:23:00 | NOAA-20 | PAIM FILHO | RIO GRANDE DO SUL | Brasil | 4313607 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 65cef467-8364-3742-be06-a97d69749a8a | -28.48198 | -55.54509 | 2026-02-09 04:23:00 | NOAA-20 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 5680899e-35c8-3ea6-83f4-b6dac50fe702 | -28.48316 | -55.54725 | 2026-02-09 04:23:00 | NOAA-20 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 9c4a68d7-66ea-34ac-bb32-0a587aba0775 | -30.29352 | -50.92308 | 2026-02-09 04:23:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| c70c2a2a-9833-381d-9adc-63b8d1ca1cd7 | 4.01784 | -59.62873 | 2026-02-09 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37f7c4d2-790e-38bd-a10e-fd3a1aa7f1d9 | 4.45822 | -60.68029 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15323e34-3412-37eb-9437-eebddeae63c5 | 4.45753 | -60.67542 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de989cf9-1e6a-39a2-b4f9-0495d064cceb | 4.41859 | -60.65944 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d0cabd6-96a8-3e24-b479-b6c993bb89ed | 4.45863 | -60.67254 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2828701-1a63-3da8-a1a4-5cfdc8bfcf37 | 4.45398 | -60.67331 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c05bfce-eeec-333f-9dd0-9d31c5bc2788 | 4.76899 | -60.32955 | 2026-02-09 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61651484-4eef-333f-b9bc-7be0d4db1528 | 4.42459 | -60.69997 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0bd0e7b-b0b8-3535-9e5e-130e29f79fba | 4.45936 | -60.67741 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eac98af2-d494-36c1-bc94-7799053373ff | 4.32756 | -61.16935 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21497de3-01a3-3417-9e87-0791d31bf403 | 4.32201 | -61.16518 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bfd33e3-dd42-378b-9505-a74cc4d7e1e9 | 4.37485 | -60.68566 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44e136ac-9b2b-3003-8338-410c22563d2e | 4.37555 | -60.69051 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1063c2fc-e37f-321b-b796-0e86e5b12d45 | 4.76374 | -60.32549 | 2026-02-09 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbe7035d-e441-316f-95fa-a097d272d75b | 4.32681 | -61.16438 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d06782-fb2f-364a-85d0-fafdd8fbfdd3 | 4.45151 | -60.66663 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1c65682-2419-31da-a43c-5c9dce61e596 | 4.42326 | -60.65886 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f43ca43a-4168-3399-9b89-8a29245eef65 | 4.42794 | -60.65829 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ac25c46-92a0-3cbd-9f29-8251770bb4e6 | 4.41996 | -60.70089 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52cbe125-1ddd-30e7-96c8-0c9096d71a7d | 4.32143 | -61.16362 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 757e7dfd-45d4-3aab-9025-49519e416ca5 | 4.45327 | -60.66858 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a356aa61-5061-3eb0-8efd-45f2aac73f1c | 4.42863 | -60.66298 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba92b8c0-9784-3f7d-8119-6abcb81e51c7 | 4.32695 | -61.16782 | 2026-02-09 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2aa0cbff-052b-3d24-bb46-3d1d7e30b2e1 | 0.95369 | -60.53872 | 2026-02-09 05:03:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5109ec6-30cd-37b6-b62c-bec386b517d4 | 2.04115 | -59.87002 | 2026-02-09 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82b6d3f3-b917-3a19-9a48-a38d390f6358 | 0.95673 | -60.52961 | 2026-02-09 05:03:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 952b2a77-1685-3b5a-9e5f-f0b7ddd04b78 | 0.96044 | -60.5247 | 2026-02-09 05:03:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c24e28-be64-3dc6-9f1b-2633a51fdb75 | -1.82475 | -54.49578 | 2026-02-09 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e781232-3304-3be2-8de0-319f4806f39d | -2.52373 | -51.82447 | 2026-02-09 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74ea3daa-8d67-372c-963a-61c11b2b1c9d | -1.96102 | -54.05751 | 2026-02-09 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e51e9969-2d63-3eed-ace2-048d9b665451 | -2.52438 | -51.8203 | 2026-02-09 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 780b15e9-2922-3df1-8145-a47ebc841d8c | -16.28917 | -58.26544 | 2026-02-09 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 965ff5b1-0207-3ebf-9dda-83e648b476d6 | -16.01759 | -59.90509 | 2026-02-09 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a82f6a6-ae15-3537-91c4-4640f75d8cc0 | -13.50072 | -46.7065 | 2026-02-09 05:08:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0ba7a8f-05cb-37fb-ba8a-29d51159c1ea | -13.50024 | -46.71085 | 2026-02-09 05:08:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
