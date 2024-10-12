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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8eddda4f-911d-3c1e-a471-22bfc52dc80e | -17.627 | -56.3318 | 2024-10-12 01:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 8430f435-e528-3fd5-acea-b74cb6c769c0 | -17.6467 | -56.3292 | 2024-10-12 01:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.6 |
| 4b32c04a-e21a-34bc-94ee-6ec5b11469c9 | -17.6471 | -56.3084 | 2024-10-12 01:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 031582fc-56cd-3186-b23f-e999ed9234f7 | -17.964 | -57.3843 | 2024-10-12 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 4005de1a-b322-3a88-ac03-f9b9079e1384 | -17.9643 | -57.3637 | 2024-10-12 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| af0df120-4997-35f6-9cf7-e502b6aa06d5 | -17.9837 | -57.3819 | 2024-10-12 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 802c5154-b26c-3b5d-9c0b-7e05f1b494cc | -17.9841 | -57.3612 | 2024-10-12 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| f9c586c0-d168-3906-9d9d-283433a81b89 | -18.194099 | -56.4879 | 2024-10-12 02:01:53 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b2b91a22-ea0a-3d3b-a095-e41d2350c669 | -18.202499 | -56.517101 | 2024-10-12 02:01:53 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 91b22b5a-ce85-3c3e-ba39-ff5c392cb71d | -18.1931 | -56.520199 | 2024-10-12 02:01:53 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aaae0deb-d77d-38c2-862e-fec139b99540 | -18.183599 | -56.5233 | 2024-10-12 02:01:53 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0275c0e-2196-34bc-85c0-03d1620ee2be | -17.690399 | -56.254002 | 2024-10-12 02:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a5eaa413-e124-3e29-ab5c-850c93ffcd87 | -17.699301 | -56.285 | 2024-10-12 02:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22f48d47-80fb-3c7d-80dc-fa8cf8ff9af2 | -17.6623 | -56.229 | 2024-10-12 02:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 792ceb00-60d1-3a21-817e-c2823a3c37c2 | -17.652901 | -56.231998 | 2024-10-12 02:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3f01e86-c3fb-351f-9ae1-347b21dde582 | -17.6619 | -56.2631 | 2024-10-12 02:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 841b9223-e061-347b-88e9-135b6841f150 | -17.6418 | -56.337002 | 2024-10-12 02:02:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cc7cd421-6f57-336c-a5a8-437bd832b069 | -17.6234 | -56.3092 | 2024-10-12 02:02:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6dc1a0f8-623f-33d8-97cd-7ad1c7b23073 | -17.632299 | -56.34 | 2024-10-12 02:02:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8f847ce5-3dae-375e-b33e-fce0e2dc9d2b | -17.6434 | -56.2351 | 2024-10-12 02:02:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1db2ac13-db24-3852-94fa-f1794152543c | -17.642401 | -56.3032 | 2024-10-12 02:02:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 69b10c10-14e3-36f8-9cea-3899f792451a | -17.632799 | -56.306198 | 2024-10-12 02:02:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 652d7a62-5fc3-36db-9666-518edeb3551a | -17.8729 | -57.2878 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0be6bf03-4d76-3038-a9e6-06d38190ff48 | -17.8804 | -57.314201 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3bdbfd0c-248c-3759-95ac-0f04295df900 | -17.8634 | -57.290798 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 48e5724e-e27e-3838-a7b3-32bad2c5de06 | -17.870899 | -57.3172 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9e3454bf-961e-307c-8316-ff316e936bb7 | -17.8783 | -57.343399 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5790c07c-e516-337b-80a8-fcceaef5f331 | -17.853901 | -57.2938 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 235ee414-3fab-31a6-9ef4-5b37e1cbd121 | -17.861401 | -57.320099 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 012da85c-9cf3-33fe-83dd-f66bd9b497cc | -17.868799 | -57.346401 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fd88bd56-d81c-3cca-84d7-0994b3265a0f | -17.8444 | -57.296799 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 622b540a-1fa9-3276-bb04-c9ce850dd454 | -17.8519 | -57.3232 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e7414d1-30d7-339d-998f-6d4dec92234e | -17.859301 | -57.3494 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4fd65a16-9124-3704-946e-544982146a91 | -17.834801 | -57.299801 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c67e303b-80b0-3fae-938a-110fbd31f605 | -17.8423 | -57.326099 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d870968e-30c5-3f78-9594-bdf4ee937056 | -17.849701 | -57.352402 | 2024-10-12 02:02:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 241dde38-62b1-3899-8526-dd85952d752a | -17.8253 | -57.302799 | 2024-10-12 02:02:03 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0f14bbf-b676-393b-bdd6-d9170626077d | -17.8328 | -57.329102 | 2024-10-12 02:02:03 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 399d865e-2af7-37fd-b5bc-02caf615b85e | -17.8402 | -57.3554 | 2024-10-12 02:02:03 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c933f1a1-4a4d-3ae1-a314-fee5b3b4fe2e | -17.847601 | -57.3815 | 2024-10-12 02:02:03 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b9e7c897-4fbb-3b9f-b123-350c12a9fedc | -17.8232 | -57.3321 | 2024-10-12 02:02:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce16e9f7-1959-317c-b94c-1f9368cb7493 | -17.830601 | -57.358299 | 2024-10-12 02:02:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78b460d4-f506-3698-8258-d671ea778936 | -17.837999 | -57.384499 | 2024-10-12 02:02:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2eb5e0df-02ae-35e2-852a-9e7727074286 | -16.9846 | -57.448299 | 2024-10-12 02:02:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bed1cded-5a91-3047-a6c8-488c23a9fc68 | -15.9763 | -59.084202 | 2024-10-12 02:02:40 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c821c1b-713d-38b9-ba22-a18892d051a1 | -15.6221 | -59.961899 | 2024-10-12 02:02:50 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 591f788a-0bb5-3ab5-826f-da280cdcb7f0 | -14.3146 | -57.556499 | 2024-10-12 02:03:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb56d060-e8cc-3a14-8a89-ff2972c747b9 | -14.3228 | -57.5858 | 2024-10-12 02:03:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7db33d-4fa7-30d0-948a-2f1db48bab98 | -14.3051 | -57.559299 | 2024-10-12 02:03:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acab0fb5-1231-3786-b28b-5152cf665ea0 | -14.3133 | -57.5886 | 2024-10-12 02:03:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6241dbea-7269-3ed5-bea8-c539c086e89b | -13.7643 | -60.567001 | 2024-10-12 02:03:22 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2d389ee-b4b8-3d5b-8627-1626958d40e2 | -13.7354 | -60.575001 | 2024-10-12 02:03:23 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63b90459-d0b5-3439-9dce-d2036e609d99 | -13.7403 | -60.593899 | 2024-10-12 02:03:23 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0b0f71-680c-3b01-a6d9-b4245cc5d99c | -13.7258 | -60.577702 | 2024-10-12 02:03:23 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd1fe93-a7a8-38ab-b2f2-2cdef818b152 | -13.7307 | -60.5966 | 2024-10-12 02:03:23 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd47369c-f24a-3bf6-8605-e02f830626ed | -13.721 | -60.5993 | 2024-10-12 02:03:23 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f1f2d2d-6359-307f-97a1-674c8f6ad38d | -17.84 | -57.39 | 2024-10-12 02:03:45 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e25f6d84-cc9d-38b6-a4c4-5ad8abaecae8 | -17.87 | -57.34 | 2024-10-12 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dfb150c0-93f9-3322-a80c-dc40c6a3b3da | -17.87 | -57.41 | 2024-10-12 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2e5f4c40-a192-3c11-9975-5e3df227eca5 | -17.84 | -57.31 | 2024-10-12 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 822ba3ef-a246-3e00-9955-176557cf9f2e | -12.7352 | -62.2276 | 2024-10-12 02:03:46 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 28a107bf-08de-3ca2-8942-d7a860a094a4 | -11.834 | -58.8148 | 2024-10-12 02:03:46 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 904282db-3c0a-3ce5-8600-29fa20fd68c2 | -11.8245 | -58.817501 | 2024-10-12 02:03:46 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7659ab46-bfe9-3378-a82a-0bb3bfc1fc5a | -11.8316 | -58.8442 | 2024-10-12 02:03:46 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d40fc2ee-5a77-34f4-9ac0-59f07b587b9e | -12.8417 | -62.895199 | 2024-10-12 02:03:47 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e66f5fa-e9db-36f8-bc86-06786e04afd8 | -12.473 | -62.991402 | 2024-10-12 02:03:53 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbeed0e-5668-3d99-b8dc-7bea83d43556 | -12.4764 | -63.005199 | 2024-10-12 02:03:53 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 890afae5-686b-3c17-9265-f87b5f3c947b | -12.4633 | -62.9939 | 2024-10-12 02:03:53 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 02abd6d5-ccdb-3266-ad3a-82f076f5eee0 | -11.7483 | -63.817902 | 2024-10-12 02:04:08 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18ca2368-f5c6-3fbc-ac94-fd7bcf50ad4a | -10.3859 | -61.188801 | 2024-10-12 02:04:19 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac15bf0-9121-37be-8c3b-6d335dfaaed8 | -10.3762 | -61.191399 | 2024-10-12 02:04:20 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c63ade2b-d09a-3375-884a-33bc775ed3ec | -10.3813 | -61.210999 | 2024-10-12 02:04:20 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 337b4193-092d-3536-8913-bec90a794700 | -10.3912 | -61.25 | 2024-10-12 02:04:20 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 440ad658-46ee-3a35-be44-c66876e3b81f | -10.3962 | -61.269402 | 2024-10-12 02:04:20 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df70f35b-3cea-34d1-8834-a32012ef8d79 | -10.3716 | -61.213501 | 2024-10-12 02:04:20 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac18ebd9-2336-3133-95e9-a736763c7427 | -10.3766 | -61.233101 | 2024-10-12 02:04:20 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df3de3af-6d46-37d5-bd45-46ea61f2a541 | -10.8556 | -63.883701 | 2024-10-12 02:04:23 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8af0ef7c-a63a-324a-a933-bc7bbc14d0b0 | -10.8588 | -63.8964 | 2024-10-12 02:04:23 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5c40091-b7a0-3317-9bb1-c23f9275f328 | -9.8489 | -60.261902 | 2024-10-12 02:04:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a865685-3f1b-31f5-8541-69e1a5703afa | -9.8549 | -60.285 | 2024-10-12 02:04:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84c72716-fc37-3629-91cb-cf578805c3a5 | -9.8393 | -60.2644 | 2024-10-12 02:04:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeac3e60-e07f-31f4-b86e-120a3ade315b | -10.8286 | -64.194 | 2024-10-12 02:04:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 52422578-c02e-3881-b263-55cf270e094d | -10.8316 | -64.2061 | 2024-10-12 02:04:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0a50e7-2a9e-348d-9432-260e2c7cd046 | -10.5795 | -64.020302 | 2024-10-12 02:04:28 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 52beaff9-0b47-34f9-8811-8b731ee79abe | -10.5698 | -64.022697 | 2024-10-12 02:04:28 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 10f36e3c-66fc-3735-894f-f4aace1e7f26 | -10.5729 | -64.035301 | 2024-10-12 02:04:28 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21ae1d31-f75d-3eb5-866d-4bfc6e8b3fb5 | -9.8899 | -64.790802 | 2024-10-12 02:04:42 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb2e0eb-1c39-3b6b-9e7b-831bea48e828 | -9.8927 | -64.802299 | 2024-10-12 02:04:42 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aed4d155-2a43-3c4b-af9b-57bdd7d692d9 | -9.8829 | -64.804703 | 2024-10-12 02:04:42 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd102117-3424-3026-8c79-819ddd0f6a85 | -9.5829 | -64.080101 | 2024-10-12 02:04:44 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 004baea8-21ad-38e4-95a7-f783bf067856 | -9.5861 | -64.092903 | 2024-10-12 02:04:44 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9699ef4d-35b6-3521-a9de-a714f759b327 | -8.9673 | -62.3395 | 2024-10-12 02:04:47 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eacc3dce-cc40-3241-adad-6b245df01dcc | -8.9716 | -62.3568 | 2024-10-12 02:04:47 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba48353f-1549-3f2d-8da0-c6fb19fb372b | -8.9577 | -62.3419 | 2024-10-12 02:04:47 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7334d2e-0c4d-3166-ba37-cec5e6759d4b | -9.363 | -65.732803 | 2024-10-12 02:04:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39b94e20-0513-3335-8f44-1281500ac175 | -9.3654 | -65.742996 | 2024-10-12 02:04:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcf2cdc3-cdd6-3a18-8b79-81f90342a6e4 | -8.2341 | -61.180401 | 2024-10-12 02:04:54 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3734db54-53fe-3765-81d1-dd5d2c73c496 | -8.219 | -61.1614 | 2024-10-12 02:04:54 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9a71b7c-7fbb-3ca3-9234-f17340d31147 | -8.2244 | -61.1828 | 2024-10-12 02:04:54 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d33bfe7-f315-3f9b-8e29-a730430ece4b | -8.2147 | -61.185299 | 2024-10-12 02:04:55 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README29.md)
