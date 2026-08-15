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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41440a15-ae24-3db6-a555-a5b9549f7b41 | -13.47566 | -44.04081 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 618a29d6-56ac-37ab-b1f6-4d701476696e | -14.3073 | -53.07077 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f5c25e9-1d64-3f1b-ad7a-a3fc08f6cd62 | -11.48932 | -54.61359 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 677ca0f7-0996-39dc-a72d-0c956f72515a | -15.03923 | -52.69482 | 2026-08-15 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69090230-206e-3b60-8e48-305038b05654 | -14.42839 | -51.91925 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f02a8e31-13cb-3b5e-a82b-3538141671c0 | -14.45399 | -45.67675 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98f0f7d5-9280-374f-949d-0e9465dfb097 | -14.46631 | -45.68176 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d1791cd-45c2-3cd3-bdb0-66bf37ca8758 | -14.44362 | -51.92151 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fd6483f-0ab7-35e3-b8d1-f517af6b7217 | -14.09002 | -54.52188 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65d80bcf-b7db-3691-897c-3783c9ad67bd | -14.44405 | -51.91347 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3bfa138-edc5-30e3-9cb8-f53233dc6d19 | -14.08211 | -53.67635 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ba35e4-0b00-3f20-8ffc-826f117b19b7 | -14.44049 | -51.91616 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2313d80-d1fb-3a88-917f-ff9a63c8ca5e | -11.47879 | -54.61557 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0647a66-8b91-3eac-bb29-48350542d467 | -14.40399 | -48.95115 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98903a9d-3ad1-34e8-9bfd-ddd86dc5af90 | -14.44565 | -51.90713 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 363cbc77-f7ec-3d7c-acb5-2c8a3206b96f | -14.43896 | -51.9225 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddd07b70-03e7-3241-a631-2019d928ec41 | -12.35292 | -51.21246 | 2026-08-15 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dbd61a1-23dc-37c9-b98f-6d32d58ba475 | -13.75526 | -53.4182 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf106e4e-7436-352d-a5a5-1dbbfb1e1bbc | -15.04352 | -52.69097 | 2026-08-15 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e2291cd-b378-3248-9769-f8802b724f1b | -14.30847 | -53.06252 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c4c151f-9ed6-36b2-b585-7c566dc1020a | -12.70332 | -48.44806 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc27602b-c5bd-36bd-8169-b274d28104b7 | -14.09667 | -53.62598 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 613b8c87-06a0-340a-acd0-59a1e7e7f44e | -14.96657 | -46.62989 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9c1158f-d4d5-35ce-9fc9-6bf443e3e9fc | -14.45038 | -51.9242 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ba84e24-1bda-3a2e-a268-4c79ba4ff004 | -15.15212 | -50.0668 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7da072f1-b778-35ff-81f5-e6396291edf0 | -14.9611 | -46.62956 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acbed16d-85ca-31e0-89db-9f8242d74f50 | -13.54185 | -46.25541 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f006bc6-795a-3200-91fa-16948004b29a | -13.4333 | -57.05095 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68e7fe40-9dde-3506-854f-134ad2fae791 | -11.48103 | -54.6232 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38772fd8-411b-3fe8-8d18-2804f65cd6cf | -11.49822 | -54.62226 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b1d447c-ba62-3b81-97c2-6e3af84a143c | -11.58997 | -54.68808 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fa145cb-ed5c-398b-8e59-1948a2053e53 | -14.45259 | -45.68903 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be7ecba1-02ce-3ce8-a024-b4c2957bbf0c | -13.42383 | -57.04567 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae9efe1c-dbde-3fff-a7b6-38765ea5155d | -13.80864 | -53.81901 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f11dd62b-2428-3626-b173-97324a2f6acd | -11.23289 | -54.82344 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8be54cc8-c8b2-382c-a37f-8aef5865e047 | -12.69284 | -48.45586 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e57bd720-523a-3628-891d-8e2ec92125be | -14.45972 | -45.67749 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a75b491-9f02-32c7-b51e-ef12e71e5fe4 | -14.42277 | -51.90374 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78924ac3-4dfb-3b25-be98-4059cd33ab33 | -13.8109 | -53.80367 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ef6ac39-0114-3954-8cdf-3b07e0befac4 | -13.76053 | -53.43114 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bc97ecb-2c33-3464-89dd-d0d5af48c9fc | -11.21298 | -54.8203 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63320120-3826-36e7-a0cd-9d0fe00ca2fc | -12.14172 | -47.16187 | 2026-08-15 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c93fb04-3212-369e-93a1-9a7570e209f3 | -11.5899 | -54.66626 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 674bdbf0-1c79-3130-906d-c3e748a71dbf | -13.4266 | -57.04985 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f570805b-840b-385b-bbb5-9724d58dd985 | -12.69749 | -48.45654 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4754a471-8142-39cc-800c-7d08d651d40b | -13.23436 | -54.1708 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6602afb0-74d4-32fc-90e2-b322c574209f | -14.75067 | -48.24819 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 628a3aca-1222-3a6e-84c2-71e86e1abb85 | -11.50325 | -54.63396 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b485c6df-6c96-32ab-b701-170d710e3aa0 | -14.43447 | -45.69498 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50fda1cd-493c-36f1-8809-d5aa17e50ea2 | -13.23269 | -54.18195 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35bf733d-df5e-3937-a1fa-9e59b90e2916 | -13.80913 | -53.79176 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 904c2ac9-63c1-3260-ac25-b27c7fd5fd33 | -9.71323 | -69.06638 | 2026-08-15 04:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3726c129-b8ca-3bbd-bab9-034833c82844 | -14.45259 | -51.91304 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47695e7a-67e8-3c1d-bb4a-092f56beb203 | -13.47366 | -51.81347 | 2026-08-15 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d757f39f-6bcd-3719-b37c-804caf725306 | -11.49156 | -54.62122 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58389e63-78af-319e-93e1-b82c0d57dd70 | -14.72461 | -52.88583 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a225b864-bad8-3e3c-be12-36fc39fed402 | -11.50651 | -54.61264 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51aa2ea1-1101-3628-9e70-7973bc97de56 | -13.54223 | -46.25206 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1478aded-ea88-365b-a5a4-d012cf724fa0 | -14.43086 | -51.92939 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c261205e-b9a3-35f4-9570-8c669af4a23d | -14.92713 | -46.63773 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25f2b99e-dd87-3140-bc3f-33e5d91e305f | -14.43421 | -51.90544 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ebae174f-e38b-3e40-8303-7151b90d2f82 | -14.44088 | -51.9081 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4a7a0dd6-141b-384a-82ca-65acf672c3ac | -11.99713 | -53.44911 | 2026-08-15 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f724d293-fe21-3586-81c7-167b8daae550 | -14.45124 | -51.92264 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81dacc44-3de8-327b-a8d9-c23b6ec35567 | -14.49435 | -52.028 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7c862fe-2113-388a-8da9-09f50510e8f6 | -14.4183 | -51.90798 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 681aa32a-4860-3b1e-a9c5-bdb3ef3a741c | -13.81662 | -53.7888 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd85e660-23d6-3491-b971-30a76d18da88 | -13.25982 | -54.19314 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3489bbd-8d7f-30e0-9b86-cf70412f5e7a | -13.47813 | -44.04146 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 46351cb5-2c1d-32ad-8198-915c2c1e2715 | -14.458 | -51.92532 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efb3e2d0-7617-347b-88aa-6ba7fda1e42c | -13.24174 | -54.191 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c6128b9-f207-3b9e-8b89-7af36e32e5fc | -14.91736 | -46.62656 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd2607a2-ccb9-39fa-b864-3ee604f86162 | -11.59268 | -54.67034 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10ee944f-53c7-35a4-80b1-1948b71f3a07 | -12.37791 | -46.42282 | 2026-08-15 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f28e2b6-182c-3f44-9bde-af0a0c68a215 | -14.44657 | -51.92363 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e64e2c52-a9f4-3629-897e-d5295bee604a | -11.20912 | -54.8233 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc81953a-0ff8-30f4-8b56-aaeeb2dfd195 | -13.91432 | -53.95674 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c440c725-d68c-36b9-8c03-a216fbc07456 | -13.23041 | -54.17397 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d00b4663-f765-36f9-92e1-47e35455b221 | -12.14638 | -47.16555 | 2026-08-15 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68fc5a2d-1e56-32b4-8a13-7aade6f09c88 | -13.42937 | -57.05403 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4dd4107-a595-3b72-a83c-67311afd8b47 | -14.44217 | -51.89847 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70f498f2-a7b5-3271-884e-28177c5ff7da | -15.65175 | -48.20549 | 2026-08-15 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd65f97f-f446-3963-add5-bcb552440e02 | -14.07863 | -53.67585 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 255ad231-0609-3193-99a4-978deff7a334 | -13.23664 | -54.17878 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50b3875f-0a9b-334c-ad4d-5549db1e0abc | -14.43332 | -51.93951 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa7df704-8663-3274-a4d8-d6eceb008346 | -13.42602 | -57.05348 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6da380f-e1e1-3678-ad5d-94d121bbae37 | -14.30852 | -53.08799 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 029bffbe-7be6-3d76-b45f-95d35e45836d | -13.808 | -53.79942 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9772c358-8139-3be9-97c1-d44708ab4db5 | -14.10173 | -53.62626 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7caa063e-6663-3ca3-8d38-77e5a2ff3e53 | -14.9268 | -46.6406 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 693a849e-22ea-3c8f-9fab-65f571771a8b | -13.91718 | -53.96113 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6187ef6b-02a3-3fdd-bc96-e6a75bb1eb12 | -14.4481 | -51.91728 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95e87e80-746f-379c-8949-63700d5dbc53 | -13.69738 | -46.26459 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 173a859c-3712-38d1-bcee-79bbc375b860 | -13.68715 | -46.25695 | 2026-08-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9ba8c30-de57-3a50-96b6-3de6810b6bb5 | -14.10773 | -53.70802 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a621160-13dd-394b-9676-21d95608a842 | -14.7216 | -52.88095 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f71fe3b-3b00-3e37-82ff-ca50b0ca6b8e | -14.32279 | -53.06466 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54dd56fe-32ed-374a-a8da-27471401f46d | -14.07519 | -53.60254 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a847d906-4ff4-3799-b954-3995b16e834b | -14.4378 | -51.93529 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a50b148e-0866-3bd3-8d89-f9daff2e6a38 | -15.17036 | -50.06191 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README32.md)
