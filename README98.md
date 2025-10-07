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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f87e579d-ec4d-30df-b2f2-ea8d475b103e | -15.38567 | -47.99228 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f33f8de3-91d5-3bcf-bf3b-53c41cdb7439 | -9.68175 | -48.39545 | 2025-10-07 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aee22cd-553d-3867-a84a-37df58958b9f | -12.91065 | -54.74023 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0b64af-c854-3ad6-b6db-7c483743a971 | -13.66769 | -44.31285 | 2025-10-07 04:57:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffb1672c-31d6-3718-82f0-5ad566dd48ee | -8.1869 | -50.30272 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64503f5e-6d59-3472-9177-eb1ed3ab01a1 | -14.75086 | -46.02484 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d135b531-e984-3196-b43d-8518b3276ba2 | -10.15657 | -45.42202 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f29ef37-5a58-3719-9375-f037504b853f | -13.36437 | -47.25841 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5055da38-073f-3ced-9658-48492120bb41 | -14.7751 | -46.05863 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa3aeff7-46dd-391b-b186-2e0307688376 | -14.54989 | -46.64746 | 2025-10-07 04:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4986f076-c3f0-3300-bb8a-c1a38ddf86d7 | -15.27264 | -46.34919 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38edda51-53e2-30d5-9c44-8660cdcbf19f | -14.27919 | -45.85102 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2388f10f-60ae-3ec0-a1f4-2762efbf708c | -11.74594 | -54.72169 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e044f6ab-80fa-3199-8b57-ac1067c6836a | -9.6362 | -54.31757 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 389415e3-95a6-3cf0-9fc1-365396a78c29 | -14.73539 | -46.01217 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e1076ae-b4ef-3b3d-83f2-2b9b47908639 | -11.95785 | -51.46582 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8d93b1e-560f-3e51-920e-af27d787acea | -10.0706 | -50.51847 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa6855cd-c8a3-30bc-8550-8ce58ee8b3aa | -10.08576 | -57.80321 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa8fa190-bca6-341a-aa0c-42cab5dbfccb | -14.2899 | -45.85633 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9e7b4eb-15cd-3a3a-8c0a-e5c694952b72 | -11.23225 | -47.7679 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0e37461-2e05-3074-b503-e089ab8d87b0 | -13.24725 | -51.6803 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8b9fede-c828-3511-b20d-bc1baa301e2d | -13.34702 | -48.03193 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6226db50-8066-36d9-9f11-60a9cb855f80 | -13.23315 | -47.24746 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b9ee1c-b74f-3650-8073-e6af76bf26b0 | -9.3356 | -54.52403 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0a66f5e-eef3-3dcd-aedd-ea1d8952602e | -9.02476 | -50.69871 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2248605-6818-31d6-a16f-7b3826dbfe9e | -11.88412 | -44.96064 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b89bd9c0-ae3d-30c4-a1ae-a71b108c65ae | -10.38146 | -50.30135 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 733aec74-b1b0-35f0-9661-b3c71482c4b6 | -13.2587 | -47.16709 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a15fdb7-48d5-3755-bfa4-44bb53f3816e | -13.31325 | -47.7697 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d598d31c-d4e3-330f-a982-9704d0c101af | -11.1157 | -47.21983 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 819774fb-4625-33d4-8d74-d33ee643faba | -12.9816 | -46.78416 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 884fe76b-bd21-360f-9921-4027ecfb43ac | -12.06435 | -51.20555 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c182815d-1490-325d-97b7-45ae5d897475 | -13.37599 | -48.03693 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae39764b-9397-3125-94b7-9cd879a4fd65 | -13.5931 | -48.68707 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 703f904b-89da-31a0-ad6c-5e5d2ac7756a | -8.41825 | -50.69838 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03cad0c0-3035-33f2-a6bf-ed333fb0e86b | -8.52829 | -54.86173 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03b1b63-9a8a-31c8-82bf-081300cb4d6a | -13.05293 | -48.71143 | 2025-10-07 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed7f3d97-952f-37dc-8148-e4578805a870 | -13.71959 | -54.71076 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e41e446-aef5-3050-857f-f8207c526b50 | -15.59458 | -42.36537 | 2025-10-07 04:57:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4204f019-776d-39c4-aaa8-4fe88c39b458 | -12.23587 | -43.77823 | 2025-10-07 04:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64d9b47b-8251-30ce-91f9-d5503bf16970 | -8.48146 | -50.21242 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c22c390c-2db7-3370-898e-348ae28c32cf | -12.9123 | -54.72952 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae3bfd50-1e24-3cfd-9c34-1b74c399ee67 | -12.90677 | -54.74327 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dea38854-863d-369f-b18c-f43572caac87 | -9.15119 | -60.62519 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f135eb1a-189e-39ec-98bc-04b1731de98f | -10.23295 | -52.69709 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73cabc12-d9cb-3601-8de4-624ea2156aca | -9.3848 | -59.41963 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec5f0bb-17c6-3dae-bd18-c2941b4ea5ba | -8.18238 | -50.30688 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ba119899-94a3-37f0-a1ba-fda57f459cfb | -10.31853 | -51.45693 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c5f2bb-8f1b-305b-8050-1a8f03553297 | -15.07793 | -46.63844 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62c14858-4172-34b3-bf6d-956bed29d469 | -15.79341 | -49.39699 | 2025-10-07 04:57:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72cd4cf1-1d17-34c5-8688-1439872a9081 | -14.56187 | -48.95424 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed21ebd7-6ccd-3d4b-8351-bdec2bad6267 | -13.50205 | -43.67314 | 2025-10-07 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8c5b3836-7c9b-39f4-be74-e4b277ecb2b4 | -8.83243 | -62.3724 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23b33dd7-d2d0-35cb-a332-dce88705063f | -11.94529 | -46.45069 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9686935-abf4-3151-b703-5c381b2fbd37 | -13.78639 | -50.7865 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 611064c6-0bbb-35f6-9596-9bef9b6b74c0 | -13.27831 | -47.16772 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9203287b-32a9-3490-a2fc-f0308d6bc3d6 | -10.40576 | -50.29975 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1512b061-ff98-3051-b5e9-a6a673d84a23 | -12.21719 | -44.25414 | 2025-10-07 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b39499f-e9fe-3dce-bf88-bdd1961b5458 | -14.91901 | -46.81256 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a522cf9-60f6-33f8-b257-fee1d922ee99 | -10.99767 | -57.05605 | 2025-10-07 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 790e905f-238b-359a-b9cf-3f1eccea24af | -11.03621 | -50.92006 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 36ac8835-b45e-3dfe-b95b-9c9b631b8f93 | -6.6966 | -62.83857 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5882ea01-6c6e-39b4-9c54-fee0f55e8e72 | -12.91618 | -54.72647 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8889a23-7f17-3142-b22d-94b3c7e11570 | -13.3514 | -47.56753 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bb6de7b-db34-3b35-a7a4-8131aa44dae3 | -14.28608 | -45.84085 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e466a291-c147-3c30-bc96-4a6d00204e60 | -13.23018 | -48.46041 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f52e35eb-858e-313c-85c9-41785b8913c5 | -14.73848 | -46.03448 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2d9e4b5-beb1-3f3f-ade0-ac5ec0085cb7 | -9.83633 | -61.994 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a51dd06c-dd9d-340b-a5c5-08eb71eb4b88 | -13.39254 | -47.59848 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d46e2aed-7d63-3b86-95f1-8d0a63c31048 | -9.03928 | -50.70702 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa8860ea-4d58-3f38-8727-871a9ed76edb | -14.28477 | -45.85184 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3c5f393-cd82-3f83-b088-b3311617ccc8 | -9.40027 | -49.36766 | 2025-10-07 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f01df8b-3b79-3134-b7b8-c3a828d5efc4 | -10.62152 | -48.70271 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed9d8329-802a-3d2a-8516-56a0ee5fa5a2 | -12.8918 | -54.75182 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a3fa87c-7522-3207-8b0f-49b13a091c77 | -15.28615 | -46.33508 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39114c9c-924e-3ce4-a6e8-86ba8ffd9beb | -10.23641 | -52.69761 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402aab6c-21f4-3bd5-a155-7e4e5f71157c | -12.93616 | -54.72968 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82805f79-e505-3794-af0b-f546eb1f4938 | -10.8151 | -48.59976 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f36ecad1-3f05-36de-958a-e7d7304c6f78 | -14.76867 | -46.06546 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d48d098-7c6a-3bfb-b632-210adf4a2991 | -14.90332 | -46.85627 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a22f323a-5982-312d-9983-640fd492d837 | -11.12138 | -47.21457 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be7cbed4-bb34-3ae7-8a47-aa231cfc18cf | -12.94159 | -46.81063 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38498a31-d195-394c-a90f-52a92357d56c | -13.66828 | -44.30759 | 2025-10-07 04:57:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47afac57-2528-343a-92cb-554716c01b58 | -9.56003 | -63.50683 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f5435c0-c28b-30ba-9d9f-278b64578fe7 | -8.34134 | -49.65794 | 2025-10-07 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d09b3d79-2c36-34a4-8103-e01274772810 | -11.23699 | -47.76836 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88363a24-689c-3b37-949f-8565ae338c28 | -13.08663 | -47.86337 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d3d0820d-0f1a-3db4-9e91-6c2300b5fbf8 | -11.71264 | -45.44717 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c0541c2-a878-3cf5-b7d0-0ca926623ca0 | -11.42261 | -55.07367 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd62f670-b8cd-3ebc-a226-2b2a8c158232 | -9.02548 | -50.69598 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d474c7d-a4ee-3faf-8319-549ca9897c7f | -15.88162 | -46.25681 | 2025-10-07 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4de1bab5-e1df-37c4-b02c-e9accfe06e0b | -10.61717 | -48.70186 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e9c839e-d8a1-337f-a1da-2514b2cc84f0 | -8.63039 | -51.084 | 2025-10-07 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ef3478b-f070-3527-b65b-6b674af382e8 | -15.60435 | -47.29621 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 74cf1780-5e57-33c0-abdf-273ece643f17 | -13.94707 | -48.17662 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43680f12-40ca-3f12-ae1a-b7beb646a6bd | -11.46528 | -43.49256 | 2025-10-07 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f6e6a1e-48f2-3300-abd0-9ff58b079028 | -12.3455 | -47.05832 | 2025-10-07 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c65af8-8be6-3942-a107-715b91b56706 | -14.28862 | -45.8562 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64761ea4-22b5-3668-9927-37a1d8236728 | -15.21962 | -49.31462 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c03c615c-52f9-3d57-976f-5b5f3f722e6f | -10.42148 | -50.30205 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README99.md)
