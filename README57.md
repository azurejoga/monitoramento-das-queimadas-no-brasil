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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 432b9988-9252-318d-be8a-e799f7620fa0 | -15.62076 | -49.39103 | 2026-08-28 05:12:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e478679a-bbee-3d77-a1cf-6d123d196556 | -8.99809 | -65.43811 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b502a9fc-fe91-37be-afb8-906856dfc0e3 | -11.72547 | -54.54077 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f38f9af5-dfb4-3a30-ba93-d6f13589f2f7 | -13.59549 | -45.77871 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d76f2ad-e5d0-39c3-ada9-255a70402388 | -13.40771 | -51.41496 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 569ffb42-41d4-310f-bbb3-59465403ed08 | -14.4815 | -52.16429 | 2026-08-28 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efee262b-0d24-3991-8cb8-f2aa8c73d27f | -14.59665 | -53.15881 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 157662b1-2c14-30ef-8448-29953c4021cd | -12.77376 | -46.45982 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f66924c7-27e5-3a60-b85a-6c6e9eb1ac88 | -11.02338 | -49.66151 | 2026-08-28 05:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2c29b92-a14e-3744-90b8-886a11966f4c | -12.2581 | -50.58089 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bff6fadc-0484-370e-8885-3013ec175c62 | -10.80241 | -54.01592 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f487011b-be33-39f8-b375-020d1671cc6c | -14.17213 | -52.81967 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c0f5ad8-9af6-3b0a-bec3-d775ac34e96f | -11.49281 | -45.11506 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6bf9da1-2392-3d66-8078-34489b809d5e | -13.41318 | -51.40714 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 06aab08f-84d3-3613-95c5-217de79c0686 | -11.22224 | -53.99461 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92ee1883-a49c-378d-a4ca-9139aaa5d37e | -12.29127 | -50.58833 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48c23317-fbcc-3dbf-97a2-0c4d7dc14fdc | -11.74255 | -54.52282 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2304f393-988f-32fd-bdda-926bd3251ef4 | -11.65195 | -46.73026 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a899103f-f85e-3c48-8465-6d12a0c56925 | -10.57206 | -57.48819 | 2026-08-28 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3ad5006-6e94-3b43-ad8d-ee5731547638 | -14.45484 | -53.34919 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c80d5bc-1157-39ba-893f-6ed62a36ec2d | -8.99113 | -65.44664 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f3443f4-30a4-38a9-b40e-29b52cd19034 | -14.29794 | -51.73425 | 2026-08-28 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4303965-2d26-3623-a9a6-7bfe1768fb98 | -11.21505 | -53.99349 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6a9d705-f4b7-3772-ba73-73eaef8a93b0 | -15.76643 | -56.4485 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6953c6c-3aba-3415-be18-8e208290ccf9 | -12.26484 | -50.58001 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 72a5e264-e1ea-35a5-a011-f9c0d69bd218 | -14.93122 | -52.60268 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 633a5f9f-ab09-365a-966c-874c04ac0416 | -10.92428 | -50.53099 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1236281c-a8c9-31ce-8c43-e5fb515e3905 | -13.48029 | -57.05116 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1033ad72-1f3f-320a-9060-433c0c38c157 | -11.81151 | -47.20127 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b9aa2f7-b88b-3a5e-b254-4bb1c4723b6e | -14.19059 | -52.83324 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50165049-fff8-3bcc-a294-3c5ac743f895 | -14.45316 | -53.35254 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93911819-5604-3bc2-931d-b80ea7c8ee86 | -10.94141 | -50.53788 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 04071287-3a35-3526-8ba1-b7edc8a0ca88 | -10.66487 | -55.15319 | 2026-08-28 05:12:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf811a9-8186-3c12-83eb-f8041a209658 | -10.99321 | -51.0947 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fc2d368-44c7-385f-b2d7-d3940d85e10c | -11.20601 | -51.23168 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 36c576bf-6eaa-369a-a456-46c90e15825c | -11.94898 | -60.96149 | 2026-08-28 05:12:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a846a97-aa54-3ac9-8dbb-692a7eda4826 | -10.88053 | -50.52035 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dc33b73-e808-3695-a087-9dbfcd1151b9 | -10.50005 | -64.51794 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a85e652e-b7ba-3a0c-b1ed-14b1a134eaf9 | -14.86391 | -52.61263 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6d9a00a7-442a-34d1-a8e5-70d14493e2e4 | -15.51082 | -55.95533 | 2026-08-28 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca23733c-d728-3d42-a80e-c4197f356cfd | -10.5029 | -64.50245 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 36d5d17a-ab12-3071-8383-c31bb07cef81 | -11.19283 | -55.0867 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d93b145-c0e5-359b-a22a-ced228eb2d26 | -12.28045 | -50.60083 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3955bc78-537c-3de8-b497-264726555f7f | -10.92368 | -50.53539 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9e640863-b490-38f2-9bf6-5279da33b974 | -14.86998 | -52.59871 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e30e898-4c2e-3f21-9ab2-1b9c3ae08406 | -15.63066 | -55.97374 | 2026-08-28 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89b246c7-2c17-39b5-ba91-fecf7cc8cef5 | -14.85983 | -52.61208 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59c45aef-b9de-3228-8d86-46442ffcf929 | -12.01709 | -47.16746 | 2026-08-28 05:12:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c864cb7-c6f0-31ec-acc9-d43cc8554bd4 | -12.29067 | -50.59292 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5b3d5b21-976b-31ce-a24c-6a1bfd7c6759 | -8.99054 | -65.44981 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39dd71b6-e3db-38b9-9957-d8fca42d7f2e | -9.19881 | -67.77706 | 2026-08-28 05:12:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0c4c47e-1010-3105-ba8c-ad8d9cafe133 | -11.62099 | -54.58678 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5173c02f-dae1-3de9-b54d-ab7bab024aaf | -14.95722 | -52.59538 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58ef714c-d56b-3ae1-bf50-8a1aeb9a86d3 | -11.1943 | -51.22714 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 5d0adc6d-99fb-3283-b248-f09ce21059ab | -11.22287 | -53.99042 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8132df79-aeca-38b8-a828-fa717b322b32 | -14.93169 | -52.59919 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 110e21d4-c13f-334f-8239-b9e82a15bd4e | -10.77132 | -54.03782 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 071df5df-2c2f-35f8-9dce-4acc3249cdf2 | -11.7349 | -54.52575 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92478a28-bf46-3a98-9649-664944a9fd26 | -10.75876 | -54.04852 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4a82ecf-5233-3c2c-8f33-ac57a945b3df | -12.78164 | -46.44394 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bccf027-1784-3a83-a5e1-a0b0efd24f00 | -11.23177 | -54.00455 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 005cc6e3-e0fe-34a6-8fad-d38606f0629a | -14.96132 | -52.59587 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9392afc-cf0e-3211-9da9-95834cbefd51 | -11.72369 | -54.55279 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3294bb1d-e996-37b4-a59b-9cfb53b17cb9 | -13.59492 | -45.78387 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2db08cd9-896d-3ad5-a190-f738c793566e | -11.29161 | -54.03347 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3c49a18a-af97-3192-864e-92d578380609 | -11.27365 | -54.03077 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7e2bc71-cd46-3512-aef1-148f57be9ce7 | -11.16737 | -51.203 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68bd5d29-8223-3178-a906-3d786a896253 | -14.90204 | -52.60284 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 649115e8-0999-3686-b45c-9e46b8ce8071 | -11.53139 | -45.52051 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81532302-20d8-3d53-9ee5-395e56105d57 | -12.78715 | -46.44883 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5884b427-9e0a-35b1-b2e5-30a0c0961f42 | -14.92758 | -52.59874 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00039ae4-1e32-34b1-aa0e-c739ca2022d1 | -12.78064 | -46.4527 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b509781a-0c6e-37b5-8ed4-f23f8ff894ab | -11.72254 | -54.53622 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a44a7434-9f23-335d-890d-eecd11f377b1 | -14.42561 | -52.60483 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a773a5bf-9a99-30b6-8d1e-c2f3d69ac06b | -10.77162 | -50.63138 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 008c1981-bf06-3202-8a79-fff19765bf39 | -13.86546 | -54.11808 | 2026-08-28 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dc99a84-54f5-3fe0-ad7e-1cc03f9a39a5 | -11.2755 | -54.01826 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa9506e8-a572-3603-a625-d3fee2f2bb3b | -8.99502 | -65.44933 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ce8bbaa-ed02-332e-9856-0f48420722bb | -12.2474 | -50.5729 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14e91dd2-81eb-35bb-897c-baab03e785c5 | -13.46395 | -57.04837 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a916b98-ce44-3fb4-bfef-eb30b2012d70 | -11.22579 | -54.00648 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7764c76-403d-3595-bbcd-ccd35997974d | -10.75851 | -53.97679 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8912c5e9-087f-3dd1-911d-695a7dae0955 | -12.91578 | -59.89503 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84bb9f32-531f-3bd6-98ad-390740540371 | -15.32033 | -52.75879 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27227fef-80a1-3312-88f5-54167c936ae0 | -12.76735 | -46.46289 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62d660a8-6414-3c44-ae2d-b67c6c2f047b | -11.71078 | -54.54263 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e022f9-cb47-3c3f-bc82-2549cd4bc6cf | -14.59595 | -53.16046 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b60663b-3b9b-344b-b244-58217e33002d | -13.86914 | -54.11861 | 2026-08-28 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87b03aa0-79e9-3c91-9dde-05a7236dee6b | -11.21443 | -53.99768 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b32048a8-0119-37e7-a70c-fc9180681b67 | -12.91082 | -59.88208 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8431b8a-65c1-3dc2-9a94-1232d0e8ccd1 | -11.2342 | -53.99918 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51b1ccbd-4b0b-3294-b302-5c4db0db2b03 | -14.88209 | -52.59612 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88c79429-c361-32e6-9dce-aa367eceadc7 | -11.21802 | -53.99824 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f251125d-8703-3979-9115-b021916fd390 | -12.91296 | -59.89051 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8335830e-21b6-3ab8-a811-ca52e60f89c8 | -11.82131 | -47.21418 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4786dd0f-fa56-312f-9bd0-d9f0649aa170 | -9.8743 | -60.25419 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eefc148-3b3e-3a99-bc6d-66ab71f254c7 | -8.63808 | -66.53989 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69e4cad0-3800-31f0-90a7-f88d04e51420 | -9.82765 | -63.00982 | 2026-08-28 05:12:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35849c99-c55a-3010-9abb-d472b53182aa | -14.16416 | -52.81844 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fcccff9-0d85-3312-a2f6-35e807799225 | -11.73431 | -54.52978 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README58.md)
