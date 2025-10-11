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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd77340a-e752-3b1e-88ab-e3284adf58e7 | -6.82844 | -42.7998 | 2025-10-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 913ab629-5898-3ca1-9cab-9312e8e4801f | -4.41701 | -43.47037 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a91952fc-750a-309f-a797-fa48f5bcaa28 | -6.04758 | -42.5115 | 2025-10-11 03:40:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2440e03c-db11-3112-9f6c-f2de1dbd2bbf | -5.27785 | -45.27006 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c667f579-6b14-376f-8ce0-d669bcd2ef91 | -5.59091 | -41.1046 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ab8f4bce-4dc4-3d73-a85a-738c84e85921 | -4.45035 | -40.77386 | 2025-10-11 03:40:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb38840c-9878-3af3-abf0-d9043c091dda | -3.0116 | -41.12795 | 2025-10-11 03:40:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd3cef4f-585e-3260-827f-5894626f7fcf | -5.14921 | -38.06082 | 2025-10-11 03:40:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9cedaa3b-4a80-39cd-818e-6d8cdfae470d | -2.52198 | -44.11902 | 2025-10-11 03:40:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83747b01-fb7b-3163-9ead-7c1bdd6a3377 | -4.41144 | -43.47047 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1a9a9388-d170-3133-ae85-f903ab79ee50 | -6.03887 | -42.50482 | 2025-10-11 03:40:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 09986970-f645-341c-b127-1d8968b0a4e6 | -5.67978 | -47.90644 | 2025-10-11 03:40:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 260c6e22-2cea-3f1a-9d59-1b7f0f6b7acd | -5.20461 | -44.60546 | 2025-10-11 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4522ba5c-a5b0-360b-9827-c043e6703192 | -5.40796 | -40.98467 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aa997b58-b0cd-36aa-8968-3bd5f3132d10 | -4.98386 | -45.6413 | 2025-10-11 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db321663-767f-3f93-80a7-dad9823e6667 | -6.62605 | -40.99037 | 2025-10-11 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae6cecd7-4ac8-3e85-a700-f652a218d28b | -3.77819 | -44.11244 | 2025-10-11 03:40:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4111fdcd-5911-3da8-8415-b571778b647e | -5.58943 | -41.11327 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cdebb91d-b8f5-3384-8bef-e4952393464b | -5.15354 | -38.05717 | 2025-10-11 03:40:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af10ef58-451e-31af-bfee-dcff307d76b7 | -6.27394 | -39.95306 | 2025-10-11 03:40:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c750d75b-adb4-34ba-aa7a-3be7527d6398 | -2.52134 | -44.12284 | 2025-10-11 03:40:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd8bc7a6-650e-31c6-843d-6dc71e5ad3ed | -5.20392 | -44.60937 | 2025-10-11 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e56f3c66-cc01-3d0e-90ff-b627c69d98f9 | -4.42192 | -43.47239 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eedc07f3-5af4-3a2e-b0a3-77b7bed6d078 | -5.5858 | -41.10818 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a75df522-2d16-394e-ab55-b24ea770516f | -5.91356 | -42.85224 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4c12e41a-58c1-3418-97d6-9b4e6998d59d | -5.58869 | -41.11765 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| af7af5cf-3897-31f8-9479-c20eabea2edf | -6.18587 | -39.70663 | 2025-10-11 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c25cbe33-4185-3098-b679-2b6c7c5dde88 | -6.1631 | -42.55538 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4bdcdc4-4a2a-3b25-9e15-844875102de1 | -4.93817 | -37.99931 | 2025-10-11 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aeed2014-7866-3447-9909-ec7370c89f4e | -5.86112 | -42.85263 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| df0f6a7f-04a4-3bf3-ac05-f31fcda07e64 | -3.69758 | -43.2011 | 2025-10-11 03:40:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90c940b5-024d-38d8-9858-ad3098d89d60 | -6.55072 | -39.99916 | 2025-10-11 03:40:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eddc24e2-a51b-37cd-b5bf-04e039b453b4 | -5.85521 | -42.85756 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 4d469be6-bba5-3fa7-a893-bdaf78d7f0b2 | -5.29285 | -45.3885 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e295cbb-4dbc-375a-b0c5-5f0f5bcc46bc | -6.80982 | -44.63656 | 2025-10-11 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4660aa35-8b75-341c-ae45-a59213ed186a | -6.18525 | -42.57024 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 541771a3-1719-3af3-9ec4-56470018d063 | -4.23875 | -40.35744 | 2025-10-11 03:40:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 84a7983b-4549-3b46-b84b-c8c829f214ce | -2.51632 | -44.11811 | 2025-10-11 03:40:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f1f6ac8-21f6-320a-8443-a5b8911d11a7 | -5.2848 | -45.26893 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6684a623-e879-393c-8ddb-5cf86233e925 | -6.43212 | -45.83117 | 2025-10-11 03:40:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7f14db8-2e74-31b0-9009-993f9d4799d6 | -6.72511 | -43.5955 | 2025-10-11 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0141ae01-04d5-357f-b587-98ad76d5f1b6 | -5.93926 | -42.2851 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 64d2dccb-0751-354f-a5f4-3d652b6f1c03 | -5.96715 | -42.26403 | 2025-10-11 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6893b205-2231-3cdd-b9d5-50425482f88d | -5.89133 | -42.70634 | 2025-10-11 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dfdd28e7-faa6-3032-b834-bc1eadd8b7a6 | -4.44655 | -40.76982 | 2025-10-11 03:40:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8edabe4f-55a1-37c3-b05f-5d51b2e0b3d2 | -7.36603 | -38.75738 | 2025-10-11 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ba96cb91-99ff-35b3-8ba3-4fbe38136a8e | -5.74424 | -43.37686 | 2025-10-11 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b86264b-315c-3f65-a83c-7da96c2d1a4b | -5.32244 | -43.08534 | 2025-10-11 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 361d443a-a2c5-3a5d-ab19-0bdef55a1213 | -7.21372 | -39.90767 | 2025-10-11 03:40:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 761111fe-cce1-36a6-9c04-4f23ec505c86 | -3.12731 | -40.99794 | 2025-10-11 03:40:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b50afe53-9c4f-3eb4-b98f-f07fec60462c | -6.18542 | -42.56618 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 97479b88-5333-3164-9780-cfd3c55bbca2 | -4.42136 | -43.47562 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab3aa171-98e5-3eb6-afd1-aa45c806e1c5 | -4.8823 | -40.45011 | 2025-10-11 03:40:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35162e2a-c29a-3db0-91a9-b8ddf9de73dd | -4.0769 | -48.05085 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5fe730c-4b39-3afd-b309-6967b972aa0b | -3.97972 | -40.92064 | 2025-10-11 03:40:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee789405-7bdb-3c9e-bb42-b0c88c686e11 | -3.9791 | -40.91782 | 2025-10-11 03:40:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 060ded41-4eba-3f78-96c0-7a71ba7752be | -5.89886 | -38.47524 | 2025-10-11 03:40:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c953ad39-2c2d-337a-a2fd-2a121994821e | -7.36163 | -38.76122 | 2025-10-11 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 14bc3d9c-2720-333c-8b23-91b78b97cee6 | -6.4329 | -45.8268 | 2025-10-11 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42a97881-bd59-386a-8b85-dda71b5d1a3c | -4.41557 | -43.47784 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b665c44d-9152-32ae-8041-cb7d0ce6e3b0 | -5.32195 | -43.08825 | 2025-10-11 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 363c5637-3622-3690-a9ba-5b5f9d65ae26 | -6.75606 | -42.82319 | 2025-10-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 14fc526e-c7ae-3758-a541-13adfdd9e76b | -6.24542 | -42.75529 | 2025-10-11 03:40:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1b60f954-d8b8-3168-a08d-4901c60d7512 | -6.25617 | -42.98002 | 2025-10-11 03:40:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb15e9c9-549f-33ba-8e92-d5c47dddfce4 | -4.40622 | -43.46943 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9016f71b-6048-39fb-ac51-94d5ec934585 | -5.68652 | -47.90797 | 2025-10-11 03:40:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48d1649-beb9-3f71-8a9f-d690556f662f | -6.07645 | -42.60372 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99fccb7d-11f6-32eb-94e6-8cf8576cfcbe | -5.90165 | -38.47447 | 2025-10-11 03:40:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d43436e7-8d39-389f-8a62-5254ed63e412 | -5.8758 | -45.30067 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa8d945-211a-3944-bf50-55435e88dbe5 | -6.87484 | -42.39644 | 2025-10-11 03:40:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9101f3f1-6bf6-3d5a-bda7-5c192d7a5694 | -5.89413 | -42.80734 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4ed49758-92f0-327a-834e-675f917fcf57 | -4.42625 | -47.60125 | 2025-10-11 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d36065cd-3634-346e-bb52-bed4fe4d362b | -6.80435 | -44.63571 | 2025-10-11 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1ff6b9a-3532-358a-9700-f9ef51cf019a | -5.24856 | -43.45958 | 2025-10-11 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6e533d3-d28e-3160-9563-713b705d823f | -6.75745 | -39.67834 | 2025-10-11 03:40:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9d8dfb3-ec0a-333c-a5a4-4598134d9bd9 | -6.2502 | -42.98512 | 2025-10-11 03:40:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 795e0203-06f8-3928-95f5-8feedc7d4bac | -5.46271 | -43.53085 | 2025-10-11 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c62398b-b71e-37c8-b518-be0f8b4bfa68 | -5.97499 | -42.78924 | 2025-10-11 03:40:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 90689124-4581-39d8-b721-2fa84c282daa | -5.32744 | -43.08644 | 2025-10-11 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fc476fa6-b18c-3e97-bbbf-9d73354ab500 | -3.77756 | -44.11608 | 2025-10-11 03:40:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c71427e0-0b88-380f-ad42-db4a155554a1 | -6.80504 | -44.63186 | 2025-10-11 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c45f719c-f6e8-3503-96b1-9e4d9d15387c | -5.86603 | -42.85349 | 2025-10-11 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 61d63c80-f6e6-3e02-b428-38b65d66905c | -6.92203 | -43.58504 | 2025-10-11 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35b1c831-86af-369f-a3b5-34ab35897082 | -5.39564 | -40.97817 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 61d19a69-0177-3c73-a3a5-e5c35278fef3 | -7.36532 | -38.76178 | 2025-10-11 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 509352f1-d9e2-316e-a34e-e4a2c3040ee1 | -5.41158 | -40.98978 | 2025-10-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8c39e3f1-4af4-3bbe-8efc-383cc3878cd3 | -6.73766 | -42.81455 | 2025-10-11 03:40:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 711279de-8cae-33c6-8eaa-ac34535d2721 | -3.8335 | -43.98793 | 2025-10-11 03:40:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11ae7eb8-f0a2-3cd1-a7e6-5f03d53937ce | -4.41612 | -43.47465 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcc751bd-7094-3837-907b-0cc78f2347f9 | -4.41595 | -43.47678 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd3b4861-a294-3d7b-b9e6-fa17a98042da | -4.88836 | -45.96088 | 2025-10-11 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c580f710-2a10-3fc1-aa71-7da3c2a9de06 | -5.42845 | -41.36821 | 2025-10-11 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c8f2c2a-9e0e-3736-a867-f260a72ebdfd | -3.40822 | -39.16848 | 2025-10-11 03:40:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbd237a2-a6bf-3857-8001-79f3da008a24 | -6.16398 | -42.55018 | 2025-10-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 801d6a2c-7761-3f02-b553-383f1798db8e | -5.32695 | -43.08937 | 2025-10-11 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6c08d99-54c8-347d-9e6a-928d1aba003d | -6.55247 | -39.98879 | 2025-10-11 03:40:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b07f749e-a00c-3547-a727-1e9d724a3daa | -5.279 | -45.26778 | 2025-10-11 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b96ef51-10f7-3f3e-96b8-b3eb944de273 | -4.41648 | -43.47358 | 2025-10-11 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2c0c4ec-46b1-3a40-9f9a-15de062e143f | -3.69728 | -43.20062 | 2025-10-11 03:40:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26f0baa2-0885-37b7-be22-76f34c1880c6 | -6.32424 | -41.60205 | 2025-10-11 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
