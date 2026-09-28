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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc3972e7-acd0-3058-a9e3-4c16ea8bec6f | -6.62959 | -60.01418 | 2026-09-28 17:09:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 33ab240a-a73a-31b0-8bd5-3bc25e777747 | -10.57726 | -46.36681 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 64ef46d7-5b52-3701-a9b0-3679e3b16fa1 | -8.27347 | -54.74711 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 4dd3108c-f468-3995-ac4e-cec1a96fa3e3 | -12.85125 | -54.02958 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 797fd931-639f-37ae-85d3-d3292543e9c9 | -7.14805 | -47.54535 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 3368b34f-031d-3908-986b-a17ebe6bf784 | -9.32759 | -46.56425 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9438a605-6701-39b8-9428-896fb88b51e7 | -8.44703 | -44.66711 | 2026-09-28 17:09:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b21cac75-a85d-348f-bfdc-f304d47f1fee | -10.20608 | -49.99128 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 570b1efd-725e-3377-aab2-785ce314b875 | -8.15253 | -54.82293 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fcc4681b-4e43-3a22-9407-236e89f317a9 | -6.2099 | -52.90807 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| e90b6e88-277d-3190-a92c-d89a25128027 | -8.38288 | -46.52902 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 99fc5c55-f837-3a2b-b838-66dfce2a5b2f | -7.82307 | -55.13418 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ebab1903-f844-3f4b-9a1a-41be1a82d109 | -7.49871 | -54.97023 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 903976b3-b7c4-304b-a3ff-425fc4ecba2a | -11.4676 | -49.75257 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4e085f18-ac35-3441-9eb0-2d8c8dd8193c | -11.05394 | -42.99137 | 2026-09-28 17:09:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 04b06d64-0f55-31fc-bc55-52218889dc4f | -7.76731 | -54.79159 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fa84125-c4ac-32d3-8f1c-f4aa852ac252 | -10.45784 | -47.48301 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 879c2627-2fb6-3bc4-a4d6-93717c8b09e5 | -6.15882 | -52.9039 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3e9303fa-5dce-3509-8247-417d88007db4 | -11.53245 | -47.38697 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 66967042-be42-3972-bc1b-49394d90fb7f | -11.90393 | -49.99173 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 590a6888-42b8-33fb-b864-6a818d3dee12 | -7.69492 | -54.76456 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6d28564-7f66-3cd2-9fd1-213f69fa3989 | -6.19682 | -53.22421 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99a1c1d4-0b36-388d-a37c-ef36d50b2ce6 | -8.23289 | -45.41034 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f0c6e2e2-9170-3fd7-a17e-7530f4e7e40c | -10.21249 | -50.00563 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ec04d751-bbca-3f2e-a8c6-eaf22deb475c | -9.98089 | -45.34503 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2e77418-a648-3bb0-8585-090d4a616103 | -7.50388 | -55.02617 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0c499bbc-5531-3b1e-b6e1-cf253064323d | -6.20763 | -52.91649 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 31ae61f2-653c-3eeb-8fbd-b9dd21353feb | -9.96186 | -51.4488 | 2026-09-28 17:09:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2f6d8c62-9ab7-33f9-815a-22902763ab5b | -6.03702 | -49.56611 | 2026-09-28 17:09:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b3e6fe0a-1165-3950-b85b-791cc4abd0de | -7.70922 | -54.76947 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f9a6322-f795-3fb9-b527-75ce711f94a4 | -9.08271 | -46.54914 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15082154-135a-3bb9-9154-b61f724887d0 | -12.13358 | -50.34233 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3e7d16ee-328c-3133-a6ea-b60c04e6d63f | -6.78706 | -43.22459 | 2026-09-28 17:09:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 71f2ab51-a67c-3e42-9da4-902700192b1f | -9.96779 | -50.15457 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 7b1c3853-7bd3-3c13-95ec-03c4bd58cf7e | -12.21971 | -50.43581 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 77bdfc43-00f0-3fee-a222-b8363329f757 | -5.73518 | -45.05956 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 22ce7b86-7837-3561-acea-4546ca3a765e | -7.83021 | -55.13663 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c7c0a1be-891e-3f7e-8cfe-6f263e617b82 | -10.20915 | -49.98558 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 1da850d8-57b5-39ac-b939-10baaf4e0443 | -5.63883 | -45.53587 | 2026-09-28 17:09:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 87c07739-f15f-3a73-85af-21527dacfe98 | -8.32819 | -44.17467 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fdaaef63-0776-309b-968e-43612867f829 | -8.10098 | -44.00674 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f1c602b3-bb72-372e-96bb-a93fe3299991 | -10.8388 | -61.42302 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e460bbc0-215d-3365-b044-b3018e7ca6a0 | -7.50057 | -55.02668 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 81a20883-4da9-30c3-95c8-7918db7e85f8 | -11.17624 | -45.13052 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93a3f320-7eb3-37c0-88f9-a536a5174038 | -9.11168 | -58.90631 | 2026-09-28 17:09:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f97ff801-bf9f-357f-8049-d6af0b7c986f | -9.63786 | -46.76929 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f9f8bb0-056d-3c79-9a07-5f281630b213 | -7.33461 | -55.58761 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3f31625-f88f-324c-88aa-d45da3c8bf41 | -8.51953 | -48.11172 | 2026-09-28 17:09:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ba3bffc-863b-393e-b866-96157ad02250 | -9.93234 | -60.72181 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0c8a6e24-ec26-3281-84a4-a6e86e703241 | -7.69002 | -54.75465 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| db83785b-4c11-3de0-a24c-8d74659f659e | -7.16903 | -52.62184 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ce33498-152e-35db-a4fb-72ee22c7dc97 | -9.94701 | -49.36892 | 2026-09-28 17:09:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 15422dae-3dc7-3cbe-aead-498bf5db15dd | -7.50771 | -55.02913 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b3129d1b-9d39-350f-bccd-a427ccc3b7fc | -6.14083 | -52.72307 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d5944b7a-24d1-389a-98da-098617ca258a | -9.10159 | -46.53918 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e10cff0-cab7-3a96-9c68-5d49a4615806 | -8.1825 | -55.21922 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78f504a7-90dd-3dc4-99c9-a9c895e93bd0 | -11.20811 | -61.27689 | 2026-09-28 17:09:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2312126b-7c1f-3b44-ba1b-e2f59a1d4939 | -9.10145 | -46.53869 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0cdee71c-4638-335c-99dd-c6707ada123a | -11.19949 | -44.79706 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 92db132a-53df-3f32-b5ce-fcbf86c2f7b9 | -9.51608 | -46.37704 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f506127-2150-3e94-b2c3-62362eefda79 | -10.99549 | -50.70133 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c1e3434a-5723-3d01-8496-8078b26888a9 | -10.77831 | -48.74387 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ba570aa9-5868-3adb-b9ed-8dc22a380501 | -11.84356 | -50.86132 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 206ee269-9fdf-35e1-8eb0-67ba0b530e60 | -11.47064 | -49.7469 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fe979aa5-a38d-3d0c-8d68-d85bd878bc43 | -8.67455 | -45.3711 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ff18513-95d2-3436-a7cb-61e94cbffa5f | -6.04767 | -45.16844 | 2026-09-28 17:09:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| af8e755c-0299-37a6-977d-21aace8a77c1 | -9.07523 | -47.18308 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 28ac1f22-6ef0-3409-8506-4cced6e3517b | -7.49924 | -54.97369 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f360673-1c3e-324a-8046-25c9df27e937 | -6.23306 | -53.03269 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0549d8e1-29d4-3e6d-89c6-b132c7521f82 | -6.51114 | -55.3607 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 596d88dd-8337-3cd4-93f7-ad4431250233 | -9.67748 | -45.57291 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ab3a6746-7148-3649-92fe-92552283f959 | -4.31522 | -45.27233 | 2026-09-28 17:09:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5655e854-ea80-3c3b-91f6-0ca2f8f19c37 | -6.36451 | -52.69257 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 30624050-575a-308c-bc7d-1bccfd38ee35 | -10.82269 | -57.23022 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| acae20b9-40e8-32c9-abf4-6604d0ccb284 | -11.17559 | -45.12703 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 605129fc-997e-3799-b06c-bc6f8c5aa71d | -10.85636 | -54.07737 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 06545573-7a79-3d60-ac3f-f5d040b2a134 | -7.34597 | -54.94785 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c82fe388-2861-32ab-aea9-6c3a66985f27 | -9.98403 | -45.3618 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0bf1fa9d-f9a4-3912-a6c4-13f61c2b3407 | -12.81873 | -61.57307 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1eca0d52-43ad-3d67-b8a9-29ff0d0464d1 | -11.13107 | -51.18456 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 415e702e-050f-3e3e-9066-e6e3d1c4bd66 | -11.11094 | -51.17492 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f4fd8e0e-cf13-338b-b347-76c6fd0d5bbc | -10.951 | -50.68586 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56a3d13f-7109-345b-a07d-e9f7f96b8633 | -6.16384 | -52.82204 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ada0c40c-a40c-33d6-961b-e5f233b8474c | -6.01403 | -53.89952 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae399fb2-6592-34c6-90e4-a4b80f15f8f7 | -6.89335 | -52.48334 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b4142ddf-89aa-3685-9a73-fd736a3fb13d | -10.12856 | -45.1382 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c668f859-5a42-3dba-ae21-792f7feaf70b | -8.9694 | -50.97469 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 44c6324c-b178-3db4-a851-aea172b3faac | -6.11382 | -53.45872 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 29d3421e-e173-3b57-bb3a-9a42ac5b8b96 | -9.85353 | -44.94003 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0c777245-e6ec-3f7e-8d19-fa380baedd18 | -7.49235 | -45.9667 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72002a41-195f-3189-bfb7-d71e7f26fb52 | -11.39904 | -45.4211 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c12829c1-c22f-331b-b1d7-1a78d471d75f | -7.65846 | -55.10427 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86fc9d8b-39a6-3286-9c95-c23be7721ff4 | -11.45059 | -44.92001 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| df1b48d1-7514-3990-a700-1e732299b225 | -9.12863 | -46.46014 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42412de6-b89d-3d9e-aec1-bb8816f5091d | -11.98477 | -57.60935 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17b8a9f2-6438-3abb-a6ba-ea339fa14003 | -7.50441 | -55.02964 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| eb85fd6a-db96-315c-8397-e8945d011377 | -12.77934 | -54.0274 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 20158f06-b8f6-34de-a9b9-018b749837e5 | -7.38535 | -60.60915 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cc81a64d-8dde-3b51-9ae3-16995bae3ac0 | -8.28169 | -54.70972 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 324c2030-1330-3e38-84b4-0444c2ff9c0b | -10.74868 | -54.08409 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README162.md)
