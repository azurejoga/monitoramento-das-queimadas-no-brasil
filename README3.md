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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0557424-ae3a-3f49-b482-145b3ffe3b64 | -3.28976 | -42.52583 | 2024-12-21 03:27:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 841cb4a2-cec6-3c97-aead-7faa191f11a3 | -4.58082 | -38.60319 | 2024-12-21 03:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 846e110d-b54d-34f3-baa6-0750c0658b65 | -5.17867 | -37.58561 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f58027a0-d637-3e5d-9883-f4f421ac8dc9 | -3.83395 | -41.57096 | 2024-12-21 03:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3af36d1a-9f3b-396a-86c1-39d0f2386732 | -3.28896 | -42.53044 | 2024-12-21 03:27:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3d91de2-0280-35cd-ba33-ae8592b39d8b | -8.12442 | -38.76588 | 2024-12-21 03:29:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bc659a2c-1607-3639-92f8-d3c7d03a365e | -7.84153 | -35.22264 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 8c3ee4a6-6100-30c3-89e1-bd23941789f1 | -7.9151 | -35.19764 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 5143c29e-08de-3663-903d-aa7645326b52 | -6.23177 | -39.28363 | 2024-12-21 03:29:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bfd2f1c6-83b5-3551-ad5e-2bb64cadeb78 | -7.8422 | -35.21861 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 385be1b2-0044-3360-9c76-5e1108703c1a | -7.74359 | -40.21564 | 2024-12-21 03:29:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5abb270a-f7e8-3233-9260-f35fe0b9acac | -6.23263 | -39.27863 | 2024-12-21 03:29:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e72db108-4279-3f4a-a0f0-4732b92cf66a | -10.87506 | -41.23799 | 2024-12-21 03:29:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cda70ce-6944-37ac-8ed7-02513219b0aa | -7.84266 | -35.22393 | 2024-12-21 03:29:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| f6bd4287-2ea1-3ba1-901f-b7d3999432bd | -7.68902 | -42.03265 | 2024-12-21 03:29:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 216f0fa2-8750-37f4-93ce-02a7385d1842 | -7.9122 | -35.19302 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3e715b8a-b6a8-3c56-89f5-1c52280e56fd | -7.68527 | -35.25711 | 2024-12-21 03:29:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ac91abd-f9ec-3146-973d-780cf01f0fb0 | -7.84086 | -35.22666 | 2024-12-21 03:29:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| baee753f-86a3-3a9c-a15a-34e8ec36a63d | -7.15424 | -40.26352 | 2024-12-21 03:29:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bbf6c7f3-c363-307a-aab3-5074ad69dad7 | -7.74182 | -40.21401 | 2024-12-21 03:29:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a9b2e56b-0b5d-3c56-9d75-f7d501856a97 | -7.84576 | -35.21919 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 2434ccdf-46f4-3b20-9b4f-437e00569738 | -7.90005 | -35.24496 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0a5838ac-aa32-34fc-892e-145db6574e1c | -5.32806 | -38.09841 | 2024-12-21 03:29:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e0eb9237-145c-3a42-a674-9fd7208834ad | -6.98449 | -40.00224 | 2024-12-21 03:29:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 81777bb1-d7bf-39ff-a951-51cb1251d96e | -4.31052 | -43.77486 | 2024-12-21 03:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aaf28ea-5b16-3933-b352-c32a45e0b4a3 | -7.92221 | -35.1988 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 658a612c-aa78-324d-98f1-0afd390223b1 | -10.69665 | -37.04806 | 2024-12-21 03:29:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2066a18f-0867-3b3d-a383-6ecfc441c5cb | -10.17651 | -36.37603 | 2024-12-21 03:29:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c02989a5-404c-3965-bac7-e612d70b5a9b | -5.93532 | -35.6273 | 2024-12-21 03:29:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 472b92b4-722f-3a8d-a991-f86d7c7b68e8 | -4.30961 | -43.78014 | 2024-12-21 03:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08ab47b4-8f6c-3488-8e5f-5a6db6a58b7d | -5.93231 | -35.62229 | 2024-12-21 03:29:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d201c86-511a-397a-8dd0-3ef4cd296fae | -5.93667 | -35.62527 | 2024-12-21 03:29:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2b1cede3-ac59-353b-a82e-114b5c855c49 | -7.68461 | -35.26115 | 2024-12-21 03:29:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d37385ba-cf22-37d7-9d40-e6c8de805afb | -7.84509 | -35.22323 | 2024-12-21 03:29:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| db014f0c-976a-3738-b3c9-c616614e8456 | -7.91576 | -35.1936 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 7774e31b-b9f8-3c13-bdd7-e5558fa7009d | -9.50332 | -35.93785 | 2024-12-21 03:29:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 04d41369-83a8-35c5-8f4f-f9f125cbf708 | -5.93295 | -35.62468 | 2024-12-21 03:29:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f3dbf99-e1e1-3120-b2e2-6860389a163f | -7.92287 | -35.19476 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3cfbe8f7-4681-3698-82d5-2972d209c301 | -7.89648 | -35.24439 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 752c4ff2-88b1-35ec-a0f6-71da931dd90e | -7.74086 | -40.21957 | 2024-12-21 03:29:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fd05ca93-e9f0-3d99-aa65-380f7cfa9525 | -5.82233 | -39.21422 | 2024-12-21 03:29:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7844aa0b-3505-3da1-a401-a58d98e6b9bc | -6.84578 | -35.07038 | 2024-12-21 03:29:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a01d05b3-3778-3ab8-89af-d886bc7cfa79 | -7.84332 | -35.21989 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 7d62797a-f495-3549-b3c3-ad86d2b6234e | -7.91865 | -35.19822 | 2024-12-21 03:29:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| cce1f63a-2ca4-3efb-8633-ea7ab0565f25 | -5.08187 | -38.82659 | 2024-12-21 03:29:00 | NPP-375D | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27883723-62b3-35a1-aacc-90a09bb357f5 | -5.61659 | -35.35613 | 2024-12-21 03:29:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9c27128d-2e8a-32ec-b01d-d8f623eb3f61 | -15.96607 | -38.95647 | 2024-12-21 03:32:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9209520-309c-3629-9bba-1a1a8900c9a8 | -12.86219 | -38.36658 | 2024-12-21 03:32:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38142b81-991b-3be2-b6c5-fe2e6dc8be9a | -15.38951 | -39.38577 | 2024-12-21 03:32:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 11195633-fffc-3121-8755-4a68dc002121 | -12.38815 | -39.36966 | 2024-12-21 03:32:00 | NPP-375D | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6706b39-aaf1-3e0c-90c5-c87ad72629d8 | -29.77672 | -51.17734 | 2024-12-21 03:36:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 2ae818eb-3fa0-3879-80ca-375f15a504e6 | -7.68757 | -42.03305 | 2024-12-21 03:53:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7b53d798-35e5-3a6a-aa10-0e2da226ca79 | -8.07238 | -34.9749 | 2024-12-21 03:53:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 12ef44d9-f4cc-3eb3-9b41-09777a889c10 | -2.73046 | -47.73239 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d77d148c-23e5-3633-9d58-08d79d0ffcf4 | -0.85732 | -47.1335 | 2024-12-21 03:53:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 028bda6e-1e58-3531-81ce-4b3ddc04d6d3 | -12.33484 | -43.67872 | 2024-12-21 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9298f8c-83b6-33b1-81bc-a1332e97eb29 | -3.94709 | -46.41501 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a456e9e3-3a09-351e-83d5-249d559856f2 | -2.88195 | -48.28088 | 2024-12-21 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82a33012-de66-36c2-8088-8dd93fdcf81c | -2.7298 | -47.73648 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f02b44d-7ab4-376a-a527-e0a10e142874 | -7.3226 | -39.97016 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0965f9d-7ca1-38c3-85cf-dc0c69f70518 | -2.43735 | -47.48531 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67ea3d95-d453-3ffb-8477-bc1368364060 | -2.8498 | -46.73026 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a71fd5-0f37-3337-a6aa-18d7b56ade36 | -3.08715 | -46.56403 | 2024-12-21 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfcd083c-a984-3884-a9e2-6a3c0d3265ab | -0.33356 | -48.44297 | 2024-12-21 03:53:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5f3c572-7317-3164-9412-699c0e084dcf | -3.24483 | -46.02733 | 2024-12-21 03:53:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49827206-776f-3374-972c-a98acdb1bba9 | -4.50844 | -42.05786 | 2024-12-21 03:53:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 159f77e4-eae0-331c-bcc9-f20f940760f9 | -14.62097 | -39.5628 | 2024-12-21 03:53:00 | NOAA-20 | COARACI | BAHIA | Brasil | 2908002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea7055dd-9b28-35f4-a737-fddadc0526da | -2.63189 | -48.0388 | 2024-12-21 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8efb8619-42ca-32a7-8f9a-c39f7a23569c | -1.29877 | -47.75323 | 2024-12-21 03:53:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 272b7151-6304-37bd-94e4-86cfaf87b1a2 | -7.90216 | -35.24455 | 2024-12-21 03:53:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0a7cf4f-f637-3913-bd14-21cc11c8ec7e | -6.60647 | -39.11637 | 2024-12-21 03:53:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d86e47f6-deaa-3495-aeae-3e46eebf2f0c | -3.94658 | -46.41801 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 020fb3c9-dd72-330b-8c17-17877710cdc1 | -1.87851 | -45.56037 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e8caeda-1bee-3dde-8bfa-28c37e7a52a1 | -6.73638 | -39.99774 | 2024-12-21 03:53:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41912c4a-ca4b-3601-8c3b-f716d438f6da | -1.56382 | -46.77795 | 2024-12-21 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b32c8395-6c15-30cd-a78f-e8cb96822411 | -3.49836 | -41.92249 | 2024-12-21 03:53:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 057a58a4-74bb-3a71-8b27-85293bbe72c2 | -6.49842 | -39.60025 | 2024-12-21 03:53:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ad3e1d1-a34b-369e-9c5b-dab81208e9b6 | -11.961 | -40.61829 | 2024-12-21 03:53:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b50296a9-e3d1-34b4-9cfa-5d1934f1b6e8 | -5.83359 | -39.21384 | 2024-12-21 03:53:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a346c0d-c3f6-3927-8178-cfcfc7c4be1d | -7.74213 | -40.21698 | 2024-12-21 03:53:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0e054000-c826-32e5-9f48-ac93d285bfb9 | -2.7676 | -47.39889 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b257f72-5226-392c-b7d1-6f562d0aa860 | -2.78733 | -45.86964 | 2024-12-21 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e4d8d1-b672-381f-a181-25d9b5ad2d38 | -7.32144 | -39.97741 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e024e5e1-8b5f-3db4-98ef-6f9e04adefbb | -2.70593 | -46.13806 | 2024-12-21 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb78a643-c790-3ea9-80f0-fb5d6954aae9 | -4.96201 | -38.6477 | 2024-12-21 03:53:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7f7ed24-7f07-32fb-a1f7-8c98c5150652 | -0.3406 | -48.43908 | 2024-12-21 03:53:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64fa587a-5e97-3e61-983f-9f317c6a055f | -2.76823 | -47.39507 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57cbb983-ddbe-3a0b-b882-63dd5d39c6a3 | -5.93168 | -35.6223 | 2024-12-21 03:53:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2b26a17-6145-344d-849f-650b5e587278 | -4.24285 | -41.92194 | 2024-12-21 03:53:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 66f9f89c-3249-3930-88e7-fbe4775fbd7e | -2.67963 | -46.93753 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02abc0b0-9ed1-3974-9bc5-490182374200 | -0.33435 | -48.43805 | 2024-12-21 03:53:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed3e73ff-d5c8-3524-b736-5610414fcc59 | -3.99822 | -46.55669 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e7bb32-8a0c-3499-a582-8aadc4743844 | -4.58459 | -38.60648 | 2024-12-21 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 407b0ccc-020c-376c-9cd6-f96ad725ca04 | -2.78782 | -45.86666 | 2024-12-21 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e20b2af-5c20-3fb2-b3c4-0b666441668c | -1.87488 | -45.55066 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89ff4162-62a0-3534-8d48-2c130624bb73 | -11.8569 | -46.95736 | 2024-12-21 03:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 227b9901-1d36-36db-ba52-0984b990c10d | -2.4424 | -47.49031 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1be4777f-3927-3981-83ea-cc0a7fb88fd0 | -3.95177 | -46.41886 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 10b33027-2a92-3b35-bc46-c7b7d61ed465 | -2.67777 | -46.9151 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23928b37-66a2-3fd4-92db-9175b293f9d2 | -4.30419 | -39.28439 | 2024-12-21 03:53:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
