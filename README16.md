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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d7d9349-029a-3365-8e9a-b0fb314aaa13 | -14.74636 | -48.288 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1b41a4-4346-38c9-b398-ee138e771224 | -12.03542 | -63.77519 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a31af32-39b6-3939-a823-863006eb5d98 | -12.52291 | -57.23616 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e30edd17-082c-3fec-b8d3-8a458178089e | -9.91277 | -55.53088 | 2025-07-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61516bc3-9235-3e9f-bc4e-72b08be5ed7a | -12.9816 | -46.91499 | 2025-07-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45e2bd10-2c1e-35e1-9456-a6031a24f368 | -12.0205 | -63.7473 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e013e82-04bb-3dfa-b38c-e247680a20c3 | -10.83709 | -47.16819 | 2025-07-20 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c3cc3eb-101c-36fc-82b7-a73d5f8e2a90 | -11.46078 | -48.16495 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eb41912-3e87-3944-b611-c79e210ebb03 | -12.34875 | -50.3204 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69dd503b-812c-37a8-be80-0eee5521725d | -11.35911 | -48.73071 | 2025-07-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 129c5bef-320f-3f45-abd9-96dac79e8d83 | -10.68661 | -46.78917 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5cdffc00-8d26-3128-a8a9-8472bbbd2b5b | -11.8217 | -47.50672 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c3963ea-b873-3099-a36f-1817032567a5 | -11.95833 | -46.75184 | 2025-07-20 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c7c207a-b31f-304f-9135-834a8f9620c7 | -11.83623 | -47.50886 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d30166b-8758-3cb6-85a2-8e43960366e5 | -14.17987 | -58.18391 | 2025-07-20 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9def46cd-8788-36d1-afef-b994d2575c77 | -10.6329 | -45.22987 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fddb4276-452f-3851-9a2d-a7e73938ea4b | -12.00898 | -48.57692 | 2025-07-20 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60293ac8-b57a-3395-9064-fb40ce8f6758 | -12.36258 | -50.31899 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b922c2-cd23-39c4-8fbf-85bc7313cb50 | -11.8334 | -48.20708 | 2025-07-20 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c2606ad-9501-38ea-8e6f-2486763cb5f4 | -11.81744 | -47.51046 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a151cd33-cf72-37ef-a759-b61186757836 | -14.72184 | -48.25349 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a17dca4b-6b6d-3351-9886-4487909aa83a | -12.65793 | -47.09708 | 2025-07-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d094ef95-17f7-3ce6-9ff8-919ac12a8953 | -11.49247 | -48.07206 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f12aa9ca-e74b-33ef-9d69-a479c85b596d | -11.83691 | -48.20761 | 2025-07-20 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da51419a-215c-3f38-85ca-3f3968cc6507 | -8.96887 | -61.51448 | 2025-07-20 04:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfcfacb4-3505-3d48-989a-10dac5a6bf38 | -10.62974 | -48.0902 | 2025-07-20 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51c56f65-7e5b-3b43-b206-75d290d97508 | -12.58131 | -56.9827 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a451199a-d1ba-3c28-83f9-d0005a8b8c60 | -11.82596 | -47.50299 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 789ad770-69da-3c8d-ac54-ad9982f20a78 | -11.5727 | -47.09209 | 2025-07-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b00db3f-d198-3124-9fba-4f7a3db8a563 | -14.14883 | -58.20135 | 2025-07-20 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6915b977-5dbc-3408-9394-4b1dc6decd94 | -10.66235 | -46.79935 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| a40060c9-a720-353a-b8e9-b7fdac598ba4 | -12.66168 | -47.09765 | 2025-07-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b5b04b1-7179-33d9-8e65-1d51cd82ed0e | -10.81212 | -56.95771 | 2025-07-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83561c2d-278a-3bed-99b6-c02009801a31 | -10.66671 | -46.79539 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7a0f06be-ed51-365b-a0d9-07a886f08cbd | -10.69537 | -46.78114 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9eca9fd3-8be5-3c2c-b779-d578634dd068 | -12.35207 | -50.32094 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c12b77-706f-3df1-a53e-732f533ddb31 | -10.69909 | -46.78172 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b631fe-30ec-33f2-9e86-4037ba6aae6c | -14.48322 | -46.357 | 2025-07-20 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd56fcb9-bfc1-3529-844f-ddab70ec4bed | -9.40069 | -47.93962 | 2025-07-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1060bab8-9bc2-34f1-8c69-d0c38514fcd6 | -10.96951 | -45.10735 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 790b5e37-cd5a-3fdf-844d-e37d819689e6 | -12.02169 | -63.7415 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f52d8d96-a1ee-37d2-b36c-f5c399d615fa | -11.46429 | -48.16547 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da8ff934-59f9-3927-bd99-7911275d411b | -13.89505 | -50.65935 | 2025-07-20 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5d8e642-8681-3258-9c3c-ac039ca95038 | -10.66885 | -49.68044 | 2025-07-20 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 013e2d2d-199a-3a9e-b1cf-953f9ffcf464 | -10.38412 | -62.76513 | 2025-07-20 04:40:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7efc9e7-6834-36c7-83fb-c6aa37349787 | -9.97968 | -47.79926 | 2025-07-20 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ebc10cc-d510-38c9-9a21-ec525f2120d1 | -11.62908 | -50.73131 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df13a1ba-b842-376a-b21f-8efe3b4d11a5 | -14.20504 | -54.653 | 2025-07-20 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92a2f43f-f5a9-3534-9fa7-2beace73cc68 | -14.79101 | -48.29371 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fbe7430d-fd5d-3978-9196-c80eb17fdfc5 | -9.91388 | -55.52706 | 2025-07-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dca385e5-9a80-3b70-bd29-719430945d07 | -12.37092 | -50.41826 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ad7cbe9-63e0-3094-881a-ffa6274e52dc | -12.018 | -63.74728 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06fe2d26-6647-3793-aa4d-8905d9d999a2 | -9.6175 | -49.017 | 2025-07-20 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc3cadda-476d-3d80-aa7b-5e22035450cf | -11.78516 | -47.55391 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5ca18df-bead-3186-83d5-cb9a148e4dab | -10.63237 | -45.2336 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fe4354a-c12d-342c-9b5a-a69f8a1254bf | -10.66103 | -46.79667 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 64895157-fb4e-3fc3-b57f-d3ad429668bd | -10.54527 | -49.49409 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5a6542-802c-3c15-9cad-64845cab99ba | -10.01206 | -48.22254 | 2025-07-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ad5b6f-64cf-3279-9ba6-dc660cacc3e0 | -12.52085 | -57.22274 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f3d9406-e06c-3424-9c84-0d61345f2a35 | -11.46487 | -48.16151 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 770931eb-91d0-3ed9-9f9b-8563bc9174d7 | -12.51274 | -57.24303 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42970280-df23-3aa2-8a3f-59fbe834ef20 | -10.65665 | -46.80059 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6e30cde8-ff99-3a83-b62b-c24798538186 | -10.96898 | -45.1111 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bca1042c-c908-36c3-87bb-e65760af4445 | -9.39721 | -47.93911 | 2025-07-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e88c30a4-d921-37d7-a9fe-8ec3a281dedf | -9.79901 | -48.56224 | 2025-07-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fd01363-46b4-32c2-a4b5-d1110745aac4 | -12.68187 | -44.33158 | 2025-07-20 04:40:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b1ac642-6141-3880-aee2-98ee2318727f | -16.1351 | -52.24577 | 2025-07-20 04:40:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce764a15-3dd1-389c-9729-783a850d751a | -10.69844 | -46.78624 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7503844e-61ae-3156-8978-ddb73d6efb55 | -10.69471 | -46.78569 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9eb00b41-7202-3038-8c21-ed3bda875824 | -10.62775 | -45.23675 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45d726e1-debf-3dab-887f-a7ef4171cbfb | -10.65598 | -46.80511 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0afcbefd-6f61-3e67-a10d-49cde276b824 | -11.55725 | -47.09436 | 2025-07-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f6b222e-c266-38cc-8982-4e3383e3aa68 | -12.28911 | -48.78395 | 2025-07-20 04:40:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed5fdb37-aac0-3181-aca7-1170c0415769 | -14.71278 | -48.23949 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0340499c-7ad9-3990-b254-b1158e015487 | -10.9659 | -45.10294 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c119ef5c-5884-361b-b116-9eb880fecc00 | -9.93493 | -46.26926 | 2025-07-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d45e523-01a3-3aa2-93d6-84743f1b5719 | -12.51783 | -57.23958 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a900754-93f8-3615-b23f-71fd751c3203 | -13.54448 | -43.71 | 2025-07-20 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bef0a17f-d26f-38f9-b2a3-885354ad4ce7 | -23.25328 | -47.1166 | 2025-07-20 04:42:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 322315ac-5755-3a0d-80e3-ee69f9430656 | -22.43428 | -48.99042 | 2025-07-20 04:42:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfe24b87-b2c7-37cd-8bf5-469029061a81 | -20.05903 | -47.58645 | 2025-07-20 04:42:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331d408c-7e94-31fc-8e56-dcb50c64ad23 | -22.52434 | -52.01435 | 2025-07-20 04:42:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0cc4f52b-6bf5-38ad-8876-540e81be8383 | -18.40639 | -44.18921 | 2025-07-20 04:42:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7245be9-1398-321a-83d2-48ca5a3fc35c | -22.43387 | -45.47409 | 2025-07-20 04:42:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8e9ac3e1-23d7-312d-8967-21095a2b4453 | -20.05857 | -47.59011 | 2025-07-20 04:42:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b8f9fbd-e5ec-3813-8ceb-c81e3368b194 | -18.21941 | -50.95283 | 2025-07-20 04:42:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fde41044-5fa0-3ebc-9f14-ed2495b7210f | -19.90022 | -45.04059 | 2025-07-20 04:42:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c0292bb-89b7-38c4-8127-4a7bd86cd1d6 | -22.71246 | -43.84637 | 2025-07-20 04:42:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 70b08f14-380f-3bc5-b781-b21c5ffb311b | -22.912 | -47.02222 | 2025-07-20 04:42:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8109ed02-be01-396b-99c8-37ddc8c9a58c | -19.01937 | -54.66105 | 2025-07-20 04:42:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b7b040e-682c-3de4-a121-54646e09e142 | -17.88435 | -51.68257 | 2025-07-20 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29ec813a-02de-30ec-aace-3ad1631ae10b | -22.13775 | -43.19143 | 2025-07-20 04:42:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ca2071da-302e-3158-8dbe-02082fb9f870 | -23.32876 | -46.95937 | 2025-07-20 04:42:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 871e2ee1-91d2-379a-9f22-921ee8134223 | -23.14104 | -48.49345 | 2025-07-20 04:42:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 835c5e6f-0f2c-3725-85a5-469e23978787 | -22.13231 | -43.19033 | 2025-07-20 04:42:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74bd5f56-5663-3711-8deb-2f32dd7d7c11 | -18.89799 | -43.3404 | 2025-07-20 04:42:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 921c2288-13e8-3bda-a959-81683ee72e63 | -18.40443 | -44.18502 | 2025-07-20 04:42:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 689a958a-d54c-3920-a52f-349056585b38 | -20.09797 | -43.90896 | 2025-07-20 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a8c6ffe-09a3-3970-b5a3-acd946f54d44 | -22.51875 | -52.0055 | 2025-07-20 04:42:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08d2644a-4fc3-3646-a1dd-cb66eb594078 | -22.13126 | -43.19211 | 2025-07-20 04:42:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README17.md)
