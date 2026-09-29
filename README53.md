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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 309f25f2-d193-392e-8c86-27db9573e371 | -21.06822 | -48.83968 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cf7614fe-a7f9-3b9a-820b-82ffd548e7ad | -20.91817 | -47.46684 | 2026-09-29 04:55:00 | NPP-375D | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25735b30-44ba-3891-bc0a-d4209e32eb36 | -20.9141 | -47.46618 | 2026-09-29 04:55:00 | NPP-375D | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12ed5286-3021-3684-822b-8ad5fb0e5d57 | -20.827 | -57.69053 | 2026-09-29 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1a731314-0a91-3ba6-8705-1b1557e70f31 | -20.09591 | -57.20522 | 2026-09-29 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 62e20d9a-cf76-3b4d-9b45-1a76c4e09fbb | -21.06809 | -48.83665 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 68cecde8-bfe3-391a-a44f-e2f6c6ebb0df | -20.73111 | -46.92349 | 2026-09-29 04:55:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7dc26501-90ae-3f8a-bb35-cd89eedb6be2 | -21.06433 | -48.83601 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 37a429cc-27ff-30c6-8cd5-f964402118c1 | -22.16879 | -49.23645 | 2026-09-29 04:55:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a72a8902-d5e0-3290-be9d-3e8ce093546c | -20.99498 | -47.04086 | 2026-09-29 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7024c20e-eb0b-32e9-875d-1b4241d756dc | -21.32715 | -49.50549 | 2026-09-29 04:55:00 | NPP-375D | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2c37559-1a61-3648-8173-057bc7a99504 | -21.0555 | -48.8739 | 2026-09-29 04:55:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2edcd7e8-a285-3b9c-8ca1-0fc426cbf85e | -22.23328 | -57.14865 | 2026-09-29 04:55:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af65e860-91d3-3c78-90dd-a6fc13e88920 | -21.05231 | -48.87149 | 2026-09-29 04:55:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 59f09e2f-d473-3fbf-9c49-2d796ccd370a | -20.83034 | -57.68831 | 2026-09-29 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6fd55af3-8132-3fa8-b212-816a6f72ced2 | -20.83426 | -57.68914 | 2026-09-29 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 06e3c3b2-0860-3926-94db-bd0821231775 | -20.83092 | -57.69137 | 2026-09-29 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 573ddb9d-8843-3a46-92eb-2d088d0daf2f | -20.9945 | -47.04478 | 2026-09-29 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 868d8093-be0f-3807-b139-473fa1b78924 | -21.70119 | -47.17027 | 2026-09-29 04:55:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4479d59e-9bf4-3988-9557-156e6cfa116e | -21.79501 | -47.13665 | 2026-09-29 04:55:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 560232dc-fcbe-3bff-87ae-4a26191fcbce | -21.05237 | -48.86853 | 2026-09-29 04:55:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3d1760ef-c270-3a6d-9211-9d2ec08fde69 | -21.0607 | -48.83844 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 36ddc46e-094b-3e63-a889-778f3851b224 | -19.90379 | -54.58307 | 2026-09-29 04:55:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d8d4f34-7636-3b0b-9380-7a591d6ac846 | -23.00591 | -48.62455 | 2026-09-29 04:55:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7b9e8a2-b46c-3f23-ada2-5ff8768d6878 | -21.70143 | -47.1686 | 2026-09-29 04:55:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 41912468-35ff-36f1-823a-a9840e6ed80e | -20.69832 | -57.9601 | 2026-09-29 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| afe49a33-7223-3aa2-b236-a3a50dbcecdf | -24.36344 | -52.33654 | 2026-09-29 04:55:00 | NPP-375D | LUIZIANA | PARANÁ | Brasil | 4113734 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32ca9a57-5469-37a5-993a-2f21d5347489 | -22.09397 | -46.96256 | 2026-09-29 04:55:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91337f91-b468-3007-a65e-47839934d05c | -20.93847 | -55.41756 | 2026-09-29 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b3d0258-3637-3650-9359-283f3a2c2d91 | -20.35114 | -48.29647 | 2026-09-29 04:55:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad82edf7-f89f-3d0e-9d78-23085aba8d9a | -21.05175 | -48.87327 | 2026-09-29 04:55:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2153a817-2e14-3494-b82a-676accdc43a6 | -21.0637 | -48.84077 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c7cc80c-7796-3cde-a037-27575093649e | -20.82933 | -57.69359 | 2026-09-29 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ec7be410-0514-392c-8cdc-3858f919a83e | -19.90723 | -54.58372 | 2026-09-29 04:55:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f935752-3462-321e-90d4-a14ead99988c | -21.05925 | -47.03787 | 2026-09-29 04:55:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aaf0c5a-ed00-39a0-9dc2-720dbcfd94d8 | -21.06446 | -48.83905 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b56636de-a44e-3b01-905e-838f45fa2cb7 | -21.05993 | -48.84016 | 2026-09-29 04:55:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bed26b94-7758-3f68-8081-abf3c3662579 | -21.2412 | -44.32992 | 2026-09-29 04:55:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c417de83-e572-38ab-90c3-fd375152dbe0 | -21.05606 | -48.87212 | 2026-09-29 04:55:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5d9592ed-b7e2-36ff-b8a2-10e322d4df90 | -22.78448 | -55.39586 | 2026-09-29 04:55:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71a5c49e-dfc3-329c-9cee-ebdf1eb4ddae | -20.91764 | -47.46658 | 2026-09-29 04:55:00 | NPP-375D | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06de8318-4f9f-3975-a40e-a95c0bd9d36c | -22.09824 | -46.96319 | 2026-09-29 04:55:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aba6519-4e9a-3ef5-84d5-665819416efe | -23.01051 | -48.61987 | 2026-09-29 04:55:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a277f4f2-94c2-3f36-815d-cfee04b89ede | 1.84378 | -55.62477 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26825be5-5ade-300e-8fd0-92fc77093cab | 1.8494 | -55.61655 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a179e70b-74c1-3f3c-b9bd-59b216146f18 | 1.67392 | -55.90274 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67836808-f191-32fc-a046-3e6b419e6a90 | 1.68188 | -55.90898 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d776956-a250-3e60-a804-cd8bbc8019a3 | 1.71542 | -50.95089 | 2026-09-29 05:08:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b0c345d-8ba6-350b-bc53-a01413f78a65 | 1.05772 | -50.03663 | 2026-09-29 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5cb556-6805-3628-987a-5844fc262f25 | 0.52944 | -50.81404 | 2026-09-29 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef7e7d0e-2783-35b0-a669-8553de7b2fa7 | 3.28386 | -60.62963 | 2026-09-29 05:08:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb2dd027-b909-3b8b-aedb-9fbf4c54d1f7 | 1.8695 | -55.60219 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 218a05ef-1e59-3a8e-8e1b-f849846b7083 | 1.83424 | -55.62999 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23795a39-d3a8-3384-97d3-ed486873358c | 1.82578 | -55.62026 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47861a58-e2b9-38b6-ba10-ba7ef6067259 | -0.49339 | -49.12643 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fad41503-ad8f-36ed-b2de-f2f6bf021cb3 | -0.48863 | -49.12956 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62397db0-e9cd-3580-9944-840c606c815f | 1.65686 | -55.883 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 727986ce-e19e-3bce-97a0-13e71b75fb20 | 1.6711 | -55.90691 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 419ba721-7f57-3655-9206-1759ed909936 | 1.82411 | -55.63159 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baa93552-5141-3197-8d32-e0002ccd67ae | 1.67276 | -55.89545 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5527542-2729-3cae-927b-8c861d9daf41 | 1.67052 | -55.90327 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 257711a7-cf8e-32b6-bde2-841fb64b2022 | 4.00228 | -51.67484 | 2026-09-29 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa67480c-3bab-396b-9e81-672cfbf63cec | 1.66821 | -55.88869 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90436021-09bb-384c-8f14-c4ce14e89765 | 3.28242 | -60.62035 | 2026-09-29 05:08:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64f471ed-14e8-37e7-b823-9b1f57edabb5 | 1.69117 | -55.96752 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d29eaf2-8ac7-3106-bb0b-33af9eca14df | 1.69333 | -55.93716 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099f97f5-bd8b-313a-8d39-9cdb4e3b9664 | -0.48922 | -49.12578 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59967dd0-1301-35e3-b9bc-aa166fbdc6a3 | 1.68246 | -55.91263 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7666e9f2-0e6f-3541-94af-6aa24b49af8b | 3.2833 | -60.62207 | 2026-09-29 05:08:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4b46e8b-f78e-3df8-840a-97b572dee8c4 | -0.50231 | -49.12394 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e701a49-0db4-336c-a9ab-41515e591fd5 | -0.49045 | -49.14531 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6108063-d49b-3463-84d9-7c969ea36d3c | 3.38279 | -51.29311 | 2026-09-29 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ad246b0-311d-39d5-9636-40d16cff0ea1 | 3.43433 | -61.09294 | 2026-09-29 05:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc9012f0-eca6-3b61-88a3-40bd3573a0f0 | 2.56299 | -50.83944 | 2026-09-29 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d4a23662-0839-33e5-a7ed-d44cdce3885f | 1.67218 | -55.8918 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 419b253e-e000-3d41-b5d6-d3bd9160af37 | -0.48805 | -49.13334 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b200faff-6b1c-3c4a-803b-a1d3d7894255 | 1.82916 | -55.61973 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2dc0c5b-bd89-3527-a479-aafe893b0514 | 1.68777 | -55.96805 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6966221-06da-3800-968a-50251df06b50 | -0.48746 | -49.13712 | 2026-09-29 05:08:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a8ec500-0aab-38ab-abee-ca9dffffbdb5 | 1.67161 | -55.88816 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1db940fb-861d-36a5-87db-9c87757c55cd | 1.86503 | -55.57353 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e463951a-829c-3ddb-ac0a-349d1ff0ef91 | -0.50707 | -49.1208 | 2026-09-29 05:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2d8044b-1478-3d9f-88b9-55e92ad701de | 0.07611 | -51.14342 | 2026-09-29 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0191fe25-3d1c-3f9e-9bbb-eebbc8bc375c | 3.98377 | -59.76837 | 2026-09-29 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85b031f5-f78d-3ace-8a7b-8e39b4283e68 | 0.70275 | -51.43444 | 2026-09-29 05:08:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cedd3ae9-2728-346c-89a0-fbf693f38f0b | 1.84041 | -55.62531 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7e213a9-1dc5-38c0-b8c3-c5ce7c184858 | 2.08383 | -50.74804 | 2026-09-29 05:08:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e6736d0-26ec-3a05-b1e0-f292727c4349 | 1.68702 | -55.9194 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27f36361-b59b-3e85-b3d9-48b5c59c8a6d | 1.69391 | -55.94082 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9105e493-20b6-324a-af0e-4bf1cc01d217 | 0.53313 | -50.81347 | 2026-09-29 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4d0622-f441-3d14-925f-cc43dffd9ec8 | 1.82017 | -55.62852 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cec99ef-af48-325b-9d38-2a022d8b25a6 | 0.69918 | -51.43501 | 2026-09-29 05:08:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ae43deb-d7fe-36c2-b423-9212c2908802 | 3.43357 | -61.08791 | 2026-09-29 05:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8efbb2c3-639e-3887-ab0a-ab7b84e55282 | 1.82635 | -55.62386 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 323004ec-c519-3a79-8c8b-5be51948325e | 1.69449 | -55.94448 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16a13579-06f9-394e-8132-f2940297838a | 3.99886 | -51.67537 | 2026-09-29 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11bd704e-c2cc-3518-b0fb-69d832283108 | 1.69109 | -55.94501 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5055eff-55c7-3498-bcbe-c199fd137ef9 | 1.83704 | -55.62585 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65057ed-af85-3810-9530-345e9f408c6b | 1.67334 | -55.89909 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35654527-5efb-3eec-8086-6c8766b17a0f | 1.87065 | -55.56528 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
