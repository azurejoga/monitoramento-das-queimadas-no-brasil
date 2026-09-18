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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b4b3704-c815-391b-8131-f3f219c59edf | -12.16649 | -46.98655 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 586910e2-4946-352f-9648-e8b0362b6f5f | -12.531 | -47.09051 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 770085ca-c5ef-3430-8000-6a3c63aa9e0c | -10.6475 | -50.2396 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65e4fc07-7ecb-3ca5-b21d-9c3f646fec2a | -11.67437 | -54.44474 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a573a3a-b257-307b-b892-3ed622fc5066 | -8.93785 | -44.39802 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 622bd81e-a12c-3e44-899e-a487042a7d94 | -11.36841 | -44.04449 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d591512b-b076-3a8e-9c40-5f502517b1be | -13.62894 | -46.94779 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a2d580f-cb31-341e-9ad6-01a627e216c0 | -12.65288 | -54.71272 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0ef0abaf-e713-3c49-ac83-f8bc1ee2986e | -9.45944 | -45.44471 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76180467-7dcd-371a-a9d4-b5b2cd42cf65 | -10.43613 | -47.50811 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63313669-d2c9-3a47-ad75-4fe82f5b5295 | -12.39694 | -50.69583 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25d3e8d2-1b3a-3dbb-9f35-75370e4c7d1d | -8.90742 | -45.01562 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38015266-8e79-3b54-9040-59d87589328a | -9.9393 | -45.33254 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c433e1db-8421-38bc-a01a-81d57985a899 | -12.17812 | -46.97769 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97fba3fb-d714-373e-b968-f5f00a257fa9 | -13.59892 | -48.28551 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf201d6c-5e7f-30df-b728-3890b9b9193a | -11.89512 | -47.61524 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d28fa59-66be-3461-92db-cd1b3a42b1ac | -11.77544 | -47.43448 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56b171c6-eafe-3592-9c8b-548109acabef | -11.22302 | -43.48568 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93fe2648-ddf5-3c98-be0a-c501bccc4729 | -11.52096 | -46.8733 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be063aac-a9c7-36c8-9858-d30e677aa55d | -12.4085 | -50.69788 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a3fa146-e032-319b-a6a8-bf73ed4e0f4f | -9.55893 | -45.48252 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cf91884-047b-3dd1-ae59-767cc1b7101e | -14.22987 | -48.51421 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4bed491-50c8-3b5a-94b5-d4473d4845e9 | -11.81087 | -46.80464 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef96650e-0915-35bf-ace0-6ec7bb67eb73 | -9.71236 | -54.81294 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bc58152-39ca-35d9-89d5-e89dda1cbb16 | -9.70399 | -54.8288 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 619415bb-3528-31dd-9046-d5f276e32b31 | -12.26273 | -50.75039 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ff66831-a187-3a8a-87b0-fc2b93a27bc0 | -12.06276 | -47.50785 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bd30080-6cf6-34f7-95f9-242143e6d24b | -9.78444 | -49.1767 | 2026-09-18 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ceefda6-9cf3-33e5-baa1-83771a75ba76 | -10.38532 | -46.6332 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40219f12-3de0-337a-98fd-a95b0da9e3f3 | -10.12731 | -45.5699 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88e70d46-15fb-30b1-89eb-f239cf77f989 | -8.11688 | -46.79243 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5d1e6a-4848-3a1b-8640-4f101578c013 | -8.9384 | -44.39447 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89840484-9af8-362b-a04b-ee20ca9fccb9 | -9.39832 | -46.86533 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 667aeee3-33b3-38c4-8138-6134ecf80561 | -8.48409 | -46.88493 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 053eeeca-f983-3c8a-b2e6-7cb5e78dec5b | -12.17092 | -46.98008 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ae7cb496-1c0a-3bd9-bdbd-51465504e220 | -12.30148 | -50.75726 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6490b20b-1c0f-3b5f-9398-e8a3765e0754 | -11.88481 | -47.5722 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb8303fc-7335-339b-9007-6467cbd33500 | -9.6043 | -45.365 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92216c2d-6337-38c2-8617-42a6dc01c306 | -8.50809 | -48.4943 | 2026-09-18 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6a07b46-8fb5-3cb3-80ea-6167c860c2f3 | -10.65356 | -50.25068 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7902ae8e-2747-3bea-965b-56b70f532768 | -11.32541 | -43.3545 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dac4aa8-01b6-3533-8e15-09ce2e4bf0dc | -13.74776 | -48.79044 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc1bbbd4-f891-355f-9629-e5908d182843 | -9.90809 | -46.5088 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d062f881-7d1d-3312-9556-f09162eba7d4 | -9.9545 | -46.60337 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e64215fe-88e5-3809-ab44-f173c2349e11 | -14.17222 | -47.85089 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fd4c443-1c12-3bc7-9de6-4ab5d7a7c6a8 | -9.48639 | -54.48313 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 682ec2df-ed22-3c8d-b56f-e4f4c4cd25d6 | -10.37307 | -50.45726 | 2026-09-18 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99ed3c84-3221-3eb8-bf61-8e3545911e51 | -9.54728 | -48.09037 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24bdc283-186b-33ff-b1e4-10380030c9c3 | -9.70333 | -54.83236 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a09541a-a9d0-37a7-892e-cd18ba608273 | -12.32995 | -50.76027 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daadc2e7-bf42-338e-af39-837fbad4c4d6 | -9.24443 | -45.90622 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c80abe3e-3fb2-3548-82fb-78244d279abf | -10.6378 | -48.70168 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f66778a8-98f8-3683-bce2-34ca8d647c4b | -10.7999 | -46.65767 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5644ad73-cfff-3c81-93f4-bf00ffb6cbc4 | -12.26289 | -47.13028 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c5c4c80-4ab1-3611-b593-fecc5ace4aa0 | -9.93799 | -46.53524 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35d0b34a-ef44-3b82-b480-eac25b4d8ab2 | -10.12086 | -45.56467 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98944e7b-454d-35fe-aaa7-47236ed4e66f | -9.83274 | -48.34289 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1abc136a-9bf7-3fe8-b119-f3b7dbc68850 | -9.95818 | -45.4534 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a590ec13-221d-3af6-80a3-9ff7c98fa3d9 | -8.99092 | -50.16812 | 2026-09-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 987a466c-ffe3-36d9-9f21-2a7a0da996be | -10.49166 | -46.30433 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82c9ed18-ff08-326c-9aff-9d304d0ab10c | -10.81899 | -50.86286 | 2026-09-18 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 096fcf52-44f2-36fa-b207-45ba2e248fe1 | -13.47631 | -46.90072 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cbac8c9-b27c-372f-ab4a-6224c684c547 | -8.90325 | -44.97501 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c45c48-09ec-35a3-b6bb-83db6869c78d | -9.76445 | -46.08298 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4788796b-b078-3638-a158-85a80fb07d8e | -9.60586 | -45.33319 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6358bb87-82a6-3bc8-abc7-ba1f96393535 | -8.49156 | -44.55975 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fadde51d-99a5-3fae-a570-a02203849736 | -12.30789 | -50.74305 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e97ca94-4b1f-3fe0-89c4-5a817015b7fd | -8.44455 | -45.7133 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f0fab8f-04d8-3767-bc68-6b751cb263af | -11.29289 | -43.39954 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd868b48-0514-37a9-ab54-ebef007173c6 | -11.77208 | -47.43393 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8196011a-6594-3bef-960e-2501a7b77d9f | -10.65438 | -50.24581 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecabc997-a587-3a75-be50-9aba4e5baa35 | -14.131 | -48.72919 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c5ff98c4-44a0-3f23-bc8b-7700c1ef9406 | -9.39612 | -46.85759 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2288430c-64f1-303d-9e87-6bbf16960696 | -9.59657 | -45.85196 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d14f1e9-55f9-3818-a9d5-538a75f228bf | -12.36609 | -50.69038 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 096acdbc-cbfe-3296-b4e4-c06361816e63 | -13.65158 | -46.93338 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8177fa68-3bba-30dc-9d26-5aa8727b4466 | -9.94904 | -45.33768 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 801d42b0-bbb8-3fbc-a0b5-c6fdbb9cadb9 | -8.48714 | -57.62675 | 2026-09-18 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 476b5f9c-0ad1-373e-9940-478873ed8fb5 | -9.7161 | -48.1491 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5a34bc2-3f38-316f-8fd0-eb86bd321a02 | -10.61154 | -46.55783 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69191a32-c6ec-3ad8-852c-0bf8f2e67191 | -11.66995 | -54.44088 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c5dfe74e-be35-30fa-8068-3a653e1c602c | -10.4097 | -48.67461 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5c2f79c-4417-3b3b-a496-edd3e88d82ba | -8.76605 | -44.23354 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dd54210-5e90-347a-a188-db2053f24a66 | -7.10981 | -55.12429 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44a2b587-7ec2-33b3-8779-849f26d6a120 | -9.9214 | -46.51087 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bcdd71d-5846-3f4b-b108-fdb4a2297a68 | -13.76382 | -48.03485 | 2026-09-18 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a10ab9a3-11b0-31d9-9063-c87f832d1342 | -8.15857 | -54.81603 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7885c79-73e2-3245-ac29-e2a82d92a917 | -10.61375 | -46.56541 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 617b7542-4090-39f1-982c-d0060b754c9c | -9.77213 | -46.59244 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f50154c-6399-3ab6-8f91-9bd7314c3223 | -14.80004 | -48.55255 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46e0a403-a5a4-358d-9456-1172c6282e2d | -10.54742 | -44.85176 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f853bfe-0dad-322d-9fb6-d8fdbd6058b0 | -13.52195 | -48.94286 | 2026-09-18 04:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbca2511-e160-3be1-bcb0-c76da0fa9f19 | -14.89308 | -48.15216 | 2026-09-18 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8bf45cbd-153c-387d-aa71-d8dd57a0e522 | -8.55576 | -44.89178 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76bfdd42-4163-386b-86c6-09da35577588 | -8.88256 | -50.78049 | 2026-09-18 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cba070d-6f29-3a74-b647-a2a1a0153b12 | -12.3286 | -50.76207 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffba7dbf-3e92-329c-a0f8-2ca6befc5053 | -8.70218 | -44.89015 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23a82f3c-aed4-3b09-95e2-034b6457392e | -12.29543 | -50.74595 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 226fcd8f-97b0-3d58-8daa-d2638f12cb21 | -12.30874 | -50.73809 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31fdd59-b10e-344e-8ddc-620d87c0df9e | -12.05823 | -47.51455 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README46.md)
