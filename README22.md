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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05df2b54-dd51-3184-8997-f548474ac598 | -3.79512 | -51.38713 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6921b43-e5a8-3b38-a94c-77c292af616b | -1.64334 | -55.1723 | 2025-11-06 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40cbc7f3-f010-3be1-bde9-ceff8ced74da | -2.84326 | -49.40863 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b9b0ae4-a7ff-3557-b4f7-67ee657dcfcb | -16.30408 | -45.09163 | 2025-11-06 04:46:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e5f2c83-9634-380a-8a7e-a13502a82a10 | -10.226 | -56.77719 | 2025-11-06 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07cacdc4-8541-3f2a-bce2-54f2e4e184d7 | -10.33167 | -49.63477 | 2025-11-06 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c775ce0-0ae7-3a09-9c84-43c1162fd813 | -12.81784 | -43.7776 | 2025-11-06 04:46:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55efca52-b649-329e-ab77-31e6b6523134 | -10.3311 | -49.63857 | 2025-11-06 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d91c9eb-c9f1-3bd1-a82a-e97b64dd0aa5 | -15.36821 | -49.20778 | 2025-11-06 04:46:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ce6d4c4-15fc-3016-8029-057e9c121c53 | -10.93299 | -48.82296 | 2025-11-06 04:46:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6b0e488-8a75-3c0a-b844-67adf00848c6 | -10.3351 | -49.63531 | 2025-11-06 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 69e55868-99b1-3418-9da7-2ef412a0fd35 | -9.8869 | -48.29608 | 2025-11-06 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34dc8c5c-9f0a-39cd-b90c-48ecbedec983 | -9.44815 | -56.64605 | 2025-11-06 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f66b0d7f-250d-35b9-a61d-60e84817259d | -16.3083 | -45.09787 | 2025-11-06 04:46:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8130c355-b568-3408-b197-dda5fb75b245 | -10.93239 | -48.82713 | 2025-11-06 04:46:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5722784a-faf9-317d-9bfd-62631a4bcc1c | -11.84493 | -47.92591 | 2025-11-06 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 358f38d6-28cd-3053-9de4-1e60b5e74381 | -12.63899 | -55.71001 | 2025-11-06 04:46:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad4b298a-5166-3d1a-80a8-53ad575571af | -16.55821 | -45.08708 | 2025-11-06 04:46:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66e4a2b3-c114-3c71-b75b-51982cdf236c | -12.0716 | -56.67832 | 2025-11-06 04:46:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28fa43a1-d2ea-3c78-a4ce-e7559ccb78a9 | -11.10193 | -54.75518 | 2025-11-06 04:46:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e08fef73-3b8a-3437-a97c-0587d393b88c | -16.31137 | -45.61594 | 2025-11-06 04:46:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18ca00e3-c3a6-3b98-a164-05b88921357c | -8.06795 | -54.92229 | 2025-11-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8eef650b-e963-3db7-8a7b-74c20abc79ed | -11.72665 | -59.30572 | 2025-11-06 04:46:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 243283d6-ec32-3658-81ab-228f66dd1b98 | -16.55888 | -45.08145 | 2025-11-06 04:46:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6accd8f-57c3-3d47-a223-e8fc8f38f3d4 | -14.47252 | -52.79576 | 2025-11-06 04:46:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fac91349-1838-3632-a183-d199633be537 | -11.73127 | -59.30652 | 2025-11-06 04:46:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83d5d150-c288-36eb-97a0-d6fc58ba67ca | -12.81821 | -43.77455 | 2025-11-06 04:46:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eed2c7c5-ffcb-3a9c-b6e0-1fa4d644f859 | -8.59992 | -54.66072 | 2025-11-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 770a56d4-bed4-3891-b5b3-055e1b3345a4 | -8.04872 | -55.08473 | 2025-11-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb2e500d-7592-35c9-a5b1-20b5f5fa0fe2 | -11.7299 | -49.8451 | 2025-11-06 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 975e69a2-63ac-3c20-9fa8-8e8c6bd94b54 | -9.88327 | -48.29552 | 2025-11-06 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cc4bc83-37b7-3cda-936c-f8ce2dcdcd3c | -9.78077 | -44.20273 | 2025-11-06 04:46:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 994f5ad0-7177-387e-b9c8-987a852c4515 | -16.3095 | -45.6147 | 2025-11-06 04:46:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cecbbd4-0840-37a4-8ba6-e55dbf8fa3f6 | -11.38569 | -49.19249 | 2025-11-06 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53b7669a-569a-3640-b420-6bea8a59e4f8 | -10.07396 | -42.74154 | 2025-11-06 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a8cfe7ca-7d7c-3b51-aae2-3ba1975e6073 | -9.59632 | -54.72128 | 2025-11-06 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d5de613-4efa-3adc-a507-20b6eae791df | -9.44473 | -56.64176 | 2025-11-06 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3660006-eee6-3673-8e03-5abd3b0d873f | -11.54234 | -49.92654 | 2025-11-06 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37b7c632-be2b-3173-8516-1df4c00cdcfe | -11.63115 | -49.41922 | 2025-11-06 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df6e444e-5207-3ae2-b5a4-69f1774186a4 | -12.07108 | -56.67488 | 2025-11-06 04:46:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de39530d-ab65-35e3-b074-0b3ca35a45a5 | -16.55399 | -45.0808 | 2025-11-06 04:46:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e641f228-379e-3f25-a215-281d490e0aa9 | -8.11617 | -55.08076 | 2025-11-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b24dac0b-8394-335f-a5aa-f0e6ef272c1f | -8.1199 | -55.08136 | 2025-11-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 336750a0-e6ec-308d-9791-ea876b940ff3 | -11.63466 | -49.41977 | 2025-11-06 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb070b8e-d5ae-36c9-8e5d-bdc8b2cfab5b | -10.23 | -56.7779 | 2025-11-06 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b973681f-b688-39b4-9654-c140386baae9 | -8.32668 | -55.03365 | 2025-11-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff656d28-7e41-3a13-809a-419a3f4ca45d | -10.33453 | -49.6391 | 2025-11-06 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9700140-8465-33d6-bf1b-e9d11688ca4d | -9.78144 | -44.19771 | 2025-11-06 04:46:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e20ff6-2a61-3936-a375-9dd1c30c9d24 | -11.73048 | -49.84125 | 2025-11-06 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc14c7b-112a-36c3-bd6e-787f6378c52c | -9.44413 | -56.64532 | 2025-11-06 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fbce465-c659-35d3-a47a-1777d7a90fc2 | -11.7359 | -59.3073 | 2025-11-06 04:46:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03253fe1-c145-302a-bc79-85d12e7145ee | -11.73037 | -59.31139 | 2025-11-06 04:46:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a4107c5-f073-3b2c-a1cd-16dea58f8043 | -11.73501 | -59.31216 | 2025-11-06 04:46:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a513c3-0a68-37d6-adcc-ac256e404663 | -20.72187 | -47.94624 | 2025-11-06 04:48:00 | NOAA-21 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78f47f39-c35e-3b1b-9bd7-53938cf1cbe3 | -22.12024 | -44.70534 | 2025-11-06 04:48:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 086c4299-ec9d-33b7-90cf-01c1363995bf | -17.96526 | -52.69864 | 2025-11-06 04:48:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6769e10d-04f2-3a62-b344-e35edb645702 | -17.96858 | -52.69918 | 2025-11-06 04:48:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b54f4e1c-e3c3-3a63-be64-2dae5f5ec3e4 | -17.19772 | -50.87336 | 2025-11-06 04:48:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e9e1510-1027-3f79-8b14-0a615b13a940 | -18.50967 | -53.49012 | 2025-11-06 04:48:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9008084a-4951-3a40-9dba-95b509210f79 | -17.1983 | -50.86935 | 2025-11-06 04:48:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 849a19b9-39e3-3939-8e42-1b812b98c807 | -17.14085 | -44.67201 | 2025-11-06 04:48:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3f4ab6f-d761-38f3-8206-92b9d1cec3ed | -22.12561 | -44.70603 | 2025-11-06 04:48:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6284b89-862c-3211-b475-54623a1b188a | -17.19482 | -50.86878 | 2025-11-06 04:48:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 439b6310-d2e3-3195-aa04-28133e3439d6 | -17.19424 | -50.87279 | 2025-11-06 04:48:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0935bf35-2bee-38e9-81e7-4123ea627210 | -17.1405 | -44.67504 | 2025-11-06 04:48:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86278817-e90d-348a-a6cd-56d7a6c65094 | -18.51298 | -53.49068 | 2025-11-06 04:48:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b5cef95-f60c-3e4c-a50d-8051de748ac1 | -3.9324 | -47.6962 | 2025-11-06 04:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 920feceb-a73d-3cd7-9dec-22eaea402e23 | -29.27011 | -52.83229 | 2025-11-06 04:50:00 | NOAA-21 | LAGOÃO | RIO GRANDE DO SUL | Brasil | 4311254 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 45d99ed7-1e7a-399f-8f8e-194f5f84c411 | -29.7302 | -53.87373 | 2025-11-06 04:50:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 59088c69-5955-385b-bb96-0a6db5903bc4 | -26.85967 | -50.55316 | 2025-11-06 04:50:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bf7bc0dd-945c-3561-a846-590fc85e491a | -26.17777 | -51.21788 | 2025-11-06 04:50:00 | NOAA-21 | PORTO VITÓRIA | PARANÁ | Brasil | 4120309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c5f5170-7e2d-39ce-90fc-ee87818504da | -26.17816 | -51.21555 | 2025-11-06 04:50:00 | NOAA-21 | PORTO VITÓRIA | PARANÁ | Brasil | 4120309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 830f8646-e260-33bc-8598-d47eb619c615 | -27.3594 | -49.99085 | 2025-11-06 04:50:00 | NOAA-21 | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a2802e5a-03f0-32c8-bcb3-a00fe2e1b9fc | -29.6326 | -56.8683 | 2025-11-06 04:53:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| a0e40d2a-2d34-358e-bf48-ea79e2ab7939 | -30.25719 | -56.62033 | 2025-11-06 04:53:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d5484234-fdec-36a4-a669-996579513803 | -4.5747 | -43.325 | 2025-11-06 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 40d27dc4-1296-3b06-8092-7351bcec7b7d | -3.9324 | -47.6962 | 2025-11-06 05:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2506f3c9-070e-35c3-b629-98b89439d0c6 | -4.5932 | -43.3471 | 2025-11-06 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f71a1d7a-22ee-38b4-a393-a248be2d09aa | -4.5934 | -43.3239 | 2025-11-06 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 82a4db52-2ae3-3183-a853-7ea433d5fbe0 | -4.5934 | -43.3239 | 2025-11-06 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| dc55fb9b-2eab-3024-a6ac-7fc26560724a | -4.6119 | -43.346 | 2025-11-06 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 788b6ba5-952f-3aca-88c2-1ee7d2f0c921 | -4.6121 | -43.3227 | 2025-11-06 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f5da971b-f6b7-37d3-b55e-f9d4ffdaa506 | -4.5932 | -43.3471 | 2025-11-06 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 887c3577-2936-3a04-9bc8-aadaa4bbe9fd | -4.5745 | -43.3483 | 2025-11-06 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2172fe79-fcdb-3513-869e-bd1bfd94712c | 0.44822 | -60.49603 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4047f1cb-55d9-3aa4-8c5f-310863fa59c1 | 0.44268 | -60.48667 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c02a02-8dfd-3379-a7cb-10ed03391847 | -1.62519 | -53.71561 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94af0d5d-838d-38d3-be6e-6e65fccd719f | 2.62048 | -51.0112 | 2025-11-06 05:12:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50d518fb-6d69-36ea-a62d-23d22114135b | 2.61971 | -51.00636 | 2025-11-06 05:12:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a50bc9-94c3-38e8-95fa-8f04313e9398 | -1.63225 | -53.71672 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e185c2-b46d-3a2d-993b-3e68b7b522f0 | 1.68912 | -61.07772 | 2025-11-06 05:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e9fca94-d8eb-30bd-9540-fc762981c413 | 0.45057 | -60.4854 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b339f44-d346-33fe-9f92-54faa9028e97 | -1.9707 | -52.10793 | 2025-11-06 05:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 924367ac-6c8d-3d9c-b548-2f98b9841a46 | 0.45286 | -60.48363 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23ab9d0b-586c-3afd-8d15-22f9f09db458 | 0.44977 | -60.48042 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7713b5f2-4648-392a-a7f6-9dabdd293677 | -1.62293 | -54.70971 | 2025-11-06 05:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1b4c54e-ae89-32f1-92a0-95f861f48940 | 0.44891 | -60.48423 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a358c13-d696-3df2-bad1-c64635350830 | 0.45362 | -60.4886 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0706f792-56b8-3d85-86a4-a915dfeb5ff2 | -1.62811 | -53.72009 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2612a736-7264-3986-93f8-c81d3ce44bfc | -1.63866 | -54.06265 | 2025-11-06 05:12:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README23.md)
