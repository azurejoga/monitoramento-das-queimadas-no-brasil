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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c13a3318-f434-3686-bbf5-f95976b196d1 | -11.57252 | -54.57402 | 2026-04-15 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7aded7d8-f785-32ff-8f87-1b96e6c154e9 | -11.93327 | -58.06758 | 2026-04-15 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2831037f-17ab-3723-bab3-4138e8375c3c | -11.43083 | -55.09803 | 2026-04-15 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21a023e6-17c8-35d1-8e93-08278a54275e | -11.9366 | -58.06812 | 2026-04-15 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d65dd11-dd1a-37dd-a8c7-f386b1d227e8 | -11.20542 | -56.87984 | 2026-04-15 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f495eb66-4097-337b-81cd-3989a2e66c50 | -12.29182 | -57.39313 | 2026-04-15 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c17d8fb-d6ec-3697-bdef-48da51c21a9d | -11.43147 | -55.09366 | 2026-04-15 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 581e201c-8727-3111-ba42-739a14a98cb3 | -12.99542 | -54.68066 | 2026-04-15 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4be1bad-4255-3e8c-bcc4-26060740d55d | -11.92549 | -58.07362 | 2026-04-15 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bde5e15-e11e-37ad-99f5-df808591b2dd | -11.20202 | -56.87929 | 2026-04-15 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5f244dd-77e6-3568-b8f1-2ab92f890499 | -21.69922 | -56.31116 | 2026-04-15 05:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 873ddb3f-7423-3fe3-8a21-e94aa3db2de3 | -16.59147 | -58.21505 | 2026-04-15 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f775c577-8bc9-3989-b0bd-496ceaacaf67 | -20.22679 | -46.47791 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 07347a9f-ceb5-30e8-8eca-51b28fb2a4ba | -20.1851 | -46.59949 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cb93519-4621-343e-a894-058fe8b134ee | -20.22451 | -46.46527 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 74b12e94-ba91-3f50-9f8e-084aad4a980d | -20.22732 | -46.47087 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b5a4bf85-6553-303f-883b-7f32cee0a27f | -16.5943 | -58.2194 | 2026-04-15 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2eaa3dd4-d087-3904-9730-b0ee33faf9ea | -21.88754 | -56.26641 | 2026-04-15 05:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afb18c95-7087-3f93-b93a-807b2de0d4fa | -22.8778 | -48.64674 | 2026-04-15 05:23:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73d67edf-24e3-3400-8c32-ef485be4aa5d | -20.22392 | -46.4724 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6136afdc-d0b8-38c7-9db8-b671732f4a13 | -21.8836 | -56.26587 | 2026-04-15 05:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4221882-7919-31d0-aa0f-49cad7886b9d | -18.50854 | -55.523 | 2026-04-15 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cd4faf1b-0ee8-336c-943c-884a8467292e | -21.6953 | -56.3106 | 2026-04-15 05:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 595a561b-602e-360f-9f3f-bb0058e3a64f | -16.25099 | -60.03249 | 2026-04-15 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f4d2bc1-31b1-3685-9fc5-503565fac60f | -20.17178 | -46.58879 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4968dc5-2868-3c83-9c63-07974441bbff | -16.59487 | -58.21561 | 2026-04-15 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 24f7b51b-1637-3ca6-9e40-91db715e89ce | -20.32438 | -55.00505 | 2026-04-15 05:23:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f1d6256-c73d-35ee-928c-c1976dd50c4f | -20.53861 | -49.49807 | 2026-04-15 05:23:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69fad9c0-cf8c-3d90-9544-d94d48363cff | -20.18722 | -46.57325 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 239451f5-7f56-33c0-ab7d-5fd2191cf61a | -18.50817 | -55.51995 | 2026-04-15 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 76e25472-f9ba-3073-9fd4-f3ca8fc96f7f | -16.59089 | -58.21884 | 2026-04-15 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cbc6d91b-2c1c-3706-a03e-fb31962e8e0e | -18.7307 | -49.7935 | 2026-04-15 05:23:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1f382af-87ac-3ea1-99a6-20921e667556 | -18.51211 | -55.52052 | 2026-04-15 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8ca597f3-9456-3758-8af3-c6784a6911ca | -20.23166 | -46.46519 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfb743c9-52e6-350d-921d-86934de2dbfc | -20.53816 | -49.50281 | 2026-04-15 05:23:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40c650e6-d3e7-3290-8ea2-2e0b61a8cb55 | -20.32487 | -55.00102 | 2026-04-15 05:23:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 096d19d3-1334-3708-a07f-0e8d4db35bb0 | -20.32856 | -55.00555 | 2026-04-15 05:23:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc0c94df-dc66-352f-bcfe-ec9b0d10905c | -18.50461 | -55.52243 | 2026-04-15 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c56011b5-ac90-3c0e-a06b-f13aca52604e | -20.18561 | -46.59314 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e32ac084-2321-3ff1-a3e7-885a13717bff | -20.22785 | -46.46381 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 68c569fa-6f7e-37fc-ae3e-c893a7eac68f | -20.53906 | -49.49329 | 2026-04-15 05:23:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d6e497b-af6a-395e-9e36-10a29b4f07df | -20.4654 | -54.68961 | 2026-04-15 05:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e19d1187-4cef-385b-845f-d5eb96b5f899 | -20.23107 | -46.47236 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d98f126f-d149-3b8e-b802-2c8f21f58f47 | -20.16494 | -46.58554 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a06f1805-1b06-304a-8dd0-67e3d5c24d4e | -20.18667 | -46.58008 | 2026-04-15 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac82410d-db9b-3c7a-a7eb-d0f6e7cacb71 | -20.46115 | -54.68899 | 2026-04-15 05:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 335d3aca-dc89-3465-bfd3-3c954da2aa3b | -18.50926 | -55.51778 | 2026-04-15 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3805fad3-3208-3c35-8877-af9173b12a5a | -22.87822 | -48.64119 | 2026-04-15 05:23:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2e9776d-a68f-3624-83f4-3962f5860e01 | -25.64869 | -50.12055 | 2026-04-15 05:25:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b395e45a-aeee-3c05-a43e-668d8d115f7f | -25.65479 | -50.12056 | 2026-04-15 05:25:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5a3132b4-30dc-3ada-b1f6-4041327451b2 | -25.65328 | -50.12268 | 2026-04-15 05:25:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2fdfab7d-33a9-3887-9c50-efeddeb77fe0 | 2.9373 | -60.17432 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d414594-5437-3697-8cb0-77eb6358d1a0 | 3.23236 | -61.21775 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3025df8d-b11e-3525-8a85-a55d2dba5410 | 1.93867 | -60.37428 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16d2274f-01b1-3296-998e-903d32b55bfb | 3.23512 | -61.21379 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be9fda34-865c-3aa5-b218-e3dc1de7f422 | 2.56244 | -61.02228 | 2026-04-15 05:36:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3126c6f5-02fd-3aa2-b6e1-c9fa006005ef | 3.23951 | -61.22016 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 993ff718-a218-378e-ad60-a4e44fa80648 | 1.9043 | -61.09397 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce300fd-aad1-3549-952c-aa967c19ecbe | 2.56883 | -60.54928 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b3899795-b321-376d-84af-763999361bc7 | 1.91694 | -60.57465 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09bdffc5-c385-35a0-99c6-745f7b738708 | 3.23182 | -61.21431 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f28644cc-8b9f-3bec-8840-79e5d3f10c08 | 3.23897 | -61.21672 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bf651cb-8da9-3a1b-86a5-3599ad84dbe2 | 2.19892 | -60.80882 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56e7d4c9-c7f9-3380-8a1d-0675298a2780 | 1.88804 | -60.67344 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f69b457-3b78-3dee-868d-22cc1bb3d43c | 2.94403 | -60.17326 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abe88f4-0cb4-350d-bb49-76ebe71c6bd0 | 1.9381 | -60.3707 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38d38fe9-2b00-301b-b7b5-ccf88daa932b | 1.82841 | -60.85212 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df6bda1-bebf-3334-aedb-e3b8e4644f74 | 1.81521 | -60.44432 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 468c79ea-edb0-3ce5-b2f0-f46e96895066 | 2.38556 | -60.8937 | 2026-04-15 05:36:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbbe7b28-74e2-3f73-b58d-3996c0538c7b | 2.56549 | -60.54981 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 531fed9b-57fd-3981-9a48-6cedfba0dd2b | 3.23567 | -61.21724 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5099d676-21b4-34d8-9094-d4c80262b090 | 2.45978 | -61.31833 | 2026-04-15 05:36:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffcc2d55-9f71-34a2-b881-a56e9ed3a83b | 1.90485 | -61.09743 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c76251ae-30bc-36dc-b207-55c7fce1a2d8 | 2.93787 | -60.17791 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1505eed-8093-33ad-bf96-8b427114a195 | 2.57478 | -60.32659 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cfcdc6b-dbd9-338a-aeff-6cf805d46e8a | 3.22851 | -61.21483 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7e4cf91-6304-36ea-8377-1631d191befc | 2.94124 | -60.17738 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d258e0e3-460c-3345-8d95-1811c19b1062 | 1.48225 | -60.92113 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0fa3b47-87bd-3991-8555-1a35998a5b37 | 2.9446 | -60.17686 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02be0370-8f28-352b-ab82-b62f55221b84 | 2.01529 | -61.08723 | 2026-04-15 05:36:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3b683ef-1efe-3b2d-9fa3-f9a35b9ac7d4 | 3.17327 | -60.20376 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f506f2a-2d1d-3dcf-b8a9-368fd6a68c0c | 1.85396 | -60.64609 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6fd9511-0835-31df-ad44-004176752eb6 | 2.38501 | -60.89022 | 2026-04-15 05:36:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af2d3362-fec6-3258-8d47-c579ecdfe3d5 | 2.01197 | -61.08775 | 2026-04-15 05:36:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91404c0e-19d4-3caa-b3dd-40aec488ca76 | 2.01474 | -61.08376 | 2026-04-15 05:36:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 861f4bc5-3fc1-301b-968a-bbde783e9f45 | 2.44655 | -61.3204 | 2026-04-15 05:36:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c49892f-eb80-3ede-a702-16f446782a1f | 3.22906 | -61.21828 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d852e151-c5ce-341e-9671-6c2e206cfb75 | 2.56939 | -60.55281 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 70f28b1a-df37-3088-a26f-3cacc5c943eb | 2.23558 | -61.27624 | 2026-04-15 05:36:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ff7e787-1efb-3418-9454-9f2e27827c32 | 2.42393 | -61.34863 | 2026-04-15 05:36:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d64b896-68c8-364b-82af-bf3df2c3c2b7 | 1.85061 | -60.64661 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc783db-85b4-33bc-85f4-d65fb64f4769 | 1.81241 | -60.44843 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 473b345c-70e2-3dbc-b73a-7f82929a534b | 3.23843 | -61.21328 | 2026-04-15 05:36:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d5454a3-e197-3f7b-9f23-a70877153bd4 | 2.57421 | -60.32301 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cb88761-0ab1-336c-b2d6-3cdebbc5d0c1 | 3.17271 | -60.20019 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6e1cd71-2d05-3332-a611-058eb0dd9856 | 2.9345 | -60.17844 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 697e41fc-6e70-33ed-9211-fe0ae6f0e693 | 1.91453 | -60.45097 | 2026-04-15 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1df81f0-f2f6-3dbc-b5bb-93fc3a6aba75 | 2.94066 | -60.1738 | 2026-04-15 05:36:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bc45e3e-7d21-3eb0-b500-203bc4a7fa36 | 1.89564 | -60.86673 | 2026-04-15 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab7cc23d-f556-3bb7-a57a-90538474fdcf | -11.93292 | -58.06952 | 2026-04-15 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
