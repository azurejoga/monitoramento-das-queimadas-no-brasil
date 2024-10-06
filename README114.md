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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab3eaf49-0d86-3deb-ad25-b45c8bc5cac5 | -15.1562 | -48.04662 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bb60021-4408-39ad-bb91-04100c7965af | -20.58748 | -49.3688 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a40854c-6dc2-38a0-a97c-92a03ecb06c2 | -20.58709 | -49.37319 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49307f25-361e-38d6-abe1-16b3b6df7403 | -20.58668 | -49.37763 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 712c2ce0-cff2-36d0-be7c-9412c58f8cda | -20.58628 | -49.3821 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 292d4796-f5df-3714-b86b-232e43676585 | -20.58587 | -49.38661 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d6a1e251-f05e-36bf-afbc-2375101f8095 | -20.58075 | -49.37695 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fbce0568-9083-385d-9dae-1f816ecc075c | -20.58034 | -49.38153 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c9c8a35e-27d3-3606-9426-86907d04246a | -20.57992 | -49.38621 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e5dba742-f51d-3037-9ddd-ba5f533d46e3 | -20.57951 | -49.39072 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 39a121a2-e87b-3179-b9ee-4d6b9ee98b02 | -20.57869 | -49.39975 | 2024-10-06 05:14:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 38.4 |
| cd063aba-f113-31cc-b1f3-0cfe410dcfb5 | -20.57827 | -49.4044 | 2024-10-06 05:14:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 0434e420-8afe-38a7-bb42-2317679c66b3 | -20.57439 | -49.38105 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1db95cf7-4b2b-30ef-9dd5-e2c444f3f476 | -20.57397 | -49.38568 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ae86d73-e8cd-3adb-9db9-4fd3beb6c420 | -20.57357 | -49.39017 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b88a7fea-3ae9-346d-bf31-ea0e17dc1772 | -20.57318 | -49.39454 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4681d928-ba0f-3c92-9267-905e0c6d1362 | -20.57277 | -49.39903 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 936e881d-a719-38d2-82c6-ee91becf7afd | -20.57237 | -49.40356 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 6409ed2c-7b56-358b-a112-03577dca4fd2 | -15.05259 | -49.46977 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56d9cf65-78bc-3c54-9208-4da24cdcb0e2 | -15.05217 | -49.47353 | 2024-10-06 05:14:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45eccb60-4f5b-359a-9d5f-4015539b527f | -14.48135 | -49.27139 | 2024-10-06 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9519007f-c4f8-3033-9a63-b920a1dd37e9 | -14.4809 | -49.27524 | 2024-10-06 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac9a8999-e796-379f-9cf0-2b853ad584a5 | -14.47579 | -49.27077 | 2024-10-06 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e97067c7-330b-32c0-9e19-d2f17dd9528d | -14.47534 | -49.27462 | 2024-10-06 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53e53fe4-9746-3c8a-b6fe-b74fe1490c58 | -16.44205 | -49.45574 | 2024-10-06 05:14:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51f32476-7d76-3f7c-aadc-25ef1e723616 | -16.42364 | -50.1761 | 2024-10-06 05:14:00 | NOAA-21 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9cdf91fe-83b9-340a-bef8-98d8245d747a | -16.4212 | -50.17635 | 2024-10-06 05:14:00 | NOAA-21 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2b8573d-39af-3860-b059-4bd0c35ab538 | -16.35606 | -49.92979 | 2024-10-06 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ea90b21-2cf7-3000-8c42-fa2416da8f58 | -16.0958 | -50.23282 | 2024-10-06 05:14:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7317c64e-1c93-33c2-8269-073a0b1f6ed7 | -16.07021 | -50.2322 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 508b012a-53b7-3b8f-940f-5ff7c5cfd9f1 | -15.75692 | -49.93551 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ad0a02a-bd4f-31ca-8e37-df12ab5826c8 | -20.45405 | -49.98135 | 2024-10-06 05:14:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1af7f63f-5e91-3f24-b5e1-2af33703ce92 | -20.45365 | -49.98551 | 2024-10-06 05:14:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 574ae7a5-6186-379e-995e-b2c55ee8fe99 | -20.44044 | -49.9425 | 2024-10-06 05:14:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 860912d1-c68e-30a8-88df-aef524dc6f00 | -20.44004 | -49.94674 | 2024-10-06 05:14:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b3ee058-ce20-3553-a9a0-15c2e0a030d5 | -20.46162 | -51.28581 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 6fa7a61e-8516-388d-a8a4-b15ce4c79665 | -20.46135 | -51.2872 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| cee58390-404f-3ccf-841d-132c5df092fd | -20.46128 | -51.28931 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 421500c0-6925-3c83-b236-374b5aecf117 | -20.46099 | -51.29068 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 3c63101d-eba4-33c1-a780-fd1041297abe | -20.46094 | -51.29279 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| c8b17a6b-8c23-398e-948f-5e60b2164632 | -20.46062 | -51.29415 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| d72b1914-504d-330e-a25a-9e3a36cba89e | -20.46059 | -51.29627 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| dc96a8c1-387a-3090-8887-4f1e84eeefb4 | -20.46025 | -51.29761 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 280aacf1-50a3-3ee4-8f60-072eaee23a67 | -20.45684 | -51.27955 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 1b1f3fe7-e20c-349d-8aca-e7f5f07a73fb | -20.45671 | -51.28161 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 8896af5d-ba94-33f4-b7ad-17b0daf97570 | -20.45647 | -51.28301 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 206de6b4-c3f5-3e2b-ab47-e9c845e95934 | -20.45638 | -51.28508 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 4b2798a7-3216-36d1-92e7-b081f3b6096f | -20.45611 | -51.28647 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 23dae7fa-fdea-3e35-bd94-6969d7f32e29 | -20.45603 | -51.28855 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 7a11f5f7-50d7-3797-93f3-1a31e41d9e8c | -20.45575 | -51.28991 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 30522acf-8d92-379e-a10b-2019fa38c22f | -20.4557 | -51.29197 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 78f71c6e-a34d-3f87-ad77-0c5200c3ab43 | -20.45539 | -51.29333 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| 65ec6506-5f65-37ce-9332-b90a8c258b37 | -20.45536 | -51.29541 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 16c6ea05-322c-3609-9daa-a2fcfd87e283 | -20.45502 | -51.29889 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| 4b7bd630-98a9-3bb2-ae4c-86bed3e85418 | -20.45502 | -51.29675 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| a31fe9f9-4e09-367a-85b4-564b2119bfb0 | -20.45468 | -51.3024 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| c387ef53-f8e8-3580-bf29-0d45419ebdd9 | -20.45466 | -51.30025 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| 0c917cf6-c2e6-3633-b997-271e3894ea5d | -20.45087 | -51.28575 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| b33376a4-203d-3dc4-b3a6-de886023dcd2 | -20.45079 | -51.28781 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 0df7377c-8f78-34f8-a5e0-e87bebd9c882 | -20.45051 | -51.28919 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 8c8d13ff-183a-3b1f-823e-97fc0008c203 | -20.45045 | -51.29126 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| dcfbd7dc-e366-3a17-aafd-d87bf6fff616 | -20.45012 | -51.29471 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 61c27a82-7968-3e73-81fd-d8e0d183041a | -20.44978 | -51.2961 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| d4baefd8-c9cf-39ca-8c5c-2e867cb17c47 | -20.44977 | -51.29822 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| 3d563be7-b0c1-3b8b-9c63-d37b2bc4d8f8 | -20.44943 | -51.30174 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| 670adf11-fb23-3efd-88c1-8cc4aca0b5c9 | -20.44941 | -51.2996 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| 54e25935-79d7-3ca5-b12d-43a7e5f5f0f5 | -20.44904 | -51.30312 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| c2cee13a-a9df-3aad-84c2-75a048d2fbb1 | -20.14439 | -50.3459 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 7f1b72af-dcd0-368a-ad98-3c11729fd55d | -20.14402 | -50.3498 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| f1ea1dee-76c8-3695-aa76-2975a4fc01fb | -20.14364 | -50.35371 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 27ba1048-9369-349c-a8c1-23e17095b732 | -20.1392 | -50.34814 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| c720ba50-e1c6-3d67-8eda-7bd3832ed903 | -20.13881 | -50.34542 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| c54cd4e8-d550-3f93-acf9-eed9681349de | -20.1388 | -50.35208 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| 1f481b05-06fc-3663-9a0c-e122119443fe | -20.13844 | -50.34936 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 853ca974-723a-369e-9fb7-bfa05a81289a | -20.13806 | -50.35331 | 2024-10-06 05:14:00 | NOAA-21 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| bc38526f-5dc3-3dee-a34c-4767f37bb71b | -13.68063 | -51.18538 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 500eb225-45eb-3f1c-bcae-81daed53b6e5 | -13.67996 | -51.19081 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c9808d8-f4c9-3fbb-991e-57543d5d32ba | -13.6758 | -51.18471 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 093a3f14-b877-3b12-b0a4-cc223daf604f | -13.67513 | -51.19013 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 37513908-f6b6-35e4-aaae-8fbeded6f149 | -13.67097 | -51.18404 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98c58051-f96b-3df6-ad53-678950fd88c7 | -13.6703 | -51.18947 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7397d86c-9beb-3257-ad1a-733dcdca020d | -13.66547 | -51.18881 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6abdc83c-3026-3bcf-a889-0555a04a6a70 | -13.65997 | -51.19357 | 2024-10-06 05:14:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b40947b8-ec8a-3a95-86fe-4b482a52659e | -16.33133 | -51.27229 | 2024-10-06 05:14:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a289fd8c-1237-30cb-9533-861e103537ca | -16.32637 | -51.27136 | 2024-10-06 05:14:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c5a1713-8040-3a62-afba-c1a74127a9ad | -16.32568 | -51.27747 | 2024-10-06 05:14:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 98eac750-ec01-39bc-8430-0f64f604802c | -16.32073 | -51.27653 | 2024-10-06 05:14:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fcb990bb-218b-3f7a-9b4b-a4300fd58055 | -16.12431 | -50.45957 | 2024-10-06 05:14:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d18f287b-f886-32c4-9a8e-4920b9d0e580 | -16.12395 | -50.46277 | 2024-10-06 05:14:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e728612-411b-3b42-9808-29cfefd89f78 | -16.08236 | -50.45395 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd1bc3f8-0023-3a62-b27d-f62f5986e20d | -16.08211 | -50.45345 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff5551a2-bc2b-3cee-babf-a5576e4de6b6 | -16.07712 | -50.45313 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 653085ca-6680-3b39-b7b5-90396e643c44 | -16.07689 | -50.45264 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b1d509b-a445-3d81-b5b4-a2d9b14b88e5 | -16.07677 | -50.45634 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ee987cd-8d35-3ddd-bb62-a7f9d1f4e83b | -16.07651 | -50.45585 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6da4c6b9-743e-31f3-86f7-463b3032d1f2 | -16.07261 | -50.44578 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b163eed2-a428-363a-b33b-52f3fb3f7a8e | -16.07242 | -50.4453 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccda36c1-601b-374c-bac9-cf50b1cc23b3 | -16.07204 | -50.44857 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7146ab87-e34d-3ec7-b068-d69ff7fbd73c | -16.06738 | -50.44493 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f2ad9a5-d7af-3d94-bf1e-a23c9f825f62 | -16.06702 | -50.44822 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README115.md)
