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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d501886-4771-3bf5-9011-8388d002f233 | -11.68174 | -50.22803 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d789d91a-6ad2-3440-94f5-aaefd8d5f94e | -14.17658 | -51.90013 | 2026-07-25 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a83d11de-e659-3280-b879-561bfd02fe9e | -12.4288 | -50.41118 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30f36c6e-89dd-30cc-a4cf-4a0667dee360 | -14.17543 | -51.90805 | 2026-07-25 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eed0951a-fbe4-36a7-ad37-f3cda19510d9 | -11.69867 | -49.02233 | 2026-07-25 04:53:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05906581-fdb1-3be9-90cf-d50a4972c2af | -12.34212 | -48.22176 | 2026-07-25 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3cef341-a924-3e34-8a0f-06a3bdc1da09 | -11.79893 | -47.08945 | 2026-07-25 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 55c68ed0-3533-319f-8e71-d488acb87eab | -12.66829 | -48.20375 | 2026-07-25 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9eb00f0-77e3-3d25-96b3-08a54797673c | -11.45253 | -47.50191 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6f769d7-4a4e-3bc8-be7e-b32ae21f9295 | -10.02256 | -65.05283 | 2026-07-25 04:53:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f5c3cec-8e70-3b57-b64f-1ee66911d780 | -13.31309 | -54.33279 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82ba47e9-f8f8-3499-ab92-10bfd5a16dd7 | -11.96464 | -50.49676 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8b3910e-a6b5-34c8-90e0-2a86ed2abda1 | -13.77947 | -47.12917 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd87eda1-4da2-3247-933d-adee5df676e6 | -12.00484 | -49.26618 | 2026-07-25 04:53:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b994134b-b50e-32fb-9974-1be5160a1b8f | -13.30978 | -54.33225 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cae7afd-66a5-332f-8766-e27adc8436c3 | -11.42311 | -47.48967 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8f09836-4f87-3760-bdb0-48ee569028af | -12.34266 | -48.21782 | 2026-07-25 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d18b3a61-4f1f-3b52-b44c-5539b162bfc0 | -11.40946 | -47.4922 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d38e1c40-6fe1-3d13-8827-9dd358e1d4f8 | -13.79211 | -47.14103 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9af8f18-1077-33b1-b119-c686abd33ebf | -11.79832 | -47.09409 | 2026-07-25 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9292192-dae4-3c95-8bab-e61620c5e1ba | -11.41032 | -57.80942 | 2026-07-25 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8682e805-b24c-3f74-851d-953f82dfdcb5 | -11.74839 | -57.80997 | 2026-07-25 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2755fb3c-1e31-3405-9826-55a82e82c202 | -13.30295 | -54.33057 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b0f2bd2-75ea-3ed7-bc1e-a36ea2ad4c90 | -11.43626 | -47.49095 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adfc09c2-392c-37b1-9328-82365e4c5188 | -13.48172 | -44.03593 | 2026-07-25 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2714c029-1678-3bc4-a7ae-37b467452664 | -12.02482 | -50.49256 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebadaa9a-046b-3b3d-a6f7-a5047812c1d8 | -11.36849 | -47.4574 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1d36795-9d36-3ebe-aff9-b5a583087977 | -13.2991 | -54.33356 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eca7b7b2-9558-3da6-9d71-9c6cac1992d8 | -11.72897 | -50.42068 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e09ac08-9ca7-3cda-90d1-905753895e3f | -13.39707 | -48.16897 | 2026-07-25 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cdfb7ac-1d9a-3a40-a803-954b14148db5 | -11.72184 | -50.41709 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8b2088a-c0e6-32cf-85f9-65f99c1e9668 | -11.44442 | -47.49628 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2eb4f537-dd87-39d4-b575-20647d6d6c92 | -13.40189 | -48.16549 | 2026-07-25 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f053cd1-bda2-34f7-b577-c4e1339c321a | -11.37346 | -47.45356 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 952352ff-816b-3f0e-9b2a-d08f64d37a63 | -13.78345 | -47.13513 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b93107-464b-3e2c-a374-6318d14bc687 | -13.61196 | -44.35807 | 2026-07-25 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3f4fbb2-e181-319b-af19-48b70114d80c | -11.36979 | -47.456 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f30093b-31a5-3238-a973-e05f8d5fe45d | -13.48127 | -44.03982 | 2026-07-25 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4cb0cc9-dd87-3234-9211-55357d1d041f | -11.60764 | -50.14626 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66b7f2e5-1244-3946-9f91-6bacd3c8848b | -11.36109 | -55.43822 | 2026-07-25 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6280950f-07b3-38fd-8446-1435f4d0015b | -12.41776 | -50.40952 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8520159f-9dfa-3c30-85fe-92098c799e9b | -10.02352 | -65.0509 | 2026-07-25 04:53:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab2851ce-fb8f-36e1-81eb-13d262e9c8c1 | -11.64488 | -49.46952 | 2026-07-25 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9512d3e0-5228-32a9-8944-1b93e4f9a289 | -9.00668 | -64.13955 | 2026-07-25 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b3c172e-b14f-3909-8091-d4f42680f808 | -11.41874 | -47.48911 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5cc9c58-7b29-3a82-9c05-96b4173f3caf | -11.60267 | -50.15461 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 266fad26-bc7f-3023-b5b7-fd0c0c0722aa | -15.5323 | -56.04077 | 2026-07-25 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5df703c-0387-3f4b-88f6-d485efc6e8b8 | -14.18007 | -51.90067 | 2026-07-25 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0351339-7946-39c4-914f-37f62851aa77 | -14.18065 | -51.8967 | 2026-07-25 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4df58b1b-0c6a-3d76-be3f-3c2685174fec | -13.79207 | -47.14482 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c230faca-dcb7-3b92-aa27-362cd2e00e66 | -9.00753 | -64.1351 | 2026-07-25 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69548476-cabf-3cfa-90ce-a66907b264b9 | -12.02117 | -50.492 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 63eaf4d8-78e9-3b04-9159-e908eb5c5c1d | -14.37646 | -50.33188 | 2026-07-25 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 369d93ea-f472-378a-9080-d431f0aa69aa | -9.00925 | -64.13914 | 2026-07-25 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b130dc7-e7e3-3e1f-9e21-4c827927ee3f | -15.86601 | -55.50634 | 2026-07-25 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62e1565f-c439-353b-ad92-65ba3966db3e | -13.30868 | -54.3393 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cbb542a-4a85-3f44-a1e4-389ee97af028 | -11.44878 | -47.49682 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 983c1be6-2077-3aa8-8626-376d4137291b | -13.77886 | -47.13425 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7009ebff-fd33-3e05-b236-a82abb99f6ea | -12.0359 | -50.46765 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff61c1b-d21e-3333-94d4-aeaefdcbdd44 | -11.36412 | -47.45678 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa3fc6b-8049-33e7-9365-a7db1df4eabc | -11.78362 | -47.10138 | 2026-07-25 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78963c11-8af3-321e-9e94-8a6928b30267 | -13.30516 | -54.33817 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad82c918-f704-3d36-8c78-f6c6d79ed527 | -12.03195 | -47.80413 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab48b0ce-6f59-3c65-b96f-0db26ad71c57 | -11.71391 | -50.42031 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 643d0ae8-fa1c-3c60-91c1-2636affa1803 | -10.01643 | -65.05155 | 2026-07-25 04:53:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12ccf670-a74b-3be8-ad51-c58720308f20 | -12.0218 | -50.48768 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 64105184-f050-3314-a3d3-dfb4cfc953a7 | -12.43679 | -50.40786 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68c40f2d-32de-3bbb-9c90-a18e9ac398de | -13.19893 | -48.32945 | 2026-07-25 04:53:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a5d756c-c2c9-32c7-8213-549253aec7d0 | -12.05895 | -58.04392 | 2026-07-25 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5d4aa9-1296-3e09-a40c-9984e38ae14b | -13.40135 | -48.16958 | 2026-07-25 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d9d329b-fa19-31a1-b153-f960afce43c7 | -11.67494 | -51.37054 | 2026-07-25 04:53:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a5dd8f1-b8c7-3922-bf58-acea24c76ff2 | -12.62564 | -47.55516 | 2026-07-25 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 822131d2-8ef9-3e4b-82b1-696d29ebf57c | -13.31033 | -54.32872 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af0b1ed4-4b04-3e90-9190-2296ae149a5b | -13.78013 | -47.12826 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4780af3b-3ad3-3099-ade6-6bdc75c9c6b6 | -11.41409 | -57.81005 | 2026-07-25 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14de65a3-f596-367c-b579-69e916505c7a | -12.66353 | -48.20705 | 2026-07-25 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68d0ccf3-f8fe-3391-8e12-34baa675a3da | -11.86544 | -50.32753 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9410a1ad-95aa-3315-a2f9-bacf90f12fc1 | -11.72167 | -50.41959 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53fd6f76-20d6-345e-99fc-86c94300d11c | -14.38025 | -50.33244 | 2026-07-25 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb5ca5c-9cbd-35ef-afeb-eecccfecc0e4 | -12.01815 | -50.48713 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80db027b-0cc8-351b-a79d-416335e054ff | -13.30923 | -54.33577 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d83f2f6-7a88-3d3b-87e6-080a0ce4b017 | -11.60331 | -50.15016 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1e9671a-f701-3eff-9ea6-904daa7aebf3 | -13.40617 | -48.1661 | 2026-07-25 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b0b9116-3b24-3017-a8f7-c0d9617e8350 | -11.42747 | -47.49024 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc971278-7c24-3539-98c5-88f198793276 | -13.61153 | -44.36185 | 2026-07-25 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f22c970d-be09-33f7-a624-3c41bacbaec8 | -11.71756 | -50.42087 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23491167-1d93-359e-b5e2-b43c7d700688 | -12.03162 | -50.47144 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 425ddc84-8cc1-37d0-9c27-17eaf8dd2d45 | -9.01007 | -64.13467 | 2026-07-25 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eac5cf7a-8f26-396a-adb9-766c26bbe0a7 | -12.66407 | -48.20311 | 2026-07-25 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc4ebb6d-eb5a-36b7-bd99-77c51aa92095 | -13.33123 | -54.30325 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a5a1cee-01e5-3c4d-b790-a791e6ae20c5 | -11.3583 | -55.43396 | 2026-07-25 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbd0ee86-002b-3bbb-b9bf-f548d9678eb3 | -13.79269 | -47.14006 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e54827d-7ff7-36d8-b78a-d205d059c161 | -12.43248 | -50.41173 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dbc8686-a520-3214-9fb4-b344d891724d | -11.80283 | -47.0947 | 2026-07-25 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 4dcbb0d5-5275-37da-8cea-76ae3fa829a9 | -15.88108 | -52.30932 | 2026-07-25 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc5f3782-89af-3271-b150-3a5299df2fba | -12.19132 | -44.50088 | 2026-07-25 04:53:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e05f6c8-fd44-337c-aa3c-6df76169e5ec | -13.77947 | -47.13333 | 2026-07-25 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74a86755-2929-3932-8350-12215023e760 | -11.72532 | -50.42014 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f90fcf66-17f7-302a-8228-7c68ff8c3eaa | -13.30571 | -54.33464 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a54f81b8-2445-31bc-90e1-99ef90c6bbca | -12.42144 | -50.41007 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README7.md)
