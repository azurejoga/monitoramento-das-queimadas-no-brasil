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
| 999a2644-a86f-3f2a-91da-151a87167144 | -11.25539 | -60.79428 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23a62dac-b007-3752-8293-837b564f311d | -11.36796 | -56.56018 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 11408531-61ae-3a53-a595-08d4f804e23f | -11.77861 | -47.39563 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 33d78424-8af9-37dc-a8c4-4f5f2ab6665d | -13.51992 | -56.56086 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc865dbf-5b54-39eb-9473-cbea70b5cdf7 | -12.87758 | -52.20442 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0d3214c-37d5-3282-8e92-f35dcbf3f731 | -10.29936 | -57.13793 | 2025-06-07 04:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 265e3618-76d8-3e9a-87d1-b897d011d6ea | -14.1987 | -45.49852 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71849bfe-a7a4-3142-9a84-a47ce4b885ee | -12.32948 | -52.47318 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 598ba2c9-15f1-3902-a6aa-6daa160bcb47 | -11.77789 | -47.40082 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5fc7b9b1-5e76-3308-a443-1ad78307cdf8 | -13.95996 | -50.10125 | 2025-06-07 04:46:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bd7ae8f-5f63-3527-ad8f-9d2acef7da65 | -10.81635 | -56.95471 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9331a92-3fba-3695-b252-9ee566d50a20 | -13.36724 | -54.25992 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d307c4e4-2613-303f-904f-382909970704 | -12.28421 | -57.26682 | 2025-06-07 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c932f136-1370-39ff-b975-2480161162aa | -17.02294 | -50.29938 | 2025-06-07 04:46:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecd2ba69-f51b-3605-8fb1-cb3031d84636 | -13.33794 | -45.48576 | 2025-06-07 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb303fa1-8633-36cb-94b1-84eb0e623871 | -12.95984 | -46.76031 | 2025-06-07 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 081e36ec-71b1-30a4-b4f2-8f6b196e202c | -12.88089 | -52.20496 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46f1b9f-6123-3062-b6e8-7b42843b5d26 | -15.52078 | -53.51025 | 2025-06-07 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 76793255-3451-336e-85ce-9e8c54bb0efc | -12.28388 | -50.10042 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 462a7b68-9d9d-3831-91c2-836320b328e1 | -12.32892 | -52.47669 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227b57a5-ebe3-3195-a901-67c5ed3c2d69 | -11.67276 | -54.5527 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26b710c1-b4cd-353b-8065-90d092c4b801 | -11.37734 | -56.55173 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee19a117-b981-3755-9659-4fe71d29f2f0 | -14.88058 | -48.11089 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e2b55cc-8127-32a1-9fa2-dc87c3cde8a0 | -11.83002 | -57.8176 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c7bb28f-b409-3a86-a134-da9fd53d04f6 | -12.07719 | -48.45362 | 2025-06-07 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1498af9-1402-35d4-8a0f-f06b9067f4a2 | -12.4774 | -54.42117 | 2025-06-07 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 131e8438-2185-3477-861b-0d745c434ac0 | -14.8873 | -48.11362 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b1f62b4-e5d0-3b6b-b0c0-43a393cce201 | -13.09609 | -52.2835 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67ac8a6a-371f-3086-bacd-293d8f0f611f | -12.88144 | -52.20144 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11e64f8f-f1c1-3f59-9d05-debadd08a79e | -17.81183 | -51.00965 | 2025-06-07 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5dcc44d2-9d15-326e-8189-9145b62811fb | -11.37265 | -56.55594 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 02b81333-473e-3949-8923-38f5970ca6b1 | -12.28041 | -50.09989 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c51dda6c-db67-3c63-80d1-7b2c31cbf77d | -13.28221 | -57.9365 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2cc3768-0155-37be-b38c-6e9d764f2280 | -11.88621 | -56.412 | 2025-06-07 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07d89bde-3441-3483-b323-a8df9195235c | -11.53789 | -60.99306 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd77dc23-0a62-3066-a5e2-45efda5c4e1d | -12.90401 | -55.04231 | 2025-06-07 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c2c866-9b99-3271-a286-d968c5eaf746 | -11.89 | -56.41266 | 2025-06-07 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5bc0148-f1c6-3ace-af62-eaf912b5547d | -10.87978 | -54.30042 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccde4a1e-f510-3cb3-87fc-f248eef690f7 | -16.97604 | -49.7306 | 2025-06-07 04:46:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa3e9cb8-aa45-3987-a9dc-0943f8a0fc5b | -11.4103 | -55.08432 | 2025-06-07 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c238f03-71c8-36d5-a272-3774a1598732 | -11.25142 | -60.78728 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a2e9f0a-193b-3b35-b03e-3b1c03f47a32 | -11.38504 | -56.5531 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d25843-7705-36b7-a944-538b8ad68ff8 | -12.28734 | -50.10095 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5caff86-b807-350e-8069-a1b17e2f05eb | -11.25821 | -60.80753 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 107210c3-61a6-3d2a-9012-20f00c31e2b8 | -14.03265 | -55.13205 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2fdadd4-0830-3823-8f11-71470b1e7c0b | -12.3361 | -52.47426 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8c25f9c-ab63-3980-b2db-139351e30a44 | -17.26491 | -42.65946 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da03cf8b-13b2-3b8f-a043-554c39da6c01 | -18.81835 | -46.43764 | 2025-06-07 04:46:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2b23916-2026-3ade-9b0b-99316c5697fe | -11.5687 | -54.56768 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99fb469d-e0a0-32ab-8053-b7e3e085b187 | -11.25084 | -60.79039 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23e831a5-8d55-3396-be10-dad6ece2d893 | -11.37181 | -56.56088 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a7684b8-34ba-3a1a-a976-1da230530871 | -14.728 | -45.07241 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd2bdb64-6c8f-3141-a63b-50e87f19046b | -13.46864 | -56.85604 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 808ff19f-5ec4-39c9-9db3-8e4a2cd97b7a | -11.25878 | -60.80442 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5beff1-390b-324d-9c20-694f5123c383 | -14.884 | -48.10808 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb0043ce-b12e-3eb9-b60a-c3807e3e4df8 | -12.78007 | -48.72381 | 2025-06-07 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 943031bb-f2da-302c-95ce-81700e887ca7 | -11.13391 | -53.94756 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c15dc6-80f4-37a9-a09f-858fcb52b425 | -11.78186 | -47.40137 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| becf5ab5-568a-3007-9b13-5ff318cc89e5 | -11.37817 | -56.54682 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2531c9b6-5542-3c92-bc53-be5c39f87d60 | -13.28628 | -57.93729 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23cfb9d5-567a-32cd-afc7-4d8e34805446 | -11.13854 | -53.94063 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cab88d2b-982f-353e-9454-ef423ed4b87b | -13.29849 | -57.93957 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb402a5a-9d03-32b1-9868-0179cc36dbc0 | -13.46399 | -56.86018 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79e3fcc7-0c39-3723-9634-be63936e775b | -13.3413 | -45.49606 | 2025-06-07 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 051743ed-e1c6-30e1-bbd4-f6516f960bfc | -11.3688 | -56.55524 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6ce3f958-5bb6-3e1d-940a-60666647385f | -14.7411 | -45.09498 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0373493e-768c-3684-bc61-99e2d121d928 | -17.91144 | -54.11234 | 2025-06-07 04:46:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9683b61f-d283-3858-b384-6b3c8f1bd7c1 | -14.03612 | -55.13267 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 138f1a52-b25d-3d3e-b38b-44dc34d254b5 | -9.41815 | -63.33894 | 2025-06-07 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7fa8b0a-319e-3c22-ad73-a7ba2204b3b8 | -13.36385 | -54.25935 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c5703e9-c009-309e-a293-50ef35880faf | -13.29442 | -57.93882 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 589cdecc-664c-35c9-b8b3-01ce7c5a8645 | -11.54273 | -56.44157 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6d0299e-ae16-3bdf-b502-d79538e891ca | -14.23727 | -45.49355 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b95fa360-1143-3adf-ba15-e74cd50c01aa | -11.25935 | -60.80135 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c62ad818-d2cc-3355-9b35-5f117db5154e | -14.7425 | -45.08397 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82472b83-228d-3747-acb2-fde6dc2a9e6e | -10.87568 | -54.30369 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68687a62-a477-339a-944a-9d4a6894135d | -12.41846 | -43.81546 | 2025-06-07 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f7e4978-510e-390a-b5eb-a485a54229f4 | -12.70137 | -58.24163 | 2025-06-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edebf42d-6a4e-339f-a8ee-78a3e9ed6f18 | -14.72734 | -45.07801 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03a2c0d1-e12f-32a1-a804-60950ae2cc95 | -12.29196 | -50.09374 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d165283-6205-38a5-8b8b-74779e2ae6ea | -16.00235 | -49.71415 | 2025-06-07 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d72beae3-9a3b-3f6f-a707-696f8c2f94bb | -11.36411 | -56.55946 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59b07c4d-89c7-348c-838b-db609e3d7c0f | -18.23474 | -47.93753 | 2025-06-07 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 143630b1-2d06-385b-8688-9de0753c47f5 | -14.73701 | -45.07919 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eec83132-0bca-3e43-a11c-d0a0ce740be5 | -11.06362 | -55.07521 | 2025-06-07 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be046470-d6a8-3d7c-9d10-1936c6ad2b6b | -11.78258 | -47.39618 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a3286efa-d9cf-3cb0-a878-5ed9052a3f7c | -14.88331 | -48.11328 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 608862a9-e56e-3a6c-901f-2bd9514f6b92 | -12.88752 | -52.20604 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc20dbbe-6ba6-38d3-9163-09817f254e10 | -12.88476 | -52.20197 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa0872d5-a9bf-3fd0-ac1e-2605a0f9346f | -17.34887 | -52.0098 | 2025-06-07 04:46:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d5fa12-29b9-3ca5-9078-cba80408565e | -11.77392 | -47.40025 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a86944e7-eaa1-3d58-bf37-482a8dcda04e | -10.05513 | -59.36127 | 2025-06-07 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acb03dd9-ffe6-3fff-ad98-baa703542f45 | -14.73569 | -45.09031 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ead6a8df-35a4-3b95-a62e-cca44ded10f1 | -17.25874 | -42.65533 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2125508f-ef06-321d-b836-bc72342e8582 | -10.69363 | -57.65104 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90d2132b-76f8-3050-ac81-75317326c10d | -13.07502 | -49.24246 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95dd9c95-39a7-385c-9def-27d31887aacd | -11.83407 | -60.92104 | 2025-06-07 04:46:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 461893db-5beb-3199-a03f-7e464fa19fb8 | -13.88377 | -54.68253 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4795fe2d-61aa-3b51-add9-396296260313 | -12.28209 | -49.52883 | 2025-06-07 04:46:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af20aeff-b0e2-32a5-b1f1-c569795fd66e | -14.72797 | -45.08241 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
