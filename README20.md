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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d3d226-18d5-3cdc-b83e-78d688da33fe | -13.24387 | -54.3256 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b00156d-af62-3005-8a83-54a097037b7b | -13.23856 | -54.37064 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5ebd945-65bf-3e90-a41c-1fdfcb607539 | -13.2564 | -54.3225 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 993fe502-f33f-3afe-83e3-d5449e5c5dc9 | -13.25948 | -54.31913 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e347e183-c7ca-385d-afdf-050c14d8d9f8 | -13.2254 | -54.32759 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0e0a65a-43d6-3927-a227-bc5f3c55c9cf | -13.25143 | -54.33677 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b976001a-b501-34ba-b947-eb27b91886b2 | -13.23737 | -54.3292 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409e17a7-ebbc-3568-90fc-30ee4c4830a4 | -13.24932 | -54.33093 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8820e1f8-a9bf-3cec-98c0-44cf07a3c9f6 | -13.23897 | -54.33956 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 51fc385d-43b9-3e62-a0b4-5b0dded7f455 | -13.24798 | -54.3131 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be879b4-6d55-30fd-a69b-c711bf97f20a | -13.25042 | -54.34587 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cfbadbe8-2418-34a9-8f48-c699aca87be7 | -13.24644 | -54.32697 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb36575c-857e-30aa-b996-2c65ca077609 | -13.25346 | -54.31858 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7746fcf-58a3-389e-a56c-48833e8f8ce5 | -13.24444 | -54.34502 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d94184c5-c832-33ae-8070-1918dc549e8b | -13.23031 | -54.33753 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58887148-26ae-3248-b1ce-f841c6e6928c | -13.22977 | -54.34217 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f5bd083a-fd2a-3961-8a28-4c50cbb855a7 | -13.24441 | -54.32106 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2f915f5-a262-38a3-8410-80abf4df5ec9 | -10.06867 | -67.56037 | 2026-07-04 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00291a16-6e60-3e07-8c14-a6c37c487008 | -13.25294 | -54.3232 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f45596d-3c9c-3355-978b-9a61564e86f8 | -13.22922 | -54.34681 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b322131a-94ec-383e-aa5a-09b7b520479b | -13.2564 | -54.34671 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fd9fd9d9-de95-38db-88bb-ae95a9ae2089 | -13.24229 | -54.33902 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bfae9631-e879-325b-818a-c748ba99d9c6 | -13.23997 | -54.33056 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c365dfbd-6c24-3dc6-ba7b-00ad9215b3ad | -10.90336 | -56.8553 | 2026-07-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b6357ca-b5f9-397c-8862-a283b40ccded | -9.23416 | -65.74859 | 2026-07-04 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ec0186f-727a-339d-9d7d-c5ed346e4867 | -13.23467 | -54.3521 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b626f977-6b13-3344-9c68-2083542fb5c1 | -9.37315 | -65.77519 | 2026-07-04 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4fb6352-284d-3846-afd7-5e33dde0e26b | -13.23577 | -54.34282 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4616178c-fb4f-31ed-bfbe-eaf4b6f1ece6 | -13.24747 | -54.31777 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06778c6e-cee4-3e97-9273-60e65d9bd782 | -13.23684 | -54.33367 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83206617-4fa7-318b-89e9-2e5a68c44b97 | -13.25742 | -54.33756 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10f58c08-faf0-3632-9979-917c9df5abd2 | -13.25095 | -54.31722 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931824d3-e506-3b55-9e5a-f7980e6db28c | -13.23896 | -54.31565 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cac91ec-acad-3cb0-8d9f-8249eda2db4f | -10.9053 | -56.85543 | 2026-07-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28dac3b3-1767-3b1c-82c4-920184655a06 | -13.24496 | -54.31641 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d398d575-0b46-30f7-87bd-a35ef8ca2a7c | -13.23206 | -54.37432 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bb163f0-a717-359d-b05a-7b8e0921be54 | -13.22377 | -54.34151 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd41f56c-2a67-331d-8908-a449ca030207 | -13.24718 | -54.34902 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 03874deb-fd74-324b-a96b-5689c3595f2d | -13.23947 | -54.33502 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba64ca96-50d6-3def-b782-d81860eeac7f | -13.25793 | -54.33297 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a54eb0ef-2d19-3f46-8481-2fb4a65eea33 | -13.24147 | -54.31696 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c6bddcf-aea4-3789-8938-1018cdcb5889 | -13.24175 | -54.34361 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2787bb9-017c-3c53-8553-ee20955409bb | -13.23497 | -54.37574 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2074a8a1-98bf-34ab-89da-6bbbc13c7d33 | -13.24551 | -54.31175 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2ea2f19-f846-33fd-a60e-351c93df2f16 | -13.22997 | -54.39209 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c60ed22-33e2-31bb-84e6-1ed37fa874fd | -13.24334 | -54.33009 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753a7b9c-bb02-3206-bf47-41fde689c7bc | -10.90828 | -56.85592 | 2026-07-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98321b8e-a4c2-34f0-a8a8-e501da0f01e0 | -13.23139 | -54.32834 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9229cca6-c3c7-362e-95b6-4ae87baf892c | -13.24282 | -54.33453 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac99ea07-1737-3882-abfd-4c227a6adf02 | -13.23191 | -54.32389 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c98823a-5bd7-31ff-bc61-04c5d10e3810 | -13.24826 | -54.33988 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a149230b-e881-36e0-8fd5-6e120a538d77 | -13.22486 | -54.33222 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aa680ad-21f6-31c5-8db5-c257f40ced9c | -13.25896 | -54.32374 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad344f3a-4cc7-3ffb-8945-133308dbfc52 | -13.23546 | -54.37126 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9639991-4cd7-3b6c-8f1e-92684584848c | -13.25424 | -54.34073 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 23f8d388-b73c-308f-89d1-53c2057d6667 | -13.22323 | -54.34613 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43cdb914-2118-30e9-9dc0-c6c643d3eee1 | -13.23522 | -54.34746 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 185d738b-cd00-3c97-8cce-21a8ba370931 | -13.25691 | -54.34213 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5784c101-7905-3105-bfb7-53da732b39a5 | -11.70304 | -62.71805 | 2026-07-04 05:42:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 219012f4-4bb5-3c09-b76a-4e1703f27310 | -13.23795 | -54.34882 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3d5c1ed-adef-3dc7-9cc3-2cb3f9427f91 | -13.2504 | -54.32185 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25adb47d-17be-3d86-9a57-06f2842078a2 | -13.24393 | -54.34961 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcd758e7-2631-3e98-ba74-d1e61f42a3de | -13.2401 | -54.351 | 2026-07-04 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 640ebe68-f14f-32b3-8bf2-f5713f36a7ec | -10.9397 | -43.0593 | 2026-07-04 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e02c3997-b5e6-3c70-afe7-601b1d251c4c | -12.7553 | -44.5194 | 2026-07-04 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 68cb8f18-8ee8-314a-abd1-5a63c62e9cc9 | -13.2404 | -54.3303 | 2026-07-04 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ac2d0170-568b-3ef2-9999-23520a94b573 | -10.9401 | -43.0355 | 2026-07-04 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 200b852f-9def-3550-912a-23c75b837988 | -13.2209 | -54.353 | 2026-07-04 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5a571e7e-60a5-3299-90ee-a9b911df0c39 | -13.2212 | -54.3324 | 2026-07-04 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cae77b33-8d61-3d5f-83e2-61e61e9b535e | -10.9209 | -43.0384 | 2026-07-04 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d3ddff88-1049-3918-9f62-946f03fadfcb | -12.7548 | -44.5428 | 2026-07-04 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 8dfe73c2-04fc-3cd7-8ce4-e92012c4f6e4 | -10.9205 | -43.0622 | 2026-07-04 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7b6c7fd6-4c85-3b0d-b40c-19c27133b7b7 | -12.7741 | -44.5396 | 2026-07-04 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| af5c8c13-d5a3-3acd-be44-d9b0d457e74e | -10.9205 | -43.0622 | 2026-07-04 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 15d1c023-792a-3ec7-b38d-8804b181c56d | -13.2209 | -54.353 | 2026-07-04 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8b8c7bd4-be17-3b47-b86c-18a386977988 | -13.2592 | -54.3489 | 2026-07-04 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 804fbb4a-c14d-37a0-b61b-9e5bc86d48ef | -10.9209 | -43.0384 | 2026-07-04 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a4f9f704-f2b3-32b4-ab12-2d4f800832ba | -12.7548 | -44.5428 | 2026-07-04 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 390d44a0-8ec1-3777-aeb5-eca0bb5b570e | -13.2401 | -54.351 | 2026-07-04 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 281a3d55-38c6-3bb7-b697-23880167c238 | -13.2404 | -54.3303 | 2026-07-04 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 859853ac-98e1-3445-82fa-9e0b11daf165 | -12.7553 | -44.5194 | 2026-07-04 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 61f0cfd7-6457-3f7f-9f40-781fde8eda85 | -10.9401 | -43.0355 | 2026-07-04 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6c2ea539-a77d-37fc-9edf-09d620ec5113 | -10.9397 | -43.0593 | 2026-07-04 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 9f1923d6-16a9-304b-88ef-a4d5f8d308ba | -13.2212 | -54.3324 | 2026-07-04 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ab519cb9-2bdd-374a-b7a2-5cdeed23a2fd | -3.41799 | -41.70416 | 2026-07-04 06:05:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 6ed319a2-cef4-3b74-b0b5-e7814120609e | -3.41642 | -41.71441 | 2026-07-04 06:05:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8eb2fa20-dfdc-3925-8b36-f248699a1b9e | -3.42586 | -41.71585 | 2026-07-04 06:05:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 23600f47-6261-3d3c-9775-6bb559795931 | -3.42742 | -41.70562 | 2026-07-04 06:05:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bb8c8f72-1877-3068-90f7-c2d87e37326f | -12.75883 | -44.52448 | 2026-07-04 06:08:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b4c444fa-75aa-3f47-b98b-d8a9a19fa5db | -5.31981 | -43.55143 | 2026-07-04 06:08:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 59cdc2ce-7515-310a-9439-d0d764a9b230 | -11.92552 | -43.38067 | 2026-07-04 06:08:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 42ff4b91-3019-3dc6-b574-277fdcf397a7 | -12.74711 | -44.53429 | 2026-07-04 06:08:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 83407378-b893-3963-8cb9-8ea0a32bcee7 | -5.31782 | -43.564 | 2026-07-04 06:08:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b5b17a9a-91ae-31a7-96e6-ff228cb1ec27 | -12.75696 | -44.53595 | 2026-07-04 06:08:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6e85ce14-71e9-387b-afc8-7c8d7db80056 | -12.75509 | -44.54742 | 2026-07-04 06:08:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 22e70e40-2ec7-3b40-aaea-26011518f18e | -10.93089 | -43.04898 | 2026-07-04 06:08:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 64967093-f492-3e5b-9428-35f20e6cfef5 | -12.74899 | -44.52282 | 2026-07-04 06:08:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| aa70faaf-0d33-369f-b22d-939816669741 | -10.92323 | -43.03749 | 2026-07-04 06:08:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3136e2cb-ff3d-3300-a90a-24aa73addf7d | -10.93248 | -43.03899 | 2026-07-04 06:08:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| de963b76-0d67-3496-b8ee-9737d0422cca | -11.42376 | -46.57925 | 2026-07-04 06:08:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README21.md)
