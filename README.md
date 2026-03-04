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
| d0eef092-9926-36d9-9773-89a015c3a89d | 0.2825 | -60.6203 | 2026-03-04 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 116.5 |
| a38c8123-0608-3e25-bcbc-e1e0d79bdd1a | 1.5047 | -59.9116 | 2026-03-04 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d6487a8a-f9f6-373a-9359-34182ebcbd52 | 1.5229 | -59.9114 | 2026-03-04 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 169f3740-ad0a-3675-a470-d8dff19f60a9 | 0.2825 | -60.6013 | 2026-03-04 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 93081d48-aaf3-34cd-9439-9c09a3b7e2ae | 1.5047 | -59.9116 | 2026-03-04 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1c550580-1adc-3de1-b429-6d4b53d39940 | 2.2332 | -60.7397 | 2026-03-04 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 67dde56d-540e-3898-a316-1ce839996169 | 0.2825 | -60.6013 | 2026-03-04 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 63bf2c36-ed88-3528-80f4-9f0deb938c95 | 2.2332 | -60.7586 | 2026-03-04 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8d0c3909-0cd5-363c-b4bb-de474c1fbc0f | 1.5229 | -59.9114 | 2026-03-04 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9513fba4-2638-304a-801f-0110615901ad | 0.2825 | -60.6203 | 2026-03-04 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 118.6 |
| dc9a9399-053f-30cb-b6fb-15132e840a6c | 0.2825 | -60.6203 | 2026-03-04 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 9d35aabf-a596-306f-b216-213119d83056 | 0.2643 | -60.6203 | 2026-03-04 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7b768452-e1b4-3719-bc29-78e073596508 | 1.5047 | -59.9116 | 2026-03-04 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 75931e1f-9d83-3820-bbc7-879dba2772f9 | 1.5229 | -59.9114 | 2026-03-04 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d38a2161-5546-3e39-81d9-f04601a23fe4 | -24.99868 | -49.29435 | 2026-03-04 00:20:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 183c116c-1864-3b2e-b94c-0d5be922cb95 | -27.62029 | -50.45044 | 2026-03-04 00:20:00 | TERRA_M-M | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 8f21e972-4857-3de9-b0e1-25810d3df9f0 | -25.00826 | -49.293 | 2026-03-04 00:20:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 0c882ea1-ef26-3196-98b9-4d2e8c296a55 | -27.60964 | -50.45176 | 2026-03-04 00:20:00 | TERRA_M-M | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| d14f104b-6653-328e-8055-d13311b04320 | -25.0001 | -49.30609 | 2026-03-04 00:20:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| cab68b80-0244-31eb-90ce-51dd3a4ea9f2 | -25.00961 | -49.30421 | 2026-03-04 00:20:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| b0a5018f-876f-3d5d-bc4f-f5c8663c0daa | -21.31447 | -48.53339 | 2026-03-04 00:22:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 77bdb7e3-8353-38c0-9788-115563998f05 | -20.8207 | -48.27636 | 2026-03-04 00:22:00 | TERRA_M-M | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f67f9a3c-4891-35ac-b5c9-707178f85458 | -23.4495 | -48.93238 | 2026-03-04 00:22:00 | TERRA_M-M | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68f4a6f1-29e5-3df5-b25e-8928565c7561 | -23.02254 | -49.26416 | 2026-03-04 00:22:00 | TERRA_M-M | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1a31f954-42e5-3b56-9d5c-023b0f3cbafe | -20.304 | -49.58606 | 2026-03-04 00:22:00 | TERRA_M-M | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6d822a7b-5eeb-360d-ab70-30a2ec5db515 | -21.31576 | -48.54319 | 2026-03-04 00:22:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2d3177d4-188d-3310-8d24-c6491b06b3e5 | -20.82198 | -48.28588 | 2026-03-04 00:22:00 | TERRA_M-M | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e546256e-b40b-3118-bae0-1d30a5be7e16 | -23.01604 | -49.26011 | 2026-03-04 00:22:00 | TERRA_M-M | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8c691bb9-e55d-353b-aebf-a77d91d268f3 | -22.91376 | -48.60874 | 2026-03-04 00:22:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e227f2fd-28bf-3190-b767-96bce6137364 | -17.90372 | -54.14237 | 2026-03-04 00:22:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aaa63792-b5f6-3a59-ae76-9132c13256e4 | -23.0174 | -49.27078 | 2026-03-04 00:22:00 | TERRA_M-M | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 1ccb034a-450b-3ba9-8ece-79cbc25088de | -20.92016 | -48.53912 | 2026-03-04 00:22:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a1930b2-e12a-3532-b1df-7160f0667c47 | -17.90811 | -54.13615 | 2026-03-04 00:22:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 48422d49-691a-3f41-af37-14f34dbd4a68 | -21.70625 | -48.43901 | 2026-03-04 00:22:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9782ed10-dff4-3a2f-8dd1-13f4c465cebb | -15.42607 | -52.19321 | 2026-03-04 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| dadbd18e-7d21-3f02-b514-4afb3b6c8b2c | -15.42753 | -52.20525 | 2026-03-04 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4b7af210-9180-3490-aa51-e9331182c76b | -16.43968 | -52.47901 | 2026-03-04 00:24:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 53ccb2fb-d655-3855-a67f-166c8b0d23f2 | 0.4974 | -60.50362 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 40868a16-ab6a-3fa1-b83f-deffb2247b7f | 0.27175 | -60.6017 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9646d186-6476-39fd-a76e-e423aaa6392c | 0.46465 | -60.41241 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 24.9 |
| bd0cc760-5d60-3931-ac82-28e392f597d7 | 0.73387 | -59.91945 | 2026-03-04 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 26.9 |
| e32cc396-1629-36b2-a226-d758683fd7c1 | -1.2929 | -53.10656 | 2026-03-04 00:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 57be48b0-0889-353f-8218-cff781a09dcf | -2.20107 | -53.48361 | 2026-03-04 00:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4a2823aa-0cff-39ef-b7e0-94aaf8faeb25 | 0.03525 | -60.96392 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| aa3ba554-3767-369c-91b8-dd86551fac27 | 0.46873 | -60.38442 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8937b73d-4763-33b2-936e-36ad5ade1360 | -1.29164 | -53.09735 | 2026-03-04 00:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fa16564-49a4-3b47-866f-51873896cada | 0.73074 | -59.91379 | 2026-03-04 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 2175de6f-9a1c-3629-ba91-d3ea431e7e27 | 0.28022 | -60.63808 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 7564156b-331f-3cbf-b8ca-12d2cd551cec | 0.49333 | -60.53227 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a7131b85-ca4d-34ca-a35f-55b06dd2175e | 0.30908 | -60.43594 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b89b91a1-7b05-344c-a5aa-e4f74e9194ac | 0.04084 | -60.95956 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 391.7 |
| 37419dc0-3214-3042-9377-b3f271762b7f | 0.28442 | -60.60872 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 403f134b-2d86-3010-a75d-6ebfdb640f79 | 0.05094 | -60.96616 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1042.1 |
| 32f5b587-0ed2-367b-979d-11ff08d1fce3 | 0.03071 | -60.99551 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9595c466-c46e-34d3-9f68-8573818d312c | -1.29416 | -53.11576 | 2026-03-04 00:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e44a00da-17b6-3f61-b094-5c12aa91a8cc | -1.51533 | -54.52544 | 2026-03-04 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4c02dfe1-22ad-372d-87ee-8ef50585cfb3 | 0.26774 | -60.63111 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 8fee9f8d-9745-3ee4-bdf3-fca0830f570d | 0.46543 | -60.40732 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ecd71bc7-89cd-316f-a9b1-be855c0c8409 | 0.7375 | -59.89437 | 2026-03-04 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d915a72a-f4de-3f88-8bf1-e63d5ea151d5 | 0.03655 | -60.99113 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 723.2 |
| ac83c8af-1dc6-3b78-bbdf-44b50c4cdc82 | 0.30503 | -60.46436 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 39251a17-f8d9-3503-872e-c0fedaa47194 | 0.04644 | -60.99778 | 2026-03-04 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 827.0 |
| aaf84dd1-e81b-394d-917d-a0f740bb2105 | 1.50847 | -59.9242 | 2026-03-04 00:28:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 95256ed7-c43c-341b-b7b4-8b64b83d0522 | 4.1677 | -60.42374 | 2026-03-04 00:28:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| da298f46-be42-350b-a84b-b3b0af1241da | 2.22693 | -60.75727 | 2026-03-04 00:28:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ec725d24-5e97-3ec1-8875-f66be29be1a2 | 4.18559 | -60.3997 | 2026-03-04 00:28:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| ebfd6159-74a1-3e87-b399-c4272cbcca40 | 2.22762 | -60.75241 | 2026-03-04 00:28:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f7a3517e-a270-3648-9088-bc4e1f4f4c6d | 4.17138 | -60.39914 | 2026-03-04 00:28:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 34f63f61-1828-3caa-931c-0e663a514781 | 1.11258 | -59.20163 | 2026-03-04 00:28:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| eca04715-fe20-3e33-91e9-ddf55bdbdb7e | 1.51252 | -59.93174 | 2026-03-04 00:28:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| aba494b7-2836-3e14-8378-5299a491acaa | 1.0567 | -59.49064 | 2026-03-04 00:28:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 2bf044c3-e033-36a5-b716-3dff51761965 | 1.51634 | -59.90631 | 2026-03-04 00:28:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 3b7fc6ae-0baa-3f91-b5fe-b1dc38927dfd | 2.23112 | -60.72961 | 2026-03-04 00:28:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 81808675-ceee-3f17-aeaf-6d0bcc66bd68 | 1.06387 | -59.48517 | 2026-03-04 00:28:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 241a9f29-0b38-361a-b690-df00ebcf8772 | 2.92662 | -60.46693 | 2026-03-04 00:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 1f4ff076-c8bc-387b-8ba5-db324ffd9ce2 | 1.51203 | -59.89922 | 2026-03-04 00:28:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.6 |
| bb80503e-0eb9-35a7-aa96-fe6f1da7ab34 | 0.2825 | -60.6203 | 2026-03-04 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 268e0ca9-50e1-3baf-b056-3c0bba30968b | 0.2643 | -60.6203 | 2026-03-04 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b6a449ec-2b03-32a9-bc9f-0ada18b879c8 | 1.5047 | -59.9116 | 2026-03-04 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| bdb48fb1-f571-3f69-84b3-6e614ac0624f | 1.5229 | -59.9114 | 2026-03-04 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 34c778d5-c18e-38db-ae05-388723cd7e51 | 0.2825 | -60.6203 | 2026-03-04 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 6a0bbb41-c288-3089-b146-09c8f1215b0a | 0.2643 | -60.6203 | 2026-03-04 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 28edb4a0-0f0e-3ee0-9884-c4a6a07d5ac2 | 1.5047 | -59.9116 | 2026-03-04 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 7913fc6e-5bf7-3583-9641-cebb3c89fa74 | 0.2643 | -60.6203 | 2026-03-04 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7d8d7b43-0e5c-3ff2-a8b4-92f9c6ea067c | 0.2825 | -60.6203 | 2026-03-04 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 99.1 |
| ee52d6fd-4566-32e2-8ffa-c07b5b1ad4aa | 1.5047 | -59.9116 | 2026-03-04 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b443cda1-55aa-37f2-8b5c-5fc8b81bb6c5 | 1.5229 | -59.9114 | 2026-03-04 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 146ab987-4526-3eff-90f0-27d071944188 | 0.2825 | -60.6013 | 2026-03-04 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4bc66742-068f-3072-8996-27cf2fb26ea5 | 0.2825 | -60.6203 | 2026-03-04 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 99.9 |
| fccc3d01-f775-341f-8bc0-7c466245744b | 1.5047 | -59.9116 | 2026-03-04 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.5 |
| f75678f9-ff46-3a40-bbcb-835aa74ea934 | 1.5229 | -59.9114 | 2026-03-04 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9c7e3aea-5a19-3460-bacd-086368ab4b22 | 1.5047 | -59.9116 | 2026-03-04 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.2 |
| d8c7f19a-56ba-320a-bb23-24c6cdaa3bf8 | 0.2643 | -60.6203 | 2026-03-04 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 856fdd83-6a67-3001-8262-6c2fe42b6360 | 0.2825 | -60.6203 | 2026-03-04 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e5d58a79-80de-3854-9308-63946362004f | 1.5046 | -59.9306 | 2026-03-04 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b8c6134a-17a5-3d76-aad2-2299891f418c | 1.5047 | -59.9116 | 2026-03-04 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 5cd80151-27d8-338e-880b-e7ff1a549761 | 0.2825 | -60.6203 | 2026-03-04 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 60bbe06e-9d51-3d62-b9bd-50deafe457c4 | 1.5229 | -59.9114 | 2026-03-04 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ef15a7c6-3d41-3877-aaa8-123c51a50720 | 1.5229 | -59.9114 | 2026-03-04 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 468ad3e7-6a98-30c6-835f-8ef6d3ed9d4c | 1.5046 | -59.9306 | 2026-03-04 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.6 |


[Clique aqui para ver as próximas entradas](README2.md)
