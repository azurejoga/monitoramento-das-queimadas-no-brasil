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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3b80a91-2180-3cc5-b267-5ab97f36019b | -14.1443 | -52.8828 | 2026-07-09 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59f76ec9-20f7-31c5-9480-bc22505bc6c9 | -12.84535 | -44.36406 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3af71076-703e-3093-b7ae-1c1f326e671b | -14.15047 | -52.88757 | 2026-07-09 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e0d840f-2673-33e6-be21-1a010ce2bd83 | -14.14766 | -52.88333 | 2026-07-09 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 538e9a48-e364-3718-982e-3966a5575854 | -13.95503 | -53.90261 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4436a7bb-92a6-3dd4-a9e3-6b27f8e03d1c | -13.76918 | -46.30325 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aee64557-9107-3ab5-ae16-765e81bab408 | -13.96495 | -53.90422 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d97626d-fd4f-380e-9afa-c93b8289d3b9 | -17.27168 | -47.43364 | 2026-07-09 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c97ce079-7acd-3940-8004-640872a411a5 | -11.21234 | -53.82518 | 2026-07-09 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3f35817-f728-30ab-a19b-23deb28c55d7 | -11.4671 | -52.92504 | 2026-07-09 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e1d4522-4942-3ff1-8fe6-3c25f892928b | -11.55579 | -52.79 | 2026-07-09 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba48079a-00a7-3853-8164-826e6b72a12e | -13.9644 | -53.90776 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15715a0a-2ac5-3114-8909-19097a84385b | -11.83716 | -48.23961 | 2026-07-09 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 129e5194-fd93-3fac-8779-6f0982f85b7a | -13.27833 | -45.18279 | 2026-07-09 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b0cad16-4bac-3e9f-9daf-62b458206e28 | -12.84734 | -44.35538 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1f9e610-abbc-3001-b3c1-4501c275c511 | -12.83531 | -44.35537 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44b94a98-d3aa-35b9-8925-fd8f8bb87bc6 | -14.15102 | -52.88388 | 2026-07-09 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5266c9e3-8cbd-3b0b-b425-b9bbb9ead207 | -13.27794 | -45.18596 | 2026-07-09 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0046e99-38c0-31ab-abc7-fc162d1bf16a | -11.18229 | -55.02024 | 2026-07-09 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cad4ea1d-1e69-3c37-80ae-3ecf2746d91f | -13.76427 | -46.27455 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28f2c38a-39db-3d05-8a2a-bd83c72ae856 | -14.44079 | -48.76103 | 2026-07-09 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79376951-f84e-33d9-ae32-75fe111882c2 | -12.75379 | -44.52849 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21849f53-93ce-353a-9c69-cd4d3c1e488c | -14.91506 | -43.43028 | 2026-07-09 04:53:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 9e731c35-1863-3fa0-a61c-6ebfa281d905 | -13.77126 | -46.29769 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f47c714-32bd-3a87-b04a-a6e5e7f35c0e | -12.93182 | -56.62574 | 2026-07-09 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4b10a72-c9e1-3b1e-a07f-a2ecbc4e7701 | -13.27975 | -54.41479 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15c0d613-2454-34b4-b6fb-52ce036faa39 | -13.76983 | -46.29767 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2dddde07-c952-34bc-9d61-b011f50da3f1 | -13.94842 | -53.90152 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85581cbd-70a3-39a5-84dd-34c3649619d4 | -13.28361 | -54.4118 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fb258dd-de12-3570-821b-fc695691e63b | -12.92843 | -49.4824 | 2026-07-09 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba9d37e1-ed03-3082-89f7-85262bcb7c0c | -16.71741 | -50.70799 | 2026-07-09 04:53:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9bc0e473-604b-31aa-b0bc-f4d5ca5edbaf | -12.84776 | -44.35177 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c60996c-23b0-3085-bf06-f94f8b95088b | -13.77056 | -46.30326 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ff6d168-8f7a-3174-a88b-136ab0454f3d | -12.82985 | -44.35456 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8c8e9e4-ab6c-331b-8a4f-75cd1d73a204 | -13.60692 | -56.59494 | 2026-07-09 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e04526af-93fa-3aa8-a810-40eb817d9f2f | -12.35314 | -47.42218 | 2026-07-09 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e92ecc52-2e6f-360e-8fb6-d9537128e79f | -12.93686 | -56.6389 | 2026-07-09 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b63ab3-eed3-3507-80e4-cd27aca24aec | -13.27963 | -45.1819 | 2026-07-09 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dc54eeb-67cb-3a4a-8cdf-30d66a138e24 | -11.83302 | -48.23896 | 2026-07-09 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b106ce89-fd03-3f28-94b8-4f5555c3ea6b | -12.75337 | -44.53201 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11e10c7b-4954-39a0-9f74-a2aa15fe0f4a | -15.95911 | -47.76299 | 2026-07-09 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccb70a06-65bc-3e56-aa5d-c0d201ecb492 | -14.92101 | -43.43111 | 2026-07-09 04:53:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 0cb19925-9356-3c3b-bf89-6dd13416c2f5 | -12.35787 | -47.42115 | 2026-07-09 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a8d44e7-2a7a-3e06-8444-21ad3f5efc9a | -12.75836 | -44.53621 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f155efbf-2932-3c22-8e17-b953c94eea5e | -11.85934 | -48.04112 | 2026-07-09 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7768f0c4-4816-31ce-8cb5-9787a7bdbf08 | -12.93231 | -49.48296 | 2026-07-09 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d4aabc76-d401-35a5-bd97-498948d00c80 | -12.84667 | -44.35328 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ada8844e-cc77-3395-bd75-271c8e021890 | -11.3102 | -54.47556 | 2026-07-09 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be2916fe-6f38-3cfc-be04-5181915505a2 | -12.38281 | -54.17018 | 2026-07-09 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f99d2b5f-8d02-3280-9191-0d2336bfe56d | -12.38336 | -54.16667 | 2026-07-09 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cece520b-22ed-3dfe-a50c-692b564f7760 | -11.46046 | -52.92399 | 2026-07-09 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cc4e84a-72be-3156-85dd-987109d77591 | -11.45673 | -52.92654 | 2026-07-09 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a61298e8-02d7-3577-99c5-0e900ad7fe73 | -12.84527 | -44.37333 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f61af5a4-24de-3902-8168-408608e6a4c9 | -16.71676 | -50.71278 | 2026-07-09 04:53:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 03e7a20b-ff76-364d-b8f4-464e9a0de1a6 | -12.84447 | -44.37121 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ddb59c8-0cf3-34b8-b30b-b8febfd9b5ed | -12.92921 | -49.4848 | 2026-07-09 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9eb122d-9575-3384-ab16-d66a57e021c7 | -13.28636 | -54.41586 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39a57b0f-9eec-3051-a25e-165ac031e304 | -13.28966 | -54.4164 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b1d7492-63ca-3f7e-b538-60efa67c18fa | -12.35345 | -47.42056 | 2026-07-09 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bd22aff-554d-3c9d-b7d4-0fa4dfb5d0e7 | -10.90062 | -56.85215 | 2026-07-09 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9ce12a-2549-3de7-b4c5-ea1ad9bba0ab | -21.77906 | -56.29198 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30368a23-26e8-3441-b269-29911a474bd3 | -18.11219 | -54.00455 | 2026-07-09 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc80dcd9-91b6-35ed-a6f4-ab60e5d59ff6 | -21.77575 | -56.29139 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bef31117-6ab3-30bc-b0cd-4266c3eacd6c | -21.35424 | -51.04398 | 2026-07-09 04:55:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e303ae51-1d2f-33c9-a27e-5c37c5d0470d | -23.56405 | -47.51217 | 2026-07-09 04:55:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 335fa2d7-b822-3794-a9d9-257807000588 | -21.19436 | -56.92813 | 2026-07-09 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5caceb5-d7a6-365a-ac37-1062efa0e629 | -18.02497 | -54.35693 | 2026-07-09 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b289bab7-f714-3491-9108-5b26f2d888b6 | -21.79633 | -56.26851 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46a2bdf8-25f7-39e6-bfc8-63980b77ef0d | -18.11164 | -54.00826 | 2026-07-09 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27590e75-629b-3b4e-9382-78b2df3ff898 | -21.13533 | -51.06934 | 2026-07-09 04:55:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac7b318b-1ec3-36e8-bd42-fc8cd1e44177 | -22.92181 | -49.20676 | 2026-07-09 04:55:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 759a9b68-58c5-322b-ad62-068ed8c49be8 | -21.80746 | -52.71981 | 2026-07-09 04:55:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c217b7c0-c94f-3e64-ba37-69fd5df6e789 | -18.02442 | -54.3606 | 2026-07-09 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 462038aa-8fea-3b98-ba30-55e476e05483 | -18.02165 | -54.35638 | 2026-07-09 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8759e90-0401-3470-b965-1b523030be21 | -21.76914 | -56.2902 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 246362c7-1d78-3002-bfce-06ee393828ff | -21.80353 | -56.266 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc612f55-65f0-367f-a179-80d6be2698c5 | -18.10828 | -54.00771 | 2026-07-09 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d204f8dc-7e97-3b14-899e-53d209e04a43 | -23.21844 | -55.48236 | 2026-07-09 04:55:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7cce29c9-a377-3ef5-9fd5-5cd5ee1630bf | -21.4682 | -54.48365 | 2026-07-09 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6497ac3a-7fb7-3a6e-b0f2-922c4c0853f4 | -21.207 | -49.21408 | 2026-07-09 04:55:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f0859d17-f747-33ce-b704-9db370c232bd | -19.8554 | -49.07373 | 2026-07-09 04:55:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2eacd18-c8a4-3035-8cbe-f348b5a628b4 | -20.19214 | -56.17181 | 2026-07-09 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 552fea63-5f42-3671-8389-9cc415e82fb5 | -21.79576 | -56.27215 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cea5f36-9f61-3bb1-915c-00083ab299f5 | -23.8196 | -48.71471 | 2026-07-09 04:55:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2e8f003-f526-3db3-b058-cac1f8c12482 | -21.81472 | -52.72093 | 2026-07-09 04:55:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0de276b3-5151-332a-8cd2-37c07b36ae3c | -21.77245 | -56.29079 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75a4b089-e698-3c68-bfce-e74c929e0fff | -21.81169 | -52.71584 | 2026-07-09 04:55:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d66ce93a-e9c7-3ada-89fb-2297a4ebe3cd | -20.4738 | -56.73045 | 2026-07-09 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 980bc758-1674-37e4-be83-03721ba39c49 | -22.28853 | -46.8618 | 2026-07-09 04:55:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01e97148-6e12-300d-9777-45c9f34cac7e | -21.76856 | -56.2939 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fea0896-af4c-3a5a-a62f-f7e6f7bb3fed | -18.11275 | -54.00084 | 2026-07-09 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe9dd2f6-5927-37f2-b985-e5d8c9b72b1a | -21.46482 | -54.48308 | 2026-07-09 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34c4ef48-ce6f-37ad-be30-f0ccf8601a90 | -21.79964 | -56.2691 | 2026-07-09 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64c09eea-d6b9-3513-93d7-8af54b2a6cba | -18.02775 | -54.36115 | 2026-07-09 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b02e79d2-ae29-3cd5-a3e6-8380ee77ab3d | -23.94612 | -54.28099 | 2026-07-09 04:55:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a5bf2d8b-83e8-3dae-b9b0-943a39a7b69c | -21.50739 | -48.8204 | 2026-07-09 04:55:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47cce6d1-8fb1-32a9-b2c9-62f4abca4c80 | -23.61963 | -51.78495 | 2026-07-09 04:55:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27691a11-29c6-3f3e-8c44-21710c707581 | -30.14136 | -52.57063 | 2026-07-09 04:57:00 | NOAA-21 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4d09bf80-e934-3f7b-a095-3ac4bd06b8a3 | -2.63826 | -47.98598 | 2026-07-09 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 467b41ac-0089-3ebc-8aeb-0cbbed8046aa | -2.98359 | -54.60289 | 2026-07-09 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README11.md)
