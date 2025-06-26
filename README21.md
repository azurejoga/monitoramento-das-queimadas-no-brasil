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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4359177f-9c51-3a33-8c55-0e5954f5592a | -8.76168 | -63.753 | 2025-06-26 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317e7fb7-b18e-3205-98d4-f56aa6b16f83 | -10.06543 | -55.55432 | 2025-06-26 05:29:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80d41f28-e01c-3355-8fbf-60ee7264f7a6 | -11.23422 | -49.48929 | 2025-06-26 05:29:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39e72d85-e23a-36c8-bc8b-6fb79654d415 | -11.83252 | -51.25964 | 2025-06-26 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea6916ba-751b-39aa-a534-6bf9cdafe29e | -11.82609 | -51.25877 | 2025-06-26 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b55e34d-3e86-3584-8a28-86af7fcbcd94 | -11.06749 | -55.06661 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 418b592c-7f0a-395d-b47a-53eb51256540 | -11.57176 | -52.1002 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3c65596-c4c2-3113-8f97-3eb263a0e1d1 | -12.52789 | -57.1883 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5940c05a-3221-39c8-9019-d444410840e5 | -9.39328 | -63.26708 | 2025-06-26 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6aff12f-8495-321f-a57b-e8e01e0ff854 | -13.29426 | -57.08836 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 346b4407-ed3d-3a6f-b7c5-110deb4b47c9 | -9.1213 | -49.4313 | 2025-06-26 05:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 9fc1322c-672d-371d-8f26-c2b5b23d5ed7 | -18.09179 | -54.28339 | 2025-06-26 05:31:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce458be5-40b2-3434-8d2c-1c944394454d | -18.09225 | -54.27905 | 2025-06-26 05:31:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38cac95b-3967-3d19-aecc-59b116c11aee | -18.09307 | -54.28162 | 2025-06-26 05:31:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae92e284-a732-3741-a30c-881d86de0e7a | -18.09264 | -54.28596 | 2025-06-26 05:31:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 861c1a93-a667-3012-a524-887d5b181868 | -9.1213 | -49.4313 | 2025-06-26 05:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e8e978e1-f5d6-3176-855b-164afefcead2 | -9.1213 | -49.4313 | 2025-06-26 05:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 010b503d-de84-348c-a6c2-813b92a55bfa | -9.1213 | -49.4313 | 2025-06-26 06:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e9cbd606-510a-3b35-9ced-7a3fd656c598 | -9.1213 | -49.4313 | 2025-06-26 06:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 57399741-127d-31d9-b7fb-c89c5322c9bc | -9.11335 | -49.45565 | 2025-06-26 06:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7aba645a-5bd8-30f5-8411-811fda7dc21d | -11.81204 | -57.3466 | 2025-06-26 06:29:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e8dfd626-9cdb-35e7-8a22-119aebad42f6 | -9.50386 | -56.09018 | 2025-06-26 06:29:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ad739d76-437e-3cd4-9a34-839a07668414 | -9.11815 | -49.43691 | 2025-06-26 06:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 8c1b4cb1-a910-3ebd-a4a2-fa4b0a715c26 | -11.3643 | -48.68999 | 2025-06-26 06:29:00 | AQUA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 1a513c13-6a89-3d82-b44b-5f09cf205f49 | -11.35707 | -48.69641 | 2025-06-26 06:29:00 | AQUA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 653c53e1-48cf-3673-a0b4-e43c9cb0d0ab | -10.82041 | -53.73309 | 2025-06-26 06:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e62dbea7-33e6-3377-9e45-2df5d57bb7ce | -9.11688 | -49.42916 | 2025-06-26 06:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a8fc1ca5-4aa4-3796-b578-c05c51bcfaa2 | -9.49484 | -56.08886 | 2025-06-26 06:29:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| af8da189-3056-3ca1-b54d-f862720dfebe | -11.06261 | -55.37149 | 2025-06-26 06:29:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 232bf93e-e103-3f3e-95bc-fe94a810e66c | -11.07209 | -55.37281 | 2025-06-26 06:29:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9572658f-9924-3137-844e-d3cca8c92016 | -10.30164 | -57.12652 | 2025-06-26 06:29:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9343544f-7909-34f7-8003-485c7f0235df | -9.51016 | -56.11015 | 2025-06-26 06:29:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 50887ee6-df44-3578-9aa5-911dca9aff54 | -11.8107 | -57.35565 | 2025-06-26 06:29:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ca798f3d-207f-3209-8e89-b5a9b3d0cd9a | -11.06115 | -55.38191 | 2025-06-26 06:29:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f8b13d32-2e1c-3e61-a518-15d48ac1258b | -9.5025 | -56.09951 | 2025-06-26 06:29:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 58f6c6ff-6b51-3c69-bfe9-76a879d4dd25 | -12.02615 | -57.08422 | 2025-06-26 06:29:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| be2c21f5-6a9e-33a7-af30-2fc00e38786c | -9.51152 | -56.10084 | 2025-06-26 06:29:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7a4c6a1f-b48d-3ce3-a092-046878831bd5 | -10.87285 | -56.44949 | 2025-06-26 06:29:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3cc40648-ddab-3573-993e-982f61d4e630 | -9.1213 | -49.4313 | 2025-06-26 06:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| afa94690-c1ad-3100-acfc-e697828f0fb8 | -9.1213 | -49.4313 | 2025-06-26 06:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| fa54acef-961f-379a-9a2f-791bad7c270e | -9.1213 | -49.4313 | 2025-06-26 06:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b1d33b2f-c0a1-35ac-88ec-fe8896fa4e06 | -9.121 | -49.4528 | 2025-06-26 06:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| e6e18695-51bc-34b4-be33-00acc0c2f159 | -9.1213 | -49.4313 | 2025-06-26 07:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| a764faa5-3a18-3e8d-9a39-d639461ab012 | -9.1213 | -49.4313 | 2025-06-26 07:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e48ab7bb-7d9d-3866-b802-b70ba51f1d35 | -9.1213 | -49.4313 | 2025-06-26 07:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 144eb671-d8fb-36a5-9ab2-8d6ab8aadc7e | -9.121 | -49.4528 | 2025-06-26 07:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 499de703-8b6b-3ed4-91c8-e6a694dfcf55 | -9.1213 | -49.4313 | 2025-06-26 07:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8d126bb6-7b48-3cf3-bced-7890ee778274 | -9.121 | -49.4528 | 2025-06-26 07:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 4923a1de-addf-34fd-8917-585f140a2a8d | -9.1213 | -49.4313 | 2025-06-26 07:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 04b49b7f-14cd-3790-8245-b6e54b556184 | -9.121 | -49.4528 | 2025-06-26 07:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 845ea974-2989-3cb2-988b-ffc41c20148c | -9.1213 | -49.4313 | 2025-06-26 07:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d007f759-f6d8-35ef-9d15-cd19f5cbf2ab | -9.121 | -49.4528 | 2025-06-26 07:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 74440547-283c-3752-9c83-d88e8576b0f2 | -9.121 | -49.4528 | 2025-06-26 08:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d05628c3-6657-30ba-8b56-6f36bb0d01c1 | -9.1213 | -49.4313 | 2025-06-26 08:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ea86260d-30fc-3e2d-b3e6-503968a40457 | -9.1213 | -49.4313 | 2025-06-26 08:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 11d73332-8736-3579-a148-504c4a902a86 | -9.121 | -49.4528 | 2025-06-26 08:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 188d9758-52a4-34a0-a238-102b2c55120f | -9.121 | -49.4528 | 2025-06-26 08:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7b52e728-43ff-3753-a099-930feedca613 | -9.1213 | -49.4313 | 2025-06-26 08:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| e21b17f4-3807-30dd-ade8-6da395969cee | -9.1213 | -49.4313 | 2025-06-26 08:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 87565d03-01ee-3f1d-8ddb-9f27bb531f75 | -9.1213 | -49.4313 | 2025-06-26 08:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 02cc54b1-a3f3-3678-a860-5abf4821e3c1 | -14.2442 | -45.5002 | 2025-06-26 10:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 951a1237-aeb2-3a1a-bbcb-dc3ed63abace | -14.2442 | -45.5002 | 2025-06-26 10:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 262.6 |
| fff23e62-354c-3dd5-8e90-f7b60a84504b | -14.2247 | -45.5036 | 2025-06-26 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 38b2ccf2-61d2-3bcd-a5b6-a92e681da999 | -14.2442 | -45.5002 | 2025-06-26 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 374.4 |
| 9b2a2a1e-74c2-3f35-bfe0-d6d72c9be534 | -14.2247 | -45.5036 | 2025-06-26 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 2feb818c-4d29-33a0-af08-b6ccfe1c73ef | -14.2447 | -45.4769 | 2025-06-26 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| cd4a1e72-fbc0-3d36-85a0-9f6c45ef7ecd | -14.2442 | -45.5002 | 2025-06-26 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 422.2 |
| ec63c7bd-47b2-3533-9c4c-52d1ce4f8c43 | -14.2442 | -45.5002 | 2025-06-26 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 443.9 |
| f613ae96-f25c-36f5-b772-f7ee812cd19f | -14.2247 | -45.5036 | 2025-06-26 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 6b89ae65-dd31-36f6-8c86-e8a8a09e5f2a | -14.2447 | -45.4769 | 2025-06-26 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| efff09f4-5b82-37cc-87f0-c408206de84c | -14.2247 | -45.5036 | 2025-06-26 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 4ccba329-9d36-37aa-bd81-cf54f02a91b0 | -14.2442 | -45.5002 | 2025-06-26 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 379.4 |
| 0c8927fe-4fc8-3f96-9852-dc80489580c9 | -14.2447 | -45.4769 | 2025-06-26 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 72857246-ba51-338b-9463-4ce6e37b7950 | -14.2247 | -45.5036 | 2025-06-26 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 36c31ca6-f82c-3cb2-a83f-2906c989d352 | -14.2247 | -45.5036 | 2025-06-26 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 3cd4a600-73a3-3686-bd6e-cb1e36162c3d | -14.2247 | -45.5036 | 2025-06-26 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| a12483b7-476e-345d-9bdf-cdcaa94bfff8 | -14.2247 | -45.5036 | 2025-06-26 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e0815cd2-95f9-36fd-9c9f-cab8fe89da49 | -14.2247 | -45.5036 | 2025-06-26 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a00d5e7d-b820-3ba3-a9f8-44de0a182d61 | -11.8079 | -43.779 | 2025-06-26 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| aca1991b-ee74-3e33-b1b2-ab7cbb63506d | -14.2247 | -45.5036 | 2025-06-26 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 257cd612-76be-3d7a-bc0a-775f8ce73e63 | -9.1213 | -49.4313 | 2025-06-26 12:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ad8e0fd7-c1f5-3614-a6cd-515e24166859 | -14.2247 | -45.5036 | 2025-06-26 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| c77f1f5c-6746-3ed0-969d-ba3afc5faf21 | -7.56409 | -44.49514 | 2025-06-26 12:06:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70acfce1-2cc6-3eff-93a3-5000beddca27 | -8.48394 | -48.25648 | 2025-06-26 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2c9e1557-5a72-3012-b179-5e49d6fd56db | -8.80648 | -45.00264 | 2025-06-26 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c924dbee-afea-3c5c-9e67-ca9b70fa99e5 | -6.90192 | -47.84561 | 2025-06-26 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 68aba4ac-64c8-3c14-a8f3-3b427f180f12 | -7.20668 | -43.08918 | 2025-06-26 12:06:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ec5b6bc7-df80-3987-816d-5ade5623fdde | -9.07004 | -46.90366 | 2025-06-26 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2ae19a05-4423-3a5a-8ebf-5905b6b6dca9 | -6.63933 | -39.35765 | 2025-06-26 12:06:00 | TERRA_M-T | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 14d28d35-214b-34fe-b47f-7380ce6e352c | -8.79251 | -47.22839 | 2025-06-26 12:06:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b6026cef-f18c-3341-90a6-6bd7cde3641f | -9.38793 | -47.33791 | 2025-06-26 12:06:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2a87fe18-6eaa-3a6c-b061-8f6417947609 | -6.18687 | -48.07253 | 2025-06-26 12:06:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 92f7a272-ca0b-3788-bba0-8373a977d000 | -9.16604 | -40.52674 | 2025-06-26 12:06:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| ac09c7b5-40f5-3fba-a0da-7cf53e898a1f | -9.07324 | -46.92407 | 2025-06-26 12:06:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6678ce0a-6782-364e-af07-9206b7af3bc8 | -8.15031 | -46.81931 | 2025-06-26 12:06:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8892f25a-544a-3b69-a4c8-01389768d256 | -9.07529 | -46.91108 | 2025-06-26 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 16ab3457-b638-342b-905c-17be14e660fc | -9.17149 | -40.52277 | 2025-06-26 12:06:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5f261e38-1b17-35e2-a617-6ab6d37a17b4 | -9.0681 | -46.91653 | 2025-06-26 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 3770fe75-a7d9-3b28-b5d0-bad6eb2d90bf | -8.8158 | -45.00401 | 2025-06-26 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| bd6c2288-a467-30e7-9e82-89c5c66db6c6 | -8.89602 | -44.78447 | 2025-06-26 12:06:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README22.md)
