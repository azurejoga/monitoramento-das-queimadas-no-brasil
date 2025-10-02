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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05d322ba-c0bb-3122-9079-a27a325c9c92 | -13.79799 | -48.04395 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3320cdd-679c-3376-bd2b-19eb65978f94 | -12.76589 | -50.59598 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3821196-1968-393f-a57d-de70b6b3e8db | -17.09305 | -48.55951 | 2025-10-02 04:04:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b6da6742-a58e-3b57-a36c-9c0fd2cf4b4b | -12.50046 | -50.25762 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cece8d97-c488-3317-bee0-ba227124b0ed | -14.46747 | -48.39936 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3da51c8-5246-38ce-8258-2b6538bad149 | -15.76605 | -43.67022 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| babbe4da-4168-3e55-b813-c40bd3015cf8 | -13.17594 | -47.81139 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc93826a-d1d8-3c0a-9db5-b06ed38a016a | -15.41276 | -47.04257 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fbd8ef9-52b8-33cd-8f86-1da957835aca | -14.64051 | -48.1331 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d1239b8-1370-349b-9b70-c7181e5b9d60 | -14.22461 | -46.10376 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f139c655-0f00-3bec-81eb-ed8f77ccbce5 | -13.086 | -47.0768 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6efb4b0-899f-31ce-98e4-561bcc1ae043 | -14.88339 | -48.33586 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdf77d14-37e8-3634-af9c-9906d5c591c9 | -15.39011 | -47.2817 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2693125-7a63-3e9a-a63e-7f7d2459b06f | -15.83577 | -46.2445 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af69e080-fba6-35c9-98de-c8e304dd155b | -12.93929 | -48.42347 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53420c37-bc36-3216-8055-f5da597744b6 | -15.76147 | -43.67707 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536921ae-077f-35f9-9a26-b42e1c05f9d3 | -18.50743 | -44.03591 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a1988e9-7417-3535-9438-185719ad3735 | -13.08459 | -47.08452 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f5bbc93-9808-3747-821c-d3d5996b2b85 | -14.86987 | -48.28809 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5ff86a3-99bc-3933-8cac-d981de148e08 | -16.04008 | -50.86536 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abdd7372-4a09-39fe-bf28-37962e067a3c | -14.47985 | -48.40605 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6265c6ea-f7f8-3bf8-a340-4bf122757e32 | -13.19801 | -47.84795 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a61e74e9-b2fa-3765-935d-f190f5f36ea7 | -15.31049 | -45.06043 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 285fe875-8da5-33a9-8f8f-4df5e0b4c7c5 | -13.0727 | -47.01641 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50bf017b-729b-3802-9487-be7b9daed410 | -15.21042 | -48.00342 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 006362e4-7487-3012-9c89-8e44cae1ee02 | -13.70486 | -48.61644 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb999f46-8089-36a9-8313-09d141d978b7 | -19.59542 | -43.81381 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 758d741f-54c4-3609-b8f8-2fab8c18c06f | -18.44457 | -43.8111 | 2025-10-02 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eaf9df19-1ed2-3420-a344-e0e1f7a9dc67 | -18.3455 | -43.58255 | 2025-10-02 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e106ba38-11c5-33fe-8bec-c8ccdfa2002d | -15.222 | -47.16439 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed3376dc-7f8f-38c2-b4fd-9c23b1e65675 | -13.77443 | -48.04245 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac077d91-3a73-30f1-97f1-65c716f1fbcc | -13.07978 | -47.0876 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7e33c1f-ed4e-3043-aad2-5f2bc4cc89cb | -13.54866 | -47.28382 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1293539-c27d-3e5e-a2a0-f2391fb69b81 | -13.7572 | -47.98935 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 200eb87d-d022-3f8d-b856-8ca7ff0425f9 | -15.94262 | -43.34058 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26f52d3a-e8bc-3fac-a2ad-f8c8b78bc8f9 | -14.59347 | -48.33035 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1091d60-1476-3ae8-be75-0c2d8cec194d | -19.45677 | -44.28782 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92960637-2855-3ff7-b1d8-f27f416ab8ce | -19.11257 | -43.17022 | 2025-10-02 04:04:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c21a7a84-7155-3922-8bca-2d07b36d44c4 | -14.30762 | -45.89508 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4edac376-3fd0-3803-b85d-ab92919dd97b | -15.2478 | -48.08539 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9028ae1-eae8-314f-b798-b558e3c1f839 | -13.31719 | -47.33551 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb570c99-9821-3466-bf47-7cadc50cbd30 | -19.71717 | -45.87983 | 2025-10-02 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba446f07-6c29-3a1f-a397-bd6cbf8b922d | -13.318 | -47.00396 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4236a162-9af2-322e-b844-f98dbba8f61a | -17.2642 | -41.42045 | 2025-10-02 04:04:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 09f808ab-23c5-3801-9ba3-656ebf656902 | -15.26065 | -49.30993 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 48e02458-c78f-34fe-b29e-579c0086857a | -20.13767 | -42.85667 | 2025-10-02 04:04:00 | NOAA-21 | SEM-PEIXE | MINAS GERAIS | Brasil | 3165560 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3ca8c199-6529-35ce-8d04-55fc69dbbc9e | -14.6131 | -48.23145 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aaeff86f-3570-3bbe-bc3f-75d920a1da97 | -14.58645 | -46.71572 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e8371f9-f04b-39be-93bd-f30e7d6dd64c | -13.30305 | -46.99311 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 657c36f1-5b8e-3c3b-9ad7-f0af3e9586a4 | -14.50587 | -48.4865 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74eeca02-175e-3c4d-b942-f41997f62103 | -15.93869 | -43.34368 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fee2d838-fbcc-304c-93f9-568167b4e22e | -14.40627 | -46.08766 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9781b9a3-97c6-3fbc-92ee-894373b77a89 | -14.47188 | -48.39999 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 08175e7b-5355-357d-9d91-5bf7421ecd6f | -19.00411 | -43.01421 | 2025-10-02 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3cefd42-6999-3998-8171-31c744e44ba5 | -13.08531 | -47.08062 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c6f7ac6-b0f2-379a-aeb0-3192b6318025 | -15.86404 | -48.12791 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a1cb864-8e6d-3351-abbf-961d6bb83a4d | -13.31865 | -47.00023 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aff13b49-d151-339a-a845-413028200c10 | -15.22349 | -47.17919 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38e73bb6-59aa-36ed-b2fe-bda5c91f8737 | -14.36763 | -45.95303 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c535005b-3b5f-3f88-b31c-f1059aef4742 | -17.68606 | -44.43588 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7332b08-9632-3e10-9a69-50955a150e83 | -12.70616 | -48.58833 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c282221c-b09a-3cc7-90b3-b66b50ddfc9c | -14.02776 | -47.95702 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f41eeb2b-464d-3218-b8c6-b6ad3d5ea4e7 | -13.20958 | -48.50211 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebe01051-7897-317b-9c17-f49b0251e909 | -14.69263 | -48.26075 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4284926-8160-3165-a54e-0f01d19eb983 | -13.36996 | -47.28021 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81b495b4-9e52-36ae-9260-98bb03df8572 | -18.65802 | -43.69371 | 2025-10-02 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d30de6a9-9cb2-379c-8804-60205a28be8a | -19.09916 | -44.06019 | 2025-10-02 04:04:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71f228c3-f5de-3431-8d5f-8036777b0e85 | -14.37225 | -45.9701 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7777fe4-3aaa-3058-8f47-379c4c304657 | -14.91019 | -47.21826 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f7dae9b-9be8-3cac-b135-d6b708892b4e | -14.41601 | -46.09912 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a20ace7-bc36-31ea-ab4c-3904aae90dc9 | -15.75963 | -43.68822 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86bfc1df-47c0-3121-bf3e-b3ea0d39d973 | -14.79607 | -46.99101 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2b24c69-8a7b-398d-b731-a580c2864077 | -20.28152 | -49.23676 | 2025-10-02 04:04:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d112da4-e8de-3041-8c22-10f000059789 | -18.91256 | -41.95516 | 2025-10-02 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 315c5277-a133-30f1-a41b-766c0d4ac414 | -19.59402 | -43.84381 | 2025-10-02 04:04:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af9edd17-0ff6-374e-a0ec-eeb37a5f9b59 | -15.40879 | -47.04189 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad3f540b-33e6-3fca-aa48-dd52e5903da2 | -14.21622 | -46.10685 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0ffbafe-32e6-3e97-9324-40995009fdab | -14.43806 | -46.34756 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fadff6ac-ff5c-38c6-b006-b24556a4be07 | -14.31763 | -45.88219 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78095586-1ef3-3689-838f-b7c2a8cde70c | -12.9468 | -48.43352 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ad2fb67e-16d6-39b8-a707-b18e2e4830af | -13.46585 | -47.23343 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6461d0ea-3a69-341a-9738-c8a6ca167097 | -18.66507 | -43.87992 | 2025-10-02 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795581f6-3fad-398f-b18c-d9214f5c738b | -16.35944 | -47.0378 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f211d97-ac97-341f-84b9-159aa0753e9b | -13.32219 | -47.21228 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41641be6-9305-30a8-b5ee-802e41f4e5d9 | -17.70693 | -46.88559 | 2025-10-02 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea259f83-3892-3c3f-a51d-65be31fc4d44 | -16.03954 | -50.86813 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51dc778b-6ef2-3e84-98b2-5d7417ce1950 | -13.30985 | -47.00236 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b722239-1877-3f17-bf7b-637e09cffd3c | -14.67644 | -48.22726 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 619292e9-11f0-307e-a8eb-d3e15468eb22 | -16.00769 | -50.89735 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4be6935e-8f1e-3374-b5ac-f0c4f8c537d6 | -14.98133 | -46.92401 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 85a0c6d1-3c13-390e-ad6a-d792dd7d86e3 | -15.31679 | -46.29401 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 290ecb70-f957-31a9-8fe4-3821b3470cf5 | -13.30776 | -47.84418 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8cc03df2-671f-350e-a54a-e277b18d7f6c | -14.47544 | -48.43046 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2e2ed565-b2db-35b7-886f-7505f69aee73 | -20.22814 | -43.9026 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ca07bb3f-7383-3cb6-9aa5-cf547b46d52f | -15.32526 | -46.401 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2ad321c-0a20-3c03-bdcc-2b706c1a5669 | -14.42322 | -46.12526 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77fe6ebc-9596-3007-8227-b39400563e92 | -13.16954 | -47.83296 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9bc773d3-2101-3b39-8765-49e21012981c | -19.44373 | -44.16338 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1c06cce-2f9b-3c1e-a7ab-04a6fa81dce7 | -14.84056 | -41.28881 | 2025-10-02 04:04:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4381d08b-72a3-398a-a2f6-2e1cb8fedf89 | -15.39709 | -47.06137 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README52.md)
