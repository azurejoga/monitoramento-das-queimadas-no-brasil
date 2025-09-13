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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 061f8da3-6c41-3167-af24-e2c9cfe25e68 | -11.16329 | -50.70732 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7759e07-db40-3c61-b9eb-76431de2f49c | -10.33928 | -54.32415 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11180566-c56a-3590-b3b1-9c50c7750267 | -10.51384 | -51.54482 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d55f7e42-2c31-3b56-bdfb-b87b63ada973 | -15.06602 | -47.98798 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52d3475f-79c8-3bbc-a58d-ed003a550558 | -11.58257 | -50.57414 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 12a843dc-889b-317c-bdb0-4af0d3dcedbd | -15.5515 | -54.79403 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88020755-bb87-36fb-8b2a-490050fc6ba5 | -9.91037 | -57.05686 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a012c4b-25c9-351a-b12a-3ba60cf9bf2b | -10.14843 | -64.72806 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76a27ba8-9725-3bad-bd14-0c71baf87295 | -11.84384 | -50.55735 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8bd8ba72-cfe0-37f7-9162-a93e0d60900a | -11.40752 | -50.73658 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20bea4ac-7a4b-3d36-8cf2-30e2e78fd58e | -14.46671 | -55.95583 | 2025-09-13 04:59:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97acfba7-f972-312b-936f-899dbe2775a1 | -15.13646 | -52.49409 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddd77a7f-e65d-3aae-aa7f-203ef1df11ec | -13.8854 | -48.27359 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 82cddba2-8046-39ed-913c-ba5345fbfa8a | -11.10764 | -51.44529 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4f64a6e7-33d1-310c-81ae-e81aca9b66e2 | -15.14215 | -52.48001 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 161eaa5e-c1ae-35fb-b5a9-b42f383bd409 | -13.11842 | -56.80221 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df178a14-3572-321e-896a-f77aa49b01e9 | -15.23933 | -51.39409 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1bde34f3-ef2d-3322-bb6c-8cc12b457ed4 | -13.47344 | -48.44885 | 2025-09-13 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51f676e4-e54f-300f-9a7b-887c9a587a63 | -11.39303 | -50.47134 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 22383ba2-7d2c-3723-bbc7-a6244fc0005c | -14.61963 | -46.3623 | 2025-09-13 04:59:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cd2bef5-6188-32a2-a44a-7a15a2b41dbd | -15.07821 | -48.0192 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72790190-33f6-3db8-9fd2-185268e33896 | -14.224 | -46.29384 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bffea85-6cf4-3262-b968-0ef4e51a164f | -11.09618 | -51.96827 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cc2f201-3c6b-3508-a84f-1fafe8406bd2 | -9.88442 | -58.33137 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdbcd3fd-dabe-31a1-9df1-32f2b0074f2d | -11.81036 | -50.54966 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f6f9e10-ca28-39e2-9e42-ee445a206edf | -11.13856 | -50.71284 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f153c1c3-3671-3f26-bcaa-a2233781494b | -12.92661 | -54.74131 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 243d2597-7204-3d75-8bd6-466bd74dc9ba | -12.92172 | -54.79573 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d5641a2-2acb-360a-a738-dafa1bc99d64 | -9.62734 | -64.17641 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df1f5464-4157-3e4a-9006-a7b3c25f677c | -9.27081 | -59.41547 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b2465f0-67f7-3cd5-9be6-c8bcb4cb342c | -12.10523 | -47.59293 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a0af896e-239c-3101-a097-bb74b6002290 | -11.17991 | -55.07013 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7acaf7-508a-34f4-924b-5157bad6c47d | -15.00118 | -50.12506 | 2025-09-13 04:59:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6affa8b4-aee9-3d21-9598-452b914ff3ff | -15.81237 | -52.2098 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8420be98-3ba4-302d-a2d6-70530cfc9f5a | -9.97915 | -55.04551 | 2025-09-13 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8396b34c-1c6f-3f95-ae33-f50aa1b7de20 | -11.87541 | -50.5656 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 18f86f27-7a16-33ca-97fb-3252862c0672 | -15.41282 | -54.24286 | 2025-09-13 04:59:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de9f57a5-0b0a-3d3a-bc2a-b6351f9f5769 | -12.86457 | -62.14503 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0e18da7-7085-3edd-9c48-a020943a4517 | -12.13229 | -44.84212 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd1adfc4-315f-38bd-9c1d-019b3584bdff | -11.20572 | -48.42598 | 2025-09-13 04:59:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8880716-d7ba-3a49-b2b5-c0f5059618e0 | -11.83983 | -50.55677 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 450e3269-2fe1-3cf3-9bc3-9e7b7b81b03f | -11.63541 | -46.91832 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c88fe3a1-01b1-35be-bfbd-e0942c901582 | -13.77603 | -46.29219 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ba4e851-bffe-39fb-8574-773595fb4b8d | -14.29332 | -46.08025 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e66cb6b3-e6b6-3791-9b43-7c39a5d94c31 | -10.51074 | -51.53998 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f492962-5e49-3b63-b1dd-8bfdd8ec1b94 | -15.27372 | -51.42827 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26478dca-55f6-3c30-a474-27e77bea4c4f | -14.22951 | -46.29457 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24b5a2cb-4522-3412-96c7-dd570241229f | -12.08775 | -47.57329 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a0cfd5-06ee-32b7-9b22-01a592813303 | -9.26043 | -59.39628 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c82a261b-8a22-3b1c-8561-80c076ba2da1 | -12.12595 | -44.84524 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49fff18a-8e35-3f54-aeb3-487d233449d4 | -14.16086 | -46.16021 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd73591b-1f22-3743-844d-3ce17d24cc76 | -9.27902 | -56.89758 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 806c2ffd-300f-3a94-9d9b-89274b031e54 | -13.91278 | -48.28943 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6f41bf9a-8f6a-32ea-9c54-c465ec2a20b5 | -9.26863 | -59.4051 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| d2f4b450-a00d-332b-b726-b558d7a4683d | -11.9956 | -47.76206 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e1c48d22-f45b-32d6-ad2d-83216c50b398 | -10.00248 | -59.96936 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ad41db9-e4fd-3c89-9207-4989c51c5616 | -14.17102 | -46.26732 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf608dc0-9fc0-3cf9-9b28-f754ee1c330a | -12.9358 | -47.99894 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 82e32452-b4ee-3957-949a-b0d9bd240c61 | -12.08283 | -47.57264 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b6947d9-1b57-33f2-8684-5b9cfea5d7b6 | -14.38337 | -60.2891 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8212dd96-fd9a-3883-8792-928ecbe28ee3 | -11.85283 | -49.77646 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dc67309-770b-309a-95ec-2cf9458c175b | -14.21591 | -46.26605 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 292dae76-c305-346b-aa12-a286ae9529a0 | -11.77604 | -64.9369 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b66cb70a-8d2a-39d2-8789-aef496c00a1b | -11.1838 | -55.08868 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7840ccb4-214c-3c4a-8ff1-3a82a373b2bf | -10.69527 | -48.6639 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5542d451-aef7-3bb0-bb8e-230a48e8b280 | -14.19708 | -46.28438 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b4c7fff-5a8f-395f-96e9-91b56c569e25 | -14.63368 | -52.09996 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b60e3ae1-1d7f-34b3-ae2e-4103e891b171 | -11.71418 | -46.55163 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d949e881-6b30-31f5-ab89-9b634b9c1c46 | -10.36286 | -50.50296 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2fc10b1e-660c-31d7-8cdd-6032391fc4db | -11.85891 | -50.56679 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4272c2e1-46d3-3f32-a22f-46f798218ca0 | -10.50693 | -51.55103 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ceb08ab-afe7-32f6-b7e8-a28967a370c7 | -15.59403 | -54.77302 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e465f67-9675-391f-afd1-cb729102905c | -11.85987 | -50.55971 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95c04ca5-b669-36e4-8566-8c1b600e2673 | -11.18136 | -51.41378 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 929bbb3e-4f99-3f5e-83ee-167df1009e50 | -15.70398 | -50.58143 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56ac30ca-add3-38ba-807f-fc0bbd6dcc44 | -12.96388 | -54.74349 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04eb48fb-10aa-3a2e-8b17-034d40ce4c27 | -12.11911 | -44.85292 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d134a9e6-92d3-3a7e-bea3-b68430f3d72e | -9.73748 | -65.00986 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2000939-0bcc-3164-a62a-0ffdede0f631 | -13.29258 | -51.7107 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e3f132a-4386-3c96-88fb-8f84318cc816 | -9.97861 | -55.04899 | 2025-09-13 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27483604-5c2b-356a-9f37-405e5ccc2d68 | -10.4023 | -60.80859 | 2025-09-13 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 97730161-97d6-3f2b-a74e-3b39382334eb | -15.1628 | -50.13238 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c5b7858-84ac-37a7-b053-6de91bdf0bb4 | -14.2167 | -46.26025 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4c72bfd-99a5-337e-a8f6-ee67d1aa3971 | -12.25609 | -59.34968 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31fa1867-db90-39bf-8c56-be74dc6272f7 | -15.68444 | -49.90406 | 2025-09-13 04:59:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 218b75d4-67c7-39dd-bc3e-ed7a284d517c | -11.41075 | -50.74227 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 4534c9e4-f1c5-325e-affc-40314392c72b | -9.25577 | -59.40044 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc88e25-6d6e-3e19-8151-5ab842290846 | -9.74231 | -65.01465 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e85e27b5-5c21-352e-afa2-ea6bd157380e | -14.39083 | -60.31318 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ace30515-8a3d-31f9-b3d9-8f207acfea29 | -16.28878 | -45.68615 | 2025-09-13 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b3efd26-645a-340f-94de-4d659214c601 | -14.44018 | -47.34008 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55d52a60-0021-35a2-8f5c-31f9ddb04cd8 | -15.5771 | -54.77033 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1173b961-bc0a-38cf-8146-8e9b9a6da61d | -14.1923 | -46.27704 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f59da2db-5f03-30c8-a86b-9f18822d21ca | -14.18151 | -46.27347 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| ffe78f65-c817-34ef-999c-04f97c2a7fb2 | -12.12692 | -44.83669 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a8b24ed-aa12-38f7-b372-7cabf8af8760 | -9.26225 | -59.41903 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f98d1bb4-b83a-32f5-8ec6-a92ee7fc67a6 | -11.85186 | -50.55853 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be6abdcb-07fe-3bcc-bfd7-4364be52ab5e | -13.58437 | -44.89183 | 2025-09-13 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46cf4454-a576-332a-8f44-409b60f62a04 | -11.09681 | -51.96397 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c90954c-66ed-3e45-a380-988aea1b0826 | -10.6527 | -48.97024 | 2025-09-13 04:59:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README94.md)
