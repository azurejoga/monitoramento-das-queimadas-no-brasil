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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6e25d16-07f9-35ac-ba7f-58126e6e6d1e | -11.89595 | -64.98598 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f96c573-0a41-3ecb-be83-1d02d9a2e87e | -15.75373 | -53.59127 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c62209b9-5e2b-34a5-98a6-8207c2411c9d | -11.31894 | -55.12167 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aed2fdfa-8887-320f-b292-24f52ff9253e | -15.74936 | -53.58309 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6999947a-f9ff-3b50-b2d4-a09166516503 | -11.22175 | -55.00629 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23a45786-33d5-3afa-8253-c2e38ddf6242 | -13.81402 | -46.27534 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| feab2c74-e766-34ae-acbe-869c9758ef6c | -15.25529 | -53.81529 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df6c4630-42ee-39b2-9228-e700a9bd7d79 | -16.52453 | -45.10115 | 2025-09-08 04:53:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdc3d56a-1122-3efe-991e-2641c07dd29f | -13.82714 | -46.24939 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11aa855b-d3b9-3328-87ee-f745ecc3845e | -12.95099 | -54.76947 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aee78cfc-5c50-3497-8863-7a8ee80f0a65 | -17.25979 | -49.78745 | 2025-09-08 04:53:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26a325aa-781b-3e0a-8e50-d2eb77a1d819 | -15.82841 | -52.2736 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5691b87-c0b7-37c8-9101-9af0e2a2675a | -11.98163 | -50.39179 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93391529-5feb-3d25-90d9-13897244cccd | -14.50922 | -48.81091 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ea4baea-9e43-325f-8d2e-748b99356d68 | -15.23123 | -52.3548 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2211537d-9b53-3df0-b436-02b2ea8304da | -17.66581 | -44.18504 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9c38355-199f-33a0-a013-64e2b8e6815b | -13.83777 | -46.24465 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7de41ad9-34c2-3984-81d6-36724486fce3 | -9.68161 | -63.17002 | 2025-09-08 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbb0f828-9bed-31e9-91d9-0a466a654a6d | -16.44588 | -49.29045 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6124af5-740f-33b2-a649-be1c890b56a4 | -11.37232 | -50.33743 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42250537-d48e-3187-b550-375142fad01f | -12.47238 | -53.85365 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84e9e078-be70-3d20-a566-9fe74cc850a7 | -12.82627 | -52.93876 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f520370-7c50-30ee-b791-5e1727c8d36f | -12.82292 | -52.93822 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcb4b733-85a9-3965-97aa-04475a8f4a6a | -14.51495 | -48.79981 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f812015c-359b-3835-8cc5-5142488a6edf | -13.32355 | -51.7495 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15582a70-ea34-3ccf-a39b-005361f0fe72 | -15.7572 | -53.55404 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d59f3b7a-2622-305d-a9aa-2627f6d55bd1 | -10.02846 | -63.47653 | 2025-09-08 04:53:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a82d94c-79ff-3734-8c95-38f107b4e57f | -16.34304 | -52.94043 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c0cc7f2-403a-33a7-8ae4-e8fc62ba80e7 | -17.16226 | -44.44481 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9adbe7f6-2d19-351a-ae8e-1d3cb5b1c417 | -10.96332 | -56.20872 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 042a5cd9-e12e-3818-b9f6-fb2b47129590 | -12.72082 | -56.569 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de3e7a21-eeef-31f5-a53e-fe95e0f11cec | -17.66254 | -44.19035 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 873172f4-1056-3a7f-95d2-b546f25ac325 | -12.52305 | -53.85459 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6676d4c5-3c10-3226-a2a5-350014402024 | -11.18357 | -55.05163 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f34c46db-bea0-37dc-9ef6-af04e6d0b4b4 | -14.60123 | -52.13725 | 2025-09-08 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 615142c3-e7d5-39ce-8342-88441c00d2ce | -13.91994 | -53.96788 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a410b3fa-3f60-39b9-983c-c9251b42cfab | -12.47459 | -53.86121 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54945cd4-d0f3-3fd1-bfd1-a8cf7c70157d | -9.44649 | -61.82489 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9fbd1d27-90c8-3034-b1f0-512a7a110888 | -16.34247 | -52.94429 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9aba5232-3ba3-3f6d-ab92-b6239ca0698d | -14.53631 | -53.15176 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6343a19c-e2eb-356a-a4a4-dc6b16b65321 | -14.45974 | -53.50739 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 600ba352-e4b8-3444-97fb-de58cdb6dad9 | -16.90117 | -45.76594 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a2f8fdc-eea4-3333-a229-ea143db191e1 | -16.93705 | -45.78373 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baac7853-4b20-37fe-a6fc-a7b465245285 | -10.50602 | -57.80037 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fc4d32c-ef03-396e-b6d7-f0355f4caa7b | -9.20224 | -65.90586 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 942b2d58-9f6f-3475-a0f1-83a434983367 | -10.61995 | -54.91869 | 2025-09-08 04:53:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bd29372-afa4-37c2-b480-95bcfadfd87f | -17.29559 | -50.38768 | 2025-09-08 04:53:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c830bde3-863b-32e0-a452-fe7e548ccc0f | -11.10734 | -52.05917 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4be32ea1-e8a8-3a85-bd5e-f6bc2fd9972b | -11.76661 | -47.74685 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34ceb8d1-c75e-3da9-b202-b4faf2a4424b | -11.83568 | -46.77116 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b61e890a-a22d-3783-8b64-d74d1218ae92 | -14.52627 | -53.98199 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb94f163-ff4d-3e46-a201-ba0d5478b3a2 | -12.83822 | -47.98891 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a069ff85-24f7-3585-b6f3-988a828d87d8 | -12.62168 | -56.96874 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 60264603-a180-3eab-991b-4f64cf9f6776 | -11.20723 | -55.01126 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7afe708-31ed-3d21-b043-70c0125f3aba | -14.73977 | -47.76829 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cc5233f-a46f-3419-b9b4-78b95543db42 | -13.81695 | -46.28084 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e526d792-7dff-3eb5-ba37-abe146d9c9e0 | -11.60795 | -47.14942 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83cf6d62-3382-3855-9c51-6e8c1269e1ec | -11.22117 | -55.00987 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd2562e3-3fd3-377d-b974-36f945e00aaa | -12.61747 | -56.97218 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ff3fd73f-e8df-3574-a502-48c852b494c1 | -16.37379 | -49.48723 | 2025-09-08 04:53:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7371e25-8b7a-3587-bf4c-87de7468eccb | -12.60767 | -56.98718 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f675fe32-b755-3a9d-9a1d-122c9897c025 | -15.75428 | -53.58758 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25ed7c1d-ecb8-3dc8-a39c-e41f3c5ac131 | -17.23672 | -46.69214 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8922a9c8-a5d1-3b1e-83d8-c8c57eb1226a | -12.85414 | -47.98118 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07cf3d61-1609-314a-ae0c-82ba2181d32d | -8.88396 | -64.21712 | 2025-09-08 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5d931e40-7eb6-3a2a-b1ce-f3c15746c52e | -12.47402 | -53.84309 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8d76340-8a7e-3a1b-b0b3-e74dcda1a4fe | -17.64609 | -44.78435 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f582c35-ed00-3e25-a64d-7a29b7c3253a | -11.35813 | -50.38453 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7acc0c23-12c6-3eb0-9df4-d9d1969922bb | -12.52745 | -53.84808 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68494f89-11f8-3a0f-9c1b-69a35b2dae29 | -15.0013 | -48.01436 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bd57ff3-b119-3dfc-9ae5-a0b699dfb52c | -12.94432 | -54.79015 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99731d54-1227-3a79-b7ef-523dea949011 | -11.86253 | -51.05476 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7176d78c-634a-3a72-9444-708f2372ec6e | -11.62661 | -47.14741 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77264ba9-9536-311d-9584-c31134be9647 | -11.19894 | -54.99888 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c9294b2-e983-3670-90f5-18e0ef89e21c | -17.2565 | -46.69803 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2082c1ad-6dca-3044-836f-b67d70e28aa4 | -13.01074 | -54.82266 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffd25bd8-d463-36b5-9123-1c5caafdeccd | -14.79353 | -48.2715 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8becbf01-5a59-3dfc-99db-ae3b039d45d9 | -11.20839 | -55.00409 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6abac62d-aec0-38f9-b64c-8865423faef0 | -9.44148 | -61.82399 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c49d06d4-e042-3fd4-9380-528b558cf88d | -14.52427 | -48.76112 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7abe6544-8077-33da-88bc-addd2fa95e86 | -12.83565 | -52.89925 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f32dc2-b181-3233-b34d-50d48de93b9c | -13.00286 | -45.21242 | 2025-09-08 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eef4cc14-aca9-3e4c-a935-1353f2d34f12 | -12.17933 | -53.89983 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11fa0044-33cf-30b2-82ab-8f047a032d32 | -12.87157 | -62.11159 | 2025-09-08 04:53:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e57adede-273e-3bff-a6ec-b5682e92e15e | -15.75537 | -53.58019 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a363a95c-9ac3-37a1-ad4f-8207f99464d5 | -12.82572 | -52.94241 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a41aa3d-7640-3ac6-a6be-cdd18e8a1eec | -12.94549 | -54.76131 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c572d1c-fb36-39d7-9ba1-b753124417b3 | -11.41374 | -50.38843 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 850aef24-cc19-3643-b356-093105c26066 | -14.92766 | -55.88338 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d751b107-820d-355c-90d4-d8f5b39ae1f4 | -9.08898 | -64.01717 | 2025-09-08 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ccd9b69-32ad-39ad-9171-79e6b2a958a8 | -12.47896 | -53.83307 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f88d29c-0a50-3cfd-935e-f09dfc6c6f16 | -12.19807 | -53.91004 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a31f3aa4-e582-332f-a51a-9d95ba51e260 | -9.48017 | -60.48885 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| caf05294-a15a-3074-9e8c-a9fe34ae6c56 | -16.54543 | -45.11126 | 2025-09-08 04:53:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1f03bf-86e3-3e67-ad01-e6a7ff8679b2 | -14.79845 | -48.23248 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02dc00f8-f60f-3a8e-ad89-541d279b8679 | -15.11301 | -52.34893 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 322a3120-7b45-3c5f-8c48-99db293e2592 | -12.92726 | -54.76921 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd72668d-30ab-3507-852c-5620cc6c2df7 | -12.9432 | -54.79723 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f004743-3a4a-30bf-b32a-1f52ad585b4f | -11.87229 | -50.9632 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3079f1f6-38cc-30b5-bf08-ec6848a739c6 | -11.6044 | -52.19905 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README66.md)
