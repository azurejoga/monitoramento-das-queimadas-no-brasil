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
| bacfb749-8cd5-312d-a855-7eb4c72f73d8 | -6.34114 | -55.30289 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9485c035-3f2f-3e77-849d-333f19085e48 | -6.33548 | -55.85249 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84980eb5-d2b0-371f-a724-2c82a3a0e9a1 | -6.08005 | -57.88712 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c74561a0-8a2e-39db-beb2-5175285acdb9 | -9.70717 | -54.35567 | 2026-09-12 05:29:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 689f0955-bc8d-3ced-a8cd-b651e53b99a9 | -5.79787 | -57.72384 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc2fb194-dbaf-3f7a-940b-3c0c04548c5b | -6.82381 | -58.64863 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93dada1b-b8bd-3b3e-91ce-c8fb51abbf0b | -9.46897 | -67.09681 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf61f6e2-1c8d-3a02-89e7-2d56f35a92b2 | -6.76612 | -59.4327 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 386f36e4-8263-30f6-98e2-a46bc87c7f2b | -9.31721 | -68.77628 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9ba8b4b-9a4c-3aaa-a644-c1c08616e22f | -9.19287 | -68.21238 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a62369d0-6c65-3019-aa15-741243e435a1 | -8.75959 | -70.81007 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74187d85-4e0b-342b-99cd-cb0a29e29dab | -6.61451 | -58.84836 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a27381ee-22e6-3816-a892-b50e966c14c9 | -9.18415 | -59.6897 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13e927dc-5f49-3308-a007-def00cf3b90e | -10.53833 | -51.3685 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ed9c2c6-c9be-34ae-8a18-7adb3bbda414 | -8.57497 | -54.56976 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed837c64-c3f2-3edf-a5d7-ce8d22381d33 | -9.64182 | -49.6796 | 2026-09-12 05:29:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89cc586a-0af3-3de9-983e-e5ca6e05963f | -11.24503 | -54.12556 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a8cd478-b460-3213-898e-f807b1bb0d91 | -6.42592 | -56.1097 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83164843-870e-3591-96c2-da77c67ab2e4 | -6.10388 | -59.89579 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f51509e5-05c5-3ef1-a590-eb7251d5ae4f | -6.8781 | -55.63649 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04332d22-31db-3ab3-8c7b-a9beae27860f | -6.81917 | -58.99645 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ba56d39-92a9-3388-9f1d-0466082ec438 | -11.428 | -51.43077 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0543df5-7086-3d7f-927b-a275d356e1cb | -8.53403 | -54.70119 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34702bf8-27ae-36a9-b69b-93885c62397a | -9.18222 | -68.21997 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c50743bd-20bf-328e-a840-a0ec7f9a25ed | -6.1065 | -55.65174 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07c55550-f2c9-3e3a-a2c9-bac84ae6b95f | -10.68851 | -54.17084 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 89d1a256-1c58-3ba1-9305-40fb5306f26e | -9.15282 | -49.98583 | 2026-09-12 05:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 180624bb-0dc5-3b02-bfc5-370556e47ad3 | -11.24225 | -54.14664 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a04c6e70-8368-3bf9-a78a-294c74ba07c3 | -6.24197 | -51.69762 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97d46477-c985-33ba-8081-a88bb6a61897 | -7.92406 | -49.7374 | 2026-09-12 05:29:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ede604c-0587-37e4-a790-f4bb2a000031 | -10.51277 | -57.45157 | 2026-09-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f067d04-f867-3d44-8f2a-e8212f0d702b | -6.11408 | -55.65613 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a55ccf71-af65-3e8d-9332-08bbad5d446e | -6.2376 | -51.6904 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13be7519-2789-34ac-94fb-bfdee4aef694 | -6.1146 | -55.65268 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 043404c4-be59-3265-a3b5-6bec8db649eb | -5.97914 | -57.76603 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ea88f1b-185f-35f5-954c-2acc0f0b159d | -6.07104 | -53.49233 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 532fdfd1-e054-3a7c-92ff-ce3ae55a524b | -10.5544 | -51.33407 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 997f916d-d0d8-3b1b-8af2-a43cd559a986 | -6.23182 | -51.69298 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7013af97-01ec-32c9-95da-f806446ee389 | -6.2295 | -51.70934 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed33a016-759f-3b6b-b3b2-1091c74495bd | -11.0836 | -50.84155 | 2026-09-12 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9edcfdc-966c-35cd-8556-b0e9b2610088 | -12.11771 | -48.96142 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7a1d5af4-6164-3cf0-9677-04755db2d1b6 | -12.44553 | -49.58654 | 2026-09-12 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a728021a-592a-3a76-9f12-f4fefb5edd41 | -6.1973 | -55.25961 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 406d86a0-a362-3aca-bd37-3cb825209e65 | -6.33755 | -55.29858 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21061e5b-37b7-3b9d-847d-821ba603184e | -6.75491 | -58.68883 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ce79c4e-15b0-3b73-8e07-3f3d5592f5c3 | -5.59021 | -60.24596 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aad77e4-f428-3534-a800-d4577cd62a4e | -6.10457 | -55.63716 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c72c2fa-ff7d-3c1e-a561-2ec593dec020 | -8.95348 | -67.38575 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 342295e2-acc2-36d7-aeb7-45cafa1a1260 | -9.47314 | -67.09754 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a6a0d9-617d-3924-a0c0-f221868d75da | -6.61678 | -58.85631 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7b816d3-915f-37ac-a0e8-ae0f9bad5bd5 | -6.83486 | -55.28825 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2691dd3-b712-32da-a0e4-ad4972c714c6 | -6.06309 | -57.73568 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a61b928-d58a-3e2b-a3a8-753cb8e5810c | -6.23275 | -51.68644 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b01956e9-a707-3f7e-995e-7db9931b3a18 | -6.88219 | -55.63702 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b08b03e9-f7de-3ee5-b575-76689e4ea6f0 | -8.07615 | -54.86551 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16c21f0b-cd53-3f39-8786-14af14d65d92 | -6.88464 | -55.64844 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bf1ac67-8087-3df1-b651-51e1de2a3025 | -12.13731 | -48.97138 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 995e439c-be53-3d2a-ae44-990a9ae2e89a | -6.24103 | -51.70421 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5897cb28-d5da-3560-bd25-955c629b9245 | -8.07239 | -54.86066 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a444f6-e0fa-37b2-8725-7baab56c3253 | -6.20505 | -55.26456 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9217a035-a25d-3cd3-aa6a-da438c07702e | -6.84838 | -55.58347 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd3ea6a-1ba5-3537-b72b-949ad1ab5173 | -8.11775 | -54.7948 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ca1aa93-2a66-3359-ac61-8d600b1e356f | -10.50428 | -51.31305 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a8faddf-29c3-3bba-9600-c54d28e543ea | -10.895 | -47.83834 | 2026-09-12 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db5fbebe-f784-3c7c-ab8a-b9be71976836 | -6.19199 | -57.72062 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 909a7ce3-4278-3be9-a10e-fe53c88a794d | -6.8871 | -55.65982 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c3bd357-3628-36ba-8436-8c1123bacefa | -6.12319 | -55.65042 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04e83dad-1908-356f-a4ab-377b74b7eb3f | -9.18835 | -68.21158 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9cb672d-6ff0-3919-8b05-d035fb30a405 | -6.18249 | -57.71076 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d1e336f-71b8-36e1-831a-7e7700e98f56 | -8.53159 | -54.71898 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c18d61e8-e8fc-39c8-821c-12d853d833be | -8.60695 | -69.66324 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77d85c49-0af0-34f3-880a-90dc55f3d938 | -6.8841 | -55.65205 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a858908-c368-3e09-bb55-9b79d11d0975 | -6.34169 | -55.29919 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 414efc2c-e31f-30a9-8e52-9ae542a6592a | -9.71181 | -54.35641 | 2026-09-12 05:29:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c94f556-d934-3a84-999d-cdab566ae6b2 | -9.4409 | -67.03629 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 898c66a2-f2a6-33b3-a6b9-5593b0abb872 | -8.68505 | -71.02744 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 842f694a-7f22-3c6c-b974-9488f0eae78f | -9.33769 | -68.27664 | 2026-09-12 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1763bf68-94f0-3649-ac68-795345af474a | -9.46491 | -50.31715 | 2026-09-12 05:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a148e4-0641-3e1f-a405-b52a3fc22dad | -6.3945 | -53.18159 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2343b31-bcd1-3354-8ee4-f16539f6fb9d | -6.11053 | -59.89684 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13352d7f-a87c-33eb-820b-becc122f949f | -8.87813 | -70.84437 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c847065-9793-3bad-8762-abdec0f1e766 | -9.17226 | -59.42536 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4d9c782-5ad1-3d95-9111-5eaeaf91adbd | -6.60823 | -58.84358 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94ec7a50-27a8-3c14-8867-d508388f1525 | -8.84509 | -71.08254 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbc8779f-2ab7-321e-ab91-9c0de3f49b3d | -6.10333 | -59.89928 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 703416d1-51d7-3a18-81d7-63d03c82d5f8 | -6.06567 | -53.49654 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7caa2e0a-26a6-31b3-8e4f-402a7410b3b4 | -10.51096 | -57.45345 | 2026-09-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e013e14-6ef1-328f-a3ce-7235bfc48177 | -5.80079 | -57.72853 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6e9b5e-83b4-397d-9a29-5aeaf59bc58e | -6.61509 | -58.84465 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f92ab4ed-3ace-36f2-82ce-d67a24138ec4 | -9.47246 | -67.10145 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5024103-4e7b-3456-9a27-68e6efd1a417 | -6.18405 | -57.74875 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f60cc690-bbe1-3b67-b082-549b7383b87f | -10.50405 | -51.30994 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81b92c3b-04e6-36b7-ac1f-8187a58656e6 | -8.70649 | -49.6179 | 2026-09-12 05:29:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15e6c2c2-afc7-3192-bd80-2ca50c2f021d | -9.52659 | -67.16676 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef0e60b-4fb7-3187-bc08-40c84ec0851b | -6.10278 | -59.90279 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e92988f5-9fbd-3e65-b4e5-a3371ae5a5a8 | -6.11915 | -55.64983 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdce71a2-edbf-3cce-9dd6-6373aca480f7 | -6.79926 | -58.89887 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28898149-c605-310f-94d5-46608ace18a4 | -8.6108 | -70.96793 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248a6a07-c90f-3d1b-8898-2606a1bc53e5 | -6.2009 | -55.26398 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b37d9e73-c280-3d8f-b581-bc1638b57243 | -6.11108 | -59.89334 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README52.md)
