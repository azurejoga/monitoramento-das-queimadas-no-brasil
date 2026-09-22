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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2be3c66-09f1-3202-9368-573c7e152003 | -2.94742 | -51.03898 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23420ea1-b5d0-33af-a8ac-8451203e10f8 | -2.21512 | -48.7683 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03340657-9dca-3b81-b8f2-9a94753f0d75 | -2.08308 | -49.6891 | 2026-09-22 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed10eaef-c6dd-3471-812a-b3b8417480fc | -4.68348 | -40.14677 | 2026-09-22 04:44:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0ce5b697-ed92-3c65-805f-604683e883a5 | -2.31459 | -45.84454 | 2026-09-22 04:44:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ee71dc8-942c-3364-9537-d9f1a18e16df | -2.97097 | -50.40872 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e747cab9-f797-395a-9600-5195074f996f | 2.28766 | -50.93158 | 2026-09-22 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f41d10ab-865d-3bbc-b52d-f91c6950a110 | 1.5442 | -55.78658 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe59153c-89c3-3beb-8694-12feb60918f5 | -2.9052 | -48.90661 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a393f26-6eee-3d3a-890a-f5b5f90ea3d2 | -2.78188 | -51.3548 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36987be7-f029-3502-906f-5414386f555d | -2.02736 | -48.77615 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87082cb9-0f6e-3cf2-a9c9-4ab6fe677532 | -2.62052 | -51.73006 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ca6a286-c41c-3dc4-bb92-902d20ba4d0a | -1.97772 | -50.79832 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d9a1f82-227d-3fc7-bbf3-3f0b52567ee0 | -2.93778 | -50.49141 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab0e8ccf-02b7-394e-af61-d5f4e4733225 | -1.46805 | -60.272 | 2026-09-22 04:44:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 467521f3-2e84-3ee3-9dbc-07e677f5ce0b | -0.5157 | -49.15839 | 2026-09-22 04:44:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6139abb6-b760-304e-86f7-2752d934cff6 | -3.16854 | -48.61116 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d230e9-abd5-3c1e-a30d-a854082c4322 | -2.94109 | -50.49192 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 247fc64d-c629-3a99-9b52-987a91103cf4 | -1.29899 | -54.20914 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a8f6323-7289-3f64-90f2-98a9f103865d | -1.21385 | -55.62606 | 2026-09-22 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f5fe596-facd-35fc-8944-c756514d8b21 | 3.24659 | -60.23856 | 2026-09-22 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28f4c37d-909b-3d17-9baa-fbd3e2db7bf0 | 1.9902 | -50.87333 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf8c9f84-1b4e-3c1e-98e1-f0712d9c7aad | -2.20708 | -56.09222 | 2026-09-22 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 950a0c1a-c2ec-3c23-bde2-6f11ec151a49 | 1.50491 | -55.88592 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 48c18568-dfe5-398e-9f0a-236336be7436 | -1.46042 | -54.2416 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e56252fc-84ca-3b46-8c93-c15d0b544c89 | 1.51122 | -55.86747 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 019e53ca-4f7e-3b73-865a-ff88ca715a55 | -3.16305 | -48.08032 | 2026-09-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31afda8f-6389-3cf6-b4a2-d6872010e643 | -1.29977 | -54.20415 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6d74ccd-aecc-374c-b760-a06f0f19cda5 | -1.33556 | -54.66603 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d4ca055-f05d-35c3-bdd9-445081b94304 | 0.17211 | -60.4952 | 2026-09-22 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39f34c8a-e22f-393e-b541-528371554312 | 1.55877 | -55.79337 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09baf495-24fb-31e1-a576-0c4554f5b885 | 1.81446 | -56.08035 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b1d71c82-3d04-3731-8306-f7703b233d8a | -2.83252 | -48.6506 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccfefa79-5628-3621-a41a-18eeb8871271 | -2.96157 | -51.42558 | 2026-09-22 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4033ef5-f658-36af-9335-7c1f10ca168e | -2.95073 | -51.03949 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa02532c-e6cd-3741-a403-41c9be4840be | -2.54339 | -48.15958 | 2026-09-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c1e098c-ce7b-3493-8ef2-43a742a7ec7c | 4.03632 | -59.65754 | 2026-09-22 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad46320c-1ae5-3dcc-9831-3909cf6a5dee | 1.50552 | -55.88532 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f11f7bc1-91ee-3f67-87ad-78066b3fcfbf | -3.34481 | -42.77858 | 2026-09-22 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c98528-83fa-3784-9c8e-2095afb2f931 | -2.8371 | -50.46106 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683c69e3-b616-3a5c-8661-20cfeb0fd11c | -1.21182 | -47.90026 | 2026-09-22 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acd86f3c-26b3-3e75-ae24-f6c4d54c5f91 | -2.78521 | -51.35532 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e562d9b4-6268-357d-ac66-22adc6614985 | -2.26173 | -48.75708 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2db80322-3063-30c1-ae6f-8f9320e437c8 | -1.24451 | -54.55466 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c99f2749-de26-3fcb-a195-9743c7683723 | -3.16365 | -48.07648 | 2026-09-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 932c344a-d555-32bd-93b1-badafc032039 | -2.94055 | -50.49535 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eec75ca1-a267-33c7-a3d1-0b222ae8166a | -1.74735 | -47.13522 | 2026-09-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0d023d45-d57d-378e-9a68-cc82e1b288b5 | 2.09947 | -60.20784 | 2026-09-22 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dfbcd386-512d-31b1-959b-1ede127ea337 | 1.50556 | -55.89035 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2cec7da1-a15b-3a50-a029-f5cdf3ff38c4 | -1.78467 | -47.10744 | 2026-09-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83db70cc-4b42-31c2-b586-216b34cad1c5 | 1.53694 | -55.82788 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fa818d79-ed68-3ee7-a5a8-c405302c2bba | -2.31087 | -50.45277 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4a470df-ee5a-3c06-84c7-320ab910e4a0 | -1.46871 | -60.26805 | 2026-09-22 04:44:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad8d1ff-e68e-3ad8-ae67-eefea78dfdda | 1.50937 | -55.88541 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 71e36ce1-1d0a-3529-ac59-779e228138eb | 1.95895 | -60.57127 | 2026-09-22 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2f53df8-38c7-3798-bc67-767e0b9ae9d6 | -2.85223 | -51.58136 | 2026-09-22 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de9c14af-6922-33c2-97d5-91943c50d6d8 | 1.51761 | -55.87991 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ddaed82-c03e-358b-a26e-1015e2c446b7 | -1.20577 | -54.01356 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1801421b-d166-33a3-9ccf-52701490f429 | 1.50873 | -55.88115 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 971f483e-758a-3f01-b4e2-f7d0e68ba263 | 1.97444 | -50.88308 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a337b61-2fc8-35a0-a12a-fa46c545f2a7 | -1.68289 | -54.93339 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27391f2a-0145-3862-a9be-6735aff8859d | -1.41656 | -55.1607 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b8663cc-72d7-32a6-96ac-d9513fe916e2 | -3.68666 | -42.95388 | 2026-09-22 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fcf3dcc4-8925-3e51-bc3c-31f25eb91175 | -3.04349 | -50.26885 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ff0bf2c-970f-339a-8d67-99eb8efae72c | 1.97837 | -50.88617 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36b6f025-eef3-3d83-a7a3-6c922ee79d6b | -2.94609 | -47.96157 | 2026-09-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 367047d3-9200-34a8-9ab8-063a185d9a51 | -2.61996 | -51.73362 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 995702de-7d56-3d4c-815d-3807361f1612 | -3.34403 | -42.78392 | 2026-09-22 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3035ae3-f073-3970-9bff-00f64fd875d8 | -1.33487 | -55.46367 | 2026-09-22 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264a4d97-1b77-38b5-a680-c8a2e4e50826 | -1.941 | -49.79356 | 2026-09-22 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f83c3ea4-6587-3a0d-bf45-68987995bd15 | -2.96071 | -50.32284 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b79cde07-df4e-3539-8b64-95305b6d17e9 | -2.67994 | -49.02211 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d732b9b2-2b34-32b1-b663-b22c266a0c45 | -1.46659 | -60.26827 | 2026-09-22 04:44:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 276a2b9c-3975-3703-a564-21aeac895d14 | -3.15957 | -48.07981 | 2026-09-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2364695-70e7-376c-9c77-bb548a891167 | -2.6166 | -51.7331 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc78d72f-c025-3485-bbe5-3e7e7f65106e | -2.02681 | -48.77973 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebcce99c-daca-3da0-a39e-d7b349d3fce8 | -1.45692 | -54.24314 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57060f2c-ae98-391b-9abe-298ecaebf103 | 1.53626 | -55.82336 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a1661af-60b2-3c38-bfab-820a7dd70ab9 | -2.7729 | -51.37059 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2aeed34-cfce-3316-b7a4-4e8a32545677 | -1.11459 | -54.12379 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98e9cbb7-47dd-3a4b-9470-fcab87645e69 | 1.98345 | -50.87435 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8273ac4-889b-3a71-ae30-eb2bbdc234d1 | -1.02129 | -53.73352 | 2026-09-22 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd10bfd3-5d40-3749-aa9f-e43c40057c54 | -1.02336 | -53.72048 | 2026-09-22 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cb34b13-626e-3ea7-b9dc-7ec3141e9f52 | 1.50998 | -55.8848 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc0cee46-c3b5-37fc-9d17-e764f121a6d0 | -2.74238 | -51.36945 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de75e71a-28a8-3014-b537-14eaa293c63c | -2.32477 | -47.20111 | 2026-09-22 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d9e3474-626b-3960-a63e-78a772db589f | -1.24842 | -54.55517 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b07777f-d719-3fb0-b94a-99e948235026 | -1.39105 | -49.32594 | 2026-09-22 04:44:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e8de08d4-c351-3eb6-acdd-9627c8acd9de | -1.37306 | -48.28468 | 2026-09-22 04:44:00 | NOAA-21 | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04f69e41-222a-39fb-8d1c-8f12c59b35fb | 1.51375 | -55.87991 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c81bcd10-4d04-364f-b0f4-87f2ccfd99d1 | -2.93725 | -50.49484 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59bfde6-3e64-3623-a0d8-936245313792 | -2.95824 | -51.42506 | 2026-09-22 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e125faf-126d-3418-a56f-51788bf50d5d | -1.46072 | -54.2438 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0abb567e-22fb-3ae9-b386-c67333c8b325 | -1.78109 | -47.10688 | 2026-09-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a95ca5ba-d9d4-3a0a-a4f4-ce0a936c69b1 | 1.54484 | -55.79078 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6d33a3b-0523-38ef-8614-944402608355 | -2.93832 | -50.48798 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c98c1a5-1d59-350c-a22b-103816ade50b | -1.09537 | -48.06217 | 2026-09-22 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b84fec7a-3a12-3794-9e4d-069128c5d0c2 | -1.74672 | -47.1393 | 2026-09-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a7a68fe-83c9-39c0-8ed0-008c7375ab22 | -3.00904 | -49.55199 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8969f6ce-73a7-36cd-bf44-ecdd4589eb6e | 1.50487 | -55.88114 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
