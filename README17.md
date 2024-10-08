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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b40b8cfd-7865-3cb7-b6bb-5a7759791f2e | -12.4655 | -47.3036 | 2024-10-08 01:00:12 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef443b22-264c-370e-be20-c712db5cd8f1 | -12.4675 | -47.312 | 2024-10-08 01:00:12 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53b1c52d-4ee7-3a64-bdd5-e947b08b7372 | -12.3612 | -47.083801 | 2024-10-08 01:00:13 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa844a8-ab50-3784-bdca-3fb97f2f314d | -12.3633 | -47.092499 | 2024-10-08 01:00:13 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3a0ee0-4428-3cf6-bc4b-93735c59ce9d | -12.3654 | -47.1012 | 2024-10-08 01:00:13 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4688abfc-00c4-38d5-b98b-cc1ed0e39f14 | -12.3514 | -47.086201 | 2024-10-08 01:00:13 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee6939de-c672-39e8-90b0-6c450e87eb5c | -12.3535 | -47.094898 | 2024-10-08 01:00:13 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79b5e667-7378-3785-bfda-36ec36574d10 | -11.9188 | -45.688999 | 2024-10-08 01:00:15 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1db821c1-29ec-32ba-8961-a24945fcab78 | -12.035 | -46.8451 | 2024-10-08 01:00:18 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e74335e9-9e17-37e7-82d1-ad4672e92486 | -12.0371 | -46.854099 | 2024-10-08 01:00:18 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c72300e-441d-32a8-9e91-9b1df9a26701 | -12.1599 | -47.755699 | 2024-10-08 01:00:19 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42c3da99-3d56-3408-ae02-d3e92143cfaa | -12.1618 | -47.763901 | 2024-10-08 01:00:19 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd856bc1-a3ed-324c-a045-b05aab389c79 | -12.5335 | -49.4846 | 2024-10-08 01:00:20 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8961e2d-c0fa-3442-afd2-08e54ac3fb37 | -12.5319 | -49.477402 | 2024-10-08 01:00:20 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d52c060-0cf5-32ee-9d06-ed477f88fcf5 | -13.2934 | -53.7019 | 2024-10-08 01:00:22 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b491186-bf31-303c-9e08-5cdf52243e7c | -13.2836 | -53.703999 | 2024-10-08 01:00:23 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a79718d8-23ca-32d1-9522-b015bb65e141 | -13.5985 | -55.207699 | 2024-10-08 01:00:23 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1781825-e0a1-379b-8932-5819a044d207 | -13.6007 | -55.218102 | 2024-10-08 01:00:23 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6fc5f8-55e0-34b7-9869-932d6a2804a7 | -13.5887 | -55.209702 | 2024-10-08 01:00:23 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c052598-e035-3eff-9941-02abda4030f7 | -13.5909 | -55.2202 | 2024-10-08 01:00:23 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ceb8c9ea-4894-3f3a-9dac-7c5dd2281cfe | -12.6275 | -52.423302 | 2024-10-08 01:00:29 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba9ad837-1288-3538-8718-4e7c5f7d8fab | -12.6291 | -52.430801 | 2024-10-08 01:00:29 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c68f2241-a7f9-3514-a4a1-a034420045dc | -12.6308 | -52.438301 | 2024-10-08 01:00:29 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1fba99-e0cb-3c4e-973e-d41e95c00ea7 | -12.2024 | -50.562599 | 2024-10-08 01:00:29 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e6dfc3a-2619-3158-a3b9-e1f143e8bf0d | -12.204 | -50.5695 | 2024-10-08 01:00:29 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23a5e3dc-c7ae-37c0-95ec-97d4650a039a | -12.5932 | -52.454498 | 2024-10-08 01:00:29 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcf5d93d-5509-3f52-b468-c33852e4e8b8 | -12.6245 | -53.117001 | 2024-10-08 01:00:31 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f434ed35-0de6-3b6f-ba36-afd24019bfdb | -12.6049 | -53.1213 | 2024-10-08 01:00:32 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5140851a-b1ac-3b15-a504-7a5e21d69280 | -12.1006 | -50.886902 | 2024-10-08 01:00:32 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35a491b9-689b-30af-afb2-b395a68a31eb | -12.1021 | -50.893902 | 2024-10-08 01:00:32 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de64d540-9689-38ac-be44-42d7fc4a0500 | -11.9147 | -50.114101 | 2024-10-08 01:00:32 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83f0f576-10e0-3eb7-8cc0-fffbb7c91365 | -11.9163 | -50.121101 | 2024-10-08 01:00:32 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a8a15f8-1f5a-31e2-9a7b-f9613a9b2b0a | -11.9179 | -50.128101 | 2024-10-08 01:00:32 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a98d0ba5-950c-34ab-acdb-ba0d6a88409c | -12.0923 | -50.896198 | 2024-10-08 01:00:32 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0a85912-1154-3082-8a27-1d4c691c517e | -12.5699 | -53.0546 | 2024-10-08 01:00:32 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 977b0c4d-adb0-3831-b0d9-b4b051678790 | -12.5716 | -53.062401 | 2024-10-08 01:00:32 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcf84bb-5039-33b7-a0d7-500a4432d55f | -12.6558 | -54.702999 | 2024-10-08 01:00:36 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25a6e42e-4f23-3297-80ab-cba782de917c | -12.6578 | -54.712502 | 2024-10-08 01:00:36 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14f0aa38-1bf3-3a74-91a6-14c68bc2f306 | -9.5327 | -42.969601 | 2024-10-08 01:00:42 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a1683eb0-a59c-379b-81c1-0a3c57d6383c | -10.1169 | -45.2141 | 2024-10-08 01:00:42 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba99361b-547f-3848-9677-1bc36d5b101d | -12.1423 | -54.260101 | 2024-10-08 01:00:43 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2854ffb0-cb27-3771-9b13-1ce4955989ae | -12.1441 | -54.268902 | 2024-10-08 01:00:43 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efcb0f22-413c-38e8-a217-dcb98419450c | -9.523 | -42.972099 | 2024-10-08 01:00:43 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a54c6f97-58d6-33fe-a23f-09fba3e2fe3e | -9.5273 | -42.9893 | 2024-10-08 01:00:43 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c0b12f4a-bff7-319d-b2f0-30f8b5c516b8 | -10.0742 | -45.250099 | 2024-10-08 01:00:43 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d73aeb6c-5f37-390f-b46d-54fd2e9e79fb | -10.0771 | -45.262001 | 2024-10-08 01:00:43 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f359c9ff-fc62-371b-8cde-cec485ffc2aa | -10.08 | -45.273899 | 2024-10-08 01:00:43 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edf49b6d-e437-3038-b240-de1132442e54 | -10.0644 | -45.252602 | 2024-10-08 01:00:43 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3698ad62-c65a-3cd2-b90c-2cdd93a9c432 | -10.0673 | -45.2645 | 2024-10-08 01:00:43 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 562c8ae0-55ef-3546-bc0c-f8369bebc338 | -10.0703 | -45.276299 | 2024-10-08 01:00:43 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f88d8744-db6f-304a-ada4-3143fac33d46 | -11.3502 | -50.985699 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91aeafa2-d556-3e62-9ac1-fcadee553ab3 | -11.3518 | -50.992599 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2ebf883-78f6-3dde-b121-2898429a203d | -11.4084 | -51.243401 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5531376a-0054-36a7-86ef-e19c56c1ffad | -11.3388 | -50.980999 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29f1c0ff-4ac0-335d-b7d1-6ad2a2e3d75d | -11.3404 | -50.987999 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b90d37c0-1c73-3622-8c9c-6c1caeb87ee0 | -11.342 | -50.9949 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af8535aa-a24e-36aa-9c37-2a3f41134709 | -11.3436 | -51.0019 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5adc7ec-9e98-3718-9da4-c520b31465a6 | -11.3451 | -51.008801 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f830934-2dda-3d71-b36c-3b9b1ecbc523 | -11.3467 | -51.0158 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9bdff93-746e-3aa7-89d0-92b2717e760c | -11.3483 | -51.022701 | 2024-10-08 01:00:44 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef93756-6c62-3300-9aff-6f52aa5ff74b | -11.3306 | -50.9902 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebe0fb1f-72e7-3976-acd3-8bcf3db8da46 | -11.3322 | -50.997101 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a99e4f2d-d106-3042-84fa-09afb78c81bd | -11.3338 | -51.004101 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7185fbb4-666b-3b6b-938d-900f8333aa6f | -11.3353 | -51.011002 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56b6b4e8-1b49-3978-ba2f-7381943847d7 | -11.3369 | -51.018002 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 013a83d6-8bdf-390d-884a-74facc155ecc | -11.3224 | -50.999401 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd3b01d8-14ee-3018-8470-bb8fd6ae93c9 | -11.324 | -51.006302 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e32f497-ec77-3a26-97f3-45914d222517 | -11.3255 | -51.013302 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf14ae4-2ec5-300d-9715-e371c36489a6 | -11.3271 | -51.020199 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7710d8c3-7b51-3857-995b-07c97a95989c | -11.3287 | -51.027199 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab85ed8a-55ef-3923-9456-43551946475c | -11.3142 | -51.008598 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 418792e2-d762-3765-b80f-d4ef81ac3d67 | -11.3157 | -51.015499 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1906904-cba6-32ce-82c0-b78034493462 | -11.3173 | -51.022499 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77fae51e-920d-3562-be34-0820ad832ac6 | -11.3189 | -51.0294 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8db27e72-dcb2-3311-926d-1bee48a9bcaf | -11.3205 | -51.0364 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52d0557f-9736-37e4-8c4c-a3274609b5a5 | -11.322 | -51.0434 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21fabd70-f337-3b90-9c0a-6a8638ee5f63 | -11.3236 | -51.050301 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ddf36e7-a695-3ed8-8c30-236032a6e2ae | -11.3268 | -51.064201 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aee63dd4-409f-3b7c-ae19-22e5771b118c | -11.3075 | -51.0247 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 17130005-4861-328f-ba1b-b80e0dcacf68 | -11.3091 | -51.0317 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37e5c893-dc87-38c9-92c4-787e349eed84 | -11.3107 | -51.038601 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7409cc69-aecf-34f0-bfdd-ab6f049d806f | -11.3122 | -51.045601 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2ebad15-a69f-3537-9438-0894f792bff7 | -11.3138 | -51.052502 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77de6541-4830-3055-95c2-5c42549f9bdf | -11.3154 | -51.059502 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a18c5e3-70bc-38a1-86ff-2fae23edab28 | -11.317 | -51.066502 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc062a90-d217-3da1-8331-957ff3039ce9 | -11.3185 | -51.073399 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d63ceacb-4bae-32d3-a792-402c0f30fad4 | -11.3056 | -51.061699 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35ffbb6f-ebf5-3398-9118-1e9cd2553f04 | -11.3072 | -51.068699 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 776fc8ea-be59-36fd-aa85-d6df6418bcaf | -11.3087 | -51.0756 | 2024-10-08 01:00:45 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a259f69-000c-36c0-94a3-e75ef6ca3eb6 | -11.3148 | -51.330799 | 2024-10-08 01:00:46 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8383f1d-6e0b-3930-878a-fbeb609d5882 | -11.3163 | -51.337799 | 2024-10-08 01:00:46 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dd25869-c9a9-3643-a17d-7eb6c1990284 | -11.305 | -51.333099 | 2024-10-08 01:00:46 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90449885-759e-3792-9db0-68af9b37eddd | -11.3065 | -51.34 | 2024-10-08 01:00:46 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7944167-a936-3189-aae9-052df399da33 | -11.3081 | -51.347 | 2024-10-08 01:00:46 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07d9287b-8a8e-3011-a0fb-d017f17be2d3 | -11.2967 | -51.3423 | 2024-10-08 01:00:46 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4aeddc8-b0e4-30cb-aaf2-5c9d955a4057 | -11.2614 | -51.276901 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d78610d-bb8b-37c1-bbff-5dede464f838 | -11.2501 | -51.272202 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7542e36d-5102-35a0-8550-d949d5ae2b55 | -11.2516 | -51.279099 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c251d90f-9e9d-351d-a520-0f4ca5246865 | -11.2532 | -51.286098 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7464a456-e73a-3a9d-ae06-cf2f026dac13 | -11.2548 | -51.293098 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
