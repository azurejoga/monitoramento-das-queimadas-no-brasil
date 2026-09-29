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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 864a497b-2aad-3828-94ad-a21dd64d1204 | -10.3894 | -61.2502 | 2026-09-29 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 0251798e-e556-3566-8522-c3fec5db81bd | -5.7384 | -45.0626 | 2026-09-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b16980ea-fb37-3b00-831e-5112a12ff4f9 | -7.8297 | -45.8156 | 2026-09-29 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| d0bcf7bc-8416-320d-98d5-b9c3dc5d929c | -10.4081 | -61.2492 | 2026-09-29 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| e9457cc8-89a5-3e37-b6bd-561210e78d29 | -10.4079 | -61.2685 | 2026-09-29 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| fcc369ae-c8d9-342e-ae5b-55f7715e64e2 | -7.6158 | -46.4628 | 2026-09-29 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 12939998-1e16-3496-9e9c-4198316dcc73 | -15.0926 | -53.8862 | 2026-09-29 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ebfe5dbe-aa13-37d8-94e4-b0b79e885022 | 1.6567 | -55.8833 | 2026-09-29 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6fe020d8-b09e-3773-ac8d-8498d8866524 | -9.9265 | -60.7363 | 2026-09-29 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3ec5bec5-c11b-3e9e-9700-0970028ddfab | -11.3823 | -54.0434 | 2026-09-29 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 0434f233-b16c-3297-9507-b976ccb75d9a | -6.2949 | -43.6194 | 2026-09-29 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e865cab5-3131-3328-bc2d-76858df4b593 | -10.3892 | -61.2695 | 2026-09-29 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| f511fd26-a788-3b15-8415-927976dd59a6 | -15.112 | -53.8838 | 2026-09-29 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e4170ef1-0406-366e-be6e-9b2b366c6798 | -6.6812 | -55.1103 | 2026-09-29 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0f94a2e5-d1e1-320b-aa22-ec4e3d8242b7 | -10.7255 | -44.4291 | 2026-09-29 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f6c668e5-7532-380a-8787-2c97c4f128cf | -20.038 | -48.05624 | 2026-09-29 00:35:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| fd7f3e03-e3ca-3148-8654-adcb6c40b7a9 | -20.04907 | -48.05928 | 2026-09-29 00:35:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5459c1e2-7de6-391a-b732-afbc3148af41 | -22.09155 | -46.96043 | 2026-09-29 00:35:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 2c5ee45d-69ea-33c2-80d8-db7219c3204a | -21.70005 | -47.1695 | 2026-09-29 00:35:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 95c018ea-cd65-3218-83cc-ee625e8285b4 | -18.57957 | -48.41861 | 2026-09-29 00:35:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| 0c117a02-597e-3e2f-a6c4-c38b931cbce2 | -18.56989 | -48.44579 | 2026-09-29 00:35:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 5d4a94b1-6da1-3c04-9657-14b567b0637a | -20.09733 | -57.2072 | 2026-09-29 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 36bca4c7-31ac-3b31-b791-85e54c9ce896 | -18.68213 | -48.6336 | 2026-09-29 00:35:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| abbeca06-22d6-328f-a53b-6430bca3be20 | -18.56548 | -48.42191 | 2026-09-29 00:35:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| cab97353-ae19-3e59-878a-1dcf6801b84a | -13.56182 | -48.94158 | 2026-09-29 00:37:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ebd15176-1ee0-3d73-9300-7733e11d4ffc | -12.11844 | -57.17589 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af452c81-734c-3664-ab37-79ed60f50962 | -15.09766 | -53.88508 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 29.3 |
| bef20706-fda5-3813-a44d-8722f4db85cc | -11.37936 | -54.04061 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| c93e1ba5-435f-3dc4-80fa-95d5d081403d | -12.14767 | -57.19022 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b725d94f-f7ef-37a2-82f6-002e06abbb70 | -11.24352 | -54.07448 | 2026-09-29 00:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0b2348f3-ec36-30cc-804c-3040e885885a | -14.63848 | -52.12997 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1294c844-c75a-3b8b-8324-9863c88f54b4 | -9.13286 | -49.98275 | 2026-09-29 00:37:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| e498b1b7-d85e-3221-a786-bc2df2cfe219 | -11.9432 | -50.92007 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 83cdc6b2-fd8a-3aad-8df8-263595555809 | -14.64736 | -52.11186 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6d1072e4-8d75-362e-b698-add4fed9fc9c | -12.39977 | -50.22712 | 2026-09-29 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 92fab554-baba-3d26-a0a4-2b20b1a75cb8 | -12.61323 | -47.28719 | 2026-09-29 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 87b684c0-d54f-3587-aae4-db291d62321b | -11.35169 | -54.03786 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 662246f6-7013-3316-9c59-7906215c480c | -15.12059 | -49.53734 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ecf89a77-c6a2-34b5-a9cf-40a34828ed64 | -10.83995 | -60.73963 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c7e9dc2e-4f4d-3c7b-98a4-ee4ec30adeb8 | -11.16229 | -50.04174 | 2026-09-29 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 43c40273-d54b-38bb-9afd-960c269de89b | -11.33185 | -54.12184 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 9d827be8-629c-30f8-8326-b69e0cdfb7e4 | -9.68864 | -58.12645 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b8502f3e-5f4e-37d6-b9a1-d05aa9ec0fab | -11.35819 | -54.04394 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4156fee3-c99d-3874-a27c-83d2b7b44463 | -9.92848 | -60.72509 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2701fcfb-334c-37bb-890d-a398103040c7 | -11.39196 | -54.05214 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 1e8ba376-e4b6-39a0-8ed6-282adbd2dad1 | -15.08925 | -54.57671 | 2026-09-29 00:37:00 | TERRA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 993f5e3a-91fc-3c19-a6bb-eb4e9790cf72 | -14.21911 | -48.51365 | 2026-09-29 00:37:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 20b3034b-387f-3f17-bbbc-139605428c36 | -14.49898 | -59.74796 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3ced21c7-1faf-317d-b6a3-338b4aac74db | -11.97243 | -50.98993 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 63c4a7e6-8637-39ce-b833-6c9cf1327696 | -12.79048 | -54.01257 | 2026-09-29 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2103326e-9a9b-3fc2-99ba-1a000ec0f409 | -10.84129 | -60.75009 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 42b7ef83-343f-3918-9215-411c91fe589e | -11.3476 | -54.04555 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 83c2eb5b-4282-36fc-a6ba-f46842ae2a07 | -10.39518 | -61.26082 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| e1ef9a88-881e-3bc7-af59-926eae0e5ff5 | -11.16692 | -50.06866 | 2026-09-29 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 71221fc1-09d1-3c42-8377-5e249842e0c2 | -14.26892 | -57.67413 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 54601af7-7226-3edb-8fcc-f1ed8bb98c4d | -15.10954 | -53.89545 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b4835f98-9312-36a6-8603-84ea6f21ec8a | -11.36023 | -54.05706 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9fd03e0c-c0ba-3b20-8f3f-209062b30d8e | -12.11715 | -57.16674 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b27b5a99-cb27-30e2-ac5e-f649b39bf94c | -11.98925 | -51.00961 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b1a7efeb-0830-363f-805e-b44c5be68e42 | -11.99412 | -57.60425 | 2026-09-29 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71b2fcf6-07d5-3628-91e9-f97b80525b58 | -10.78515 | -48.74279 | 2026-09-29 00:37:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 1a63829e-27a8-3cdc-9bfd-3b2a1f95d09f | -10.83045 | -60.74092 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d052529c-d026-3f3b-ab81-c10a569e8395 | -15.19347 | -55.28092 | 2026-09-29 00:37:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e4968114-6831-3cc4-8dd0-ce60fcb7f489 | -11.96887 | -50.96783 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 445.3 |
| ca0658f5-a712-3795-a122-9aabcfae4cdf | -12.75493 | -54.05712 | 2026-09-29 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 24980151-2d66-3037-bbd2-9b36f480caf5 | -11.95194 | -50.94799 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 907.9 |
| 8aac5f2d-42aa-33a5-921c-aa94f4bb16a0 | -11.97743 | -50.95983 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 539.4 |
| b1ca3cae-149d-301a-819e-ca9fae9156c8 | -9.70629 | -58.1239 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b37b2b42-469c-3590-9cc4-2efc0849eb1c | -12.79241 | -54.02528 | 2026-09-29 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 95218362-8a84-3acc-bc42-e46a1958cf89 | -11.99811 | -51.00157 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 8a89fc12-fa0b-3289-9360-d58c01154e11 | -9.9298 | -60.7352 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a36a7d1e-7e99-3e9c-9251-b812a9894397 | -10.38541 | -61.26195 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0b0c54dd-ff2d-39a5-93c9-50df02869c1c | -11.98114 | -50.9819 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 433.5 |
| ed6bfd59-6fe6-3432-8933-b67825050935 | -13.55932 | -48.9368 | 2026-09-29 00:37:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 53fbd29f-77e4-37f1-a922-27612d371aa0 | -15.78669 | -56.19682 | 2026-09-29 00:37:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31cc1428-4170-396e-b78e-a835aa449ab4 | -9.69747 | -58.12518 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e682a1e-5caa-37f3-aa77-b980defbe6b8 | -11.98483 | -51.00389 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5e3736a3-f151-3bf1-a7e1-c69fe7f31945 | -9.9627 | -59.25532 | 2026-09-29 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c8b8e7ea-d297-3150-91c7-e621b7aaa7e5 | -15.09584 | -53.87299 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c68837d1-5e0a-348c-a476-7a71b246a96d | -11.95554 | -50.97018 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 41a4a125-5323-3b73-98ff-ea03462dde76 | -11.16137 | -50.04741 | 2026-09-29 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 58dfe94f-e27b-368a-b01c-ad3d2f5c058c | -12.80083 | -54.01082 | 2026-09-29 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a1c7d718-ea38-32dc-aeec-9d11090f5ccf | -11.55261 | -54.50231 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ab315361-ca88-3a28-b5e8-f9b51c6d68f2 | -11.44888 | -55.10707 | 2026-09-29 00:37:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a60bce3c-e85a-3790-8a40-292c9753cfcd | -15.09127 | -53.91088 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 51d44807-3e42-33f3-85d0-b902dba3bb47 | -11.36877 | -54.04224 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 77c29aa7-9fdd-3f2d-bfe7-795777a9cb49 | -11.34043 | -54.1072 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| af6b346c-31ed-3cd9-96a3-63c4f6dc496c | -10.85216 | -60.75932 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 16487813-731c-346b-afdd-a8031fd16428 | -11.16582 | -50.07439 | 2026-09-29 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a620f7db-6afa-368b-bd4c-10162c13120c | -12.12604 | -57.16541 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd6389bc-fde5-33b9-a4c4-049ebe389e95 | -15.10131 | -53.90918 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 337.6 |
| c39928b7-2e6d-354c-b2b0-a7c2fd54a519 | -10.84264 | -60.76056 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d4956ae1-4b73-3785-9a62-990f86435c97 | -12.39011 | -50.22229 | 2026-09-29 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6b12239d-6f31-3c03-8b3c-9719a56c49db | -12.78207 | -54.02696 | 2026-09-29 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 221cb566-c644-31fa-82df-b3531e9b4c3d | -12.10826 | -57.16807 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8ee0c57f-5a0b-38b2-ae73-5f2104f2ab03 | -11.13681 | -50.07957 | 2026-09-29 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 11e6129b-bdf0-3d34-aaae-06da85b0080d | -14.52434 | -52.48698 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 340ddb40-8c18-3d6e-bc00-b35668c016b5 | -15.08944 | -53.89885 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 31b1d7c6-0bff-31d7-a01f-710cfa1521f3 | -11.05603 | -54.19738 | 2026-09-29 00:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dd1f00ce-d7dc-36f4-9cbe-3227b4a66101 | -14.52569 | -52.49239 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README4.md)
