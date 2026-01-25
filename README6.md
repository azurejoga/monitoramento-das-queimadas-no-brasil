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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eb8518e-f683-3ba3-a27b-73aa2e36a20d | -17.71063 | -53.27675 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e759abb0-7489-36dc-99bb-a60b90362632 | -17.71282 | -53.28455 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0513e0e-3ff9-3aae-b3c3-bdf82af8cb73 | -19.34367 | -54.17018 | 2026-01-25 04:50:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a3f1344-2a2c-371b-ab08-6f42b02665d4 | -19.61202 | -57.27531 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8475cbe9-2154-3408-a59a-eb45f188c4e6 | -19.6433 | -57.26381 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 637171b6-ec42-3018-af02-8725ed96f1b4 | -19.6312 | -57.27024 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 7abcc176-69f9-3564-a49c-2f85ebe7f178 | -17.71338 | -53.28093 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71979416-2ef1-3333-b59d-fb738004cabe | -19.63003 | -57.23507 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 91117550-7b9d-3587-aabf-a9a23c8b67b8 | -19.6256 | -57.26041 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 461c8431-beec-33bb-b104-6a29ff34a7cc | -19.63828 | -57.2716 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 2f1a9f93-c192-3929-9ded-ebe913688abc | -19.29927 | -53.1754 | 2026-01-25 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51254177-173a-3daf-86fb-790182d9060f | -19.64462 | -57.27719 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 14d2e010-d621-373a-8f57-34e613f26db8 | -17.70621 | -53.28343 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79ecbf18-9c5c-3612-800c-f2730c916a95 | -19.61407 | -57.28447 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 28542647-9dde-3f29-9045-28b038f088fe | -19.64536 | -57.27296 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f9ba4c4e-8944-307b-885b-05e9e6bc9b22 | -19.61276 | -57.27108 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 480710fe-b6f8-3402-8b50-2858b44d9122 | -19.61704 | -57.26752 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0a14f7e8-5b11-3987-a0d0-6a30a6c4fbb7 | -20.32346 | -57.82943 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 047f6b3f-8f3e-3beb-bdb8-a3192a63d2e4 | -19.6135 | -57.26684 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ad6df873-0a3f-32ad-bca7-4782046dcf95 | -19.6191 | -57.27666 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 601db8bc-d599-3dc7-8e21-60ccc24f32fc | -20.33426 | -57.83155 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a26e14f5-9668-3709-a5f0-6670655380e6 | -19.62914 | -57.26109 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 682c0bf3-aad8-3783-befa-a50449f344a7 | -19.62486 | -57.26464 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd305e85-7ec7-3d88-9872-12ed4e652f5a | -16.02739 | -59.90976 | 2026-01-25 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46adc8a9-4688-33c7-9274-3356ae976cc7 | -19.61499 | -57.25838 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d9d5e22c-269d-38de-b62b-9ebc7c488330 | -19.6628 | -56.85996 | 2026-01-25 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 471a01dc-f0b1-3b48-abea-dc3486ba521e | -19.64476 | -57.25536 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3063ecaa-7d16-360d-bba9-73e53d4d8de7 | -19.60979 | -57.28803 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d924e0b7-b517-3064-bb6d-23dc9ba0de2b | -19.62247 | -57.29923 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aa7adb07-63e1-3a29-bdd7-303cdcb155f3 | -19.63976 | -57.26313 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 28de026d-5de5-3d56-b191-d25e3310fd51 | -17.71007 | -53.28037 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c3a496d-3b51-3e3c-9e1b-15c4225bbee9 | -18.81933 | -51.60106 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9a2b280-29c7-347a-86af-0fae17da5376 | -19.63268 | -57.26177 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e6aa9117-303f-3475-93db-47f2bc0d815b | -19.64816 | -57.27787 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f6a77bb-ea85-3d45-b78f-b6530954e8dc | -20.57415 | -55.56547 | 2026-01-25 04:50:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99ac9cb3-3b2f-3bb9-8b93-4c130d9c8ec5 | -16.22064 | -57.52569 | 2026-01-25 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9a7cf7f9-ba1f-3f16-95e2-03d9aa76880d | -19.6303 | -57.29634 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 53761165-10f4-3e26-b4e2-e26993237494 | -19.62264 | -57.27734 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 647c7098-6de5-336b-a709-5e9a4b24db24 | -19.63474 | -57.27092 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 66a90d3e-4b34-3e56-8c35-050d56c147c4 | -19.62412 | -57.26888 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| b138ec63-f5eb-3510-838b-10720c496e50 | -19.62618 | -57.27803 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| de39e937-44e7-3ee6-aab0-7af8d7c28788 | -19.60699 | -57.28311 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fd58cf4f-ad91-3bce-8632-575146cdaaac | -19.64903 | -57.25181 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c50d4fda-fba9-3e65-afbf-8983bcabdd02 | -19.64315 | -57.28566 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7a56f988-1226-3e36-9cf4-c00518e7bece | -19.62132 | -57.26396 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5a63dcc6-cc15-31c0-b9c7-c436b2d13b3b | -21.35575 | -56.87054 | 2026-01-25 04:50:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f7834ba-0e96-3dbe-a3f0-a9cb18afc47d | -19.65391 | -57.26585 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f31b0979-8730-3467-b9e1-f410e8c2b4ba | -19.60568 | -57.26971 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 99409c97-0561-308f-9c2e-f86dbfc99afe | -19.65855 | -57.19701 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 479ba84c-b483-3f16-a668-4c86ebb1e695 | -21.07286 | -49.53535 | 2026-01-25 04:50:00 | NOAA-21 | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bd9d1455-3fb4-3751-b2aa-484ed42648eb | -19.67131 | -57.18643 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e13087e6-5b53-3782-ad02-7b4fb0fe69ca | -20.33786 | -57.83226 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4d8f2a12-ba93-37ed-8418-4d8447ee3bfc | -19.64431 | -57.21602 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b6e408f9-bfeb-3f1b-88d6-dcc19de994e9 | -20.34146 | -57.83297 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6225f7e1-c919-37d1-84ce-0f96751e6a4f | -19.61425 | -57.2626 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 56318c8e-1adb-30ea-bea0-5dbdb660245e | -19.68261 | -57.18426 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0972b606-e767-38b5-ae45-803b3e9bf662 | -27.13547 | -51.13363 | 2026-01-25 04:53:00 | NOAA-21 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ca2056cf-57ab-3a77-9455-1dcf66e5b8e1 | -23.74496 | -54.93158 | 2026-01-25 04:53:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3fd366a0-58a5-3450-bb77-6c63aa948fc2 | -22.55079 | -55.64301 | 2026-01-25 04:53:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a13b5c1-9b17-3e91-9850-5aca5909dee4 | -25.22243 | -49.66488 | 2026-01-25 04:53:00 | NOAA-21 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4637db01-03a9-3c79-a108-f9e815640ea8 | -23.21477 | -51.68525 | 2026-01-25 04:53:00 | NOAA-21 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b7a83b87-07a5-36a0-9605-7f02b8b3b544 | -23.5358 | -55.50719 | 2026-01-25 04:53:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f198375-9a7e-3bf5-9c80-164b00eeb7a7 | -27.13556 | -51.13263 | 2026-01-25 04:53:00 | NOAA-21 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6c70cd7c-fd0d-3755-9836-1fe9c5c67693 | -23.46845 | -48.9007 | 2026-01-25 04:53:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ad9eb37-f546-377f-90f5-15c23bd132a0 | -29.88776 | -50.30387 | 2026-01-25 04:53:00 | NOAA-21 | OSÓRIO | RIO GRANDE DO SUL | Brasil | 4313508 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e28bd2f-b0a8-3080-8e30-fe28c65837da | -26.02881 | -52.69455 | 2026-01-25 04:53:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 2277de64-5e66-30a2-a4d1-f4ad9475beb0 | -26.02942 | -52.69 | 2026-01-25 04:53:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9d048bb8-2eeb-353f-a854-4f3550d611cb | -26.03237 | -52.69515 | 2026-01-25 04:53:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 210a73af-85f1-31d8-86b6-ebaa60ca42c6 | -23.5391 | -55.5078 | 2026-01-25 04:53:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e6361a3-7a36-3163-b185-da0fcc0f62f4 | -23.74438 | -54.93533 | 2026-01-25 04:53:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7fe28671-4ac6-3889-9c0b-e6bf1ccea1b7 | -23.47272 | -48.90124 | 2026-01-25 04:53:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05807b96-152a-3d7a-b5e6-457ce5eb2a35 | -29.60958 | -51.3971 | 2026-01-25 04:53:00 | NOAA-21 | PARECI NOVO | RIO GRANDE DO SUL | Brasil | 4314035 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3a27769f-0b70-3f88-993c-3d4dd57cdaa5 | -27.12397 | -49.37251 | 2026-01-25 04:53:00 | NOAA-21 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1103f186-04c3-3b23-af62-72d5921bbf46 | -3.0791 | -40.1063 | 2026-01-25 05:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 20f8fadb-43b4-3477-b83a-f3e8d0707260 | -19.6357 | -57.2917 | 2026-01-25 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 3f9416a7-eb0e-3080-9125-ea987347963c | -19.616 | -57.2735 | 2026-01-25 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.3 |
| 1fd2b8bc-d8df-3aa9-b754-c416af8fe4b5 | -19.6364 | -57.2499 | 2026-01-25 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 91d4dc1e-a9ed-3707-b402-254b3d0be2c1 | -19.636 | -57.2708 | 2026-01-25 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 220.4 |
| 3d7d96dd-bc4d-31b0-aadc-5233cd2c62ee | -19.6561 | -57.2681 | 2026-01-25 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 1dc176ee-4a4d-3fda-84b5-3c88b74dc12f | -19.6156 | -57.2944 | 2026-01-25 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.2 |
| 3a9fa3aa-1f09-3628-89c5-93b0e173419d | -3.0603 | -40.1072 | 2026-01-25 05:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 2a533799-92aa-3366-9567-f98a60d94306 | -19.6357 | -57.2917 | 2026-01-25 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| da580c13-a073-3e98-9f76-ebea566b785e | -19.6561 | -57.2681 | 2026-01-25 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 047bd808-9f0a-3e59-aa85-cb2de8315ee9 | -19.636 | -57.2708 | 2026-01-25 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 183.0 |
| 39298da1-4df3-30d4-933f-9ede610362d4 | -19.616 | -57.2735 | 2026-01-25 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 3630741b-0092-3ff0-875f-2ecd586edf36 | -19.64114 | -57.2928 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3623d9ff-23fe-3f9a-ac13-55586bd3341b | -19.65392 | -57.28123 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bd67685b-2afb-3ef3-b2ee-5c2292956b8e | -19.64374 | -57.22065 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0f88e6dd-d67b-334e-82af-d4a16d78b2e0 | -19.65779 | -57.20005 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 14242666-5d03-37fe-b071-ee7224b0cb56 | -19.64059 | -57.2701 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 76dbe1a3-613b-39f5-8e26-47714d01ed44 | -19.68893 | -57.19117 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 751612db-8e40-3fdb-8cd0-e6b890f78d90 | -20.33359 | -57.83306 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a776ee28-3679-3ad8-93dc-781e596a3eee | -16.44442 | -58.1629 | 2026-01-25 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 10ece721-aee0-3029-8a18-952e66f513d8 | -19.61083 | -57.27 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9b228534-758a-377f-9d81-5cf458897eb2 | -20.34432 | -57.83477 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b213351f-da03-3da3-b708-888c1c6ae91b | -18.79299 | -57.65508 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cab4967f-4cb6-3d81-8d3b-86cbd4bee8bf | -19.61448 | -57.27057 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.9 |
| 795afc65-ebc9-382e-97ed-e2abee154c72 | -19.67064 | -57.18834 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8b71642c-7f2f-3d0b-9dc1-a511e3253fde | -19.64608 | -57.25736 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 087c8707-efd1-3be7-a6a9-3605b2f02aa3 | -21.35362 | -56.87145 | 2026-01-25 05:20:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README7.md)
