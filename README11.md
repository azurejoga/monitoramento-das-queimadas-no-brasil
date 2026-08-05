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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69d48c9f-e3cf-3b30-b298-3029832e671a | -17.99434 | -47.15512 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d07942c-41bd-3f02-915d-1a4078d06d1e | -22.26153 | -46.95282 | 2026-08-05 04:04:00 | NOAA-20 | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cc207e9-b9e0-39e9-8c7b-87485e48eee4 | -22.10701 | -47.00256 | 2026-08-05 04:04:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fc696ed-dc6a-39ab-9072-b81d23a8c1ef | -20.38734 | -49.30843 | 2026-08-05 04:04:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 5145280a-0385-3453-9ca3-8409a9f8acef | -17.98092 | -47.15718 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3bff1836-23cb-32ab-afaa-1e5ec9ddaf26 | -20.21421 | -41.45348 | 2026-08-05 04:04:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6db4ed6-e72e-3202-9bb7-8d2b4775114d | -20.21478 | -41.44982 | 2026-08-05 04:04:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e854102-eca7-3ca1-aa9c-d6b7210623ca | -21.67339 | -47.8252 | 2026-08-05 04:04:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 261872e8-094c-3672-bce0-7b2a52554060 | -18.9922 | -46.27822 | 2026-08-05 04:04:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdfbf42f-8722-32df-a1f1-ece9b4c270d0 | -20.38736 | -49.31253 | 2026-08-05 04:04:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2bf7692f-2faf-3c72-8880-31f651d48dba | -20.38837 | -49.3074 | 2026-08-05 04:04:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d8215dd2-7cbf-3b0d-8329-61791055ae79 | -22.77319 | -43.45962 | 2026-08-05 04:04:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fe500e84-7bb6-3b89-af56-0901570b8bff | -17.98585 | -47.15409 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49c8c178-1860-3d12-895c-2758e445e42b | -20.88562 | -42.78051 | 2026-08-05 04:04:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7441cb0f-a129-3575-a690-6860b142d8c4 | -23.4565 | -46.36226 | 2026-08-05 04:04:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 41c3c631-c827-3f5a-8278-63b7685c4d5c | -22.91019 | -42.44782 | 2026-08-05 04:04:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7898cdcf-8c1b-3bef-a6dd-085a240f7b47 | -23.45931 | -46.36774 | 2026-08-05 04:04:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.8 |
| 36b0f76c-5a59-37ce-9636-b5e90c02e059 | -18.25289 | -43.59804 | 2026-08-05 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe0e29a1-e879-3798-89d3-5403b78070ab | -21.29827 | -49.04819 | 2026-08-05 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ece06c4d-d05d-31c7-b84f-28408ed742d2 | -20.38379 | -49.30639 | 2026-08-05 04:04:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ae071736-a599-3749-9fbc-41665c4132b3 | -21.3342 | -43.70122 | 2026-08-05 04:04:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4f66641c-146e-386b-abeb-3fddaa48d32d | -17.86609 | -44.17958 | 2026-08-05 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ddc02a8-8617-398c-853b-0ba3b8cd2a47 | -21.34542 | -41.09325 | 2026-08-05 04:04:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1cad280b-e789-31f8-addd-de64176c446e | -19.87905 | -44.05241 | 2026-08-05 04:04:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 140ae495-8fa0-3c51-b367-59a08bae1a16 | -21.26356 | -48.7399 | 2026-08-05 04:04:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 209d3f71-730f-3f0c-8ebd-6a65b2139994 | -11.1828 | -54.9194 | 2026-08-05 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 60344f0f-9acb-3126-9041-65a4834453df | -11.2019 | -54.8974 | 2026-08-05 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 550791da-fffc-3366-9bbf-29edfc732083 | -11.1833 | -54.8787 | 2026-08-05 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1b827236-b1da-30a7-aa86-f2baecba76ee | -11.2017 | -54.9178 | 2026-08-05 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 11a3715c-b72e-3faa-a4b1-106848b048f5 | -11.1642 | -54.9007 | 2026-08-05 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 774b1db8-0d2a-3dcd-8ede-180ec28e911d | -12.5947 | -46.9301 | 2026-08-05 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3640a265-4077-30f4-a468-d00289347ca7 | -11.183 | -54.8991 | 2026-08-05 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 32764637-65a2-3cd2-b240-629e696936c8 | -6.1495 | -47.1771 | 2026-08-05 04:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3b554cf2-b84d-3fae-be13-b4943cda2823 | -11.2019 | -54.8974 | 2026-08-05 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| bc92add4-39eb-3760-9f2c-3218a5474b72 | -11.1642 | -54.9007 | 2026-08-05 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cc22ea77-e3c6-3d31-8016-c0832d22f444 | -14.2161 | -54.4287 | 2026-08-05 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 513c783b-fa4b-38cc-a8e4-fb9cbe846e13 | -11.183 | -54.8991 | 2026-08-05 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 9dfd7b08-7293-3deb-a1b5-c7fe51f996db | -14.1972 | -54.4102 | 2026-08-05 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9466f9a6-46f8-3693-95f3-e61ff5f0c9dc | -14.1969 | -54.4309 | 2026-08-05 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 3b66e5cb-80da-3b4f-b964-9c682855c810 | -11.2017 | -54.9178 | 2026-08-05 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 992fc1de-dac8-3fb5-b335-9006422781a1 | -11.1833 | -54.8787 | 2026-08-05 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 27da855d-eb18-314a-a47d-09bad0757d1b | -11.1828 | -54.9194 | 2026-08-05 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2449ebdb-6c9b-38ee-ada2-96e09344b027 | -11.1828 | -54.9194 | 2026-08-05 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c42dc8a6-74a2-360a-ade1-bc83246c1a63 | -14.1969 | -54.4309 | 2026-08-05 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| bcbc714f-90e6-30e3-a2e3-f41085164d9e | -11.1642 | -54.9007 | 2026-08-05 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4f0b94d8-6813-3149-83a3-dc7db0f5de25 | -11.2019 | -54.8974 | 2026-08-05 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 46f6ae5f-dda2-35ce-9ff8-953f5e65ae58 | -11.183 | -54.8991 | 2026-08-05 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 496d7489-c15a-3b8e-ad43-4a48170a6347 | -12.5947 | -46.9301 | 2026-08-05 04:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b4290c33-db0e-3531-bd2c-583b6a9a0ba5 | -11.2017 | -54.9178 | 2026-08-05 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 9775b29e-18f2-3468-856b-378b7047ba29 | -11.183 | -54.8991 | 2026-08-05 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f0786b0a-70c0-33dc-9551-a95f68b06fcb | -14.1969 | -54.4309 | 2026-08-05 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| da13c6a2-52fc-3fe6-9868-648a39bd0799 | -11.2019 | -54.8974 | 2026-08-05 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 0be2b507-e15e-3177-8a8b-ed2a4e4dca60 | -11.1828 | -54.9194 | 2026-08-05 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7bbc0714-e72d-3ac5-93f5-0909060bc60a | -12.5947 | -46.9301 | 2026-08-05 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 522de269-1188-3d42-bb7b-9f7c26aec28c | -11.1642 | -54.9007 | 2026-08-05 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9b6b8cef-6078-3125-974f-7d80f032c3dc | -2.3125 | -48.63137 | 2026-08-05 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0699a513-b6e5-3384-b220-2111d6b2ee77 | -2.87207 | -50.47464 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d685a9-d095-3e33-b901-60602a793386 | -2.95105 | -50.31879 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e3efe1c-2102-37a2-bddc-d2c76186b9aa | -3.16713 | -48.14118 | 2026-08-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 593eb66e-edb6-3e70-93ff-44766a061ef6 | -3.42173 | -50.13551 | 2026-08-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cede0cf-79d4-3084-a408-5c1d43d5fae7 | -2.81608 | -52.28884 | 2026-08-05 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7211ecdb-95e0-3af4-a4b0-1e338c3177b2 | -3.6795 | -47.64839 | 2026-08-05 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd9eef70-f043-36c1-8ff5-99048ee3a1a6 | -2.46609 | -54.67421 | 2026-08-05 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc55cb5f-a81e-3e3a-9530-8cc2eb08d71b | -2.08894 | -54.44142 | 2026-08-05 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ca6605c-9bcc-3b01-9fa3-feda91aaa99d | -2.3252 | -47.2009 | 2026-08-05 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 931bd1f2-2f8b-353a-a011-b2bfdb9d1af0 | -2.68806 | -47.35927 | 2026-08-05 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58967acf-af6d-3e9a-8ad6-3178838fd05b | -2.86877 | -50.47413 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b3bbb06-774d-3c97-b152-0949d01a64d0 | -2.691 | -47.36385 | 2026-08-05 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a1a2f6a-5f91-3c63-8185-018c7d30f2ec | -2.94721 | -50.32171 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae78f7d-f742-3f12-ab0a-66857038895d | -3.1878 | -52.88279 | 2026-08-05 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cadbe9f-b4ae-33ef-8a70-c9692519d981 | -3.66826 | -49.46708 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9b08597-eb41-3bec-bdc8-4279325169d5 | -2.96497 | -50.3596 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd5fef28-fcc5-3e91-84c8-0b467bd12485 | -2.91754 | -54.16526 | 2026-08-05 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77a8ec9-b511-3017-ac85-0ee732590097 | -2.95382 | -50.32273 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0db8ba6d-3de3-35ff-9ce0-3c472f3be36c | -2.50509 | -49.3805 | 2026-08-05 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c39cd7ab-82ab-32e6-af3a-8f00e2c52480 | -2.32734 | -47.20407 | 2026-08-05 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b32633b1-dc71-38c8-ba10-9a7bbbe390cc | -3.1867 | -52.88256 | 2026-08-05 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c556874-93ab-36b4-a2eb-d773975cbe3c | -2.95435 | -50.31929 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c96f461-81fe-3b43-a1aa-bacec036eae2 | -2.91379 | -54.16468 | 2026-08-05 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82ec85ab-6a09-3b33-a854-7403ea726d60 | -3.16429 | -48.14172 | 2026-08-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5acdca98-85fa-38ee-aa65-c8fc8c301984 | -1.80482 | -54.47828 | 2026-08-05 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61ec8a0c-eed5-3cb5-a522-e77a28824d8f | -2.31698 | -48.58044 | 2026-08-05 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c158cb24-2238-326c-bfd5-acf3e4c470e0 | -2.04706 | -48.03716 | 2026-08-05 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26c292c9-ca9d-3258-a0a0-a99b49f68a33 | -2.74332 | -48.70419 | 2026-08-05 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57efeb5e-0110-3996-8179-2b3e0c7fb608 | -2.97445 | -52.15426 | 2026-08-05 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d856705-a6d4-36cb-a58a-f997b697dc89 | -1.59219 | -50.43592 | 2026-08-05 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85c2d5de-e19d-3631-ae6f-ebe6df9ea467 | -2.95712 | -50.32323 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73d98bcb-cf43-385e-b96b-3ffa74678ef4 | -2.69162 | -47.35981 | 2026-08-05 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d3180f2-bc27-3c99-b49f-bf5fe6c85d0f | -3.18842 | -52.87889 | 2026-08-05 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e47011ac-1515-36be-9a03-e62cdd54d163 | -2.50859 | -51.81341 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2ce98dc-2d54-3986-92fd-b3272f1885dc | -0.16459 | -50.40747 | 2026-08-05 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f8a6063-c5e6-3182-9d9a-9938596ab1da | -3.18717 | -52.8867 | 2026-08-05 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7068f7e8-332a-3cba-8305-1605e3b48479 | -3.31099 | -48.71612 | 2026-08-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 227ab3af-f8f0-3dcc-a3e6-e6d2cc180b4e | -3.67492 | -49.4681 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fb291dc-88cd-3bab-876d-126a15fb310a | -3.24944 | -47.92724 | 2026-08-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 752df994-0e35-3f9d-a812-76c8bacaebb6 | -3.02782 | -48.4113 | 2026-08-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94336de5-936d-3a0a-8437-c9bb0703015b | -2.87591 | -50.47171 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 679362ab-108d-3b23-9bac-44d1710a704f | -3.66771 | -49.47058 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b09ad197-8653-31bf-b4dc-bdd411bc4799 | -3.69194 | -47.63805 | 2026-08-05 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bccf73db-9cea-3d25-a3ad-cfb00fc4b493 | -2.31304 | -48.58352 | 2026-08-05 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
