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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 176a9f47-30f9-3324-bad0-0f54ee0efd08 | -12.76228 | -48.65111 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e4202ab-09a7-3258-9a02-95476c437dcc | -11.05661 | -40.93436 | 2025-10-11 04:34:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a2a8f45-7e14-3349-abae-3028806873a6 | -13.33282 | -48.47584 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 308c6982-f82d-358e-906c-71e96b7972fa | -14.74444 | -46.12086 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8146d8c4-9fad-3b46-8a0a-b4b650c80769 | -12.41375 | -59.90125 | 2025-10-11 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638e0b39-44c7-3783-8423-0844243a1121 | -13.41752 | -47.27142 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b98d0e7e-3ab4-39a9-a6eb-a67521585710 | -15.69958 | -48.39759 | 2025-10-11 04:34:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7004dcca-0c4d-32a1-b1e5-01ca84bf87b6 | -12.90513 | -47.0392 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71105a2c-3961-3032-b730-adc586515010 | -13.21267 | -42.33277 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5def15c9-64e4-309b-96a8-54186a7aa6a5 | -12.77168 | -48.65627 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15a36e46-8027-3b1d-a645-75798a9075df | -12.24166 | -51.14341 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38d78d94-2bbe-3562-a7ff-1f2a4d770903 | -13.53231 | -48.12484 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af1c27c1-a2f8-33f8-b1c7-11c7a9bac2b4 | -13.26488 | -48.00911 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37f3da97-77d9-3513-b623-49ed21d2c2f2 | -10.87723 | -44.1908 | 2025-10-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e3f4e088-2726-3251-9712-ff8756fd44eb | -13.31285 | -47.97858 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f3a0c0b-47d8-3624-900d-0f0194a8041f | -10.15207 | -44.60908 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 296df576-bebf-3aa3-9892-2ed027f0a866 | -10.52942 | -47.35936 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6ab91fd-204c-3984-b03d-164066ce480a | -10.10821 | -47.26886 | 2025-10-11 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92fc1984-f874-37cf-9504-5eb461148c3b | -10.53274 | -47.3376 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71e79cd5-420d-330c-9edd-5421df69bd96 | -13.41807 | -47.26762 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78f7a4ad-a55d-3941-aa50-0786e08756d6 | -15.7109 | -46.62994 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c1c9af4-a37e-3ad2-8159-63cf01868a30 | -11.76916 | -45.04291 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d74f6c3f-66a0-36e5-bf42-19685af6ed3a | -14.28078 | -45.90908 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d347ed0-af79-3df3-9091-d68aecc8f902 | -15.30078 | -46.14057 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0e88883-5845-378c-a9a6-5d4ed60e5f42 | -11.78124 | -46.38148 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d6fbc0e-cec1-30fe-ab66-e22ae29d4fa9 | -10.56825 | -44.50962 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7218bfcc-1bdd-3aa4-a2b9-b69911b4f27f | -15.32168 | -49.56053 | 2025-10-11 04:34:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4129df5c-10af-3ab1-8b92-2ec47802d6fc | -14.74509 | -46.11633 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6acaeff-3173-3ef3-b16c-8c79f9a89254 | -11.78566 | -46.38067 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cab0db7-12a8-3bd0-b410-025e005e2400 | -12.69464 | -51.1917 | 2025-10-11 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838522e9-9ec6-31f1-85d2-4e831b1714eb | -15.92407 | -43.28801 | 2025-10-11 04:34:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e41f39f-69ce-3ae1-984f-27cb5d8d1651 | -13.31276 | -48.49805 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37d9b450-ba71-34da-b8e2-eeb62a173aa0 | -12.74599 | -48.64513 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f512a22-574f-36fd-86f9-f36493cee033 | -12.7562 | -48.6465 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23fd60e2-7936-3339-8f01-1e6d48b33315 | -13.2156 | -42.34557 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 6f579df6-26fa-3b86-8bab-b10646f84c54 | -13.8572 | -45.84103 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94d91373-2a83-3434-b3b2-e525ade959c9 | -12.75235 | -48.64951 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6105b97-8c31-3c0b-b7e2-d39aabd577b5 | -13.00688 | -48.80646 | 2025-10-11 04:34:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f2152b9-d572-32e7-abb0-da2ba371b02f | -12.90402 | -47.04672 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f66b02a5-1724-36e2-b916-e5454751cd61 | -11.7595 | -46.35823 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 743f2fd0-ccbb-355b-8e78-20952efbf32f | -9.40592 | -45.78049 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b22b9b1-985e-3f26-99bb-bb0e313b2bf9 | -15.88162 | -42.59827 | 2025-10-11 04:34:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5c4b0f1c-e244-35c3-a92e-09d3f4e3e9c7 | -11.76009 | -43.31627 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0563ca32-e8e8-38f3-8a63-4fb218dbf632 | -15.83193 | -42.02657 | 2025-10-11 04:34:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 299b4321-4115-38bc-908f-8434f20ef891 | -9.82353 | -45.94276 | 2025-10-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b05b30-55a5-331a-b8dc-ae2b311f7c89 | -15.20379 | -46.33067 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b440a93-1dc8-3ddc-bb2c-fa7233f702aa | -13.48801 | -48.09944 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9371593e-a307-311c-9d6a-197f97bb08ed | -14.93109 | -46.75392 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66cf6254-ac63-3507-81d9-f8780e8db103 | -12.63331 | -48.31673 | 2025-10-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e8f6f72-394a-301e-b41b-46d80427390d | -11.77362 | -45.0385 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a568b308-683c-371b-959b-6a785f083bbb | -13.30721 | -48.48977 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8bdcbda-6829-33b3-a803-cfe1324d462b | -13.48974 | -48.11086 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c19d7f17-df17-3360-ac47-6472c7475a7f | -13.30111 | -47.98809 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6358f43-18b3-3566-bb8e-459b31f64016 | -11.88629 | -45.49035 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fee1fea-47fd-38a9-b979-1c13304abda6 | -9.82413 | -45.93868 | 2025-10-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85dd5a99-488f-3785-b869-a96a08286c0e | -12.72861 | -45.84591 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 873c8e53-d75e-3c51-b195-6d4f3cb95375 | -13.28001 | -48.00008 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 824af9cb-691c-39f5-907c-81cde431d252 | -15.71739 | -48.1617 | 2025-10-11 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e44fde9c-e59b-384f-9ab4-d4f23f2c2d3f | -15.31685 | -46.18841 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a3f88a4-9b82-3172-8d46-c4a7d5c58ab7 | -15.70597 | -46.63869 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2faa0d62-17c3-3603-95aa-b324b5e9f442 | -13.73862 | -47.96865 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac094bd-e73e-3124-a4d4-04d3142502c9 | -12.68227 | -51.18192 | 2025-10-11 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 677d2929-36a1-3b8f-8883-8fbe326eec4b | -13.29561 | -48.4988 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8684c5f-5497-3535-baac-3ed04de89300 | -11.72051 | -44.29123 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40f5e537-48d2-3f21-b6fa-ab38418ba2e2 | -11.75955 | -43.32022 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63a49102-4bc0-30c2-9e53-83a0bb50c458 | -13.85413 | -45.83596 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3a37972-1144-3b60-899e-2a98c7953a4b | -9.40944 | -45.78112 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40c2d5ff-9715-3459-af05-75e048206753 | -15.22575 | -46.38687 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5616a6fa-fa37-3d87-bc80-7e30164250c5 | -14.74565 | -46.13317 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ad241de-e439-34a4-be58-281801414386 | -13.31943 | -47.12671 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c672e05-55ec-3c28-9cb4-071858a11f02 | -14.99861 | -45.57993 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24bac28e-d0dd-310d-a731-64f5aafdafee | -13.00125 | -47.90454 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96bc533b-6b65-3d88-a8ea-617ef049ea00 | -10.17301 | -44.54448 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ad95478e-0842-34cf-b2b1-995039d13100 | -12.74267 | -48.64462 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 461c960e-80d6-32ac-b9bb-7ce43c481808 | -13.21495 | -42.35042 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 89f1e744-1596-3c0b-a89d-6f58549bfbd6 | -15.50375 | -49.46194 | 2025-10-11 04:34:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 363e94a3-1e85-3e73-8172-d1add580f2dc | -13.22522 | -42.34446 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4fa7fb3-971e-3f4a-a005-70472d13ed82 | -14.7462 | -46.13487 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cb03c4c-b432-35b0-b867-dedd7db70100 | -11.74981 | -43.39099 | 2025-10-11 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bb8fbab-5e67-349b-ac4a-4461bfabcac9 | -15.49793 | -47.98785 | 2025-10-11 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4ef038c-ea86-3d0e-bf35-382fbc7cc4ab | -11.53465 | -49.28023 | 2025-10-11 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 716e7f23-3ede-3d30-ba84-0f18c3031857 | -11.99161 | -49.85656 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1abe7ac0-ab0f-39be-843a-ad8d1c061992 | -10.17889 | -44.58429 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 862afa2a-4b7f-3205-a568-d7ee65a7494c | -12.72922 | -45.84158 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c809944-d732-367b-83c1-b1491866dbff | -9.11035 | -45.03697 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33715855-c468-303e-ac75-ede3aec42e48 | -11.92307 | -49.85988 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e59310fb-cea0-3911-8d03-8341cc95c6d4 | -13.66249 | -48.74429 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a03dd53-cafe-374d-be42-63269d121946 | -15.70963 | -46.63905 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5ffcdf3-e94d-3a5e-b533-8938a37d28d4 | -14.93881 | -46.75101 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 014bc011-897e-386d-b3d8-86277a5067c6 | -15.69147 | -46.63651 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b21d2a6-34ff-362e-9a25-95b8842317d2 | -15.01284 | -47.56842 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed533d0e-bd9b-3f50-970f-56695882c2d5 | -13.21544 | -42.34801 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 61db2b2d-3d0c-39ff-817a-a9b71ea90a84 | -12.63663 | -48.31728 | 2025-10-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b42d31f-b865-303e-abe3-5b06967b63ce | -13.48577 | -42.01498 | 2025-10-11 04:34:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 749012d7-40dd-3fcd-8dee-04993555e82a | -13.36951 | -47.73832 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3be963eb-9ca2-339f-a755-24a80b3d99dd | -15.40282 | -47.2958 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ff86568-956e-3698-bcb1-f5e1e5fd0f80 | -13.39888 | -47.75052 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0f1e76c-5309-3369-af84-6a800ce884db | -11.62446 | -48.79282 | 2025-10-11 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30d81750-c4f6-3823-9922-c28bce4e95f8 | -14.98601 | -45.55839 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3d3d3be-997e-3369-b17e-cb4391bde076 | -13.66581 | -48.74485 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README24.md)
