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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6de18712-ecd1-3a68-99f7-6589cd85dafe | -13.29066 | -43.54982 | 2026-06-28 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e10c8c3-6c6f-38c7-a679-dc4b731cb18e | -14.04488 | -46.33348 | 2026-06-28 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f0c08ec-9982-3e95-839b-84f02d256671 | -11.20739 | -54.30207 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d1690117-9e30-33d1-a89a-bd7f0dcee90d | -12.19108 | -52.89666 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c98e5ca2-c841-304c-bb2d-ffd8be3edf14 | -11.21156 | -54.31293 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3cd07ae2-c11a-31a4-b516-ddd2fd1ba3ba | -12.18337 | -52.90671 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60fa7365-85dd-3fb2-ba20-cbf18bca6202 | -12.54086 | -57.19398 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8ded384-18d6-30e5-ab58-b1773366b5a5 | -11.21496 | -53.82396 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 82c39d38-ebf9-3c15-893f-003c738a8cc0 | -12.19471 | -52.87815 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d0802442-0c59-3e45-8ee2-29ff2315580b | -10.77672 | -54.11073 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a92dc3-9c17-31fc-8f51-eaa61d345138 | -12.19759 | -52.86345 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a3560791-dda3-35ab-b5ab-2806a0bcb1c3 | -12.08825 | -52.00402 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d3b2345-6881-3695-a450-29e1976dcbc5 | -10.93291 | -56.85148 | 2026-06-28 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82998da6-aad0-3143-8b37-0f0bb7061ab0 | -12.19439 | -52.90903 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c4ee4ae-741c-3907-83a0-51a032fc5c0d | -11.21115 | -53.82898 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a9fb68d9-e25c-36d3-a961-62430b498391 | -12.19543 | -52.87448 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 63229421-a12b-3c1c-a019-8f5d6001831c | -23.58349 | -46.43381 | 2026-06-28 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 910ff080-ae07-39f7-9cd6-6942c2c4c8cf | -22.59777 | -48.43601 | 2026-06-28 04:17:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93201a0a-7ccc-3b8f-bf95-44e3a5d4a2e9 | -18.47862 | -54.10944 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 45a7dcc3-f25e-3a59-9cd8-e1a8bb81df9b | -22.70003 | -43.36319 | 2026-06-28 04:17:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 41e3bf0f-c0df-336b-a9a6-143260a6c154 | -18.47407 | -54.1047 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8cf180da-5001-3183-a8cd-ebf1ef8c5004 | -22.69383 | -46.50657 | 2026-06-28 04:17:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 582f6442-c39a-3a3e-9274-248f9b2e4c8b | -18.46948 | -54.10022 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 041662a6-012a-3505-b6e1-ec6600ad25a3 | -21.26954 | -56.03381 | 2026-06-28 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efeebe3c-5d4a-3dd8-bba9-8d7963148f27 | -18.4839 | -54.11071 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5b0bdb2c-8cc2-37c5-8d69-9bb5296f17e3 | -19.90686 | -44.69481 | 2026-06-28 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0010c057-a622-3fc3-80fd-9cfe69b1faff | -18.48466 | -54.10709 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0601ad54-b0d7-37a5-8f59-b3e5f1cf6df8 | -20.09484 | -46.41805 | 2026-06-28 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3e228f9-fa57-341c-8291-34df8b90dc01 | -20.39894 | -45.27388 | 2026-06-28 04:17:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 10324c65-36ad-3182-8de0-ee64db2db8fc | -18.47551 | -54.09787 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 213fb867-0e2e-3422-b6c3-17483d9e4c82 | -22.351 | -45.77543 | 2026-06-28 04:17:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6e38d29-3c07-30e9-8671-607d6492ac98 | -18.49234 | -51.61609 | 2026-06-28 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 065c0f4a-92a5-3d2b-8e52-59a32e4b7f6b | -18.4748 | -54.10126 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c6cffe1d-1b63-34c7-b4cf-606a1992659b | -18.48012 | -54.10233 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| efb38d30-ff5c-31ac-ac26-054917661785 | -18.47938 | -54.10583 | 2026-06-28 04:17:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 10b9ac26-48b3-3d56-bec9-7924f7dc00f6 | -23.32082 | -46.52638 | 2026-06-28 04:17:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fe43ad20-9c68-3d58-8e07-70ec5a5a9416 | -20.97501 | -49.74435 | 2026-06-28 04:17:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| dd7a343d-1d8b-388e-ad53-cc1840a5e383 | -23.48984 | -46.80201 | 2026-06-28 04:17:00 | NOAA-20 | OSASCO | SÃO PAULO | Brasil | 3534401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5e098e63-e908-30de-b995-9ba4d4a705f3 | -19.90948 | -44.04744 | 2026-06-28 04:17:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62bf00a9-8924-345e-a654-bcd12888a95b | -23.06873 | -45.55551 | 2026-06-28 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd4363da-9f74-35c5-a5c3-3a3c46c5dc4c | -12.194 | -52.8657 | 2026-06-28 04:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 04f373f6-0d07-3f1a-b5f2-de349e69f122 | -11.2093 | -54.2848 | 2026-06-28 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 43f7fe0a-55af-3145-93c8-66c46e2119b1 | -11.2279 | -54.3036 | 2026-06-28 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 31f97b35-3c12-3978-8056-3f13c8508488 | -11.2088 | -54.3258 | 2026-06-28 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 934d6780-fe0a-3754-9274-62c4593fc006 | -12.1937 | -52.8866 | 2026-06-28 04:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 034b5489-c6da-3c4c-b190-306e33979fe6 | -11.209 | -54.3053 | 2026-06-28 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 274.6 |
| 658ebd3c-248b-34f2-b793-380cd3c49221 | -12.2131 | -52.8637 | 2026-06-28 04:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a5a25a71-10ca-33fe-bfae-9c427f4b8725 | -12.2131 | -52.8637 | 2026-06-28 04:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e66bedc6-0f18-359a-a879-1fe322cb47b4 | -6.9791 | -42.9034 | 2026-06-28 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 67c5be52-b475-3812-9e72-bd88c185b441 | -6.9793 | -42.8798 | 2026-06-28 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 6df980c7-f373-3580-95d2-20cf3aa27266 | -12.1937 | -52.8866 | 2026-06-28 04:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 9e5f4eb1-97d3-3654-ba2c-3008a0bfc1ce | -11.2093 | -54.2848 | 2026-06-28 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 26016cea-0683-3861-8ce5-ed63ae750adf | -12.194 | -52.8657 | 2026-06-28 04:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e08dc656-81ab-3d21-9a28-fe3c12847a17 | -11.209 | -54.3053 | 2026-06-28 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 307.3 |
| 0ff04967-29ab-3ace-9ea3-63599c17d1dd | -10.2941 | -57.138 | 2026-06-28 04:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4d190e7c-90b7-3ed4-8c08-ad46c59e7428 | -11.2088 | -54.3258 | 2026-06-28 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b19d0c6d-49d8-3b17-8889-9e25238c429e | -11.2279 | -54.3036 | 2026-06-28 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| eaf3feab-adca-3d3d-90e4-2334852c1747 | -11.2093 | -54.2848 | 2026-06-28 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ec94bfed-3375-3a47-95af-2567257eaeda | -10.2941 | -57.138 | 2026-06-28 04:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7e37d532-b906-32b9-95da-aa52190a4266 | -11.2282 | -54.2831 | 2026-06-28 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5e3e0e2c-5306-38dc-9ce1-8b8b66be9ff1 | -11.2279 | -54.3036 | 2026-06-28 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 5abfb162-b2e5-3f30-9c97-47562d1588ce | -12.2131 | -52.8637 | 2026-06-28 04:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| cc8707fc-345d-3fe1-870c-3e154de025d5 | -11.209 | -54.3053 | 2026-06-28 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 230.4 |
| 2c01cedc-aff1-3dae-ab62-71d119b548e6 | -12.194 | -52.8657 | 2026-06-28 04:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c553c673-35c6-39f7-bd63-cbf2e5638555 | -12.1937 | -52.8866 | 2026-06-28 04:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| a3b0bb8b-c455-3d88-a344-07569f07de68 | -10.2942 | -57.1182 | 2026-06-28 04:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6c36d388-1155-3424-97f3-fdb53c8cc230 | -12.1937 | -52.8866 | 2026-06-28 04:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c25a1cd3-33fc-3232-b5d7-dd19d57ca6dc | -11.209 | -54.3053 | 2026-06-28 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 201.1 |
| dc90a5ec-db63-3991-ad26-3ff0fbaf82f1 | -6.9791 | -42.9034 | 2026-06-28 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| d0d978ba-af76-3b81-ba3e-dda28c44ccc1 | -11.2279 | -54.3036 | 2026-06-28 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| b930d542-2656-3e9e-bfb3-a7e6aaa03994 | -12.194 | -52.8657 | 2026-06-28 04:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3ad23b6b-901f-383b-8eff-ef6bf420a229 | -11.2093 | -54.2848 | 2026-06-28 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| c51eccbe-b3ee-324c-a01a-bebbe2d30cbb | -0.09023 | -51.28053 | 2026-06-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63b27ea9-208d-3b92-b9f8-bee67056d62c | 0.9677 | -60.41148 | 2026-06-28 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6b792e2-7a5c-3621-b582-96a4b6a5cc2b | -10.78773 | -46.48444 | 2026-06-28 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 632b7cfd-821e-314b-9927-fa2e8f9c3482 | -4.28946 | -48.35878 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b30b34ef-aec8-382a-b215-02679e493198 | -6.98469 | -42.8941 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1e9bf214-110a-3d8f-852d-a25e03c71075 | -7.3034 | -46.28923 | 2026-06-28 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0adbe612-e4ce-3c90-8f21-daa230e84e2a | -6.98534 | -42.88932 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 429808f2-affb-3b75-8895-c20acbec6724 | -6.97879 | -42.89305 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| db8b6ca1-5ae8-3e2d-acfe-a147ad43f629 | -4.28484 | -48.36194 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f214431d-690f-350a-ad16-e798867ef97e | -9.21003 | -46.63554 | 2026-06-28 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46ab057c-c518-33b1-9f7e-8b537576929e | -6.21183 | -47.08236 | 2026-06-28 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc976eec-8ff7-369f-98ab-e903886ed78b | -4.28939 | -48.35961 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30334934-5ed7-3461-889a-21c6b3210f73 | -4.28066 | -48.36217 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecbed0a1-b89f-3c4f-b7f2-62ce7694d7fe | -6.98555 | -42.88908 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9e58367b-3ad1-357b-b0fc-a063c103c229 | -6.99948 | -45.00651 | 2026-06-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d1f61215-56d1-3e8b-b57a-cbd7ea71e510 | -6.97818 | -42.89785 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0cca92cd-e281-34ff-8738-80e5c3ece6c7 | -6.97941 | -42.88819 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d223f5b0-3cda-3a6d-b719-f396599d4187 | -4.28893 | -48.3625 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 89f95d5b-6407-3a84-b0b8-4607288f6a64 | -9.46577 | -48.14434 | 2026-06-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f54c9dd-f29e-34a3-a3f5-b6f8cb37e1c6 | -10.36179 | -50.1819 | 2026-06-28 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e830840a-dc6c-3bdf-9cf8-d6e60d763212 | -4.2853 | -48.35907 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f886938f-b96d-31d7-91e3-9733eb13fbd0 | -9.1884 | -58.06601 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95b6d39a-cfb5-3ebf-b3a3-e2b0e8bc307a | -7.30832 | -46.2899 | 2026-06-28 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e0ea0c9-8872-3f66-80d7-1862bce9ab22 | -9.16955 | -58.06727 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d71ce4df-423d-3861-9ba3-de0f841c89ce | -9.18771 | -58.07027 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8b172e3-63bd-3a0c-97ba-05ad9fec38ba | -9.19411 | -58.05382 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46353c3f-e1fd-3b8f-9336-3ac82ff50541 | -9.12439 | -58.25037 | 2026-06-28 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4926d750-d47f-3482-be45-6721f4361571 | -3.98358 | -48.42764 | 2026-06-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
