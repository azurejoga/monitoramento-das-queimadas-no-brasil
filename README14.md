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
| c4991c70-961b-3871-a3cd-4079556ba1b7 | -2.97257 | -51.04969 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74d9f755-7859-39a2-ba67-fa9940d92e3f | -3.20121 | -53.40639 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2050b32-8fb5-35e2-8427-095060d00101 | -0.49455 | -49.15124 | 2026-09-26 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 201c182a-6910-3f38-8841-944db5b42b21 | -5.68122 | -45.86402 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcde0ec8-4635-34ef-8f5c-79eb9c789b79 | -5.73991 | -45.06733 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 482ec9ea-eeae-332c-90a2-837c5070d2b7 | -2.83776 | -51.36488 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a97e20ac-5401-344b-9174-3204faca822c | -5.77634 | -45.09437 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d705663-ed57-3aa2-89fa-3b0bef5acba2 | -8.34513 | -44.15347 | 2026-09-26 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2d8d932-82e0-36c7-b920-fac25718920c | -2.15431 | -51.98137 | 2026-09-26 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fd472ad-131e-3c4f-90e1-772a972a6f63 | -1.14741 | -54.1072 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0956ba-f393-3e1a-bb17-b443440bf49f | -4.27047 | -44.58635 | 2026-09-26 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4192aa55-73d0-30fb-a02e-7974fd055b0e | -3.23924 | -43.22263 | 2026-09-26 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 591a33d8-a2db-3fbe-9287-1d5e8487d8d9 | -3.20065 | -53.4097 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f8f2960-334b-3b52-bbcd-3bc7d9b232ab | -4.30336 | -49.12079 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b51cff-79b5-3754-9149-1f6a90505627 | -7.3497 | -42.09243 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fe7ecab5-be90-3d2e-95ed-b76c905cfcad | -5.51961 | -39.87091 | 2026-09-26 04:25:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7bc7c6ba-55b0-376a-8284-784691793425 | -3.94146 | -42.9916 | 2026-09-26 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c532945-8c33-34ae-8f39-77a3c48484e6 | -6.59868 | -47.22542 | 2026-09-26 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41323ea2-7e81-332f-a5b4-99dccd7e6b4c | -4.30282 | -48.06605 | 2026-09-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a883ac19-1584-333b-83e6-8c9e0134681c | -1.78502 | -47.83674 | 2026-09-26 04:25:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8993eca-101e-3fbe-90d1-4683dadf95a6 | -3.42017 | -50.42832 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 234f0b11-fe3d-3c74-a928-acede2d72fe0 | -2.26831 | -47.86839 | 2026-09-26 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b36e3e-6191-3293-8ff7-4038a58bba59 | -4.86967 | -48.90996 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5b444cd-1787-35b1-b031-924a59d71f7a | -2.90201 | -54.10116 | 2026-09-26 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6667910a-61a8-3e72-b4ed-e7f000dca83a | -4.29835 | -48.61639 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f27477cd-6365-3c58-9c8c-0a13260d5b10 | -1.21432 | -54.55887 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b740194-ba86-3d22-85cc-0b48b5b120b6 | -7.2361 | -37.74892 | 2026-09-26 04:25:00 | NOAA-20 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11bee42a-90ac-3639-b758-c4df5f2b5aa1 | -7.37038 | -42.09014 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a4e524fa-98db-3d9d-a309-a23d9a7c26f7 | -6.13197 | -43.74126 | 2026-09-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32e9014f-2b35-363c-9cb4-c476d7012e42 | -7.40315 | -39.78869 | 2026-09-26 04:25:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0aa2eb05-1686-3ad2-90f4-252833c08e9c | -7.36321 | -42.08903 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c7bdbde-8f56-35c2-9404-d759dab82ddf | -4.29772 | -49.13027 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f002496-7e7d-3d02-8832-33e5eef66d49 | -4.30252 | -49.12586 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25478357-7445-39a9-97c2-995841b42e22 | -5.77799 | -45.08398 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a96ac3e-1cf3-3ac5-b431-4d419e1c1659 | -5.77855 | -45.10182 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17c69a61-cfcd-3ca7-a346-c569ba4763c1 | -7.35033 | -42.08836 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b604a8b2-23f9-3d7c-bee9-6cd8df41a2fb | -4.50185 | -54.95522 | 2026-09-26 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43abfb16-edf3-398c-b000-9756f61eee4e | -2.57192 | -54.74749 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4817a518-4849-3808-ad3e-093f3ae62e36 | -1.8412 | -54.72542 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f88f12bb-3938-3f30-af88-b20042a7cb9e | -5.7791 | -45.09835 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c33d67cd-61e0-326d-8c77-d0feb57fb8dd | -7.24467 | -45.26132 | 2026-09-26 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db6057e-3336-358f-b913-29be501787c2 | -3.49898 | -50.74248 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc29052a-424d-3366-8486-a289419ec517 | -7.45185 | -44.57261 | 2026-09-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ed68a28-97b1-3f16-9c5b-0296e15c6984 | -4.2954 | -50.89402 | 2026-09-26 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0322e0f7-10e1-3248-8605-cf70df87e250 | -2.16274 | -48.96737 | 2026-09-26 04:25:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15232363-49ba-3a92-a726-97a9e1a027c1 | -3.49972 | -50.73811 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbbfebe1-e697-333e-8c71-c665426c4fe0 | -6.00253 | -44.91104 | 2026-09-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c934475-8465-314d-acf1-ecbb41f41c88 | -5.68066 | -45.86757 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04d9767d-7505-39bd-b3be-b5a4f7aff478 | -6.02553 | -35.43968 | 2026-09-26 04:25:00 | NOAA-20 | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dac4f777-a960-351e-bc8d-0acc030ae536 | -5.77359 | -45.11169 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ecb532e-9bc1-38b1-a46c-6dbe33502a08 | -5.77137 | -45.08293 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c2992f0-7f19-31b7-a196-0c7548e8eb64 | -2.98382 | -48.56741 | 2026-09-26 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 938ea645-ea17-3781-a46a-ea6b925635c3 | -0.49812 | -49.15574 | 2026-09-26 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec5993f6-73d4-3c26-9c1f-d3c91012fe4a | -3.2001 | -53.413 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c36ace-dc47-3a1a-ab71-ce24c29a87df | -7.35727 | -42.07972 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 81d2836c-dd0b-357b-8072-e78ed645cefb | -5.77303 | -45.09385 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6583b4b5-e79f-3699-99fc-cf20ef8da608 | -3.42084 | -50.42413 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dbb606f-af2e-30e4-8c0f-84ed6d802b10 | -4.29069 | -48.61516 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f1d8cf3-d899-35c1-a30c-68e0d922ad61 | -2.19225 | -47.64155 | 2026-09-26 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c42f0ce9-49c5-30d7-b220-71d3d14cbc58 | -5.7813 | -45.08451 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71295dc0-197b-372a-8bd3-35ce9a6c08c9 | -1.78466 | -47.83941 | 2026-09-26 04:25:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dede54a7-1e8c-3734-8971-308eb1694153 | -5.77413 | -45.08692 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bca5dd9a-026b-3f09-bf21-42eb23182523 | -5.77744 | -45.08744 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf2cf398-b83b-3619-a4d0-a227aed693db | -4.37265 | -42.99174 | 2026-09-26 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02698860-eabc-345f-92c0-fd4238d415e4 | -7.36976 | -42.09425 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0149deb5-4976-3262-9bcd-40ab1c5ef36e | -4.93029 | -45.81369 | 2026-09-26 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff15ca97-1625-3fd1-98a4-c1de935c14aa | -6.00198 | -44.9145 | 2026-09-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ec86bdd-8f5c-36e7-8009-d286fb07f25c | -3.87556 | -52.28501 | 2026-09-26 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc6cd2ba-f4aa-303f-9357-4b486dbe3505 | -1.21711 | -54.56359 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4441557-d43a-377a-9a45-b28d13115965 | -5.74267 | -45.07131 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8b03fed5-4f30-3003-90cc-ab99f4cec7c8 | -3.7162 | -45.96571 | 2026-09-26 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 203e3a32-f763-3d9c-b4b8-077f43e866f0 | -4.29687 | -49.13536 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e05ac19-91a5-3cce-b080-1f16a4647e26 | -3.93761 | -40.59709 | 2026-09-26 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f88f829-34df-3f18-a369-bb9a6e7e5baf | -5.77358 | -45.09038 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3490996e-9bb0-3c78-81b0-69ba8f012a64 | -3.41797 | -50.41774 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 599aeefd-733c-380c-8e9a-70575801f126 | -3.2685 | -50.14929 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 44cf0f30-4ae4-3e9d-af2d-04f595a1ead1 | -5.77579 | -45.09783 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a47cdc32-08cc-350a-b678-dc9039cd36d2 | -2.9982 | -50.47161 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 119bd1b8-9864-3390-bb76-c7168cae633d | -7.41192 | -42.63156 | 2026-09-26 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc6f3286-3bb6-312d-a3e8-87a26565c881 | -5.73439 | -45.05936 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f05f3a0-c6dd-3af2-8f9b-77db77203e29 | -5.78186 | -45.10234 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59713032-e902-3550-882d-c575028fe8c5 | -3.26985 | -50.14119 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fbbda1b4-f2bf-34e1-868e-eee9fcca378f | -7.39904 | -39.78811 | 2026-09-26 04:25:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1888334f-199a-3d82-981f-2c994ca40314 | -3.42122 | -43.16494 | 2026-09-26 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38747574-18d0-31d6-b4ad-388ae7cd1d40 | -3.42152 | -50.41991 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb9501b2-477f-3e9d-b31e-418a5b705004 | -4.8658 | -48.90934 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5bb65f4f-f5cd-3147-a8c4-d558c0ba2e6c | -1.83324 | -54.72165 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3c135996-21ee-33af-9852-0e2f9241d204 | -1.14291 | -54.09819 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b95d498-22e6-342d-b7f7-19c17a7eee5d | -3.76191 | -51.80931 | 2026-09-26 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60c091bd-6af7-3f98-a81f-1257660f7d02 | -6.70694 | -45.99111 | 2026-09-26 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84358355-b111-30bd-ad13-ddbc86b158a4 | -3.88164 | -43.10969 | 2026-09-26 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4282f382-34ee-3c19-835d-cec46a931436 | -3.26556 | -50.14048 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 155802cb-6d64-3b21-958e-5d7408cb89d0 | -3.77559 | -42.39803 | 2026-09-26 04:25:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e308015-201d-3fe8-b7a6-4927d5e47ddc | -2.46461 | -50.23262 | 2026-09-26 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b842d9b3-2b56-3a4e-bbd0-c912257ed45a | -3.22491 | -48.8143 | 2026-09-26 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3436a3e-ee4b-38b4-ac7f-e140414305ed | -5.73936 | -45.07079 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2eb7dac-ec83-3d1e-b607-eb9a20e3719e | -2.90267 | -54.09734 | 2026-09-26 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b47147a9-4c01-3177-b19a-5bf7e6de763d | -2.15408 | -53.71519 | 2026-09-26 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9646321-9e53-3b62-b00f-03612cc07168 | -3.80389 | -51.02631 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb141a88-04c1-39e4-9690-3ecf713786a2 | -6.31286 | -43.34021 | 2026-09-26 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README15.md)
