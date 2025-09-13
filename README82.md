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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6b03bd4-e71f-3274-9701-d8d3068d2a9e | -15.24331 | -51.39468 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 23db1947-5b10-32d9-9ca5-f058d6891150 | -10.77627 | -50.52386 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 296b2b56-1c1b-3c58-bd26-186de6328dbb | -14.47002 | -55.95636 | 2025-09-13 04:59:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d6d0ed2d-bd56-31a1-9e55-84aed6ad8e94 | -10.27088 | -57.80007 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b58f1dc-8d00-37be-90ce-02c95445c943 | -11.44093 | -43.56572 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c11866c5-0bb8-38cb-addc-a8762da995a3 | -10.5298 | -49.87247 | 2025-09-13 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e747801a-1a1d-3dbb-b7a9-333bef5f2616 | -15.6698 | -54.3517 | 2025-09-13 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9756e772-c24b-34b1-8e6a-a4b16e854294 | -15.81931 | -52.21595 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70e76fce-c082-31a7-adc8-6c14447bfd6c | -9.96249 | -64.96381 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87632175-828a-3096-9ff3-d8f168d50dc5 | -11.86899 | -50.58271 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f0ead7d-7d70-3572-8c18-f6ed1c92bf30 | -10.86212 | -55.70987 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5f1dc29-4ac1-37d5-9f12-c9521a942ef7 | -15.07262 | -52.47615 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e52574ab-7a2e-305b-8f93-e47fa848c228 | -14.20304 | -46.28117 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3a5a1be6-33b2-3a1e-88eb-041a9e8cb9ef | -11.57858 | -50.57356 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2100bd09-8401-3019-80df-0b42d933121f | -15.54699 | -54.80105 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ea1f9b-868c-3022-b7d0-a2e7bea8b6d5 | -11.78067 | -64.94144 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7734595-9b6b-331a-b89f-e73527bc87ee | -11.14466 | -50.69817 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 19c55d62-92f3-33d7-bb4f-80506d13bf6e | -11.21937 | -54.99021 | 2025-09-13 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6102b7e-a7f8-38e5-b62d-25929f92e6db | -15.16553 | -50.14546 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0af4a31b-b217-34ee-94bd-ae54e683ac3d | -11.8747 | -62.77017 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f681aa1c-7d7d-3af7-aa39-8a87bcc69935 | -15.06033 | -47.99318 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c518cae1-1fac-34c6-80de-62d2f313d90e | -12.40219 | -43.82302 | 2025-09-13 04:59:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c6c4251-377a-3f46-b4cc-18a1debe667e | -11.86547 | -50.57859 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bca47e63-f11f-3b94-a194-81dab8c3df5b | -12.26798 | -53.90529 | 2025-09-13 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2af85c93-b49c-360d-bcfa-f3fb94f89c23 | -13.01054 | -44.11711 | 2025-09-13 04:59:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 228bf371-9f53-320f-be5d-4d5899b38c31 | -13.4039 | -46.80174 | 2025-09-13 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c0c5357-df52-3ae8-a984-4e868d5d8530 | -15.59458 | -54.76933 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f80a3a69-e1ca-364a-aa0b-4e69f46179ec | -14.21378 | -46.28516 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3629fbe1-826c-31e1-b1b6-fcebdf0fc5c2 | -10.50515 | -51.5374 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfccf26a-67ef-32f0-a0e7-a16663b0a897 | -14.13047 | -45.37951 | 2025-09-13 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d22d129f-c8a3-3dfd-b8e1-fe9c62551e28 | -15.13452 | -52.49564 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a3d7b33-08c5-3d6a-9062-1d9e09aaa01c | -14.73711 | -60.22643 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e082f85-2b73-3de1-95fc-36256b14b062 | -9.70671 | -57.78746 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f83387a4-0a0f-35f4-9cb8-cc9601737d37 | -12.97564 | -54.7522 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86e0691e-2df3-32b8-9545-d43abaef7bcc | -15.59064 | -54.77246 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70dcf430-c77f-3fc9-9a52-6565956e75b6 | -15.14639 | -48.31078 | 2025-09-13 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f13ce1b7-eb3c-345a-a333-923c577c6f98 | -9.27119 | -59.40303 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d259c435-2539-3eb1-87f6-a58e9b07c8cd | -16.55276 | -49.22736 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7a2ab9-8eae-35e7-9669-75399aa2fc26 | -12.06736 | -47.61563 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95a3a25d-4d5c-3915-a792-df76f36166c9 | -9.26958 | -59.41278 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| df642027-9613-3861-b0e9-53eeb9b094b4 | -12.81284 | -47.95967 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c8eca31-63a0-3cc1-be2f-c0f4826e5c79 | -10.15253 | -64.73608 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 435470e5-c50d-397b-a265-8d3782b151de | -10.33649 | -54.3201 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c50ad7-d8f3-363a-8488-92b2d3e9c6db | -11.86146 | -50.57801 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3704fda1-17aa-3e29-bfc8-104b0056fec3 | -11.37516 | -63.36279 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a54636b5-3fc0-3435-88ce-320cf368b014 | -13.08201 | -48.26525 | 2025-09-13 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11d8fde8-28ec-34ea-9d77-f6fdbcad4f49 | -9.27551 | -59.41125 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f40575e3-fca6-3cca-be7c-7d5e4df68b80 | -15.20397 | -56.67885 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b246c97-dfa7-30eb-bfd6-fda201067d6d | -12.92994 | -54.74184 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 061f80ae-7b45-3133-9a57-bb87865ea40f | -11.18068 | -51.41842 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 3ef67757-6fc8-3bec-b563-aa9cbe09cf27 | -12.13606 | -44.82314 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70f1ff83-e844-31c2-8a59-74b626a71175 | -14.28946 | -46.0643 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ea6309b-ad2a-36d1-859e-3742ad8c222b | -10.70685 | -50.50628 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c33ee95-a78a-3a7f-bcbb-65789216f645 | -12.80902 | -47.99107 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b0a30e1-a8d9-3bcc-a415-00100ee8a9bc | -9.49667 | -55.971 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dfe2dbc1-ad6b-3e32-97b7-b82bb3a90732 | -14.20128 | -46.24827 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0bb5a56-20fd-3a2d-ba4b-c91859129b51 | -15.13285 | -52.4806 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 28beb49e-b566-3722-8287-6a4cdc18628e | -14.43611 | -47.33007 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39bf2d63-8613-3cec-ae63-d95a94470348 | -15.23557 | -56.3265 | 2025-09-13 04:59:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c10a8a13-b878-3e57-89d3-a2a094de5f77 | -15.11092 | -52.50129 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 734c3fad-a891-350a-a245-f0d4090ebefa | -11.84593 | -50.57212 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7da28845-f333-3d75-9315-165be6a0babc | -9.23249 | -57.07487 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8b7c684-1ecb-3a8c-9529-e2ae401a61fb | -12.9896 | -54.77287 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e42a6404-dd2d-339a-bbde-1effbd5d5d38 | -11.09636 | -51.4436 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 933b644e-9668-373c-b456-72abe807c40d | -11.81387 | -50.55378 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8d026ab5-e014-38a7-af04-10a7eae9fcb1 | -11.78376 | -51.5031 | 2025-09-13 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36361437-752a-3c4e-86f6-b9b84e61d7b0 | -15.55714 | -54.80262 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74b9d55d-ed66-3c28-9a95-0a67af6fc04d | -16.40797 | -49.04419 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a585a6b-8c7b-329d-8af4-555f8639a8d7 | -11.18326 | -55.09217 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10dea1c2-d26c-3451-861c-b2a78960f2ff | -12.11962 | -44.84832 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d536555-bd78-3e4f-acc4-80074baa7861 | -12.12746 | -47.59219 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3d89d4f-98ef-3b1a-80d5-2a901101bc64 | -11.33723 | -50.78119 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| affc85bb-5110-309e-8ef7-9d790006299f | -11.09982 | -51.96886 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86ad0868-e7e2-3916-87ec-3a25a9658915 | -15.14404 | -52.48219 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0224adeb-420f-36dc-8844-449221ba8029 | -11.43636 | -43.54917 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf4c34f-fad1-39b4-953b-694ac5ff423a | -14.19764 | -46.27924 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d8fd6ab-c270-3721-afde-5f62d7c2ec66 | -12.07967 | -44.89493 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99426e96-8b6d-3fd4-8387-8be31c05bd52 | -13.91343 | -48.28422 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6cde7d43-7ff3-347e-9281-180200f4c236 | -14.46653 | -47.33891 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ec2ab71-18d3-30ca-adaf-171a7911d03f | -10.37074 | -50.50412 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79db24d5-f78f-37b8-9a92-dfc6d62b31a7 | -15.77136 | -53.49227 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933a3a63-d8e3-35e9-9064-777801a1dc72 | -15.16393 | -50.15803 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b523134-a5b5-3b95-bbfa-674943bfe812 | -14.17272 | -46.25267 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0cee550b-2e2e-3f69-acc8-ffc854d01fa3 | -12.80707 | -47.97366 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03ee587f-d24f-3523-9561-1153b51e22a8 | -15.25661 | -53.75534 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a56055f-0a9f-3668-a91f-80f39908b53c | -13.22292 | -51.74175 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8047d253-384d-3556-9feb-95268f1eb72c | -15.59342 | -54.75367 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3da87c91-77e6-36b2-9483-fed4af8c1547 | -10.75463 | -50.50486 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5b86b367-ebdf-3678-b9a9-d93dcf9a2baa | -9.62673 | -64.17968 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07e7a2c8-1a9e-3faf-a44e-7ec5ebf98315 | -14.39095 | -60.2902 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2036ce7e-107c-3e4a-b2e1-6ee50c90c98a | -16.64983 | -44.92928 | 2025-09-13 04:59:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02f8cff6-84a7-37fb-9c8a-e20f91ce9032 | -11.99995 | -47.7574 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 63c43a72-66cf-32db-bbe7-244b48c3431c | -12.92117 | -54.79932 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d02cd48-c55f-3e02-ae31-a74a585886e6 | -12.10996 | -44.89105 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a42d91ad-b28b-3d8c-87d3-c04bee8fc4cd | -10.50958 | -51.53307 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f28c863a-4565-3a29-8120-641aa8de26e2 | -12.91331 | -54.7613 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2300872-9650-31bc-9a7e-081169ba2cc1 | -10.43247 | -50.6352 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f23da837-1ae1-347a-b4a4-5bff28bc60ad | -15.68505 | -49.89926 | 2025-09-13 04:59:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d5871a2f-e6a0-30c5-ab10-189b810a3d76 | -12.07155 | -47.62195 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea270734-954d-374a-b2d4-d42343967072 | -9.49447 | -55.96341 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README83.md)
