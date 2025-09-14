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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a442daf6-170d-3956-8c4a-ba540277ab95 | -6.11403 | -45.94003 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd49b3d7-35ac-39db-a484-ea1835c07434 | -12.76821 | -48.00951 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dd922674-8861-3b64-9da9-c93d15dd52a6 | -11.3928 | -47.33805 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de4cd895-407a-3783-b0c8-9e27bf90b374 | -13.89537 | -48.30183 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8be3fb4-185f-300b-ae71-6c842b158c24 | -15.14688 | -52.47396 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 427b113d-3660-3555-aafa-b55e6c5b46bc | -14.19685 | -46.16303 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce5820be-080b-3224-b933-aca4f8487012 | -6.55748 | -43.95471 | 2025-09-14 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6df1b2b1-dcd7-3bae-b912-a01509ecbeea | -11.82987 | -46.36669 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6df2b29-06ad-36df-85e2-0546b790e275 | -10.92716 | -47.1901 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b2ca4c9-a059-3697-9ece-f018ce496844 | -14.17899 | -46.15405 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed0729a3-56e4-3ee3-8756-4e944fca2769 | -12.77353 | -48.00921 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4585a3c6-fdf3-3f75-9281-ee83a635827e | -15.47575 | -47.32035 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6155e3f0-5b5e-3cec-bcca-69e0b8fabecd | -11.14367 | -48.09034 | 2025-09-14 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 489cac28-0e0a-33e8-9eae-32c76133d0e0 | -6.18014 | -41.16809 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f8e463a-f836-31f0-8b52-16bc7ee0c5b2 | -12.96933 | -48.02739 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ce65731-681c-3ddc-83ae-09308cdddfdd | -12.79909 | -47.96817 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22b908a4-2733-3b1d-a99c-0163eafe5955 | -6.42271 | -42.6199 | 2025-09-14 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22df9809-57d5-3f10-9412-ab280cc7b238 | -12.04419 | -46.5454 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa2cf41-92e6-3aa5-a4df-c2a47b68d02a | -6.31767 | -43.34412 | 2025-09-14 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60a20786-0719-3cfa-a6c9-665fd82bfeca | -14.435 | -43.20077 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e93a6499-519d-3135-a025-cf7fe2cae4a8 | -12.95086 | -47.9771 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38fd25b1-2230-3478-80ef-da755f8b1db3 | -12.74955 | -48.01597 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0590a9c-a5ce-31b3-a47e-6cd64b9b71e9 | -5.73195 | -43.1987 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 96459e9a-08ba-3708-9c9d-92aa43a64d48 | -17.31573 | -46.09769 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 801bbd8e-7705-3b89-94c5-1c2cb979149a | -12.79846 | -47.14039 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 47d20050-971d-3b19-9570-ded3ca525de0 | -6.32653 | -43.95595 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f868a916-5729-3ce8-bdd5-484fe122dff0 | -6.27428 | -42.3941 | 2025-09-14 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4c235ac1-69eb-3d17-998a-a2acca50e5be | -17.35556 | -42.62594 | 2025-09-14 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34dbcbe2-6bf7-374e-ae12-d08f8d32b5ce | -12.80033 | -47.96192 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab2d106-1a04-34fc-b18b-963f6e12e205 | -5.9526 | -42.78221 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e49a8695-2969-37fb-b308-11aa7dfb2fad | -12.08396 | -47.56752 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0fffb20-fcc3-39ef-a57e-5156f97d21cb | -5.60192 | -42.90647 | 2025-09-14 03:49:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 256e6a00-4c88-37c4-a9db-4d5cdae8297a | -13.92998 | -44.83887 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63fae81e-ca99-332a-a756-ab633d6ea81c | -13.90004 | -48.3069 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cadebc97-56e6-3638-9bd8-c0f0e681e68e | -5.95329 | -42.77812 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f7f1e1a4-8db7-3d92-b39e-831724dbcaf3 | -12.04033 | -46.53818 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d735a57-fe47-3e0f-8caa-d7ef4d4ca276 | -11.44869 | -50.76354 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 20f9fc93-412c-343b-8103-a8e136b27151 | -11.37943 | -47.71261 | 2025-09-14 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3be4d17-a4a5-3983-b0cd-f42e202f2344 | -14.47794 | -47.34533 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1183790c-9617-3e0b-9d6e-4c638e582010 | -11.39344 | -47.33463 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44bc7a20-99c2-3e8c-91c9-5a89345de230 | -11.38615 | -47.34393 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b5a1275-8a02-3c5d-be88-2862af2ae065 | -12.69595 | -43.46581 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2e83c44-7a21-34a2-8f91-12e67e4b0dea | -12.76894 | -48.00583 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ff0d71a5-6c87-3fc9-b41b-8e3b9a83fba5 | -12.94625 | -48.02972 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35af1c15-b20d-3a19-ac19-8144f39d9139 | -12.95149 | -47.97387 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b83d4b-38d5-3c0e-9da5-5c637b51d059 | -14.19959 | -46.17452 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 867d6fb5-a411-3f52-8d1c-3441f397beb4 | -11.05318 | -43.24569 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64133560-0321-39d3-ac50-8234cf8ee0e6 | -11.48039 | -50.7765 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1ccb9ad-5f34-3cbd-889f-2468c8bde856 | -15.12983 | -52.48623 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 707ec185-a516-3d9e-ae6a-242e589e8569 | -6.12536 | -43.95153 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 666f7e6d-f5d0-3632-93c2-af56a2211659 | -6.12233 | -42.9528 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7d10c664-71ea-3f64-8853-cb913e4a8129 | -14.43519 | -43.2033 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65b28ae2-bccc-3d43-9427-8760565c2891 | -15.77963 | -52.22404 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4544f5bc-6bf4-39c6-9504-8db18f7a4880 | -5.99252 | -43.98265 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7badb5c7-51bc-3918-8a78-90949519fb22 | -18.396 | -44.10072 | 2025-09-14 03:49:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7d70037-d037-316b-80c8-e3e213ca24b6 | -14.63264 | -52.03316 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c49235a0-0dca-3a92-802d-2446c456a8e9 | -13.93594 | -44.83104 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 116c49ad-9e97-3bfe-b133-e1352228a5b1 | -10.66997 | -46.25229 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fc48493-aed5-39bc-b6ff-282e207f2fc4 | -17.69466 | -42.56212 | 2025-09-14 03:49:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a78598e5-d299-3ead-aabe-f61b7f8f15a9 | -15.6333 | -44.37809 | 2025-09-14 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 790fbbc0-508f-36f0-90b4-82c33f9bbb3f | -17.32005 | -46.09921 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3592bbcc-8bca-3365-85c2-8ebfd5d346b5 | -12.78496 | -48.0394 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17448284-729d-36fe-ae10-0989db8ad506 | -14.46349 | -47.31176 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e98e664a-3966-3807-a96f-aa5287fa2139 | -17.96923 | -45.27319 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6692a3eb-6bb5-3c89-bf0a-efcca65886f6 | -16.11653 | -52.169 | 2025-09-14 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0db7f9e-df17-38f5-8163-d4e8f0d5675d | -5.72995 | -43.19535 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3479586-f451-3950-bdba-0539408e2ed3 | -6.42559 | -42.62868 | 2025-09-14 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2181d665-379b-3f2d-8b3e-6539bc11cf7f | -10.96948 | -49.56543 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c549c00-a557-3724-a242-1e71c83cf668 | -12.06729 | -45.62617 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4b27838-d8db-35e5-8d57-3a60262e57db | -6.17706 | -41.16248 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 045b179d-729a-3034-8719-4b11f8541f76 | -12.92399 | -47.94191 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9396e839-9331-3249-b782-d6881ecf407f | -15.47686 | -47.31466 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c653892a-4eb7-3908-b8f7-3eee8c52e718 | -17.25559 | -49.26938 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| acfb2f7a-929b-3d39-82cc-ec1f5b02a200 | -6.33 | -43.87965 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7d0fe2c-8dbc-3c53-be05-4d08c3b29437 | -15.18325 | -52.47423 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5b67b77-4101-31f2-9031-8ca2063f6d1a | -6.42337 | -42.61602 | 2025-09-14 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75b6ed10-2abb-397b-81e8-42476559eb88 | -11.44487 | -46.91249 | 2025-09-14 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2c41ba-c8be-3781-bcc8-95fc503fbcfd | -11.77619 | -46.623 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc6a3944-d31b-300f-9b21-1647cf8a1b75 | -11.43176 | -43.53606 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c5bb3db-4c85-3ce2-880f-67c2683fa7a9 | -16.66086 | -49.78309 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4f4dd11-7524-3345-8d52-181bb11fb2b0 | -16.28291 | -45.68447 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8e2f262-b986-3df1-a4aa-57fa382dfdad | -6.28234 | -39.68494 | 2025-09-14 03:49:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 48b17ee9-f307-394e-b458-a6e396577cb5 | -11.06339 | -43.23598 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca6cfb83-7aa6-365a-aa8b-9ec394465e1e | -17.26684 | -46.11193 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c9f55cb-4720-3326-b20d-a18da2b87c33 | -16.40455 | -44.04807 | 2025-09-14 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e1a9416-657b-3e07-923c-b1554cac60c4 | -12.92768 | -47.95171 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f1b7773-2344-33be-93dd-8ec316c711da | -6.68979 | -39.49621 | 2025-09-14 03:49:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d3f8ec1-e5c0-3d15-bb98-539e8e9ff7e2 | -15.16966 | -52.4711 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6432ae16-e4a7-31fc-942b-73c86a97ef01 | -16.2917 | -45.68625 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e466453a-b992-3ff0-8d94-fb02972bd094 | -11.35595 | -47.32737 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39a34c80-f08e-3843-b433-e88d8e38f9d2 | -13.93512 | -44.83542 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20087aa0-de73-3674-b195-6b597ca1aeb3 | -15.93383 | -49.97243 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1eb3df4-928c-328b-bcbd-5ac2145021c7 | -14.42242 | -47.34438 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecca0155-e5b2-32ed-964f-68bc1230bde6 | -6.27809 | -39.68851 | 2025-09-14 03:49:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 7ebd88a0-e86a-3912-a6b9-d7d0e54cc408 | -11.44772 | -43.56682 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e33020b7-f36c-33c8-a225-f144e34eb275 | -15.76604 | -52.25316 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 581b8a58-1dd1-34bf-9512-b44709a3d09b | -11.44375 | -50.76596 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 049fc117-b1fc-3fdf-b6ba-6ed560ce9299 | -17.26101 | -49.27063 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f492de0-c71e-3a82-b131-f97194c5b824 | -15.19953 | -52.49714 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9b3156c7-fefd-3145-b697-77b8d2a7250b | -14.16419 | -46.15473 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README15.md)
