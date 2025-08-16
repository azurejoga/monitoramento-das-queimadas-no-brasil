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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7682e58-79a3-31ad-b835-5e680a28e1ac | -14.9672 | -54.740799 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20900967-cbda-30b6-8776-f14c81430d9d | -13.1207 | -57.136799 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b82848b4-2dd4-3044-9a64-bffeba7e28ff | -14.9606 | -54.7117 | 2025-08-16 00:47:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 16dabd5d-eb31-3bd6-a8ef-5a79b4f14dba | -7.9131 | -61.731098 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c63086f-3d54-39b0-a714-abf315f0ef93 | -7.6048 | -61.202301 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b98faa01-e352-3a38-aa7d-75a68eb8e304 | -14.9623 | -54.719002 | 2025-08-16 00:47:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0c8704d-ac92-3bc4-af6b-72fe20f8364c | -14.9574 | -54.743099 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7938d5dd-4254-32e6-b9dd-8d976d8fdf86 | -8.9984 | -60.484798 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f652b69-dfbb-3313-8911-d60b28fad20c | -6.6342 | -59.9981 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41478e07-8ad7-3bff-b784-31a5c9b0ed5d | -14.5788 | -47.8885 | 2025-08-16 00:47:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3aabeb18-d520-3fb1-8105-ff1a8cff1965 | -8.4697 | -64.033302 | 2025-08-16 00:47:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f16043a8-503d-3214-83a2-a60f3b83ae8f | -5.7492 | -46.653702 | 2025-08-16 00:47:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c70b5c14-7acb-346e-bdfc-2530b21cf8dd | -7.6818 | -63.288601 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5cb81d8-c9c5-3211-97ab-4930fe0d5556 | -7.4947 | -63.804699 | 2025-08-16 00:47:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec8c14e-d68d-3477-817b-1c12d049d99c | -7.5071 | -63.815201 | 2025-08-16 00:47:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f124b12c-277f-36d1-a185-a60bab5ee571 | -7.4582 | -59.913502 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 437d9730-37a7-3ebe-aca8-c89814e22ebc | -18.529499 | -50.749802 | 2025-08-16 00:47:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72e26390-9afd-35cb-82bd-964cbfbed8b8 | -13.1094 | -57.131901 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2387ab83-f7e3-35c8-b10c-0a0fdd6b1037 | -14.9411 | -54.716301 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e12f6e2-d5cf-3855-9f31-01d731317ff8 | -9.1629 | -59.630402 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efc86450-3353-3da9-98fc-05864e75a012 | -12.5261 | -46.949402 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccca3678-15fc-3268-852a-796f0ce9281c | -12.5206 | -46.928398 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32ac3585-2a2e-38f9-8dad-d41abe08169b | -8.9735 | -61.6646 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d463c18-2d82-3c9a-b8bb-6a057022b44f | -7.9151 | -61.740398 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42b0ab55-0c90-326c-ae7b-e1da81c429bd | -8.9755 | -61.674198 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d93d9525-013c-3ddd-952b-059eea50d17b | -9.1925 | -59.672298 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d16e3789-b6a7-3f96-aa1d-ffdca8a8ce15 | -23.993401 | -53.152199 | 2025-08-16 00:47:00 | METOP-B | MARILUZ | PARANÁ | Brasil | 4115101 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a753d1fa-3287-3b65-97aa-221060efbf81 | -7.4308 | -60.023201 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89c204a7-3b8c-368a-9223-8728d79559ea | -13.1269 | -57.1651 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc55fe8b-0ae4-3205-a4dd-9a1a44e07363 | -7.0543 | -59.618198 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9b79785-da9f-3308-8f63-e9d0f7d440fe | -7.9229 | -61.729 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69aa1956-d853-3dd0-9768-7abe9f6a8aed | -12.592 | -46.8862 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5156bb38-e1f0-3f1b-baa5-bff9cd21f192 | -9.1686 | -58.901901 | 2025-08-16 00:47:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7ecbe6-20c5-3c5e-8eb9-05559ee11d82 | -8.9895 | -60.539101 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f921f995-5832-314a-932c-dd81c19caa20 | -13.1259 | -57.113201 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6edd299b-e7fd-3091-85e1-ae5910390266 | -9.2152 | -59.635101 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0c61e6-3bc2-3b22-a5e1-4f24b768bb79 | -9.9297 | -60.4786 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cadf38f9-efc8-39f7-aba9-0e0b971fd04d | -9.3977 | -60.530602 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab636795-d915-3572-9b98-c2dd7529aa07 | -6.142 | -57.920502 | 2025-08-16 00:47:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a7516b-d897-3d49-bdf3-d86279200445 | -7.672 | -63.2906 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc9f24dd-0643-3be0-874b-3fc331486f43 | -6.6325 | -59.990601 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3c1f406-2535-3c93-bc1d-bf788912fdd9 | -7.4533 | -59.9384 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 299b407f-36f4-3852-b24d-796660996483 | -7.0987 | -59.212898 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c92e818a-687c-3b9f-a023-70af7789a411 | -9.2186 | -59.650501 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 726c001e-3642-3fae-9c4d-02d28086b6bf | -14.9379 | -54.701801 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc54ae64-b672-3b51-b2e0-a64b8729de95 | -7.9249 | -61.7383 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d2d3687-7f06-3ea3-8185-b30375af0aa8 | -6.935 | -59.6366 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac73f54-7e77-30cb-b110-2eb77eabaa09 | -24.921499 | -52.354099 | 2025-08-16 00:47:00 | METOP-B | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae2928ff-47d3-3800-bfe7-00213160fbff | -9.0365 | -67.3759 | 2025-08-16 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42ded923-de20-36d5-aecf-33a4a7a11eab | -3.8124 | -47.734699 | 2025-08-16 00:47:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986ee5c6-6a28-3807-84a8-d0f156f9211f | -22.124001 | -51.454899 | 2025-08-16 00:47:00 | METOP-B | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 96170da9-1b00-3553-b9c2-3e8169d58dac | -9.2169 | -59.642799 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff3ef266-1b67-349d-a06a-9256538fd2f8 | -17.611601 | -46.694901 | 2025-08-16 00:47:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d9bf4423-92b5-31d1-a6ec-8ec3fd6f5098 | -14.9802 | -54.707001 | 2025-08-16 00:47:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d7fe0e0-de79-373f-8150-1b70b99e7e14 | -8.5649 | -63.903099 | 2025-08-16 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8331131e-39ac-3f51-9a55-dc0119b56134 | -9.171 | -59.620499 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc7de01-58f0-3204-b51f-425d61464e4b | -6.9366 | -59.643902 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| deadcf28-39c7-3239-9f97-860bb8cd8a98 | -14.9688 | -54.702099 | 2025-08-16 00:47:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 240828b9-80e2-3a40-9a70-0d84bc3bd94f | -8.8966 | -60.727001 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2ee7818-e971-386a-99d7-3bd6933d26c0 | -6.4885 | -62.916302 | 2025-08-16 00:47:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c195154-59ec-34d4-a0ef-e168a3f90edc | -6.8008 | -59.820801 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98f16368-9a0c-3050-ae9e-2ad6f1ab9ae5 | -9.1694 | -59.6129 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42a59795-391a-300d-9941-fe9a0c5ed7b1 | -12.5975 | -46.907299 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3857cbe4-707d-3f65-b6f7-ab8ca3675c1c | -16.2363 | -51.112099 | 2025-08-16 00:47:00 | METOP-B | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b187b39-bbae-3162-837d-3570a8545ab5 | -14.9492 | -54.706799 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6b82eb-b180-3044-9902-76cf50d36c2a | -13.1352 | -57.155701 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2946472e-ac5e-3482-936a-55a5275162fe | -9.3995 | -60.539101 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 321573eb-fe86-3c2f-b7cc-50141b83c686 | -8.1116 | -61.176102 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2323894b-9063-3cf3-9ca4-500db36df240 | -7.8231 | -61.311798 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc646584-5520-3082-8ce1-22613a9a4f6e | -7.6842 | -63.300201 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89451a15-167e-38c0-9ce3-bdec0e6129a7 | -9.5208 | -60.5308 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 994b325a-ac9e-347c-9580-1180a5441997 | -18.033501 | -47.705002 | 2025-08-16 00:47:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b21e205-6460-3864-a1ec-5cb4e352af37 | -14.9508 | -54.714001 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1456b3-5681-33ba-9b70-a4c6d1b0d48e | -14.9656 | -54.733601 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48a44482-7441-3420-be73-bd3af7f38f6f | -14.9558 | -54.735901 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfaadb0-5922-3e0b-91c1-2642e3e84865 | -7.5681 | -61.4128 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fce9d3b-dd4c-3e3b-9fb0-0c4438523e0c | -13.145 | -57.1535 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d795207-e5c7-32af-9d69-36b417ef5fbd | -7.5354 | -61.308701 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcf2aae3-05bf-3411-a620-69f5a83a7f87 | -7.6182 | -63.326199 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 760b3d25-eb45-3d8e-9495-b8e871bd9623 | -18.037399 | -47.7201 | 2025-08-16 00:47:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea0ea6d1-80a7-3123-8b11-283f5b4d7bcb | -7.0692 | -59.219299 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7c29404-8d76-3a61-a8e2-b744b56055ac | -7.4647 | -59.896198 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc937206-30dd-384e-9409-d14893f62814 | -9.1875 | -59.6492 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9420b13-f956-38c5-b27c-1312f77c370e | -8.0379 | -61.501202 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8149c23a-d77f-3fd5-971b-b85a78da368b | -16.2265 | -51.1147 | 2025-08-16 00:47:00 | METOP-B | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3772545-a702-3498-8a6f-95e4bd5afa88 | -10.0562 | -59.1096 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff0bcd4-21a2-37ee-a655-79cd5995c456 | -12.5604 | -46.962399 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c96b6490-59ea-318f-880a-9b5437c328ff | -3.383 | -52.707401 | 2025-08-16 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5853c1-ecb7-3a55-88ee-919f30a79b83 | -7.8782 | -61.807499 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc6ca96-e6ff-3169-89f0-bae836b07d94 | -11.347 | -55.416599 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fde6d088-73be-3e3c-ba22-0320fc5993c8 | -9.5012 | -60.535 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 027d0677-714b-31e6-aca6-e1c42e7b6054 | -23.990101 | -53.1371 | 2025-08-16 00:47:00 | METOP-B | MARILUZ | PARANÁ | Brasil | 4115101 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 943a7c89-27df-384c-a624-b1f165de6110 | -14.9597 | -56.234299 | 2025-08-16 00:47:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbb7f091-f75a-31f7-acba-09ac70f771d6 | -9.0508 | -67.397202 | 2025-08-16 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fef0bb5-27b6-3d32-bbd3-25725b0bad49 | -21.521601 | -49.127602 | 2025-08-16 00:47:00 | METOP-B | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 496ca4ee-19fb-3d74-9c94-82ebe6c16656 | -7.131 | -59.640099 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee276fcd-3e75-352d-ac92-fd4149d4a179 | -9.503 | -60.543499 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80887954-287b-31d0-9853-e39b15d09025 | -7.9457 | -63.185001 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2da10b76-e80f-3047-a227-90f053fa07c6 | -9.1596 | -59.615002 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fabe2761-1fb3-3a90-85cd-5e7d703588ab | -11.3454 | -55.409302 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
