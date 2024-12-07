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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a71ccafd-3a65-39fa-abc6-f7a4ddfb3d24 | -10.38123 | -50.83906 | 2024-12-07 04:33:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91c83d62-8d4a-3203-bf39-c72f93679f3b | -10.53653 | -49.47093 | 2024-12-07 04:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e260469a-837f-3681-8b46-d44177742300 | -15.07674 | -48.94466 | 2024-12-07 04:33:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b79ee1d4-2f40-3d94-9592-ea0b64edb82a | -12.86413 | -51.93749 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4be79c8-ecac-3436-baa3-d5e3209e8388 | -10.98158 | -44.46805 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 707c5ab7-a081-3c29-8fb7-05f7f059e4fe | -16.20028 | -48.22022 | 2024-12-07 04:33:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4bed28e-2919-363c-96f3-d4ed17cd71dd | -16.01568 | -51.88272 | 2024-12-07 04:33:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9b1d401-32cc-3377-81fb-0e921e7633f0 | -14.92733 | -48.13934 | 2024-12-07 04:33:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 766c2141-eb5b-3d2b-a9a5-511c2a8f39dc | -10.65854 | -44.49544 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0fb20a8c-d083-34b0-8b4c-d634cda32e50 | -10.97911 | -44.72972 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df76bcc9-1cf0-3054-8a05-ff0ec4825b6f | -12.65408 | -46.5791 | 2024-12-07 04:33:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfe6eb37-db5f-3a67-a1f6-8458f937220d | -12.91924 | -49.68144 | 2024-12-07 04:33:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c74ed172-32cd-35ab-a289-63414d81b3b7 | -10.74595 | -49.51607 | 2024-12-07 04:33:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75536653-de90-34bc-9bd5-61a1b350ccc4 | -12.45952 | -46.94039 | 2024-12-07 04:33:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3418f45a-9c2f-30b8-aa5d-7ec6e0a2dbc3 | -11.99354 | -47.16674 | 2024-12-07 04:33:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67b8c38a-9282-3133-aa7f-a172323d2aa6 | -10.7535 | -54.78467 | 2024-12-07 04:33:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db965cc3-548f-3700-a4d2-956edd98eb44 | -9.13206 | -50.03648 | 2024-12-07 04:33:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfc6c083-7b2e-3a05-bcfc-96d1ea7b6629 | -10.63695 | -47.46676 | 2024-12-07 04:33:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f91716d-4883-3f85-a7ef-cc745485a763 | -15.25899 | -53.57028 | 2024-12-07 04:33:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 981afb31-2251-339a-8bb2-e71d610541f8 | -12.86061 | -51.93687 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6acc3093-13a8-319b-ae0d-5c9b238c1492 | -9.57656 | -49.08076 | 2024-12-07 04:33:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46dd584e-d1d0-315a-a700-65e06713979e | -11.86914 | -47.71163 | 2024-12-07 04:33:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c3942fb-b81a-357b-ab3a-92353054d791 | -10.64033 | -47.46728 | 2024-12-07 04:33:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7afa0e1-478a-320d-b5fd-41c6dd3fb3f2 | -17.56779 | -48.01038 | 2024-12-07 04:36:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1097c8c5-7b39-3686-906a-d2078cd44874 | -20.32258 | -48.82122 | 2024-12-07 04:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6abf353-7152-3ad0-bd6f-1ada14bf0ab9 | -20.41463 | -43.55134 | 2024-12-07 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9fe3d7fb-151d-392a-9730-71612f2261fa | -20.76345 | -46.76949 | 2024-12-07 04:36:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 752a45ba-c828-3509-a5ac-57f126f54325 | -18.9037 | -47.09726 | 2024-12-07 04:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 673afe30-d881-32d8-9c55-dc753aa8fd4e | -18.60669 | -44.25612 | 2024-12-07 04:36:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bcc0d7c-1d9e-3465-9d9c-cc314f4e1dfd | -17.97661 | -44.58213 | 2024-12-07 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a27a2e0-a819-328a-9bab-5ea332eec277 | -16.32387 | -53.81376 | 2024-12-07 04:36:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78289a30-848e-3b9e-84d4-766c064f426a | -20.33086 | -47.58478 | 2024-12-07 04:36:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93bdaece-db3b-308c-bc5d-3c35f6b1efba | -17.97594 | -44.58035 | 2024-12-07 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85b51f2b-1d28-3677-a36c-bef8ba843081 | -22.70019 | -43.34695 | 2024-12-07 04:36:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c60b3ade-192f-35f4-8fd1-a0dfca98e226 | -17.56372 | -48.0138 | 2024-12-07 04:36:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83d71c08-45ea-3444-adb6-43dd5defa521 | -21.1948 | -44.93512 | 2024-12-07 04:36:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d7bb9fe0-71df-355d-aade-cc84e49fa020 | -18.413 | -51.99415 | 2024-12-07 04:36:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2205478-974b-3c2a-b9ea-8e901f37f2b0 | -18.76041 | -40.12708 | 2024-12-07 04:36:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eae38c6c-d58a-3ad5-b83f-67ae3cc879e8 | -22.69529 | -43.34619 | 2024-12-07 04:36:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a9329375-8b0b-3609-aa18-ca2be55ceb02 | -18.41232 | -51.99483 | 2024-12-07 04:36:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c0a3103-b768-38cb-80b7-04de21a3fafa | -20.20535 | -41.78867 | 2024-12-07 04:36:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54689f61-46bd-35be-adac-f2de25d5f2f9 | -20.322 | -48.82524 | 2024-12-07 04:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecde91db-cc89-3314-8f6a-449e3df87b82 | -19.19931 | -55.53966 | 2024-12-07 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4d03be6f-3358-38bc-ac9c-9fccc00fb1f6 | -20.32781 | -47.57966 | 2024-12-07 04:36:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaf0c2dc-9ff8-3856-83ea-c88a6d216cd0 | -17.5643 | -48.00981 | 2024-12-07 04:36:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 570f0dcd-8767-3ffa-8f7f-ce78cd1bad34 | -20.32719 | -47.58419 | 2024-12-07 04:36:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e831dace-a9af-3d13-8ed9-c33932a7af72 | -17.97236 | -44.58151 | 2024-12-07 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa307416-4b6b-3353-b8f4-d86100d89b4f | -17.97715 | -44.57798 | 2024-12-07 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bcb96e9-9ef3-3ccb-a1ae-cc55f3bc4eb2 | -17.9807 | -44.5768 | 2024-12-07 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f43599a-886c-3d22-ae40-42373e389fcf | -20.31053 | -45.58329 | 2024-12-07 04:36:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 100355c3-15da-38e1-bb80-080e443545c8 | -20.20573 | -41.78508 | 2024-12-07 04:36:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 20e09b62-0fcc-3ded-94ae-d5c7c081f8d7 | -20.33148 | -47.58025 | 2024-12-07 04:36:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 781bbf51-6cf5-3af2-9398-4e4b3880b8d5 | -22.69897 | -43.34676 | 2024-12-07 04:36:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 23adc3d9-e94d-3b39-9387-e0fd6bedbcb7 | -18.61107 | -44.25667 | 2024-12-07 04:36:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e165293-27b8-3eef-b820-5e6952c524bf | -18.75466 | -40.12634 | 2024-12-07 04:36:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d094daa-9a51-3a44-a9a3-3e30f7d7e7d7 | -16.32019 | -53.81304 | 2024-12-07 04:36:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b4871fb-1f39-3f7e-b4a6-54ba2215009e | 3.6854 | -60.55207 | 2024-12-07 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5266792d-62b7-330e-a6ed-0c9898e65a47 | -3.54846 | -47.38455 | 2024-12-07 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a060c60d-04af-3434-9c14-8cdc6fcceed8 | -4.32061 | -45.88931 | 2024-12-07 04:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a76171d-fb06-38cb-8a85-157591df662a | 3.68492 | -60.54891 | 2024-12-07 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86aa4468-13f2-37d4-b62b-d77764c6dc0c | -4.42889 | -45.88482 | 2024-12-07 04:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad27ac70-b831-3b4e-97a1-2526f3168e72 | -4.42701 | -45.82921 | 2024-12-07 04:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 783ab8ba-bbe9-32d7-82e1-dc8cb0c2506f | -0.64044 | -63.03379 | 2024-12-07 04:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74faa5f4-304a-358a-b47e-fbb5e998c044 | -4.42812 | -45.89011 | 2024-12-07 04:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92173a03-7426-32f4-8267-0941801aa826 | -4.42785 | -45.82342 | 2024-12-07 04:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 882d44f1-9ba2-38a1-9fa3-6a39b8058f50 | -11.41114 | -51.27383 | 2024-12-07 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aff48ce7-140b-32b3-ae78-dfba859ac340 | 2.7437 | -60.38606 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21c4d3c7-6081-3644-974a-a8aabf0b2db4 | 2.94921 | -60.35831 | 2024-12-07 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ed7a385-dbe0-39d4-b486-5a10ad81dba6 | 2.74414 | -60.38903 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b566e0de-19dd-33eb-9248-15f11228b6cc | -12.48036 | -46.28187 | 2024-12-07 04:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7996aaf7-9219-3cd5-b79f-d5476960b426 | -10.38016 | -50.84204 | 2024-12-07 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a265bf0-272c-324f-af1e-6cb37b3353fe | 2.51111 | -60.98774 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6a471ca-a0ac-39fb-bc1c-6d76521c3dd6 | -8.2794 | -48.0283 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e965067-f771-3ec6-b06f-5cead85bab13 | -10.03724 | -50.57267 | 2024-12-07 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f56f1402-e48d-311e-8b18-f44571b5fc30 | 2.42398 | -60.64979 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71c67810-da7e-3442-96a4-7836b35f8932 | -10.75195 | -54.7846 | 2024-12-07 04:55:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22880ed-cd31-3320-8f99-633fd2327f60 | -12.49808 | -46.34896 | 2024-12-07 04:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42bc9148-35f9-3af2-96f4-8f5f4d171656 | -6.45222 | -45.75256 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ffea9cd-a609-3d78-87d2-92cbfc730ca8 | -6.4518 | -45.75551 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c272c06c-a304-3cfb-a978-114d22f9c562 | -6.48739 | -44.68454 | 2024-12-07 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a9f7b39-ddef-39a2-9653-42177e5b83fb | -6.45771 | -45.75028 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b3f1f5d-2e9c-32d0-a5e6-4f1972b5acbd | -8.27878 | -48.03265 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 051f2bd4-2c59-3097-b2b9-eceb136ff1dd | -9.91032 | -48.58271 | 2024-12-07 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb382b6-b2f4-38d4-ab4a-eaa43f31b708 | -8.93728 | -44.24902 | 2024-12-07 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8a4ba559-abab-351f-bab3-d1c4663f5a1a | -11.87111 | -47.71343 | 2024-12-07 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68eed08c-2bf1-327d-9a12-7d535e38d19f | -8.27758 | -48.03379 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9ef3fbd-e6e4-36fe-b083-771e6c6683dc | -6.92672 | -42.84336 | 2024-12-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 316741a3-f334-3132-a493-a7456123fef6 | -6.202 | -46.06577 | 2024-12-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8b8b61a-d5da-37c9-90a2-56908b9af8ed | 2.51063 | -60.98452 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9d2a923-f503-3c43-a694-8cab0f2d9d03 | -6.45119 | -45.75191 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcbf60bb-4bbd-37ff-9367-40d52cc12319 | -5.50857 | -45.49123 | 2024-12-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e49ed4c1-81b0-3ca3-ba57-39d7bb80bc45 | -10.25497 | -52.85684 | 2024-12-07 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef4ac61e-c2a6-31c5-b84e-dc4fe042eaa6 | -8.30272 | -55.09 | 2024-12-07 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61f2b9bb-a199-39ea-bdbc-7d5510251aa1 | -10.66009 | -44.49755 | 2024-12-07 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 39aa5215-b518-34c2-8b95-68873bf69c81 | 2.51016 | -60.9813 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62dfdb8a-b75a-37c5-a617-9006a6d6f985 | -7.79855 | -50.00144 | 2024-12-07 04:55:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a03bf7e9-853d-34ef-8f68-29295bdcd8c3 | -6.45265 | -45.74963 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 625be53d-2548-386f-99cc-504f4ba75d02 | -12.28551 | -45.50632 | 2024-12-07 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa76d1bd-e503-32ce-8226-4a0186579075 | -7.08756 | -45.20395 | 2024-12-07 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e97c7bc3-9448-349a-8e51-98f15d5d1635 | -6.01038 | -46.40351 | 2024-12-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
